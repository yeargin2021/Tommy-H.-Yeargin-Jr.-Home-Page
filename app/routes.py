from flask import Blueprint, render_template, abort
import os
import re
from datetime import datetime
from app.config import Config

bp = Blueprint('main', __name__)

@bp.context_processor
def inject_globals():
    """Inject global variables into all templates"""
    return {
        'current_year': datetime.now().year
    }

# Data for the books section
books_data = [
    {
        "title": "48 days to the work (and life) you love",
        "author": "Dan Miller",
        "isbn": "978-1642799781",
        "date_read": "28 Dec 2024"
    },
    {
        "title": "The Game of Life and How to Play It", 
        "author": "Florence Scovel Shinn",
        "date_read": "6 Jan 2025"
    }
]

# Links data
links_data = [
    {"name": "Drudge Report", "url": "http://www.drudgereport.com"},
    {"name": "NY Times", "url": "https://www.nytimes.com"}
]

@bp.route('/')
def index():
    """Home page route"""
    return render_template('index.html', 
                         site_name=Config.SITE_NAME,
                         site_description=Config.SITE_DESCRIPTION,
                         books=books_data)

@bp.route('/links/')
@bp.route('/links.html')
def links():
    """Links page route"""
    return render_template('links.html',
                         site_name=Config.SITE_NAME,
                         links=links_data)

@bp.route('/blog/')
@bp.route('/blog.html')
def blog():
    """Blog index page"""
    blog_posts = get_blog_posts()
    return render_template('blog.html',
                         site_name=Config.SITE_NAME,
                         blog_posts=blog_posts)

@bp.route('/blog/<path:post_path>')
def blog_post(post_path):
    """Individual blog post route"""
    # Sanitize the path to prevent directory traversal
    if '..' in post_path or post_path.startswith('/'):
        abort(404)
    
    blog_file = os.path.join(Config.BLOG_DIR, post_path)
    
    # Add .html extension if not present
    if not post_path.endswith('.html'):
        blog_file += '.html'
    
    if not os.path.exists(blog_file) or not os.path.isfile(blog_file):
        abort(404)
    
    try:
        with open(blog_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract date from filename or content if possible
        date_match = re.search(r'(\d{1,2}\s+\w+\s+\d{4})', content)
        post_date = date_match.group(1) if date_match else "Unknown date"
        
        # Generate title from filename
        title = os.path.basename(post_path).replace('.html', '').replace('_', ' ').title()
        
        return render_template('blog_post.html',
                             site_name=Config.SITE_NAME,
                             title=title,
                             content=content,
                             date=post_date,
                             post_path=post_path)
    except Exception as e:
        abort(404)

def get_blog_posts():
    """Get all blog posts from the blog directory"""
    blog_posts = []
    
    if not os.path.exists(Config.BLOG_DIR):
        return blog_posts
    
    for root, dirs, files in os.walk(Config.BLOG_DIR):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, Config.BLOG_DIR)
                
                # Try to get creation/modification date
                stat = os.stat(file_path)
                modified_date = datetime.fromtimestamp(stat.st_mtime)
                
                # Generate title from filename
                title = file.replace('.html', '').replace('_', ' ').title()
                
                blog_posts.append({
                    'title': title,
                    'path': relative_path,
                    'date': modified_date.strftime('%d %b %Y')
                })
    
    # Sort by date (newest first)
    blog_posts.sort(key=lambda x: x['date'], reverse=True)
    return blog_posts