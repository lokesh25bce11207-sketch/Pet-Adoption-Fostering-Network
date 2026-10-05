# Pet Adoption and Fostering Network

CSE3001 DBMS project built with MySQL 8 and Flask. It manages shelters, animals, adopters, foster placements, medical follow-up, adoption applications, home visits, and completed adoptions.

## Features

- Relational schema with primary keys, foreign keys, checks, unique constraints, and indexes
- Sample data for shelters, animals, adopters, foster homes, medical records, applications, visits, and adoptions
- Views for available animals, medical follow-up, and application summaries
- Triggers for foster capacity, adoption status synchronization, and medical alerts
- Stored procedures for adoption approval, medical alert generation, and an availability report
- Flask pages for browsing records and matching adopters with available animals
- SQL examples for joins, subqueries, aggregates, set operations, views, and transactions

## Requirements

- MySQL 8.0 or newer
- Python 3.11 or newer
- The MySQL command-line client available on PATH, or a MySQL client such as Workbench

## Database setup

Run these commands from this folder in order. Each command prompts for the MySQL password:

```powershell
mysql -u root -p < schema.sql
mysql -u root -p < sample_data.sql
mysql -u root -p < views.sql
mysql -u root -p < triggers.sql
mysql -u root -p < procedures.sql
```

The schema creates and selects the `pet_adoption_network` database. The sample data uses `INSERT IGNORE` so loading it again does not duplicate rows with the same keys.

## Run the Flask application

Create a local environment file from the example and set the MySQL credentials in `.env`. Do not commit `.env`.

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Set `DB_PASSWORD` in `.env`, then start the app:

```powershell
python app.py
```

Open <http://127.0.0.1:5000> in a browser.

The database settings can be provided through `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME`. Defaults are `127.0.0.1`, `3306`, `root`, an empty password, and `pet_adoption_network`.

## Main SQL files

| File | Purpose |
|---|---|
| `schema.sql` | Database, tables, keys, constraints, and indexes |
| `sample_data.sql` | Demonstration records |
| `views.sql` | Reusable joined and calculated views |
| `triggers.sql` | Event-based database rules |
| `procedures.sql` | Adoption, medical alert, and availability procedures |
| `queries.sql` | Query examples and transaction demonstration |
| `plsql_examples.sql` | Stored program and procedural SQL examples |

## Reports and exported data

The `reports/` folder contains:

- `Pet_Adoption_Project_Report.pdf` - project design and DBMS concepts
- `Pet_Adoption_How_It_Works_Guide.pdf` - workflows and application/database behavior
- `Pet_Adoption_Data_Tables.pdf` - all 113 sample rows across the 10 stored database tables
- `pet_adoption_network_data.xlsx` - the table rows and three view results on separate sheets

The PDFs and workbook were generated from the local MySQL project database. The workbook's three view sheets are query results; they are not additional stored tables.

## Project notes

This is an academic demonstration, not a production shelter-management system. It does not include production authentication, payment processing, identity verification, or deployment hardening. See `dbms_project_report.md`, `academic_topics.md`, and `syllabus_coverage.md` for additional course material.
