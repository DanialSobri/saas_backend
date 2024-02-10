# saas_backend
Template for SaaS backend using FastAPI. Change accordingly.

## Roadmap

1. Provide basic user management with authentification feature.
1. Provide basic user management with subscription feature
1. Provide basic user management with app integrations feature
1. Provide basic user management with teams collaboration feature
1. Provide basic user management with payment feature

## Get Started

Run manage.py to populate db with admin account

Run 
uvicorn main:app --reload


## Repo structure
THis project utilize following project structure.

```
saas_backend/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── ... (other models)
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── ... (other routes)
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── ... (other services)
│   │
│   └── utils/
│       ├── __init__.py
│       ├── validators.py
│       └── ... (other utility modules)
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── ... (other config files)
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   ├── test_services.py
│   └── ... (other test files)
│
├── requirements.txt
├── README.md
└── manage.py
```

- app/: This directory contains your application code.
- models/: Define your data models here using ORM like SQLAlchemy
- routes/: Define your API routes using FastAPI.
- services/: Business logic and interaction with models go here.
- utils/: Utility functions that can be reused across the application.
    - config/: Configuration settings for your application.
        production environments.
- tests/: Directory for your unit tests.
    - test_routes.py: Test cases for your API routes.
    - test_services.py: Test cases for your services.
- requirements.txt: List of dependencies for your project. You can generate it using pip freeze > requirements.txt.
- README.md: Documentation for your project, including setup instructions and usage guidelines.
- manage.py: Entry point for management commands. For example, database migrations, running the development server, etc