# CI/CD Deployment of Flask and Express on EC2 with Jenkins

## 📦 Architecture
- Single EC2 Instance (Ubuntu)
- Flask on port 5000
- Express on port 3000
- Managed with PM2
- Jenkins on port 8080

## ⚙️ Deployment Steps
1. Launch EC2, open required ports.
2. Install dependencies (Python, Node, Git, PM2).
3. Clone and run both apps.
4. Install Jenkins and plugins.
5. Create Jenkins Pipelines using `Jenkinsfile`.
6. (Optional) Configure GitHub Webhooks for auto-trigger.
