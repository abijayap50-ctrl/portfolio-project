# Django Portfolio Website

A modern portfolio website built with Python and Django Framework.

## Quick Start Guide

### Step 1: Prerequisites
Make sure you have Python 3.10+ installed on your system.
```bash
python --version
```

### Step 2: Create Virtual Environment
```bash
# Navigate to the project folder
cd django_portfolio

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Populate Database with Your Data
```bash
python populate_data.py
```

### Step 6: Create Admin User
```bash
python manage.py createsuperuser
# Follow prompts to create username and password
```

### Step 7: Run the Server
```bash
python manage.py runserver
```

### Step 8: View Your Portfolio
- Portfolio: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/

## Project Structure

```
django_portfolio/
├── portfolio_project/    # Django settings
├── portfolio/            # Main app (models, views, urls)
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── media/                # User uploads
├── manage.py             # Django management script
├── populate_data.py      # Database initialization
└── requirements.txt      # Python dependencies
```

## Customization

### Change Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #00d4aa;  /* Change to your color */
}
```

### Update Personal Info
1. Go to Admin Panel (http://localhost:8000/admin/)
2. Edit Profile, Skills, Projects, etc.

### Add Profile Image
1. Go to Admin Panel
2. Click on Profile
3. Upload your photo

## Need Help?
Check the full tutorial PDF included in the download folder.
