import os
import subprocess
from datetime import datetime

BASE_DIR = "job-system"

folders = [
    "emails/corrections",
    "emails/applications",
    "emails/followups",
    "interviews/answers",
    "interviews/companies",
    "interviews/strategies",
    "job-search/tracker",
    "job-search/companies",
    "job-search/roles",
    "templates",
    "notes"
]

files = {
    "README.md": "# Job Search System\n\nOrganized job tracking and interview prep.\n",
    "templates/email_templates.md": "# Email Templates\n\n## Correction Email\n\nUse for fixing mistakes.\n",
    "interviews/strategies/general_strategy.md": "# Interview Strategy\n\n- Use STAR method\n- Focus on impact\n",
    "job-search/tracker/job_tracker.md": "# Job Tracker\n\n| Company | Role | Status | Notes |\n|--------|------|--------|------|\n"
}


def run(cmd):
    subprocess.run(cmd, shell=True)


def create_structure():
    print("Creating folders...")
    for folder in folders:
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

    print("Creating files...")
    for path, content in files.items():
        full_path = os.path.join(BASE_DIR, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)


def init_git():
    print("Initializing git...")
    os.chdir(BASE_DIR)
    run("git init")
    run("git add .")
    run('git commit -m "Initial commit"')


def add_entry():
    title = input("Enter title: ").strip().replace(" ", "_")
    category = input("Category (emails/interviews/notes): ").strip()

    filename = f"{title}.md"
    filepath = os.path.join(BASE_DIR, category, filename)

    content = f"# {title.replace('_', ' ')}\n\nCreated: {datetime.now()}\n\n"

    with open(filepath, "w") as f:
        f.write(content)

    print(f"Created: {filepath}")


def git_commit_push():
    os.chdir(BASE_DIR)
    msg = f"update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    run("git add .")
    run(f'git commit -m "{msg}"')
    run("git push")


if __name__ == "__main__":
    print("1. Setup project")
    print("2. Add new entry")
    print("3. Commit & push")

    choice = input("Select option: ")

    if choice == "1":
        create_structure()
        init_git()
    elif choice == "2":
        add_entry()
    elif choice == "3":
        git_commit_push()
