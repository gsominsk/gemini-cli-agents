import os
import json
import shutil
from datetime import datetime
import sys

def archive_session(project_path):
    """Archives the current Ralph Loop session data if the branch has changed."""
    prd_path = os.path.join(project_path, "prd.json")
    last_branch_path = os.path.join(project_path, ".last-branch")
    archive_dir = os.path.join(project_path, "archive")

    if not os.path.exists(prd_path):
        print("Error: prd.json not found.")
        return

    # Read current branch
    try:
        with open(prd_path, "r") as f:
            prd = json.load(f)
        current_branch = prd.get("branchName", "")
    except Exception as e:
        print(f"Error reading prd.json: {e}")
        return

    # Read last branch
    last_branch = ""
    if os.path.exists(last_branch_path):
        with open(last_branch_path, "r") as f:
            last_branch = f.read().strip()

    # If branch changed, archive the old one
    if last_branch and current_branch and last_branch != current_branch:
        date_str = datetime.now().strftime("%Y-%m-%d")
        folder_name = last_branch.replace("ralph/", "")
        target_archive = os.path.join(archive_dir, f"{date_str}-{folder_name}")

        print(f"Branch changed from '{last_branch}' to '{current_branch}'. Archiving old session...")
        os.makedirs(target_archive, exist_ok=True)

        # Archive prd.json, memory-bank, and AGENTS.md (as a snapshot)
        shutil.copy2(prd_path, os.path.join(target_archive, "prd.json"))
        
        mb_src = os.path.join(project_path, "memory-bank")
        if os.path.exists(mb_src):
            shutil.copytree(mb_src, os.path.join(target_archive, "memory-bank"), dirs_exist_ok=True)
        
        print(f"Archived to: {target_archive}")

        # Update .last-branch
        with open(last_branch_path, "w") as f:
            f.write(current_branch)
    else:
        print("No branch change detected or no previous branch recorded. Skipping archive.")
        if current_branch:
            with open(last_branch_path, "w") as f:
                f.write(current_branch)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    archive_session(os.path.abspath(target))
