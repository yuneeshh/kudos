# 🏆 Kudos API – Backend

A **FastAPI-based** backend service for sending and receiving kudos between users within an organization.

---

##  Features

-  JWT Authentication (Access & Refresh Tokens)  
-  User management (Login, current user info)  
-  Kudos system (Give, receive, and list kudos)  
-  Organization association  
-  Token refresh via interceptors  
-  Message-based kudo sharing  

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/kudos-backend.git
cd kudos-backend
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### Apply migration

```bash
python manage.py migrate
```

### Optional (Create super user and test data)
```bash
python manage.py createsuperuser
python manage.py generate_test_data.py
```
### 4. Running the Server
```bash
python manage.py runserver
```