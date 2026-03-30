import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    WTF_CSRF_ENABLED = False  # For API endpoints

    # Portfolio data
    PORTFOLIO_DATA = {
        'name': 'John Doe',
        'title': 'Full Stack Developer',
        'email': 'john@example.com',
        'location': 'San Francisco, CA',
        'bio': 'Passionate developer with 5+ years of experience building scalable web applications.',
        'skills': [
            {'name': 'Python', 'level': 90},
            {'name': 'JavaScript', 'level': 85},
            {'name': 'Flask', 'level': 88},
            {'name': 'React', 'level': 80},
            {'name': 'PostgreSQL', 'level': 75},
            {'name': 'Docker', 'level': 70}
        ],
        'projects': [
            {
                'title': 'E-commerce Platform',
                'description': 'Full-stack web application with payment integration',
                'technologies': ['Python', 'Flask', 'PostgreSQL'],
                'github': 'https://github.com/user/ecommerce',
                'demo': 'https://demo.myapp.com'
            },
            {
                'title': 'Portfolio Website',
                'description': 'Responsive portfolio website built with Flask',
                'technologies': ['Python', 'Flask', 'Bootstrap'],
                'github': 'https://github.com/user/portfolio',
                'demo': None
            }
        ]
    }
from flask_cors import CORS
