# 💳 Credit Risk Assessment Application

A comprehensive Django-based web application designed to evaluate loan applications based on customer profiles, credit scores, and financial history.

## 🚀 Features
- **Customer Profiling:** Manage and track customer financial details.
- **Risk Engine:** Automated logic to calculate loan eligibility and interest rates.
- **Secure Dashboard:** Role-based access for viewing loan statuses and application history.
- **Deployment Ready:** Configured for production with Gunicorn and WhiteNoise.

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (Development)
- **Server:** Gunicorn
- **Deployment:** Render
- **Styling:** CSS3 & Bootstrap

## 📂 Project Structure
```text
credit_risk_pro/
├── dashboard/       # Handles user views and loan applications
├── home/            # Authentication and landing page logic
├── risk_engine/     # Core business logic for risk assessment
├── manage.py        # Django project entry point
└── requirements.txt # Project dependencies
