   # Smart investing

## Indice 📑
- Project Description
- Features
- Technologies and Libraries Used
- Installation
- Developers
## Project Description 📖

Smart Investing es una aplicación financiera dirigida a inversores en el mercado de valores, inicialmente enfocada en España. La aplicación permitirá a los usuarios buscar de manera personalizada, analizar y gestionar empresas cotizadas, utilizando filtros específicos que se ajustan a las preferencias individuales de cada usuario. Con funcionalidades diseñadas tanto para inversores novatos como experimentados, el objetivo es proporcionar una herramienta intuitiva y potente que ayude a los usuarios a tomar decisiones de inversión informadas.
## Features 📋

1.**User Management (API of Users)**:

User registration and authentication.
Management of user profiles.
Retrieval and updating of user data.


## Technologies and Libraries Used 🛠️

* Python 3.8 +
* Pytest 8.3.2
* Pytest-django 4.8.0
* Psycopg2 2.9.9
* Django 5.1
* djangorestframework 3.15.2
* djangorestframework-simplejwt 5.3.1
* Python dotenv 1.0.1

## Installation ⚙️

Follow these steps to set up the project in your local environment and get started.

### Instructions

1. **Create a fork of the repository**

   Open the [SmartInvesting_back](https://github.com/Seda07/SmartInvesting_back) repository on GitHub and click the "Fork" button in the top right corner of the page. This will create a copy of the repository in your own GitHub account.


2. **Clone your forked repository**

   Open a Git Bash terminal and run the command with the link to your new repository:

```bash
# Clone
git clone https://github.com/tu-usuario/VoyageCraft_back.git
```

3. **Open PyCharm and open the file you just cloned**


4. **To start, create a virtual environment via the terminal and then activate it**

```bash
# Create the virtual environment
python -m venv .venv
# Activate the virtual environment
.venv\Scripts\activate
#And if needed, deactivate the virtual environment
.venv\Scripts\deactivate
```


5. **Install the dependencies**
```bash
# If you have the requirements file, install the dependencies
pip install -r requirements.txt
# If you don't have it, do this to generate a requirements.txt file at the root of the project
pip freeze > requirements.txt
```


6. **Create your .env file**

You should create this at the same level as your requirements and it will be used to connect to the database you can create locally. 
(There is a sample file where you can view the data you need to include)


7. **Create your branch and start working!**

```bash
# Create the branch
git checkout -b feature/nombreDeTuRama
```

## Developers 🖥️

[**Seda Gevorgyan**](https://github.com/Seda07)
