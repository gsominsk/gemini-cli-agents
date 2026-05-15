import os
import json
import shutil
from datetime import datetime
import sys

def archive_session(project_path):
    """Archives the current Ralph Loop session data if the branch has changed."""
    last_branch_path = os.path.join(project_path, ".last-branch")
    archive_dir = os.path.join(project_path, "archive")

    # Read current branch from git
    try:
        current_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
    except:
        current_branch = "main"

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
ranch)
    else:
        print("No branch change detected or no previous branch recorded. Skipping archive.")
        if current_branch:
            with open(last_branch_path, "w") as f:
                f.write(current_branch)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    archive_session(os.path.abspath(target))
