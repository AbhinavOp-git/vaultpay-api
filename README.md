Got it bro 👊 here’s the **entire README in one single document** — fully copy-ready without me breaking it up:

---

# VaultPay API 💳

A learning-driven project where I’m building a production-grade **FastAPI + PostgreSQL backend** step by step.
The goal: practice **API design, database integration, authentication, and DevOps practices** while documenting everything.

---

## 🌟 Project Overview

VaultPay API is a backend service designed for managing users in a secure way.
I started this project as part of my **backend + DevOps learning journey**. The idea is simple for now:

* Create new users (with secure password hashing 🔒)
* Fetch all users (GET endpoint)
* Store user data in PostgreSQL with Alembic migrations
* Experiment with schema design, CRUD operations, and API testing

Over time, I’ll extend it with authentication, transactions, and CI/CD pipelines.

---

## ⚙️ Tech Stack

* **Backend Framework** → [FastAPI](https://fastapi.tiangolo.com/)
* **Database** → PostgreSQL with SQLAlchemy ORM
* **Migrations** → Alembic
* **Password Hashing** → Passlib (bcrypt)
* **Environment Management** → Poetry + .env configs
* **DevOps Practices** → running in WSL2, Docker (upcoming), version control with Git/GitHub

---

## ✅ What’s Done So Far

* [x] Project initialized with Poetry
* [x] FastAPI app bootstrapped (`app/main.py`)
* [x] User model & schema designed
* [x] PostgreSQL database set up in WSL2
* [x] Alembic migrations configured and applied
* [x] User CRUD implemented (`create`, `get all`, `get by email`)
* [x] Password hashing integrated with Passlib (bcrypt)
* [x] Swagger UI live at → `http://127.0.0.1:8000/docs`
* [x] Inserted **10 random users** with Python script
* [x] Manual testing with Swagger and script — all working 🎉

---

## 🔥 API Endpoints (so far)

### Create User

`POST /api/v1/users/`

**Request body:**

```json
{
  "username": "abhinav",
  "email": "abhinav@example.com",
  "password": "secretpass"
}
```

**Response:**

```json
{
  "id": 1,
  "username": "abhinav",
  "email": "abhinav@example.com"
}
```

---

### Get All Users

`GET /api/v1/users/`

Returns a list of registered users.

---

## 📌 Next Steps

* Add authentication (JWT based)
* Dockerize the application
* Add CI/CD pipeline (GitHub Actions + Docker + Deployment)
* Extend API with more real-world features (transactions, profiles, etc.)
* Deploy to cloud (AWS or OCI)

---

## 🔗 Links

* GitHub Repository → [VaultPay API](https://github.com/AbhinavOp-git/vaultpay-api)

---

