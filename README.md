# Real-Time Sales & Operations Analytics Pipeline

An end-to-end batch data engineering project that automates sales data ingestion, validation, transformation, and analytics using **Python, SQL, Apache Airflow, and PostgreSQL**. The project demonstrates ETL workflow orchestration, data quality checks, KPI generation, and analytics-ready outputs for dashboards and AI/data workflows.

---

## Project Overview

This pipeline simulates a retail sales analytics workflow and processes transactional sales data through multiple stages:

Raw Sales Data → Validation → Cleaning → Transformation → PostgreSQL → SQL Analytics → Dashboard Outputs

---

## Tech Stack

* **Python** (Pandas)
* **SQL**
* **PostgreSQL**
* **Apache Airflow**
* **Docker** (project-ready structure)
* **Power BI** (dashboard-ready outputs)
* **Git & GitHub**

---

## Key Features

* Automated ETL pipeline for sales data
* Data quality validation (missing values, duplicates, schema checks)
* Revenue and business KPI calculations
* Airflow DAG orchestration with task dependencies
* SQL analytics for regional, product, and daily sales insights
* Dashboard-ready processed dataset generation
* Modular and maintainable project structure

---

## Repository Structure

```text
airflow/        # Airflow DAGs
etl/            # ETL scripts
sql/            # Database schema and analytics queries
data/           # Raw and processed datasets
dashboard/      # Dashboard screenshots/assets
docs/           # Architecture diagram and documentation
```

---

## Airflow Workflow

The Airflow DAG contains three logical stages:

* `run_staging` – ingest and stage raw sales data
* `run_tests` – execute data quality checks
* `run_marts` – create analytics-ready transformed outputs

---

## Sample KPIs Generated

* Total Revenue
* Total Orders
* Units Sold
* Average Order Value
* Revenue by Region
* Revenue by Category
* Top Products
* Daily Sales Trend
* Cancellation Rate

---

## Dashboard Outputs

The processed dataset is prepared for Power BI visualizations, including KPI cards, revenue trends, regional performance, and product analytics. Dashboard screenshots are available in the `dashboard/` folder.

---

## Learning Outcomes

Through this project I practiced:

* ETL pipeline development
* Workflow orchestration with Airflow
* SQL analytics and reporting
* Data cleaning and validation
* Relational database loading
* Analytics-ready data modeling
* Git/GitHub project management

---

## Author

**Anil Vaidana**

* GitHub: https://github.com/AnilVaidana
* LinkedIn: Add your LinkedIn profile URL here
