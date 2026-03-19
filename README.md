# 🛒 Django E-Commerce Project

## 📌 Overview

This is a full-featured **E-Commerce web application built with Django**. It allows users to browse products, manage a shopping cart, place orders, and handle authentication. Admin users can manage products, categories, and orders through the Django admin panel.

---

## 🚀 Features

### 👤 User Features

* User registration and login/logout
* Browse products by category
* View product details
* Add/remove items from cart
* Update cart quantities
* Checkout and place orders
* Order history

### 🛠️ Admin Features

* Manage products (add, edit, delete)
* Manage categories
* View and update orders
* Manage users

---

## 🏗️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)
* **Authentication:** Django built-in auth system

---

## 📂 Project Structure

```
ecommerce_project/
│
├── manage.py
├── db.sqlite3
├── ecommerce_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   ├── products/
│   ├── cart/
│   ├── orders/
│   └── users/
│
├── templates/
├── static/
└── media/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ecommerce_project
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 🧪 Usage

* Access the homepage to browse products
* Register/Login to add items to cart
* Proceed to checkout to place orders
* Admin panel available at:

```
http://127.0.0.1:8000/admin/
```

---

## 🔧 Environment Variables (Optional)

Create a `.env` file for sensitive data:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

---

## 📦 Future Improvements

* Payment gateway integration (Stripe/PayPal)
* Product reviews & ratings
* Search and filtering
* REST API with Django REST Framework
* Wishlist functionality
* Email notifications

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---
## 📦 Future Improvements
- Payment gateway integration (Stripe/PayPal) — planned for future development
- Product reviews & ratings
- Search and filtering
- REST API with Django REST Framework
- Wishlist functionality
- Email notifications

- Payment gateway integration (Stripe/PayPal) — currently not implemented, but planned for future development
