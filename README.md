# 💳 VaultPay API — Secure Payment & User Management Backend

VaultPay is a **production-grade backend API** built using **FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication**, designed to simulate a real-world **fintech-grade payment management system**.

This project is being developed step by step — from core user management, authentication, database modeling, to payments integration — following industry-level DevOps and backend engineering principles.

---

## 🦭 Table of Contents

* [🚀 Overview](#-overview)
* [🧱 Tech Stack](#-tech-stack)
* [🯩 Project Architecture](#-project-architecture)
* [👤 User Management & Authentication](#-user-management--authentication)
* [💳 Payment System](#-payment-system)
* [🤠 Concepts Learned](#-concepts-learned)
* [🐞 Errors Encountered & Fixes](#-errors-encountered--fixes)
* [⚙️ Setup & Run Locally](#%EF%B8%8F-setup--run-locally)
* [🌐 Swagger API Docs](#-swagger-api-docs)
* [📘 Next Roadmap](#-next-roadmap)
* [👨‍💻 Author](#-author)

---

## 🚀 Overview

**VaultPay** is a backend system that manages:

* Secure **user registration & login** with password hashing
* **JWT token-based authentication** (OAuth2 Bearer Token)
* **Payment creation** linked to users (relational database)
* Integration with **PostgreSQL** using **SQLAlchemy ORM**
* **Alembic migrations** for schema version control
* Interactive documentation via **Swagger UI**

By the end of this phase, the API can:

1. Create users securely
2. Authenticate users using JWT tokens
3. Fetch authenticated user info (`/me` route)
4. Create and store payments for users
5. Retrieve all payments from DB

---

## 🧱 Tech Stack

| Category                   | Tools / Libraries                               |
| -------------------------- | ----------------------------------------------- |
| **Language**               | Python 3.11                                     |
| **Framework**              | FastAPI                                         |
| **Database**               | PostgreSQL                                      |
| **ORM**                    | SQLAlchemy                                      |
| **Migrations**             | Alembic                                         |
| **Auth & Security**        | JWT (via `python-jose`), bcrypt (via `passlib`) |
| **Validation**             | Pydantic                                        |
| **Environment Management** | Poetry                                          |
| **API Docs**               | Swagger UI (auto-generated)                     |
| **Testing Tool**           | cURL / Swagger / Postman                        |

---

## 🯩 Project Architecture

The project follows a clean and scalable folder structure:

```
vaultpay/
│
├── app/
│   ├── api/                  → All route definitions
│   │   ├── v1/endpoints/     → User & Auth routes
│   │   └── payments.py       → Payment API routes
│   ├── core/                 → Core logic (JWT, Auth, Config, Security)
│   ├── crud/                 → DB CRUD operations
│   ├── db/                   → DB connection & session setup
│   ├── models/               → SQLAlchemy ORM models (User, Payment)
│   ├── schemas/              → Pydantic models for request/response
│   └── main.py               → FastAPI entry point
│
├── migrations/               → Alembic migrations
├── scripts/                  → Automation scripts (insert test users, etc.)
├── pyproject.toml            → Poetry dependencies
└── README.md                 → Project documentation
```

This design allows **modular expansion** — new services or APIs can be plugged in easily.

---

## 👤 User Management & Authentication

### ✅ Implemented Features:

* User registration at `/api/v1/users/`
* Secure password hashing with **bcrypt**
* JWT login via `/api/v1/auth/login`
* Protected route `/api/v1/users/me` that requires a Bearer token

### 🔐 JWT Authentication Flow:

1. User logs in → gets a signed JWT token.
2. Token is sent in headers:

   ```
   Authorization: Bearer <access_token>
   ```
3. Protected routes decode the token to verify the user identity.

---

## 💳 Payment System

### ✅ Implemented:

* `/api/v1/payments/` — Create new payment records.
* `/api/v1/payments/` (GET) — Fetch all payments.
* Each payment is linked to a `user_id`.
* Data stored persistently in PostgreSQL.

### 🧾 Example Request:

```json
{
  "user_id": 1,
  "amount": 199.99,
  "currency": "USD",
  "description": "Monthly VaultPay Premium"
}
```

### ✅ Example Response:

```json
{
  "id": 1,
  "user_id": 1,
  "amount": 199.99,
  "currency": "USD",
  "description": "Monthly VaultPay Premium",
  "created_at": "2025-10-23T11:35:05.770887Z"
}
```

---

## 🤠 Concepts Learned

| Concept                  | Description                                   |
| ------------------------ | --------------------------------------------- |
| **FastAPI**              | Modern async web framework                    |
| **SQLAlchemy ORM**       | Maps Python classes to DB tables              |
| **Alembic**              | Handles database migrations                   |
| **JWT**                  | Token-based authentication for stateless APIs |
| **OAuth2PasswordBearer** | Standard auth flow used by Swagger            |
| **bcrypt hashing**       | Ensures passwords are securely stored         |
| **Pydantic**             | Enforces request & response validation        |
| **Swagger UI**           | Built-in API documentation                    |
| **PostgreSQL**           | Production-grade relational DB                |
| **Error Handling**       | Structured validation & error management      |

---

## 🐞 Errors Encountered & Fixes

| Issue                                                                 | Cause                               | Solution                                                                                |
| --------------------------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------- |
| `AttributeError: 'UserCreate' object has no attribute 'full_name'`    | Schema mismatch                     | Removed `full_name` from schema & model                                                 |
| `bcrypt has no attribute __about__`                                   | Old bcrypt version conflict         | Reinstalled `bcrypt` via Poetry                                                         |
| `sqlalchemy.exc.ProgrammingError: relation "payments" does not exist` | Alembic migrations not applied      | Ran `poetry run alembic upgrade head`                                                   |
| `ModuleNotFoundError: No module named 'app'`                          | Ran Uvicorn from wrong directory    | Fixed by running `poetry run uvicorn app.main:app --reload` from project root           |
| `JWT token not accepted in Swagger`                                   | Swagger not authorized              | Clicked **Authorize**, entered `Bearer <token>`                                         |
| `ValidationError (422)`                                               | Missing or invalid field in request | Ensured required fields (user_id, amount, currency) are provided                        |
| Database connection errors                                            | DB not created or wrong credentials | Verified using: `psql "postgresql://vaultuser:VaultPass123@localhost:5432/vaultpay_db"` |

✅ Every error taught important backend debugging skills.

---

## ⚙️ Setup & Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/AbhinavOp-git/vaultpay-api.git
cd vaultpay-api
```

### 2. Install dependencies

```bash
poetry install
```

### 3. Setup database (PostgreSQL)

```bash
psql -U vaultuser -W
CREATE DATABASE vaultpay_db;
```

### 4. Run migrations

```bash
poetry run alembic upgrade head
```

### 5. Start server

```bash
poetry run uvicorn app.main:app --reload
```

### 6. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Swagger API Docs

| Endpoint             | Method | Description                         |
| -------------------- | ------ | ----------------------------------- |
| `/api/v1/users/`     | POST   | Register new user                   |
| `/api/v1/auth/login` | POST   | Login and get JWT token             |
| `/api/v1/users/me`   | GET    | Fetch current user (requires token) |
| `/api/v1/payments/`  | POST   | Create new payment                  |
| `/api/v1/payments/`  | GET    | Get all payments                    |

---

## 📘 Next Roadmap

### 🕸️ Phase 2 — Advanced Features

* [ ] `GET /api/v1/payments/user/{user_id}` → Fetch user-specific payments
* [ ] Update & Delete Payment APIs
* [ ] Add logging and exception handling middleware
* [ ] Add Dockerfile and docker-compose setup
* [ ] Deploy to Render / AWS EC2
* [ ] Add CI/CD (GitHub Actions)

---

## 👨‍💻 Author

**Abhinav Raj** — DevOps & Python Backend Developer
📍 Bangalore, India
🔗 [GitHub](https://github.com/AbhinavOp-git)
🔗 [LinkedIn](https://www.linkedin.com/in/abhinav-devops)
📧 [rajabhinav1001@gmail.com](mailto:rajabhinav1001@gmail.com)

---

> ⚡ *"VaultPay isn’t just a project — it’s a journey of building production-grade systems with real engineering discipline."*





