**Task App — Full DevOps Pipeline (Flask + Kubernetes + CI/CD + Monitoring)**

A simple task-management app built to demonstrate a complete, real-world DevOps workflow — from local development to a containerized, orchestrated, automatically deployed, and monitored application.


**What this project demonstrates?**

Backend: Python (Flask) REST API with SQLite persistence

Frontend: Lightweight HTML/JS UI served by Flask

Containerization: Dockerized app, image hosted on Docker Hub

Orchestration: Deployed to Kubernetes with a Deployment, Service, and horizontal scaling (tested at 3 replicas)

CI: GitHub Actions automatically runs the test suite (pytest) on every push

CD: On a successful test run, GitHub Actions automatically builds and pushes a new Docker image to Docker Hub

Monitoring: Prometheus + Grafana installed on the cluster via Helm, with live dashboards for cluster and pod resource usage
Architecture

Local dev (Flask + SQLite)

        │
        ▼
        
   Docker image ──► Docker Hub
   
        │
        ▼
        
  Kubernetes cluster
  
   ├── Deployment (task-app, scalable replicas)
   
   ├── Service (NodePort)
   
   └── Monitoring namespace
   
        ├── Prometheus (metrics collection)
        
        └── Grafana (dashboards)
        

GitHub push → GitHub Actions

   ├── Job 1: Run tests (pytest)
   
   └── Job 2: Build & push Docker image (on success)
   
Tech stack

Layer	Tool

Backend	Python, Flask, SQLite

Containers	Docker

Registry	Docker Hub

Orchestration	Kubernetes (kubectl, YAML manifests)

CI/CD	GitHub Actions

Monitoring	Prometheus, Grafana (via Helm)

Running it locally

bash

python -m venv venv

venv\Scripts\Activate.ps1       

pip install -r requirements.txt

python app.py


Visit http://127.0.0.1:5000/home

Running with Docker

bash

docker build -t task-app .

docker run -p 5000:5000 task-app

Deploying to Kubernetes

bash

kubectl apply -f k8s/deployment.yaml

kubectl apply -f k8s/service.yaml

kubectl port-forward svc/task-app-service 5000:5000

Running tests

bash

pytest

**What I learned building this?**

Building this project meant working through real infrastructure problems, not just following a tutorial — including Docker container networking (binding to 0.0.0.0 vs 127.0.0.1), Kubernetes image pull policies and local cluster networking quirks, securely managing credentials in CI/CD with GitHub Secrets, and diagnosing a database initialization bug that only surfaced in a clean CI environment.
