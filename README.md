# Data Cleaning Pipeline

A Python pipeline that takes a messy CSV of employee records and produces a clean, analysis-ready dataset.

## The Problem

Raw data is rarely clean. This pipeline handles a deliberately messy employee dataset containing:
- Duplicate records
- A text value in a numeric column ("sixty thousand" in salary)
- Inconsistent date formats (2021-05-12, 03/14/2020, 2022/01/15)
- Inconsistent text casing (Active vs active)
- Missing values across multiple columns

## How It Works

The pipeline cleans the data in a deliberate order:

1. **Remove duplicates** — drop repeated rows
2. **Fix data types** — convert salary to numeric; invalid text becomes NaN
3. **Normalize text** — lowercase and strip emails and status values
4. **Standardize dates** — convert all date formats to a single standard
5. **Handle missing values per column:**
   - Text (last name) → filled with "Unknown"
   - Salary → filled with the median (robust against outliers)
   - Hire date → left blank, flagged for manual review (can't be invented)


## Tech
Python · pandas

## How to Run
​```
pip install pandas
python clean.py
​```
Reads `messy_data.csv` and outputs `cleaned_data.csv`.