# Automated GitHub Issue Creation for Portal Retrofit Cleanup

This document explains how to automatically create GitHub issues for post-v5.0 retrofit cleanup across all STK portals.

## Overview

The `create_portal_issues.py` script automates the creation of GitHub issues from the generated issue templates in `.github/ISSUE_TEMPLATES/portal-retrofit/`. It uses the GitHub REST API to create issues with proper labels and tracking.

## Prerequisites

1. **Python 3.6+** with `requests` library:
   ```bash
   pip install requests
   ```

2. **GitHub Personal Access Token** with `repo` scope:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scope: `repo` (Full control of private repositories)
   - Copy the generated token

## Usage

### Basic Usage - Create All Issues

```bash
# Set your GitHub token
export GITHUB_TOKEN="your_github_token_here"

# Create all 12 portal issues
python scripts/create_portal_issues.py --token $GITHUB_TOKEN
```

### Dry Run (Preview)

Preview what would be created without actually creating issues:

```bash
python scripts/create_portal_issues.py --token $GITHUB_TOKEN --dry-run
```

### Create Issues for Specific Portals

```bash
# Create issues for CM, CERT, and SAF only
python scripts/create_portal_issues.py --token $GITHUB_TOKEN --portal CM CERT SAF
```

### Skip Tracking File Update

```bash
# Create issues but don't update TRACKING.md
python scripts/create_portal_issues.py --token $GITHUB_TOKEN --no-update-tracking
```

## What the Script Does

1. **Reads issue templates** from `.github/ISSUE_TEMPLATES/portal-retrofit/`
2. **Parses front matter** (title, labels) and body content
3. **Creates GitHub issues** via REST API with:
   - Portal-specific title (e.g., "[CM] Post-v5.0 Retrofit Cleanup")
   - Appropriate labels (nomenclature-v5.0, cleanup, <aor>)
   - Complete issue body with tasks and acceptance criteria
4. **Updates TRACKING.md** with created issue numbers and URLs

## Output

The script provides detailed output:

```
Found 12 issue template(s) to process
======================================================================

Processing CM...
  Title: [CM] Post-v5.0 Retrofit Cleanup
  Labels: nomenclature-v5.0, cleanup, cm
  ✓ Created issue #123
    URL: https://github.com/AmedeoPelliccia/AMPEL360-SPACE-T/issues/123

Processing CERT...
  Title: [CERT] Post-v5.0 Retrofit Cleanup
  Labels: nomenclature-v5.0, cleanup, cert
  ✓ Created issue #124
    URL: https://github.com/AmedeoPelliccia/AMPEL360-SPACE-T/issues/124

...

======================================================================
Summary: 12 created, 0 failed
======================================================================
```

## Tracking

After creation, the script automatically updates `.github/ISSUE_TEMPLATES/portal-retrofit/TRACKING.md` with:
- Issue numbers
- Issue URLs
- Creation status

## Troubleshooting

### Authentication Error

```
Error creating issue: 401 Client Error: Unauthorized
```

**Solution:** Check that your GitHub token:
- Is valid and not expired
- Has `repo` scope enabled
- Is correctly set in the environment variable

### Rate Limiting

```
Error creating issue: 403 Client Error: rate limit exceeded
```

**Solution:** GitHub API has rate limits. Wait and try again, or:
- Use `--portal` to create issues in smaller batches
- Check your rate limit: https://api.github.com/rate_limit

### Template Not Found

```
Error: Templates directory not found
```

**Solution:** Ensure you're running the script from the repository root:
```bash
cd /path/to/AMPEL360-SPACE-T
python scripts/create_portal_issues.py --token $GITHUB_TOKEN
```

## Security Best Practices

1. **Never commit tokens** to the repository
2. **Use environment variables** for tokens
3. **Revoke tokens** when no longer needed
4. **Use fine-grained tokens** when possible (GitHub's newer token type)

## Example Workflow

Complete workflow for creating all portal issues:

```bash
# 1. Set up environment
export GITHUB_TOKEN="ghp_your_token_here"

# 2. Dry run to preview
python scripts/create_portal_issues.py --token $GITHUB_TOKEN --dry-run

# 3. Create issues
python scripts/create_portal_issues.py --token $GITHUB_TOKEN

# 4. Verify issues were created
# Check: https://github.com/AmedeoPelliccia/AMPEL360-SPACE-T/issues

# 5. Review tracking file
cat .github/ISSUE_TEMPLATES/portal-retrofit/TRACKING.md
```

## Alternative: Manual Creation via GitHub CLI

If you prefer using `gh` CLI:

```bash
cd .github/ISSUE_TEMPLATES/portal-retrofit
for template in post-retrofit-cleanup-*.md; do
  gh issue create --body-file "$template" --repo AmedeoPelliccia/AMPEL360-SPACE-T
done
```

## Alternative: Manual Creation via GitHub UI

1. Go to: https://github.com/AmedeoPelliccia/AMPEL360-SPACE-T/issues/new
2. Copy content from: `.github/ISSUE_TEMPLATES/portal-retrofit/post-retrofit-cleanup-<aor>.md`
3. Paste into issue description
4. Click "Submit new issue"
5. Repeat for each portal

## Files

- **Script:** `scripts/create_portal_issues.py`
- **Templates:** `.github/ISSUE_TEMPLATES/portal-retrofit/post-retrofit-cleanup-*.md`
- **Tracking:** `.github/ISSUE_TEMPLATES/portal-retrofit/TRACKING.md`
- **This guide:** `.github/ISSUE_TEMPLATES/portal-retrofit/AUTOMATION_GUIDE.md`

## Support

For issues with the script:
1. Check this guide
2. Run with `--dry-run` to debug
3. Check GitHub API status: https://www.githubstatus.com/
4. Review script output for specific error messages

---

**Last Updated:** 2025-12-17  
**Script Version:** 1.0  
**Related:** Nomenclature v5.0 Retrofit
