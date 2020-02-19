# ModernHealthExercise

The code is written in Python and Django Framework. The code was developed on Linux.
Follow the following steaps to run the code:
1. Install the virtual environment and activate it using following commands:\
  python3.7 -m pip install --user virtualenv\
  python3.7 -m venv env\
  source env/bin/activate
2. install the following packages:\
  django\
  psycopg2\
  djangorestframework\
  Pillow
3. Clone the project using git clone https://github.com/Surabhi08/ModernHealthExercise.git
4. Create postgres database using following commands in Linux:\
  sudo -su postgres\
  psql\
  CREATE DATABASE 'databasename';\
  CREATE USER 'username' WITH PASSWORD 'userpassword';\
  GRANT ALL PRIVILEGES ON DATABASE 'databasename' TO 'username';\
  \q\
  exit\
  #replace database name with the 'modernhealth', username with 'user', userpassword with 'password'
5. Change directory and add host and port in settings file\
  cd ModernHealthExercise\ModernHealthExercise\
  open settings file and edit the host address for database details\
6. Run the migration using\
  python manage.py makemigrations\
  python manage.py migrate
7. Load the initial seed data \
  python manage.py loaddata seed.json
8. Run the project using following command:\
  python manage.py runserver host:port \
  #host and port are optional if you want to run it on particulate host and port or else the program will be 127.0.0.1:8000
  
  To view all the details in the database navigate to program/ and all the programs with their sections and activity details will be retrieved from the database. \
  To view the details of programs navigate to program/1/ or program/2/ \
  To view the section for a program navigate to program/1/section/1/ \
  To view activity for the section navigate to program/1/section/1/activity/1/ 
 
You should be able to retrieve data for Programs, Sections and Activities. Also, activities may have a html field or a multiple choice question, thus the Activity model is such that it can store a html text or Question with its choices, along with a descriptor which tells whether the stored value is HTML or MCQ (1 for HTML, 2 for MCQ). If the text is MCQ, the question can be fetched by spliting the text by '?' and the choices can be fetched by spliting with ','.
 
 
