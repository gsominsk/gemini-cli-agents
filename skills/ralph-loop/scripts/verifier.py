import sys
import subprocess
import json
import os

def run_command(command):
    """Runs a shell command and returns its output and exit code."""
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        return {
            "command": command,
            "exit_code": process.returncode,
            "stdout": stdout.strip(),
            "stderr": stderr.strip()
        }
    except Exception as e:
        return {
            "command": command,
            "exit_code": -1,
            "stdout": "",
            "stderr": str(e)
        }

def main():
    """
    Standardized Verifier for Ralph Loop.
    Usage: python verifier.py '["npm test", "npm run lint"]'
    """
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No commands provided. Usage: verifier.py '<json_list_of_commands>'"}))
        sys.exit(1)

    try:
        commands = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON input."}))
        sys.exit(1)

    results = []
    all_passed = True

    for cmd in commands:
        res = run_command(cmd)
        results.append(res)
        if res["exit_code"] != 0:
            all_passed = False

    output = {
        "status": "SUCCESS" if all_passed else "FAIL",
        "results": results
    }

    print(json.dumps(output, indent=2))
    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
