# How to Run Project

## 1. Create a Virtual Environment

Use the following command to create a virtual environment:

```bash
python -m venv myvenv
```

> **Note**: Replace `myvenv` with your desired virtual environment name. If you don't want to change it, you can keep it as `myvenv`.

- I strongly recommend using **Git Bash** to run these commands.
- Make sure you have **Python** installed properly on your system.

📥 **Git Bash Download**: [https://git-scm.com/downloads](https://git-scm.com/downloads)  
🍎 For **Mac users**, you may need to install it manually.  
🔗 Guide for Mac/Linux: [Install Virtual Environment Guide](https://github.com/codingforentrepreneurs/Guides/blob/master/all/install_django_mac_linux.md)

> ⚠️ **Important**: Do **not** use my virtual environment to run this project, as it contains system-specific paths. Please create a new virtual environment on your machine.

---

## 2. Activate the Virtual Environment

Run the appropriate command based on your OS:

- **Windows**:
  ```bash
  source myvenv/Scripts/activate
  ```

- **Mac/Linux**:
  ```bash
  source myvenv/bin/activate
  ```

---

## 3. Install Required Packages

Install all required packages using the following command:

```bash
pip install -r requirements.txt
```

---

## 4. Run the Server

To start the Django development server, run:

```bash
python manage.py runserver
```

Visit the Admin Panel at:  
🔗 [https://127.0.0.1:8000/admin](https://127.0.0.1:8000/admin)

### Admin Login Credentials:
- **Username**: `admin@gmail.com`  
- **Password**: `admin`

---

## Sample Buyer and Seller Accounts

You can use the following sample accounts to test the application:

| Email               | Password |
|---------------------|----------|
| dhwani@gmail.com    | admin    |
| anjali@gmail.com    | admin    |
| mohit@gmail.com     | admin    |

---

## Create a Superuser (Optional)

To create a new superuser, run:

```bash
python manage.py createsuperuser
```

---

## Need Help?

If you face any difficulties running the project, feel free to reach out:

📧 Email: **divyangpatel5358@gmail.com**

---

Thank you!
