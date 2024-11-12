# Django Authentication with JWT and Frontend

This project implements a simple user authentication system using Django REST Framework (DRF) and JWT (JSON Web Tokens). The backend handles user registration, login, and token management, while the frontend provides a user interface for login and registration.

## Features

- **User Registration**: Allows users to register with a username and password.
- **User Login**: Allows users to log in with their username and password and obtain JWT tokens.
- **Token Management**: Provides access and refresh tokens for authentication.
- **Frontend Forms**: A simple UI for logging in and registering users.

## Technologies Used

- **Backend**:
  - Django
  - Django REST Framework
  - Simple JWT for token management
- **Frontend**:
  - HTML
  - CSS (Minimal styling)
  - JavaScript (for API interaction)

## Setup

### Backend (Django)

1. Clone this repository:

   ```bash
   git clone https://github.com/mustafatavli195/drfSimplestJwtAuth.git
2. Navigate to the project directory:
    ```
    cd your-repository-name
3. Create and activate a virtual environment (optional but recommended)
    ```
    python -m venv venv
    venv\Scripts\activate # On Linux--> source venv/bin/activate 
4. Install dependencies:
    ```
    pip install -r requirements.txt
5. Apply migrations:
    ```
     python manage.py migrate
6. Run the Django development server
    ```
    python manage.py runserver
    
The backend will be accessible at http://localhost:8000.






