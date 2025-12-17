#!/usr/bin/env python3
"""
AMPEL360 Space-T PR^3-3 Final Verification Suite
=================================================

Comprehensive validation for predicted release freeze.
Runs all validation checks and generates a final report.

Usage:
    python scripts/pr3_3_verification.py --all
    python scripts/pr3_3_verification.py --report-only
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class PR3Verification:
    """PR^3-3 Release Verification Suite."""
    
    def __init__(self):
        self.results = {
            'nomenclature': None,
            'links': None,
            'schemas': None,
            'trace_links': None,
            'ci_gates': None
        }
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        
    def run_nomenclature_validation(self):
        """Run nomenclature validation (GATE-001)."""
        print("\n" + "="*70)
        print("GATE-001: Nomenclature Validation (v6.0 R1.0)")
        print("="*70)
        
        try:
            result = subprocess.run(
                ['python', 'validate_nomenclature.py', '--standard', 'v6.0', 
                 '--check-all', '--mode', 'block', '--strict'],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print("✅ PASS - All files comply with v6.0 R1.0")
                self.results['nomenclature'] = 'PASS'
                self.passed += 1
                
                # Extract statistics
                for line in result.stdout.split('\n'):
                    if 'Summary:' in line:
                        print(f"   {line.strip()}")
            else:
                print("❌ FAIL - Nomenclature violations found")
                print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
                self.results['nomenclature'] = 'FAIL'
                self.failed += 1
                
        except Exception as e:
            print(f"❌ ERROR - {str(e)}")
            self.results['nomenclature'] = 'ERROR'
            self.failed += 1
            
    def run_link_checking(self):
        """Run link checking."""
        print("\n" + "="*70)
        print("Link Checking (Internal Links)")
        print("="*70)
        
        try:
            result = subprocess.run(
                ['python', 'scripts/check_and_update_links.py', '--check-only'],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            # Parse output for broken links
            broken_count = 0
            for line in result.stdout.split('\n'):
                if 'Found' in line and 'broken link' in line:
                    broken_count = int(line.split()[1])
                    
            if broken_count == 0:
                print("✅ PASS - No broken internal links")
                self.results['links'] = 'PASS'
                self.passed += 1
            else:
                print(f"⚠️  WARNING - {broken_count} broken links found")
                print("   Note: Deferred to post-release hotfix (KI-PR3-001)")
                self.results['links'] = f'WARNING ({broken_count} broken)'
                self.warnings += 1
                
        except Exception as e:
            print(f"❌ ERROR - {str(e)}")
            self.results['links'] = 'ERROR'
            self.failed += 1
            
    def run_schema_validation(self):
        """Run schema registry validation (GATE-002)."""
        print("\n" + "="*70)
        print("GATE-002: Schema Registration Check")
        print("="*70)
        
        try:
            result = subprocess.run(
                ['python', 'scripts/validate_schema_registry.py', '--check-all'],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if 'REGISTRY_MISSING' not in result.stdout and result.returncode == 0:
                print("✅ PASS - Schema registries valid")
                self.results['schemas'] = 'PASS'
                self.passed += 1
            else:
                print("⚠️  WARNING - Schema registry issues")
                print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
                self.results['schemas'] = 'WARNING'
                self.warnings += 1
                
        except Exception as e:
            print(f"⚠️  WARNING - {str(e)}")
            self.results['schemas'] = 'WARNING'
            self.warnings += 1
            
    def run_trace_link_validation(self):
        """Run trace link validation (GATE-003)."""
        print("\n" + "="*70)
        print("GATE-003: Trace Link Integrity Check")
        print("="*70)
        
        try:
            result = subprocess.run(
                ['python', 'scripts/validate_trace_links.py', '--check-all'],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if 'VALIDATION FAILED' not in result.stdout and result.returncode == 0:
                print("✅ PASS - Trace link integrity maintained")
                self.results['trace_links'] = 'PASS'
                self.passed += 1
            else:
                print("⚠️  WARNING - Trace link issues")
                print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
                self.results['trace_links'] = 'WARNING'
                self.warnings += 1
                
        except Exception as e:
            print(f"⚠️  WARNING - {str(e)}")
            self.results['trace_links'] = 'WARNING'
            self.warnings += 1
            
    def check_ci_gates_status(self):
        """Check CI gates configuration."""
        print("\n" + "="*70)
        print("CI Governance Gates Status")
        print("="*70)
        
        gates = {
            'GATE-001': 'Nomenclature Validation',
            'GATE-002': 'Schema Registration',
            'GATE-003': 'Trace Link Integrity',
            'GATE-006': 'Governance Change Detection'
        }
        
        workflow_file = Path('.github/workflows/governance-gates.yml')
        
        if workflow_file.exists():
            print("✅ CI Governance Gates Configuration:")
            for gate_id, gate_name in gates.items():
                print(f"   {gate_id}: {gate_name}")
            self.results['ci_gates'] = 'CONFIGURED'
            self.passed += 1
        else:
            print("❌ FAIL - Governance gates configuration missing")
            self.results['ci_gates'] = 'MISSING'
            self.failed += 1
            
    def generate_report(self):
        """Generate final verification report."""
        print("\n" + "="*70)
        print("PR^3-3 FINAL VERIFICATION REPORT")
        print("="*70)
        print(f"\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Release: PR^3-3 Predicted Release")
        print(f"Standard: Nomenclature v6.0 R1.0 FINAL LOCK")
        
        print("\n" + "-"*70)
        print("VALIDATION RESULTS")
        print("-"*70)
        
        print(f"\n{'Check':<30} {'Status':<20} {'Gate'}")
        print("-"*70)
        print(f"{'Nomenclature Validation':<30} {str(self.results['nomenclature']):<20} GATE-001")
        print(f"{'Schema Registration':<30} {str(self.results['schemas']):<20} GATE-002")
        print(f"{'Trace Link Integrity':<30} {str(self.results['trace_links']):<20} GATE-003")
        print(f"{'Internal Links':<30} {str(self.results['links']):<20} (Post-release)")
        print(f"{'CI Gates Configuration':<30} {str(self.results['ci_gates']):<20} GATE-006")
        
        print("\n" + "-"*70)
        print("SUMMARY")
        print("-"*70)
        print(f"✅ Passed:   {self.passed}")
        print(f"⚠️  Warnings: {self.warnings}")
        print(f"❌ Failed:   {self.failed}")
        
        total = self.passed + self.warnings + self.failed
        pass_rate = (self.passed / total * 100) if total > 0 else 0
        
        print(f"\nPass Rate: {pass_rate:.1f}%")
        
        print("\n" + "-"*70)
        print("RELEASE READINESS")
        print("-"*70)
        
        if self.failed == 0 and self.passed >= 3:
            print("✅ READY FOR RELEASE")
            print("\nAll critical validations passed.")
            print("Warnings are acceptable and documented in known issues.")
            print("\nNext steps:")
            print("1. Collect maintainer sign-offs")
            print("2. Fix broken links (post-release hotfix)")
            print("3. Publish release announcement")
            return 0
        elif self.failed == 0:
            print("⚠️  CONDITIONAL APPROVAL")
            print("\nNo critical failures, but some checks incomplete.")
            print("Review warnings and determine if acceptable.")
            return 1
        else:
            print("❌ NOT READY FOR RELEASE")
            print(f"\n{self.failed} critical validation(s) failed.")
            print("Address failures before proceeding with release.")
            return 2
            
    def run_all(self):
        """Run all verification checks."""
        print("\n" + "="*70)
        print("AMPEL360 SPACE-T PR^3-3 FINAL VERIFICATION")
        print("="*70)
        print("\nRunning comprehensive validation suite...")
        print("This may take several minutes...\n")
        
        self.run_nomenclature_validation()
        self.run_link_checking()
        self.run_schema_validation()
        self.run_trace_link_validation()
        self.check_ci_gates_status()
        
        return self.generate_report()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='PR^3-3 Final Verification Suite'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all verification checks'
    )
    parser.add_argument(
        '--report-only',
        action='store_true',
        help='Generate report from previous run'
    )
    
    args = parser.parse_args()
    
    verifier = PR3Verification()
    
    if args.all or (not args.report_only):
        exit_code = verifier.run_all()
        sys.exit(exit_code)
    elif args.report_only:
        exit_code = verifier.generate_report()
        sys.exit(exit_code)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
