# 🚀 End-to-End Crypto Data Engineering Pipeline

## 📌 Project Overview

This project implements a production-style **ETL (Extract, Transform, Load) pipeline** for cryptocurrency market data.

The pipeline:

- Extracts real-time cryptocurrency data from a public API
- Stores raw JSON data in MongoDB Atlas (Cloud)
- Transforms and validates the dataset
- Loads structured data into Neon PostgreSQL (Cloud) using SQLAlchemy
- Maintains local backups:
  - Raw data → Local MongoDB
  - Transformed data → Local PostgreSQL
- Runs automatically every day at 12:00 AM using a cron job

This project demonstrates real-world data engineering concepts including cloud database integration, ORM usage, validation testing, backup strategy, and scheduled batch processing.

---

## 🏗️ Architecture

Crypto API  
   ↓  
Extract Layer  
   ↓  
MongoDB Atlas (Raw Data - Cloud)  
   ↓  
Transform Layer  
   ↓  
Assertion Testing (Data Validation)  
   ↓  
Neon PostgreSQL (Structured Data - Cloud) via SQLAlchemy  
   ↓  
Local Backups  
   • Raw → Local MongoDB  
   • Transformed → Local PostgreSQL  
   ↓  
Cron Job Scheduler (Runs Daily at 12:00 AM)

---

## 🛠️ Tech Stack

- Python
- Requests
- Pandas
- MongoDB Atlas (Cloud NoSQL Database)
- Local MongoDB (Backup)
- Neon PostgreSQL (Cloud Relational Database)
- Local PostgreSQL (Backup)
- SQLAlchemy (ORM)
- PyMongo
- Logging
- Cron (Linux Scheduler)
- Git

---

## 📂 Project Structure

```
End-to-End_Crypto_Pipeline/
│
├── extract.py          # Fetch crypto data & store raw in MongoDB Atlas
├── transform.py        # Clean and structure raw data
├── load.py             # Load structured data into Neon PostgreSQL using SQLAlchemy
├── backup_db.py        # Backup cloud databases to local DBs
├── test.py             # Assertion-based data validation
├── main.py             # Orchestrates full ETL pipeline
├── pipeline.log        # Execution logs
├── requirement.txt
└── README.md
```

---

## 🔄 Pipeline Workflow

### 1️⃣ Extract Layer

- Fetches cryptocurrency market data from API
- Stores raw JSON response in MongoDB Atlas
- Preserves unstructured data for auditing and reprocessing

---

### 2️⃣ Transform Layer

- Reads raw data from MongoDB Atlas
- Converts JSON into Pandas DataFrame
- Cleans and standardizes columns
- Handles missing values
- Prepares analytics-ready dataset

---

### 3️⃣ Data Validation (Assertion Testing)

Before loading, validation checks ensure:

- Required columns exist
- No null values in critical fields
- Numeric columns contain valid numeric data
- Dataset is not empty

This prevents corrupt or incomplete data from entering PostgreSQL.

---

### 4️⃣ Load Layer (Using SQLAlchemy)

- Connects to Neon PostgreSQL
- Uses SQLAlchemy engine for database operations
- Loads structured dataset into relational table
- Ensures scalable and maintainable DB interaction

---

### 5️⃣ Backup Strategy

To ensure disaster recovery:

- Raw cloud data (MongoDB Atlas) → backed up to Local MongoDB
- Structured cloud data (Neon PostgreSQL) → backed up to Local PostgreSQL

This ensures data redundancy and recovery capability.

---

## ⏰ Automation & Scheduling

The pipeline is fully automated using a Linux cron job.

It runs daily at 12:00 AM.

Example Cron Entry:

0 0 * * * /usr/bin/python3 /path/to/project/main.py >> /path/to/project/pipeline.log 2>&1

This ensures:

- Daily batch data ingestion
- Automated transformation and loading
- Scheduled backups
- Consistent, production-style execution

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

git clone https://github.com/Simbu06/End-to-End_Crypto_Pipeline.git  
cd End-to-End_Crypto_Pipeline  

### 2️⃣ Create Virtual Environment

python -m venv venv  

Activate:

Ubuntu/Mac:
source venv/bin/activate  

Windows:
venv\Scripts\activate  

### 3️⃣ Install Dependencies

pip install -r requirement.txt  

### 4️⃣ Configure Environment Variables

Set your connection strings:

MONGO_ATLAS_URI=your_cloud_mongo_uri  
LOCAL_MONGO_URI=your_local_mongo_uri  
NEON_POSTGRES_URI=your_cloud_postgres_uri  
LOCAL_POSTGRES_URI=your_local_postgres_uri  

---

### 5️⃣ Run Pipeline

python main.py  

---

## 📊 Output

- Raw crypto data stored in MongoDB Atlas
- Clean structured data stored in Neon PostgreSQL
- Local MongoDB backup created
- Local PostgreSQL backup created
- Logs stored in `pipeline.log`

---

## 🧠 Data Engineering Concepts Demonstrated

- Raw vs Processed Data Separation
- Cloud NoSQL + Cloud Relational DB Integration
- SQLAlchemy ORM Usage
- Assertion-Based Data Validation
- Cloud-to-Local Backup Strategy
- Automated Batch Scheduling with Cron
- Modular ETL Architecture
- Logging & Error Handling

---

## 🚀 Future Improvements

- Docker containerization
- Apache Airflow orchestration
- Incremental data loading
- CI/CD using GitHub Actions
- Monitoring and alerting integration
- Data quality framework (Pandera / Great Expectations)

---

## 👨‍💻 Author

Silambarasan R  