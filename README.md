# EcoLedger MVP API v0.1

A prototype API for managing carbon credit records.

## 📦 Features

- Add, list, and retrieve carbon credit records
- Search by project type
- Mock PolygonScan token verification (optional)

## 🛠 Setup

```bash
gIt clone https://github.com/Charles130-Anderson/EcoLedger-API-MVP-.git
cd ecoledger-api
pip install -r requirements.txt
uvicorn app.main:app --reload
