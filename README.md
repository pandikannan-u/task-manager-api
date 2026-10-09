Task Manager API

1. Project Overview

The Task Manager API is a backend application developed using FastAPI. It allows users to register, log in, and manage their personal tasks securely using JWT authentication.

2. Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Uvicorn

3. Features

- User registration with unique email validation
- Password hashing for secure storage
- Login with JWT access token
- Protected endpoints using authentication
- Create, read, update, and delete tasks (CRUD)
- Pagination for listing tasks
- User-based task ownership protection
- Request validation using Pydantic
- Interactive API documentation using Swagger UI

4. Project Structure

task-manager-api/
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   └── tasks.py
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── auth.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

5. Setup and Installation

1. Clone or download the project.
2. Create and activate a Python virtual environment.
3. Install the required packages:

pip install -r requirements.txt

4. Create a ".env" file using ".env.example" as a reference.
5. Configure the secret key, JWT settings, and database URL in ".env".

6. Run the Application

python -m uvicorn app.main:app --reload

Open the following URL in your browser:

- Swagger UI: http://127.0.0.1:8000/docs

7. API Endpoints

Method| Endpoint| Purpose
POST| "/auth/register"| Register a new user
POST| "/auth/login"| Authenticate and obtain a token
GET| "/auth/me"| Get the current user's details
POST| "/tasks"| Create a task
GET| "/tasks"| List the current user's tasks
GET| "/tasks/{task_id}"| Retrieve a task
PUT| "/tasks/{task_id}"| Update a task
DELETE| "/tasks/{task_id}"| Delete a task

8. Security

Passwords are stored as hashes rather than plain text. JWT authentication protects task operations, and users can access only their own tasks.

9. Testing

The API endpoints were tested using FastAPI Swagger UI. Screenshots of the test results are maintained separately for project demonstration.

10. Environment Variables

The ".env" file stores configuration values such as the JWT secret key, token expiry, algorithm, and database URL. Do not publish the real ".env" file or secret key.