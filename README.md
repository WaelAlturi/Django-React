# Login Register Project

This project is a full-stack application designed to handle user authentication through a login and registration system. It leverages modern web development technologies to create a robust, scalable, and secure system. The frontend is built with Vite and React.js, providing a fast and responsive user interface. The backend is developed using Django, a high-level Python web framework that promotes rapid development and clean, pragmatic design. To ensure the application is highly available and scalable, AWS services are utilized, with S3 for frontend asset storage and EC2 for hosting the backend.

## Frontend (Vite + React.js + Tailwind)
- **User Interface**: Handles user interactions and displays the login and registration forms.
- **API Requests**: Sends HTTP requests to the backend for user authentication (login/register) and receives responses.

## Backend (Django)
- **Authentication Logic**: Manages user registration, login, and session handling.
- **Database**: Stores user credentials and other relevant data securely.
- **API Endpoints**: Provides endpoints for the frontend to interact with (/register, /login).

## AWS S3
- **Frontend Asset Storage**: Hosts static assets such as images, CSS files, and JavaScript bundles used by the frontend application.

## AWS EC2
- **Backend Hosting**: Hosts the Django application, handling incoming API requests from the frontend.

## User Interaction
- **Users**: Interact with the frontend application to register and log in.

### Frontend Components:
- **Login.jsx**: Manages user authentication by handling the login and registration forms. It sends credentials to the backend for verification.
- **Home.jsx**: Displays a welcome message ("Hello") after successful login. Accessible only to authenticated users.
- **PrivateRoute.jsx**: A higher-order component that restricts access to Home.jsx for unauthenticated users. Redirects users to the login page if they attempt to access Home.jsx without being logged in.

## Setup

### Backend Development
- Used Django REST framework for API development and django-cors-headers for handling CORS.
- Defined key endpoints: `/api/register/` (POST) for user registration and `/api/login/` (POST) for user login.

### Integration with Frontend
- Used Axios or Fetch in Login.jsx to interact with the `/register/` and `/login/` endpoints.
- Installed Tailwind CSS for styling the frontend.
- Used React Toastify for frontend notifications.

## Links
- **Website**: [http://loginregister.s3-website.eu-north-1.amazonaws.com](http://loginregister.s3-website.eu-north-1.amazonaws.com)
- **Source Code**: [https://github.com/WaelAlturi/DjangoReact](https://github.com/WaelAlturi/DjangoReact)
