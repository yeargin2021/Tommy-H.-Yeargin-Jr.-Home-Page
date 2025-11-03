import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Blog configuration
    BLOG_DIR = os.path.join(basedir, '..', 'blog')
    
    # Site configuration
    SITE_NAME = "Tommy H. Yeargin, Jr."
    SITE_DESCRIPTION = "Experienced bench jeweler/goldsmith since 1989. I code as a hobby."
    
    # Frozen-Flask configuration
    FREEZER_DESTINATION = 'build'
    FREEZER_RELATIVE_URLS = True
    FREEZER_IGNORE_404_NOT_FOUND = True