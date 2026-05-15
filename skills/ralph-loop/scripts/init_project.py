import os
import json
import sys
import shutil
from datetime import datetime

def init_project(project_path):
    """Initializes the Ralph Loop environment with Memory Bank support."""
    print(f"Initializing Ralph Loop in: {project_path}")
    
    # 1. Create Memory Bank directory
    mb_dir = os.path.join(project_path, "memory-bank")
    os.makedirs(mb_dir, exist_ok=True)
    print(f"Created: {mb_dir}")

    # 2. Define Memory Bank templates (minimal)
    mb_files = {
        "productContext.md": "# Product Context\n\n## Purpose\n[Describe the project's core mission]\n",
        "activeContext.md": "# Active Context\n\n## Current Focus\n- Initial project setup.\n",
        "progress.md": "# Progress\n\n## Completed Tasks\n- [x] Initialize Memory Bank.\n",
        "decisionLog.md": "# Decision Log\n\n## Decisions\n- [2026-05-15] Use Memory Bank for context preservation.\n",
        "systemPatterns.md": "# System Patterns\n\n## Patterns\n- Standard Gemini CLI Skill structure.\n"
    }

    for filename, content in mb_files.items():
        file_path = os.path.join(mb_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)
            print(f"Created: {file_path}")

    # 3. Initialize prd.json
    prd_path = os.path.join(project_path, "prd.json")
    if not os.path.exists(prd_path):
        initial_prd = {
            "project": os.path.basename(project_path),
            "branchName": "ralph/initial-setup",
            "description": "Initial project setup and configuration",
            "userStories": []
        }
        with open(prd_path, "w") as f:
            json.dump(initial_prd, f, indent=2)
        print(f"Initialized: {prd_path}")

    # 4. Initialize AGENTS.md
    agents_path = os.path.join(project_path, "AGENTS.md")
    if not os.path.exists(agents_path):
        with open(agents_path, "w") as f:
            f.write("# Codebase Knowledge\n\n## General Patterns\n- Use `ralph-loop` for task management.\n- Use `memory-bank/` for persistent context.\n")
        print(f"Initialized: {agents_path}")

    # 5. Initialize .last-branch for archiver logic
    last_branch_path = os.path.join(project_path, ".last-branch")
    if not os.path.exists(last_branch_path):
        with open(last_branch_path, "w") as f:
            f.write("ralph/initial-setup")

    print("Initialization complete.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    init_project(os.path.abspath(target))
