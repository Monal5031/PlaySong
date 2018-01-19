# PlaySong
A small django app to play song or music via a direct link in background of the page.

# Important:
Make sure to use virtualenv to ensure that there are no dependency errors.
To install and activate a virtualenv
```
pip3 install virtualenv
virtualenv play-venv
source play-venv/bin/activate
```

# Requirements:
Make sure to use python version 3.3+
```
pip3 install -r requirements.txt
```

# Run Project
```
python manage.py migrate
python manage.py runserver
```

# Superuser Details
```
id: admin
password: adm12345678
```

# How to run:
```
1. Add a new entry in django admin panel.
2. Run the server.
3. Go to http://127.0.0.1:8000/play/play/<title>/ to play your song. 
```
