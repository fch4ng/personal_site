# Contact Site - Francisco

A minimalist, late 90s/early 2000s inspired contact page with a modern twist. Built for easy expansion and future migration to Python-based backend.

## 🚀 Quick Start - GitHub Pages Deployment

### Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `contact-site` or `username.github.io` (if you want it at your root domain)
3. Keep it public (required for free GitHub Pages)
4. Don't initialize with README (we have our own files)

### Step 2: Upload Files
```bash
# In your terminal, navigate to this directory
cd /path/to/contact-site

# Initialize git repository
git init

# Add files
git add .

# Commit
git commit -m "Initial commit: Contact page"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the sidebar)
3. Under "Source", select branch: **main** and folder: **/ (root)**
4. Click **Save**
5. Wait 1-2 minutes, then visit: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

### Step 4: Customize Your Info
Edit `index.html` and replace:
- `your.email@example.com` with your actual email
- `+XX XXX XXX XXXX` with your Signal number
- `@yourusername` with your Telegram username
- Update the Telegram link: `https://t.me/yourusername`

## 📁 File Structure

```
contact-site/
├── index.html      # Main HTML structure
├── style.css       # Styling (late 90s/2000s aesthetic)
├── script.js       # Dynamic timestamp + interactivity
└── README.md       # This file
```

## 🎨 Design Features

- **Black & White Minimalism**: High contrast, clean design
- **Late 90s/Early 2000s Aesthetic**: Monospace fonts, simple effects, nostalgic feel
- **Responsive**: Works on mobile, tablet, and desktop
- **Glitch Effect**: Subtle hover effect on title
- **Live Timestamp**: Shows current date/time
- **Hover Animations**: Smooth transitions on contact items

## 🔮 Future Expansion Roadmap

### Phase 2: Blog Section
**Technology**: Python (Flask or FastAPI) + Static Site Generator
```
/
├── index.html          # Contact (current)
├── /blog/              # Blog section
│   ├── index.html      # Blog listing
│   └── /posts/         # Individual posts
```

**Implementation Options**:
- **Static**: Use Pelican or Nikola (Python-based static generators)
- **Dynamic**: Flask/FastAPI with Markdown rendering
- **Hybrid**: Generate static HTML with Python, serve via GitHub Pages

### Phase 3: Gallery Section
**Access Control**: Python backend with authentication
```
/gallery/
├── public/             # Open to all
└── private/            # Requires authentication
```

**Technologies**:
- Flask/FastAPI for backend
- JWT or session-based auth
- SQLite/PostgreSQL for user management
- Host on: VPS, Heroku, Railway, or your own server

### Phase 4: Access Control System
**Python Implementation Example**:
```python
# Simple Flask structure
from flask import Flask, render_template, session
from functools import wraps

app = Flask(__name__)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated

@app.route('/private/gallery')
@requires_auth
def private_gallery():
    return render_template('private_gallery.html')
```

## 🔧 Migration Options

### Option 1: Keep GitHub Pages + Add Backend API
- Frontend stays on GitHub Pages (free, fast CDN)
- Backend API on separate server (Railway, Render, your VPS)
- Frontend makes API calls for dynamic content

### Option 2: Full Self-Hosting
- Move everything to your own server/VPS
- Full control, can run Python backend directly
- Use Docker for easy deployment
- Nginx as reverse proxy

### Option 3: Hybrid Approach
- Static content (blog posts) on GitHub Pages
- Dynamic features (auth, comments) via Python API
- Best of both worlds: speed + functionality

## 🐳 Docker-Ready Structure (Future)

When you're ready to add Python backend:

```dockerfile
# Example Dockerfile structure
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app"]
```

## 🔐 Privacy & Security Notes

- No tracking or analytics by default
- No external dependencies (all self-contained)
- Contact info is public as requested
- Future auth system will use bcrypt for password hashing
- Consider Cloudflare for DDoS protection if needed

## 🛠 Local Development

To test locally before pushing:

```bash
# Simple Python HTTP server
python -m http.server 8000

# Then visit: http://localhost:8000
```

## 📝 Customization Tips

### Change Color Scheme
Edit `style.css` `:root` variables:
```css
:root {
    --bg-color: #000000;        /* Background */
    --text-color: #ffffff;      /* Text */
    --accent-color: #00ff00;    /* Hover effects */
    --border-color: #ffffff;    /* Borders */
}
```

### Add More Sections
1. Create new HTML section in `index.html`
2. Style in `style.css`
3. Add any interactivity in `script.js`

### Custom Domain
1. Buy domain (Namecheap, Cloudflare, etc.)
2. Add CNAME file to repository with your domain
3. Configure DNS records to point to GitHub Pages
4. Enable HTTPS in GitHub Pages settings

## 📊 Analytics (Optional Future Addition)

If you want privacy-respecting analytics:
- Plausible Analytics (self-hostable)
- Umami (open-source, self-hosted)
- Simple counter using Python backend

## 🚢 Deployment Checklist

- [ ] Update contact information in `index.html`
- [ ] Test locally
- [ ] Push to GitHub
- [ ] Enable GitHub Pages
- [ ] Test live site
- [ ] (Optional) Configure custom domain
- [ ] (Optional) Set up redundant hosting

## 📚 Resources

- [GitHub Pages Docs](https://docs.github.com/pages)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pelican Static Generator](https://docs.getpelican.com/)

---

**Built with ◉ and minimal dependencies**

*Ready for expansion. Python-ready architecture.*
