#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys

def build_test_path(structure_type: str, problem_index: int) -> str:
  """Returns the absolute path to the test file for the given problem."""
  test_filename = f"t{structure_type}_{problem_index:02}.py"
  root_dir = os.path.dirname(os.path.realpath(__file__))
  return os.path.join(root_dir, "tests", f"t{structure_type}", test_filename)

def run_pytest(test_file: str) -> int:
  '''
    Runs pytest with the given test file.
    Returns the return code of the pytest process.
  '''
  cmd = ["pytest", test_file, "--tb=no", "--disable-warnings"]
  result = subprocess.run(cmd)
  return result.returncode

def main():
  parser = argparse.ArgumentParser(
    description="Executes tests for a specific data structure problem."
  )
  parser.add_argument("-t", required=True, help="Data structure type (e.g., ll, bt, etc.)")
  parser.add_argument("-n", required=True, type=int, help="Problem index number")
  args = parser.parse_args()

  test_file_path = build_test_path(args.t, args.n)

  if not os.path.isfile(test_file_path):
    print(f'❌ Test file "{test_file_path}" does not exist.')
    sys.exit(1)

  returncode = run_pytest(test_file_path)
  sys.exit(returncode)

if __name__ == "__main__":
  main()
