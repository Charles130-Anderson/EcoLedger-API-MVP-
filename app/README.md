````
# EcoLedger MVP API v0.1

A prototype API for managing carbon credit records.

## 📦 Features

- Add, list, and retrieve carbon credit records
- Search by project type
- Mock PolygonScan token verification (optional)

## 🛠 Setup

```bash
git clone https://github.com/Charles130-Anderson/EcoLedger-API-MVP-.git
cd ecoledger-api
pip install -r requirements.txt
uvicorn app.main:app --reload
````

## ⚙️ Environment Configuration

Create a `.env` file in the project root with the following content:

```
DATABASE_URL=your_database_url_here
```

> **Note:** If you're deploying on [Railway](https://railway.app):

* Use the **public database URL**.
* In Railway, go to your service’s **Variables** tab.
* Create a new variable named `DATABASE_URL` (or `DATABASE_PUBLIC_URL` if your code supports it).
* Paste the PostgreSQL connection string (format: `postgresql://user:password@host:port/dbname`) as the value.
* Make sure this matches what your `database.py` expects.

You can also update your code like this to support both:

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL") or os.getenv("DATABASE_PUBLIC_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE URL not set in environment")
```

## 🚀 Deployment on Railway

1. Push your project to GitHub.
2. Link it to a Railway project.
3. Provision a **PostgreSQL plugin** from Railway’s dashboard.
4. Copy the connection URL and add it as an environment variable:

   * Name: `DATABASE_URL`
   * Value: *(use the copied PostgreSQL URL)*
5. Deploy the app.
Link to the API [Ecoledger](https://web-production-d2480.up.railway.app/docs)
![Ecoledger1](https://github.com/user-attachments/assets/dd3fc785-544b-42a0-bde4-3848157235fd)


