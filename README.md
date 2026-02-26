# 🚀 Data Engineering Project

## 📌 Overview

This project sets up a local data engineering environment using Docker and Apache Airflow. The goal is to simulate a real-world data pipeline environment that is portable, reproducible, and production-oriented.

---

## 🧱 Tech Stack

* Python
* Apache Airflow
* Docker
* PostgreSQL
* Git

---

## ⚙️ Phase 1 — Airflow Setup with Docker

### 1. Create project structure

```bash
mkdir data-engineering-project
cd data-engineering-project
git init
```

📌 Initializes a new Git repository for version control.

---

### 2. Create `.gitignore`

Prevents unnecessary files from being tracked (logs, cache, etc.)

---

### 3. Create project folders

```bash
mkdir dags docker scripts data logs plugins config
touch docker-compose.yml .env README.md
```

📌 Organizes the project in a scalable structure.

---

### 4. Configure environment variables

```env
AIRFLOW_UID=50000
```

📌 Prevents permission issues in Docker containers.

---

### 5. Create `docker-compose.yml`

Defines services:

* PostgreSQL → metadata database
* Airflow Webserver → UI
* Airflow Scheduler → DAG execution

---

### 6. Initialize Airflow database

```bash
docker compose run airflow-webserver airflow db init
```

📌 Creates metadata tables.

---

### 7. Create Airflow user

```bash
docker compose run airflow-webserver airflow users create \
  --username admin \
  --password admin \
  --firstname Mauricio \
  --lastname Cerpa \
  --role Admin \
  --email admin@example.com
```

📌 Required to access the UI.

---

### 8. Start services

```bash
docker compose up
```

📌 Launches all containers.

---

### 9. Access Airflow

```
http://localhost:8080
```

---

### 10. Create first DAG

```python
def hello():
    print("Hola Mauricio 👋")
```

📌 Validates that Airflow is working correctly.

---

## 📦 Version Control

```bash
git add .
git commit -m "Initial setup with Airflow and Docker"
git push -u origin main
```

📌 Ensures project reproducibility and collaboration.

---

## 💻 How to run this project on another machine

```bash
git clone <repo-url>
cd data-engineering-project

docker compose run airflow-webserver airflow db init
docker compose run airflow-webserver airflow users create ...
docker compose up
```

---

## 🧠 Key Learnings

* How to set up Apache Airflow using Docker
* How to structure a data engineering project
* How to use Git for version control
* How to create and run DAGs
* Understanding Airflow components (webserver, scheduler, metadata DB)
* Building reproducible environments

---

## 🚀 Next Steps

* Add PySpark jobs
* Integrate Spark with Airflow
* Add dbt for transformations
* Load data into Snowflake
* Deploy pipelines in AWS (EMR)
