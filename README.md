# 🛒 Real E-Commerce – Full-Stack Project

A fully functional E-Commerce web application built with **Django**.  
This project includes user authentication, product listing, categories, cart, orders, payment handling structure, and an admin dashboard for product management.

---

## 🚀 Features

### **👤 User Features**
- User Registration & Login  
- Browse Products  
- Product Categories  
- Add to Cart  
- Update Cart Quantity  
- Place Orders  
- View Order History  

### **🛍️ Admin Features**
- Add / Edit / Delete Products  
- Manage Categories  
- Manage Orders  
- Upload Product Images  
- Manage Stock Availability  

---

## 📁 Project Structure

```
real ecommerece/
│── db.sqlite3
│── manage.py
│
├── ecommerece/           # Main project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── home/                 # Homepage + Search + Dashboard
│   ├── views.py
│   ├── urls.py
│   └── templates/home/
│
├── user/                 # Auth system
│   ├── login, register, logout
│
├── product/              # Product listing & details
├── cart/                 # Shopping cart system
├── order/                # Order placement & history
│
├── templates/            # HTML templates
├── static/               # CSS, JS, images
└── media/                # Uploaded product images
```

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the project**
```bash
git clone <repo-url>
cd real-ecommerce
```

### **2️⃣ Create Virtual Environment**
```bash
python -m venv env
source env/bin/activate   # Mac / Linux
env\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run Migrations**
```bash
python manage.py migrate
```

### **5️⃣ Run Server**
```bash
python manage.py runserver
```

Open in browser: **http://127.0.0.1:8000/**

---

## 🧪 Test Admin Panel

### **Admin Login**
```
URL: /admin
Username: (your admin username)
Password: (your admin password)
```

Use Django admin to add products, categories, and manage orders.

---

## 🖼️ Media & Static Setup

Product images are stored in:
```
/media/productimg/
```

Static assets stored in:
```
/static/
```

Make sure these folders are available when deployed.

---

## 🤝 Contributing

Pull requests are welcome.  
For major changes, open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is for educational & personal use.

---

## ⭐ Show Support

If this project helped you, star the repository or share it with others!

