# 🕒 Remind Me Later - Internship Task

This is a **Django REST API** project developed as part of an internship assignment. The goal of the task is to create an API that allows users to schedule reminders by specifying a date, time, message, and the type of reminder (EMAIL or SMS). The reminder gets saved in a database using Django’s ORM.

---

## 📌 Project Overview

This project was built for an internship task where the objective was to:

- Build a backend API using Django REST Framework.
- Allow users to schedule reminders via an HTTP POST request.
- Validate and store reminder data in a SQLite database.
- Return appropriate success or error messages via the API.

The delivery or notification part (actual email/SMS sending) is **not implemented**, as the focus was on **building and structuring the backend**.

---

## ✅ Features

- Create and save reminders with:
  - Date
  - Time
  - Message
  - Type (`EMAIL` or `SMS`)
- Simple, clean API with JSON input/output
- Modular Django structure
- Easily extendable for future notification logic

---

## 🛠️ Technologies Used

- Python 3
- Django 5.2.2
- Django REST Framework 3.15.1
- SQLite (default Django DB)

---

## 📁 Folder Structure

remind_me_later/
├── manage.py
├── remind_me_later/
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── reminders/
├── models.py
├── serializers.py
├── views.py
├── urls.py
└── ...


---

## 🚀 How to Run

### 1. Clone the Project

```bash
git clone <your-repo-url>
cd remind_me_later
2. Create a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not present, install manually:

bash
Copy
Edit
pip install django djangorestframework
4. Apply Migrations & Start Server
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
🧱 API Details
🎯 Endpoint: Create Reminder
Method: POST

URL: http://localhost:8000/api/reminders/create/

Headers:

Content-Type: application/json

Request Body:

json
Copy
Edit
{
  "date": "2025-06-10",
  "time": "14:30:00",
  "message": "Meeting with the product team",
  "reminder_type": "EMAIL"
}
Response:

json
Copy
Edit
{
  "message": "Reminder saved successfully!"
}
