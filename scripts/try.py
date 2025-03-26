#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys

def main():
  parser = argparse.ArgumentParser(
    description="Exexutes a portion of the tests for a specific data structure problem."
  )
  
  parser.add_argument("-t", required=True, help="Data structure type (ll, bt, etc.)")
  parser.add_argument("-n", required=True, help="Problem index")
  args = parser.parse_args()

  test_filename = f"t{args.t}_{args.n}{args.n}.py"

  # Allows the script to be executed from any directory
  script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of this script
  project_root = os.path.abspath(os.path.join(script_dir, ".."))  # Root of the project

  test_file_path = os.path.join(project_root, "tests", test_filename)
  
  # Check if the test file exists
  if not os.path.isfile(test_file_path):
    print(f'Test file "{test_file_path}" does not exist.')
    sys.exit(1)

  to_run_test = " or ".join([f'Test {i+1}' for i in range(5)])
  
  result = subprocess.run(["pytest", test_file_path, "-q", "-k", to_run_test])
  sys.exit(result.returncode)

if __name__ == "__main__":
  main()
