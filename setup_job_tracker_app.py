import os

BASE_DIR = "job-tracker-app"

# Folder structure
folders = [
    # Docs
    "docs/01-reality-check",
    "docs/02-iphone-apps",
    "docs/03-freelancer-aws-ai",
    "docs/04-advanced-apps",
    "docs/05-job-tracker-product",

    # Backend
    "backend/src/handlers",
    "backend/src/services",
    "backend/src/models",
    "backend/src/utils",

    # Frontend
    "frontend/lib/screens",
    "frontend/lib/services",

    # Infra
    "infra/aws/lambda",
    "infra/aws/api-gateway",
    "infra/aws/dynamodb",
    "infra/terraform",

    # Scripts
    "scripts"
]

# Files with starter content
files = {
    # Root
    "README.md": "# Job Tracker App\n\nFull-stack job tracking system.\n",

    # Docs
    "docs/01-reality-check/rdf.md": "# Reality Definition\n",
    "docs/01-reality-check/architecture.md": "# Architecture\n",
    "docs/01-reality-check/solution-design.md": "# Solution Design\n",
    "docs/01-reality-check/tasks.md": "# Tasks\n",

    "docs/02-iphone-apps/rdf.md": "# iPhone Apps RDF\n",
    "docs/02-iphone-apps/architecture.md": "# Architecture\n",
    "docs/02-iphone-apps/database.md": "# Database\n",
    "docs/02-iphone-apps/solution-design.md": "# Solution Design\n",
    "docs/02-iphone-apps/tasks.md": "# Tasks\n",

    "docs/03-freelancer-aws-ai/rdf.md": "# Freelancer AWS AI\n",
    "docs/03-freelancer-aws-ai/architecture.md": "# Architecture\n",
    "docs/03-freelancer-aws-ai/solution-design.md": "# Solution Design\n",
    "docs/03-freelancer-aws-ai/tasks.md": "# Tasks\n",

    "docs/04-advanced-apps/rdf.md": "# Advanced Apps\n",
    "docs/04-advanced-apps/architecture.md": "# Architecture\n",
    "docs/04-advanced-apps/solution-design.md": "# Solution Design\n",
    "docs/04-advanced-apps/tasks.md": "# Tasks\n",

    "docs/05-job-tracker-product/rdf.md": "# Product RDF\n",
    "docs/05-job-tracker-product/architecture.md": "# Architecture\n",
    "docs/05-job-tracker-product/database.md": "# Database\n",
    "docs/05-job-tracker-product/solution-design.md": "# Solution Design\n",
    "docs/05-job-tracker-product/low-level-design.md": "# Low Level Design\n",
    "docs/05-job-tracker-product/api-spec.md": "# API Spec\n",
    "docs/05-job-tracker-product/cost-estimation.md": "# Cost Estimation\n",
    "docs/05-job-tracker-product/roadmap.md": "# Roadmap\n",

    # Backend
    "backend/src/handlers/createJob.js": "// create job handler\n",
    "backend/src/handlers/getJobs.js": "// get jobs handler\n",
    "backend/src/handlers/updateJob.js": "// update job handler\n",
    "backend/src/handlers/deleteJob.js": "// delete job handler\n",

    "backend/src/services/dynamodb.js": "// dynamodb service\n",
    "backend/src/services/auth.js": "// auth service\n",

    "backend/src/models/jobModel.js": "// job model\n",
    "backend/src/utils/response.js": "// response util\n",

    "backend/serverless.yml": "# Serverless config\n",
    "backend/package.json": "{\n  \"name\": \"job-tracker-backend\"\n}\n",

    # Frontend
    "frontend/lib/main.dart": "// Flutter entry point\n",
    "frontend/lib/screens/dashboard.dart": "// dashboard screen\n",
    "frontend/lib/screens/job_list.dart": "// job list\n",
    "frontend/lib/screens/job_detail.dart": "// job detail\n",
    "frontend/lib/screens/add_job.dart": "// add job\n",

    "frontend/lib/services/api_service.dart": "// API service\n",
    "frontend/pubspec.yaml": "name: job_tracker_app\n",

    # Scripts
    "scripts/deploy.sh": "#!/bin/bash\necho Deploying...\n"
}


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

    print("✅ Project created successfully!")


if __name__ == "__main__":
    create_structure()
