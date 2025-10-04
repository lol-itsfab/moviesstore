# 🚀 PythonAnywhere Deployment Guide

## Step-by-Step Instructions

### 1. **Upload Your Code to PythonAnywhere**

1. **Create a new directory** in your PythonAnywhere filesystem:
   ```bash
   mkdir /home/yourusername/moviesstore
   ```

2. **Upload all your project files** to this directory using:
   - PythonAnywhere's file upload feature, or
   - Git (recommended): `git clone` your repository

### 2. **Set Up Virtual Environment**

1. **Open a Bash console** in PythonAnywhere
2. **Navigate to your project directory**:
   ```bash
   cd /home/yourusername/moviesstore
   ```

3. **Create a virtual environment**:
   ```bash
   python3.10 -m venv moviesstore_env
   source moviesstore_env/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install --user -r requirements.txt
   ```

### 3. **Configure Database**

1. **Run migrations**:
   ```bash
   python manage.py migrate --settings=moviesstore.settings_production
   ```

2. **Create a superuser**:
   ```bash
   python manage.py createsuperuser --settings=moviesstore.settings_production
   ```

3. **Collect static files**:
   ```bash
   python manage.py collectstatic --settings=moviesstore.settings_production
   ```

### 4. **Configure Web App**

1. **Go to the Web tab** in PythonAnywhere dashboard
2. **Create a new web app** (if you don't have one)
3. **Choose "Manual Configuration"** and select Python 3.10
4. **In the WSGI configuration file**, replace the content with:

```python
import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/moviesstore'  # Replace with your actual path
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesstore.settings_production')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 5. **Update Settings**

1. **Edit `moviesstore/settings_production.py`**:
   - Replace `yourusername` with your actual PythonAnywhere username
   - Add your domain to `ALLOWED_HOSTS`

2. **Set environment variables** (optional but recommended):
   - Go to the Web tab → Environment variables
   - Add `SECRET_KEY` with a new secret key

### 6. **Configure Static Files**

1. **In the Web tab**, scroll down to "Static files"
2. **Add static file mappings**:
   - URL: `/static/`
   - Directory: `/home/yourusername/moviesstore/staticfiles/`
   - URL: `/media/`
   - Directory: `/home/yourusername/moviesstore/media/`

### 7. **Test Your Application**

1. **Reload your web app** (click the reload button)
2. **Visit your domain** to test the petition functionality
3. **Test the complete workflow**:
   - Create an account
   - Create a petition
   - Vote on petitions
   - Test with multiple accounts

## 🔧 Troubleshooting

### Common Issues:

1. **Import Errors**: Make sure your project path is correct in the WSGI file
2. **Static Files Not Loading**: Check static file mappings and run `collectstatic`
3. **Database Errors**: Ensure migrations are run with production settings
4. **Permission Errors**: Check file permissions in your project directory

### Debug Mode:

If you need to debug, temporarily set `DEBUG = True` in `settings_production.py` and check the error logs in the Web tab.

## 📁 Files to Upload

Make sure to upload these files to PythonAnywhere:
- All Python files in your project
- `requirements.txt`
- `wsgi.py`
- `moviesstore/settings_production.py`
- All template files
- All static files
- `media/` directory (if you have uploaded images)

## 🎯 Final Checklist

- [ ] All files uploaded to PythonAnywhere
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Database migrations run
- [ ] Static files collected
- [ ] Web app configured with correct WSGI file
- [ ] Static file mappings set up
- [ ] Domain added to ALLOWED_HOSTS
- [ ] Web app reloaded
- [ ] Application tested

Your petition system should now be live on PythonAnywhere! 🎉
