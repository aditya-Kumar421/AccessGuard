<h1 align="center" id="title">AccessGuard</h1>

<p id="description">AccessGuard is a robust and scalable multi-user access authentication system designed to provide seamless and secure access to digital resources. Whether it's a web application API or any other digital service AccessGuard ensures that only authorized users can access the system safeguarding sensitive data and resources from unauthorized access.</p>

<h2>🚀 Demo</h2>

[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

<h2>Project Screenshots:</h2>

<img src="https://i.ibb.co/jHGJ1K9/Screenshot-186.png" alt="project-screenshot" width="100%" height="400/">

<img src="https://i.ibb.co/NN8gXjV/Screenshot-185.png" alt="project-screenshot" width="100%" height="400/">

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Role-Based Access Control
*   Centralized User Management
*   Integration and Customization
*   Easy to Use

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the Project:</p>

```
git clone https://github.com/aditya-Kumar421/AccessGuard.git
```

<p>2. Create a Virtual Environment:</p>

```
python -m venv env
```

<p>3. Activate the Virtual Environment:</p>

```
env\Scripts\activate
```

<p>4. Install Dependencies:</p>

```
pip install -r requirements.txt
```

<p>5. Set Up Database:</p>

```
python manage.py migrate
```

<p>6. Run the Development Server:</p>

```
python manage.py runserver
```

<p>7. Access the Endpoints:</p>

```
http://localhost:8000/swagger/
```
<h2>Project Structure</h2>
jobManagement/
├── jobManagement/        # Django project directory
│   ├── __init__.py
│   ├── settings.py       # Django settings file
│   ├── urls.py           
│   └── wsgi.py           
├── jobOperation/         
│   ├── migrations/       
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py
│   ├── models.py         # Database models
│   ├── tests.py          
│   └── views.py          # Views and API endpoints
├── user/                 # Django app for user management/authentication
│   ├── migrations/       
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py
│   ├── models.py         # Database models
│   ├── tests.py         
│   └── views.py          # Views and API endpoints
├── manage.py             
└── requirements.txt      # Python dependencies

<h2>🍰 Contribution Guidelines:</h2>

Please contribute using GitHub Flow. Create a branch add commits and open a pull request

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Django Rest Framework
*   MySQL
*   JWT Authentication