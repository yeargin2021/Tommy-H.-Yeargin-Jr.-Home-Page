# Tommy H. Yeargin, Jr. - Personal Website

A professional Flask-based personal website showcasing my work as a bench jeweler/goldsmith and coding enthusiast.

## Features

- **Responsive Design**: Modern, mobile-first design using Bootstrap 5
- **Professional Layout**: Clean, professional appearance suitable for business use
- **Dynamic Blog System**: Automatically displays blog posts from the `/blog` directory
- **Reading List**: "25 Books in '25" section to track reading goals
- **Contact Integration**: Links to contact forms and social profiles
- **Fast & Lightweight**: Optimized for performance with modern web standards

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5, Custom CSS with CSS Grid/Flexbox
- **Fonts**: Inter (Google Fonts)
- **Icons**: Font Awesome 6
- **Dependencies**: See `requirements.txt`

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project**
   ```bash
   cd Tommy-H.-Yeargin-Jr.-Home-Page
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your specific settings
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

The website will be available at `http://localhost:5000`

## Project Structure

```
Tommy-H.-Yeargin-Jr.-Home-Page/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration settings
│   ├── routes.py            # URL routes and view functions
│   ├── static/
│   │   ├── css/
│   │   │   └── main.css     # Custom styles
│   │   └── js/
│   │       └── main.js      # Custom JavaScript
│   └── templates/
│       ├── base.html        # Base template
│       ├── index.html       # Home page
│       ├── blog.html        # Blog index
│       ├── blog_post.html   # Individual blog post
│       └── links.html       # Links page
├── blog/                    # Blog posts directory
│   └── 202412.html         # Example blog post
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
└── README.md              # This file
```

## Adding Content

### Blog Posts
- Add HTML files to the `/blog` directory
- Files are automatically detected and displayed on the blog page
- Supports nested directories for organization

### Updating Books List
- Edit the `books_data` list in `app/routes.py`
- Add new entries with title, author, ISBN (optional), and date read

### Adding Links
- Edit the `links_data` list in `app/routes.py`
- Add new entries with name and URL

## Customization

### Styling
- Main styles are in `app/static/css/main.css`
- Uses CSS custom properties (variables) for easy theming
- Bootstrap classes can be customized via CSS overrides

### Configuration
- Site settings are in `app/config.py`
- Environment-specific settings in `.env` file
- Template globals injected via context processor in `routes.py`

## Deployment

### Production Considerations
1. **Set environment variables**:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secure-secret-key`

2. **Use a production WSGI server** (e.g., Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

3. **Set up reverse proxy** (nginx recommended)

4. **Enable HTTPS** in production

### Deployment Options
- **Heroku**: Add `Procfile` with `web: gunicorn run:app`
- **Railway**: Works out of the box with `requirements.txt`
- **Vercel**: Add `vercel.json` configuration
- **Traditional VPS**: Use nginx + gunicorn + systemd

## Browser Support

- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance

- Optimized images and assets
- Minimal JavaScript bundle
- CSS optimizations and modern techniques
- Responsive design for all device sizes

## License

© 2024 Tommy H. Yeargin, Jr. All rights reserved.

## Contact

For questions or inquiries, please use the contact form available on the website.

---

*Built with ❤️ using Flask and modern web technologies*
