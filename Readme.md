# Admin & Public Website – Django Project

A Django-based web application with a public business website and a custom admin dashboard for managing messages, services, and users.

---

## 🚀 Features

### Public Website

* Homepage with dynamic services
* Services page (powered from admin)
* Contact page with message form
* Responsive design (Bootstrap)

### Admin Dashboard

* Secure login system
* View all contact messages
* Mark messages as read/unread
* Delete messages
* Search messages by name, email, or subject
* Filter messages by read/unread
* Manage services (add, edit, activate/deactivate)
* Manage users and permissions
* Register new users (superuser only)

### Accounts

* Login, Logout, Register
* Password change
* User roles & permissions

---

## 🛠 Tech Stack

* Python 3
* Django
* Bootstrap 5
* HTML, CSS, JavaScript
* SQLite (default, can switch to PostgreSQL/MySQL)

---

## 📂 Project Structure

```text
project/
├── accounts/         # Authentication & user management
├── dashboard/        # Admin dashboard app
├── public/           # Public website app
├── templates/
│   ├── dashboard/
│   ├── public/
│   └── accounts/
├── static/
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/geecosmic/Admin-Dashboard.git
cd admin-dashboard
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run server

```bash
python manage.py runserver
```

Visit:

* Public site: `http://127.0.0.1:8000/public`
* Admin dashboard: `http://127.0.0.1:8000/`

---

## 🧪 Sample Admin Actions

* Add services in dashboard → auto appear on homepage
* View incoming contact messages
* Mark messages as read/unread
* Filter unread messages
* Delete spam messages

---

## 🔒 Permissions

* Superusers can:

  * Register users
  * Manage everything
* Normal staff:

  * Manage messages and services

---

## 📌 Future Improvements

* Dashboard analytics cards
* Pagination for messages
* Bulk actions (delete, mark read)
* File uploads for services
* Email notifications for new messages

---

## 👨‍💻 Author

Built by **George Eyo**
For learning, portfolio, and real-world Django practice.
