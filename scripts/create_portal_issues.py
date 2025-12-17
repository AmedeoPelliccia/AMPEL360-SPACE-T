#!/usr/bin/env python3
"""
Create GitHub Issues for Portal Retrofit Cleanup via API
=========================================================

Creates GitHub issues for each STK portal from the generated issue templates
using the GitHub REST API.

Usage:
    python scripts/create_portal_issues.py --token $GITHUB_TOKEN
    python scripts/create_portal_issues.py --token $GITHUB_TOKEN --dry-run
    python scripts/create_portal_issues.py --token $GITHUB_TOKEN --portal CM
"""

import argparse
import json
import sys
from pathlib import Path
import re

try:
    import requests
except ImportError:
    print("Error: 'requests' library not installed.")
    print("Install with: pip install requests")
    sys.exit(1)


GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "AmedeoPelliccia"
REPO_NAME = "AMPEL360-SPACE-T"


def parse_issue_template(template_path):
    """Parse issue template file and extract metadata and body."""
    content = template_path.read_text(encoding='utf-8')
    
    # Extract front matter (YAML between --- markers)
    front_matter = {}
    body = content
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # Parse front matter
            front_matter_text = parts[1].strip()
            body = parts[2].strip()
            
            for line in front_matter_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip("'\"")
                    
                    if key == 'labels':
                        # Parse labels (can be comma-separated or list)
                        value = [label.strip() for label in value.split(',')]
                    
                    front_matter[key] = value
    
    return front_matter, body


def create_github_issue(token, title, body, labels, dry_run=False):
    """Create a GitHub issue using the REST API."""
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }
    
    if dry_run:
        print(f"[DRY RUN] Would create issue:")
        print(f"  Title: {title}")
        print(f"  Labels: {', '.join(labels)}")
        print(f"  Body length: {len(body)} characters")
        return {"number": "DRY-RUN", "html_url": "dry-run-mode"}
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating issue: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return None


def get_portal_templates(portals_filter=None):
    """Get all portal issue templates."""
    templates_dir = Path(".github/ISSUE_TEMPLATES/portal-retrofit")
    
    if not templates_dir.exists():
        print(f"Error: Templates directory not found: {templates_dir}")
        return []
    
    templates = []
    for template_file in sorted(templates_dir.glob("post-retrofit-cleanup-*.md")):
        # Extract AoR from filename
        match = re.search(r'post-retrofit-cleanup-([a-z]+)\.md', template_file.name)
        if match:
            aor = match.group(1).upper()
            
            # Filter by portal if specified
            if portals_filter and aor not in portals_filter:
                continue
            
            templates.append({
                'aor': aor,
                'file': template_file,
                'filename': template_file.name
            })
    
    return templates


def update_tracking_file(created_issues):
    """Update the TRACKING.md file with created issue numbers."""
    tracking_file = Path(".github/ISSUE_TEMPLATES/portal-retrofit/TRACKING.md")
    
    if not tracking_file.exists():
        print(f"Warning: Tracking file not found: {tracking_file}")
        return
    
    content = tracking_file.read_text(encoding='utf-8')
    
    # Update the issue status tracking table
    for issue_data in created_issues:
        aor = issue_data['aor']
        issue_number = issue_data['number']
        issue_url = issue_data['html_url']
        
        # Find and update the row for this portal
        pattern = rf'\| {aor}\s*\| TBD \| Not Created \| - \| - \|'
        replacement = f'| {aor} | #{issue_number} | Created | - | [Link]({issue_url}) |'
        content = re.sub(pattern, replacement, content)
    
    # Update the "Not Created" status to "Created"
    content = re.sub(
        r'\| TBD \| Not Created \|',
        '| Created | Assigned |',
        content
    )
    
    tracking_file.write_text(content, encoding='utf-8')
    print(f"Updated tracking file: {tracking_file}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Create GitHub issues for portal retrofit cleanup",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create all issues
  python scripts/create_portal_issues.py --token $GITHUB_TOKEN
  
  # Dry run (preview without creating)
  python scripts/create_portal_issues.py --token $GITHUB_TOKEN --dry-run
  
  # Create issues for specific portals only
  python scripts/create_portal_issues.py --token $GITHUB_TOKEN --portal CM CERT SAF
  
  # Skip tracking file update
  python scripts/create_portal_issues.py --token $GITHUB_TOKEN --no-update-tracking
"""
    )
    
    parser.add_argument(
        '--token',
        required=True,
        help='GitHub personal access token (needs repo scope)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview what would be created without actually creating issues'
    )
    
    parser.add_argument(
        '--portal',
        nargs='+',
        help='Create issues for specific portals only (e.g., CM CERT SAF)'
    )
    
    parser.add_argument(
        '--no-update-tracking',
        action='store_true',
        help='Skip updating the TRACKING.md file'
    )
    
    args = parser.parse_args()
    
    # Get templates
    portals_filter = [p.upper() for p in args.portal] if args.portal else None
    templates = get_portal_templates(portals_filter)
    
    if not templates:
        print("Error: No issue templates found")
        return 1
    
    print(f"Found {len(templates)} issue template(s) to process")
    print("="*70)
    
    # Create issues
    created_issues = []
    failed = []
    
    for template_data in templates:
        aor = template_data['aor']
        template_file = template_data['file']
        
        print(f"\nProcessing {aor}...")
        
        # Parse template
        front_matter, body = parse_issue_template(template_file)
        
        if not front_matter:
            print(f"  Warning: No front matter found in {template_file.name}")
            continue
        
        # Extract metadata
        title = front_matter.get('title', f"[{aor}] Post-v5.0 Retrofit Cleanup")
        labels = front_matter.get('labels', [])
        
        # Ensure labels is a list
        if isinstance(labels, str):
            labels = [label.strip() for label in labels.split(',')]
        
        # Create issue
        print(f"  Title: {title}")
        print(f"  Labels: {', '.join(labels)}")
        
        result = create_github_issue(
            token=args.token,
            title=title,
            body=body,
            labels=labels,
            dry_run=args.dry_run
        )
        
        if result:
            issue_number = result.get('number')
            issue_url = result.get('html_url')
            
            if args.dry_run:
                print(f"  ✓ [DRY RUN] Would create issue")
            else:
                print(f"  ✓ Created issue #{issue_number}")
                print(f"    URL: {issue_url}")
            
            created_issues.append({
                'aor': aor,
                'number': issue_number,
                'html_url': issue_url,
                'title': title
            })
        else:
            print(f"  ✗ Failed to create issue for {aor}")
            failed.append(aor)
    
    # Summary
    print("\n" + "="*70)
    print(f"Summary: {len(created_issues)} created, {len(failed)} failed")
    print("="*70)
    
    if created_issues:
        print("\nCreated issues:")
        for issue in created_issues:
            if args.dry_run:
                print(f"  [{issue['aor']}] {issue['title']} (DRY RUN)")
            else:
                print(f"  [{issue['aor']}] #{issue['number']}: {issue['title']}")
                print(f"    {issue['html_url']}")
    
    if failed:
        print("\nFailed:")
        for aor in failed:
            print(f"  - {aor}")
    
    # Update tracking file
    if created_issues and not args.dry_run and not args.no_update_tracking:
        print("\nUpdating tracking file...")
        update_tracking_file(created_issues)
    
    print("\nDone!")
    
    return 0 if not failed else 1


if __name__ == '__main__':
    sys.exit(main())
