# 🚀 End-to-End Crypto Data Pipeline

## 📌 Project Overview

This project implements a complete **ETL (Extract, Transform, Load) pipeline** that collects real-time cryptocurrency market data from a public API, processes it, and stores it for further analysis.

The objective of this project is to demonstrate core **Data Engineering skills**, including API ingestion, data transformation, structured storage, logging, and modular pipeline design.

---

## 🏗️ Architecture

Crypto API → Extract → Transform → Load → Storage (CSV / Database)

---

## 🛠️ Tech Stack

- Python
- Pandas
- Requests
- PostgreSQL (Optional)
- Logging module
- Git

---

## 📂 Project Structure

```
End-to-End_Crypto_Pipeline/
│
├── extract.py        # Fetch data from Crypto API
├── transform.py      # Clean and structure raw data
├── load.py           # Store data into DB / CSV
├── main.py           # Orchestrates the pipeline
├── backup_db.py      # Database backup script
├── transformed_crypto_data.csv
├── pipeline.log
├── requirement.txt
└── README.md
```

---

## 🔄 Pipeline Workflow

### 1️⃣ Extract
- Connects to cryptocurrency API
- Fetches market data (price, volume, market cap, etc.)
- Returns raw JSON data

### 2️⃣ Transform
- Converts JSON into Pandas DataFrame
- Cleans unnecessary columns
- Standardizes column names
- Structures dataset for storage

### 3️⃣ Load
- Loads processed data into:
  - CSV file
  - OR PostgreSQL database

### 4️⃣ Logging
- Logs pipeline execution steps
- Captures errors and success messages in `pipeline.log`

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Simbu06/End-to-End_Crypto_Pipeline.git
cd End-to-End_Crypto_Pipeline
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

**Ubuntu / Mac**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirement.txt
```

### 4️⃣ Run the Pipeline

```bash
python main.py
```

---

## 📊 Output

- `transformed_crypto_data.csv`
- Updated database table (if configured)
- `pipeline.log` file with execution details

---

## 📈 Future Improvements

- Add Docker containerization
- Integrate Apache Airflow for orchestration
- Implement automated scheduling
- Add CI/CD using GitHub Actions
- Deploy on AWS or Azure
- Add data visualization dashboard

---

## 💡 Key Learning Outcomes

- Designed modular ETL architecture
- Worked with REST APIs
- Implemented data cleaning using Pandas
- Applied structured logging
- Built scalable project structure

---

## 👨‍💻 Author

**Silambarasan R**  
Aspiring Data Engineer  
Chennai, India