# ModernHealthExercise

The code is written in Python and Django Framework. The code was developed on Linux.
Follow the following steaps to run the code:
1. Install the virtual environment and active it using following commands:\
  python3 -m pip install --user virtualenv\
  python3 -m venv env\
  source env/bin/activate
2. install the following packages:\
  django\
  psycopg2\
  djangorestframework
3. Clone the project using git clone https://github.com/Surabhi08/ModernHealthExercise.git\
4. Run the migration using\
  python manage.py makemigrations\
  python manage.py migrate
5. Load the initial seed data \
  python manage.py loaddata seed.json
6. Run the project using following command:\
  python manage.py runserver host:port \
  #host and port are optional if you want to run it on particulate host and port or else the program will be 127.0.0.1:8000
