# Darigold Farm Management (MVP)

This project provides a starter dairy farm management system using **Streamlit** and **SQLite**.

## Features implemented

### Phase 1
- Database schema
- Seed data
- Dashboard
- Animal master
- Milk yield entry
- Animal profile page

### Phase 2
- Health records
- Vaccination records
- Breeding records
- Feed logs
- Expense tracking
- Profitability snapshot
- Reports page

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app auto-initializes and seeds `darigold.db` on first run.
