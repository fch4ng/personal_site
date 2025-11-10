# FUTURE BACKEND STRUCTURE
# This file is a blueprint for Phase 2+ expansion
# Do not deploy yet - for planning purposes

"""
Future Directory Structure:
contact-site/
├── frontend/               # Current site (move here when adding backend)
│   ├── index.html
│   ├── style.css
│   └── script.js
├── backend/                # Python backend (Phase 2+)
│   ├── app.py             # Main Flask/FastAPI app
│   ├── models.py          # Database models
│   ├── auth.py            # Authentication logic
│   ├── config.py          # Configuration
│   └── requirements.txt   # Python dependencies
├── blog/                   # Blog section (Phase 2)
│   ├── posts/             # Markdown or HTML posts
│   └── templates/         # Blog templates
├── gallery/                # Gallery section (Phase 3)
│   ├── public/
│   └── private/
└── docker-compose.yml     # For easy deployment
"""

# EXAMPLE: Flask Backend (app.py)
"""
from flask import Flask, render_template, session, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    access_level = db.Column(db.String(20), default='basic')  # basic, gallery, admin

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    # Fetch blog posts from database or markdown files
    posts = BlogPost.query.order_by(BlogPost.date.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/gallery')
def public_gallery():
    return render_template('gallery_public.html')

@app.route('/gallery/private')
def private_gallery():
    if not session.get('logged_in'):
        return redirect('/login')
    if session.get('access_level') not in ['gallery', 'admin']:
        return "Access denied", 403
    return render_template('gallery_private.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['logged_in'] = True
            session['username'] = username
            session['access_level'] = user.access_level
            return redirect(request.args.get('next', '/'))
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
"""

# EXAMPLE: requirements.txt
"""
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.0
gunicorn==21.2.0
markdown==3.5
Pillow==10.1.0
"""

# EXAMPLE: Docker Setup (docker-compose.yml)
"""
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=${DATABASE_URL}
    volumes:
      - ./backend:/app
      - ./frontend:/app/static
    command: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./frontend:/usr/share/nginx/html
    depends_on:
      - web
"""

# EXAMPLE: Access Control Manager
"""
class AccessManager:
    LEVELS = {
        'public': 0,
        'basic': 1,
        'gallery': 2,
        'blog_author': 3,
        'admin': 4
    }
    
    @staticmethod
    def has_access(user_level, required_level):
        return AccessManager.LEVELS.get(user_level, 0) >= AccessManager.LEVELS.get(required_level, 0)
    
    @staticmethod
    def grant_access(username, access_level):
        user = User.query.filter_by(username=username).first()
        if user:
            user.access_level = access_level
            db.session.commit()
            return True
        return False
"""

# IMPLEMENTATION PHASES:

# Phase 2A: Static Blog (No backend needed)
# - Use Pelican/Nikola to generate static blog
# - Add /blog/ directory to GitHub Pages
# - Write posts in Markdown

# Phase 2B: Dynamic Blog (With backend)
# - Flask/FastAPI backend
# - Database for posts
# - Admin interface for writing
# - Comments system (optional)

# Phase 3: Gallery with Access Control
# - Public gallery (no auth required)
# - Private gallery (requires login)
# - User management system
# - Image upload interface

# Phase 4: Full Authentication System
# - User registration (invite-only or open)
# - Multiple access levels
# - Session management
# - Password reset functionality

# DEPLOYMENT OPTIONS:

# Option 1: Heroku
# - Free tier available
# - Easy Python deployment
# - Add Postgres database
# heroku create
# git push heroku main

# Option 2: Railway.app
# - Modern alternative to Heroku
# - Very easy deployment
# - Generous free tier

# Option 3: Self-hosted VPS
# - Full control
# - Use Docker for easy deployment
# - Nginx as reverse proxy
# - SSL with Let's Encrypt

# Option 4: Hybrid
# - GitHub Pages for static content (fast, free CDN)
# - Backend API on separate server
# - Best performance for static content
# - Dynamic features where needed
