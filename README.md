<p align="center"> <!-- Replace with your own banner image --> <img src="assets/banner.png" alt="Tech-Inshight" width="100%" /> </p> <h1 align="center">Tech-Inshight</h1> <p align="center"> <strong>Your go-to hub for backend development, API design, and modern system insights—all delivered with clarity and flair.</strong> </p> <p align="center"> <img src="https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django&logoColor=white" alt="Django" /> <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Backend-Blogging%20Platform-yellow?style=for-the-badge" alt="Backend Platform" /> <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="MIT License" /> </p>
<br>
<h1>What is Tech-Inshight</h1>

Tech-Inshight is a modern blogging platform built using Django, crafted to deliver hands-on tutorials, clean architecture, and practical insights for developers. Its goal is to demystify concepts like backend development, REST API design, database handling, and scalable system design—all wrapped in a user-friendly interface

<h2>Key Features </h2>

📝 Create, manage, and publish blog posts seamlessly

⏱️ Automatically calculate and display reading time

Full-text search & intuitive filtering for posts

Secure user authentication and profile management

Admin dashboard to control content flow

Responsive design with Django templates and CSS

<h2>Tech Stack </h2>
<h3>Component	Technologies Used </h3> <br>
<strong>Backend</strong>	Django, Django REST Framework (DRF) <br>
<strong>Database</strong>	SQLite (development), PostgreSQL (production)<br>
<strong>Frontend</strong>	HTML5, CSS3, Django Templates<br>
<strong>Deployment</strong>	Docker, Render <br>
<br>
<stong>Tech-Insight</stong><br>
├── blog/             # Blog functionality (models, views, templates)<br>
├── users/            # User authentication & profiles<br>
├── media/            # Uploaded images<br>
├── staticfiles/      # CSS, JS, and client assets<br>
├── manage.py         # Django entry script<br>
├── requirements.txt  # Python dependencies<br>
├── README.md         # This file<br>
└── LICENSE.md        # Project license<br>
# Clone the repository
git clone https://github.com/AyushPatiTripathi/Tech-Inshight.git
cd Tech-Inshight

# Create and activate a virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
