#!/usr/bin/env python3
"""
Frozen-Flask Static Site Generator
Converts the Flask application to static HTML, CSS, and JavaScript files
"""

import os
import shutil
from flask_frozen import Freezer
from app import create_app
from app.routes import get_blog_posts

def create_static_site():
    """Generate static site using Frozen-Flask"""
    
    # Create Flask app
    app = create_app()
    
    # Configure Freezer - use absolute path to avoid conflicts
    build_path = os.path.abspath('static_site')
    app.config['FREEZER_DESTINATION'] = build_path
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FREEZER_IGNORE_404_NOT_FOUND'] = True
    app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
    
    # Initialize Freezer
    freezer = Freezer(app)
    
    @freezer.register_generator
    def blog_post_urls():
        """Generate URLs for all blog posts"""
        with app.app_context():
            blog_posts = get_blog_posts()
            for post in blog_posts:
                yield 'main.blog_post', {'post_path': post['path']}
    

    
    # Clean build directory if it exists
    if os.path.exists(build_path):
        print("🧹 Cleaning existing build directory...")
        shutil.rmtree(build_path)
    
    print("🚀 Starting static site generation...")
    print(f"📁 Output directory: {build_path}/")
    
    # Generate static site
    with app.app_context():
        freezer.freeze()
    
    # Copy additional files that might not be caught by Freezer
    copy_additional_files()
    
    print("✅ Static site generated successfully!")
    print(f"📂 Files generated in: {build_path}/")
    print(f"🌐 To serve locally: python -m http.server 8080 --directory {os.path.basename(build_path)}")

def copy_additional_files():
    """Copy additional files that might be needed"""
    
    # Copy CNAME file if it exists (for GitHub Pages)
    build_dir = 'static_site'
    if os.path.exists('CNAME'):
        shutil.copy2('CNAME', f'{build_dir}/CNAME')
        print("📋 Copied CNAME file for GitHub Pages")
    
    # Copy any additional static files from root
    additional_files = ['favicon.ico', 'robots.txt', 'sitemap.xml']
    for file in additional_files:
        if os.path.exists(file):
            shutil.copy2(file, f'{build_dir}/{file}')
            print(f"📄 Copied {file}")

def create_deployment_files():
    """Create files needed for various deployment platforms"""
    
    # Create .nojekyll for GitHub Pages (prevents Jekyll processing)
    build_dir = 'static_site'
    with open(f'{build_dir}/.nojekyll', 'w') as f:
        f.write('')
    print("🚫 Created .nojekyll for GitHub Pages")
    
    # Create a simple index redirect if needed
    # (This is already handled by Flask routes)

def serve_static_site(port=8080):
    """Serve the static site locally for testing"""
    import http.server
    import socketserver
    import threading
    import webbrowser
    
    os.chdir('static_site')
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"🌐 Serving static site at http://localhost:{port}")
        print("Press Ctrl+C to stop the server")
        
        # Open browser
        threading.Timer(1.5, lambda: webbrowser.open(f"http://localhost:{port}")).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'serve':
        # Serve existing static site
        if os.path.exists('static_site'):
            serve_static_site()
        else:
            print("❌ static_site directory not found. Run 'python freeze.py' first.")
    else:
        # Generate static site
        create_static_site()
        create_deployment_files()
        
        print("\n" + "="*50)
        print("🎉 STATIC SITE GENERATION COMPLETE!")
        print("="*50)
        print("📁 Location: static_site/")
        print("🧪 Test locally: python freeze.py serve")
        print("🚀 Deploy: Upload static_site/ folder to your hosting service")
        print("\n💡 Deployment options:")
        print("   • GitHub Pages: Push static_site/ contents to gh-pages branch")
        print("   • Netlify: Drag static_site/ folder to netlify.com")
        print("   • Vercel: Connect repo and set static_site/ as output directory")
        print("   • Any static host: Upload static_site/ folder contents")