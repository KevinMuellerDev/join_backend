# Django App Installation Guide

This README provides instructions for installing and setting up the Django app.

## Prerequisites

Make sure the following software is installed:

- **Python** (version 3.8 or higher)
- **pip** (Python package manager)
- **virtualenv** (recommended)
- **Database** (SQLite)

## Installation

1. **Clone the repository**  
   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/KevinMuellerDev/join_backend.git
   cd <project-directory>

2. **Create a virtual environment**
    Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install dependencies**  
   Install the required Python packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt

4. **Start the development server**  
   Start the Django development server:
   ```bash
   python manage.py runserver

8. **Access the app**  
   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

