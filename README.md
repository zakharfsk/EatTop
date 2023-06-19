# EatTop
This is a starter project for building a Django REST Framework application with Docker Compose and Celery.

## Prerequisites
Make sure you have the following software installed on your system:

 - Docker
 - Docker Compose

## Getting Started
To get started with the project, follow the steps below:

1. Clone the repository:
```bash
git clone https://github.com/your-username/project.git
```

2. Change into the project directory:
```bash
cd project
```

3. Create a virtual environment (optional but recommended):
```bash
python3 -m venv env
source env/bin/activate
```

4. Install the project dependencies:
```bash
pip install -r requirements.txt
```

5. Start the Docker containers:
```bash
docker-compose up -d
```
This command will start the following services:

PostgreSQL database
 - pgAdmin 4 (a web-based PostgreSQL administration tool)
 - Redis (message broker for Celery) 
 - wkhtmltopdf (a tool for generating PDF files)

6. Migrate the database:
```bash
python manage.py migrate
```
7. Add fixtures:
```bash
python manage.py loaddata printers
```

8. Create a superuser for the Django admin:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter the username and password for the superuser.

9. Access the project:

 - Django API: http://127.0.0.1
 - pgAdmin 4: http://127.0.0.1:6789
   - username: `admin@gmail.com`
   - password: `qwerty`
 - PostgreSQL:
   - host: `127.0.0.1`
   - port: `15432`
   - database: `backend_db`
   - username: `postgres`
   - password: `qwerty`
 - Redis:
   - host: `127.0.0.1`
   - port: `16379`
 - wkhtmltopdf:
   - host: `127.0.0.1`
   - port: `80`

## Development Workflow
To start the development server, run the following command:
```bash
python manage.py runserver
```

To run Celery, open a new terminal window and run:
```bash
celery -A  EatTop.celery_app worker --loglevel=info -P gevent
```

## PgAdmin4
For connect to Db in PgAdmin4 use:
 - host: `postgresql`
 - port: `5432`
 - database: `backend_db`
 - username: `postgres`
 - password: `qwerty`
