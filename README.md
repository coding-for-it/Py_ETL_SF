# Python + Snowflake ETL Pipeline

## Overview

An end-to-end ETL (Extract, Transform, Load) pipeline built using **Python and Snowflake** to process, transform, and analyze sales data.

The pipeline extracts raw data from CSV files, performs data cleaning and transformation using Python, validates data quality, loads processed data into Snowflake, and performs SQL-based analytics to generate business insights.

## Architecture

```
CSV Data Source

        ↓

Snowflake Internal Stage

        ↓

COPY INTO Command

        ↓

Raw / Sales Table

        ↓

Python Transformation & Validation

        ↓

Analytics Layer

        ↓

SQL Business Insights
```

## Tech Stack

* Python
* Pandas
* Snowflake
* SQL
* Snowflake Connector for Python
* Python-dotenv

## Project Structure

```
snowflake_etl_project
│
├── data
│   └── sales.csv
│
├── src
│   ├── db.py              # Snowflake connection
│   ├── extract.py         # Data extraction
│   ├── transform.py       # Data cleaning and transformation
│   ├── load.py            # Load data into Snowflake
│   └── main.py            # ETL pipeline execution
│
├── sql
│   └── analytics.sql      # SQL analytics queries
│
├── logs
│   └── etl.log            # Execution logs
│
├── .env                   # Snowflake credentials
├── requirements.txt
└── README.md
```

## ETL Workflow

### 1. Extract

* Reads sales data from CSV files using Pandas.
* Converts raw data into a structured format for processing.

### 2. Transform

Data preprocessing and transformation includes:

* Removing duplicate records
* Handling missing values
* Creating calculated business metrics

Example:

```
TOTAL_SALES = QUANTITY × PRICE
```

### 3. Data Quality Validation

Implemented validation checks:

* Missing value detection
* Duplicate record identification
* Pipeline execution logging

### 4. Load

* Creates a connection between Python and Snowflake.
* Loads transformed sales data into Snowflake tables.
* Stores processed data for analytics.

## Snowflake Database Design

Database:

```
ETL_DB
```

Schema:

```
SALES_SCHEMA
```

Table:

```
SALES
```

Table Structure:

| Column        | Description              |
| ------------- | ------------------------ |
| ORDER_ID      | Unique order identifier  |
| CUSTOMER_NAME | Customer information     |
| PRODUCT       | Product name             |
| QUANTITY      | Quantity purchased       |
| PRICE         | Product price            |
| ORDER_DATE    | Order date               |
| TOTAL_SALES   | Calculated sales revenue |

## Analytics Performed

SQL analytics implemented:

### Revenue Analysis

* Total sales revenue calculation
* Overall business performance analysis

### Product Analysis

* Product-wise sales analysis
* Identification of high-performing products

### Monthly Sales Trends

* Sales analysis based on order dates
* Business trend evaluation

## Installation & Setup

Clone repository:

```bash
git clone <repository-url>
```

Navigate to project:

```bash
cd snowflake_etl_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure Snowflake credentials in `.env`:

```env
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
```

## Run Pipeline

Execute ETL workflow:

```bash
python src/main.py
```

Pipeline execution:

```
Extract Data
      ↓
Transform Data
      ↓
Validate Data
      ↓
Load Into Snowflake
      ↓
Run Analytics
```

## Key Features

- End-to-end ETL pipeline implementation
- Python and Snowflake integration
- Snowflake Internal Stage for file ingestion
- COPY INTO command for bulk data loading
- Data cleaning and transformation using Pandas
- Data quality validation checks
- Error handling and execution logging
- SQL-based business analytics

## Future Enhancements

- Incremental data loading using Snowflake Streams and Tasks
- Advanced pipeline monitoring and alerting
- Workflow orchestration using tools like Apache Airflow
- Data warehouse optimization and performance tuning

