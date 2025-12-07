# 📊 Finance Tracker – Flask Application

A simple yet powerful **personal finance tracking web application** built using **Flask**, **SQLite**, and **Chart.js**.
It helps users record expenses and income, categorize transactions, and view visual insights through interactive charts.

This version is fully optimized for **deployment on Render**.

---

## 🚀 Features

### ✅ **Track Income & Expenses**

* Add transactions with category, type (Income/Expense), and amount
* All data stored securely in SQLite (`finance.db`)

### 📈 **Dashboard with Charts**

* Chart.js pie chart showing category-wise expenses
* Summary of total expenses and total income
* Clean and responsive user interface

### 🌐 **Cloud Deployment (Render)**

* Works on Render’s free tier
* Auto-deploys when you push to GitHub
* Uses a `requirements.txt` file and gunicorn server (if needed)

---

## 📁 Project Structure

```
FINANCE-TRACKER/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
│
├── instance/
│   └── finance.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── dashboard.html
│
├── static/
│
└── myvenv/   # virtual environment (ignored in git)
```

---

## ⚙️ Local Installation & Setup

### 1️⃣ Create Virtual Environment

```
python -m venv myvenv
```

Activate:

* **Windows:**

  ```
  myvenv\Scripts\activate
  ```
* **Mac/Linux:**

  ```
  source myvenv/bin/activate
  ```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run the App

```
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 🛢️ Database (SQLite)

The app uses SQLite and automatically creates `instance/finance.db`.

If you want to reset:

```
rm instance/finance.db
python
>>> from app import db
>>> db.create_all()
```

---

## ☁️ Deploying to Render (Step-by-Step)

### **1. Push your project to a GitHub repository**

Make sure `requirements.txt` exists.

Example:

```
Flask
Flask_SQLAlchemy
gunicorn
```

(Your file may contain more packages.)

---

### **2. Go to Render Dashboard**

👉 [https://finance-manager-8okb.onrender.com](https://finance-manager-8okb.onrender.com)

Click: **New → Web Service**

---

### **3. Configure Render Service**

Fill these details:

| Option            | Value                             |
| ----------------- | --------------------------------- |
| **Runtime**       | Python 3                          |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app`                |

If your file is inside a folder or the app object name is different, adjust accordingly.

---

### **4. Add a Persistent Disk (Optional but recommended)**

To save the database between deployments:

* Go to **Environment → Disks**
* Add disk
* Mount at: `/opt/render/project/src/instance`
* Size: **1GB** (enough)

Now your `finance.db` will not get deleted after redeploys.

---

### **5. Click Create Web Service**

Render will:

* Install dependencies
* Build your app
* Start Gunicorn server
* Give you a live URL

Your Flask Finance Tracker is now live!

---

## 🧱 Tech Stack

| Component  | Technology      |
| ---------- | --------------- |
| Backend    | Flask           |
| Database   | SQLite          |
| UI         | HTML, Bootstrap |
| Charts     | Chart.js        |
| Deployment | Render          |

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

## 📜 License

Free to use for personal and educational purposes.
