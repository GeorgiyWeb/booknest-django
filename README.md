# 📚 BookNest — Bookstore Management System

BookNest is a lightweight Django web application designed for bookstore management, inventory tracking, and order indexation.

## ✨ Key Architectural Highlights

* **Financial Data Precision:** Prices are stored in integer cents (`price_cents`) to completely prevent floating-point rounding bugs.
* **Database Optimization:** Composite database indexing on the `Order` model (`book` + `timestamp`) to ensure fast analytical queries as data scales.
* **Data Integrity:** Used `on_delete=models.PROTECT` on the `Genre` model to prevent accidental cascade deletion of active book categories.
* **Automated Slugs:** Custom `save()` logic using `slugify` to generate clean, SEO-friendly URLs for genres.
* **Modular Templates & UI:** Custom CSS layout featuring Flexbox sticky footers and Django template inheritance (`{% extends %}`).

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Django
* **Database:** SQLite
* **Frontend:** HTML5, Custom CSS3

## 🚀 Quick Start (Local Setup)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/GeorgiyWeb/booknest-django.git](https://github.com/GeorgiyWeb/booknest-django.git)
   cd booknest-django


1. Create and activate a virtual environment:
   python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


2. Install Django:
   pip install django

3. Run migrations and start the server:
   python manage.py migrate
   python manage.py runserver
