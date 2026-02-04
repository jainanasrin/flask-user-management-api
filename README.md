 # flask-user-management-api   
 
   A secure RESTful User Management API built with Flask featuring JWT authentication, user registration, protected routes, and profile CRUD operations.
# 🚀 User Management REST API with Authentication

   A secure and professional RESTful API built using **Flask** that provides user registration, login, JWT-based         authentication, and user profile management.

   This project demonstrates real-world backend development practices including authentication, authorization, database integration, and clean API design.



 #  📌 Features

  * User Registration
  * User Login with JWT Authentication
  * Protected Routes
  * View User Profile
  * Update User Details
  * Delete User Account
  * Password Hashing for Security
  * Token-based Authorization



# 🛠 Tech Stack

  * Python
  * Flask
  * Flask-JWT-Extended
  * Flask-SQLAlchemy
  * SQLite Database
  * Werkzeug Security
  * Postman (for API testing)


 # 📂 Project Structure


user_api/
├── app.py
├── models.py
├── auth.py
├── routes.py
├── config.py
├── database.db
├── requirements.txt
└── README.md





 # ⚙️ Installation & Setup

1️⃣ Clone the repository


    git clone <your-github-repo-link>
    cd user_api


2️⃣ Install dependencies


    pip install -r requirements.txt


 3️⃣ Run the application


    python app.py


# Server will start at:


    http://127.0.0.1:5000




 # 📮 API Endpoints

 🔐 Authentication

| Method | Endpoint       | Description           |
| ------ | -------------- | --------------------- |
| POST   | /auth/register | Register new user     |
| POST   | /auth/login    | Login & get JWT token |



 # 👤 User (Protected)

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| GET    | /user/profile | Get user profile |
| PUT    | /user/update  | Update user info |
| DELETE | /user/delete  | Delete user      |



#  🔑 Authentication Usage

  After login, you will receive a JWT token.

  Use this token in Postman:

  Authorization → Bearer Token → Paste token

  This token is required for protected routes.



# 🧪 Testing the API

You can test all endpoints using **Postman**.

Steps:

  1. Register a user
  2. Login to get token
  3. 3. Use token to access protected routes



# 📈 Future Improvements

  * Role-based access (Admin/User)
  * Token refresh system
  * Email verification
  * Password reset
  * API documentation with Swagger
  * Deployment to cloud



 # 💼 Project Use Case

This project can be used as a base for:

  * Web applications
  * Mobile app backends
  * Authentication services
  * Learning REST APIs



 # 👨‍💻 Author

   Developed by **Jaina Nasrin**



# ⭐ If you like this project

Give it a star on GitHub ⭐

 📜 License

This project is open-source and free to use.
