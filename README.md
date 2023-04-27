"TODO-list" 

Site for managing the performance of personal tasks. 

The TODO List is actually a notebook in which a person sets tasks
and records their implementation. 

Tasks are automatically sorted by their due dates, 
taking into account the completion marker Button 
Complete if a task is not done and Undo if a task is done, 
this button changes the status of the task to the opposite and redirects to home page.


✨ Initialization

👉 Step 1 - Download the code from the GH repository (using GIT)

```angular2html
git@github.com:Paul-Maslov/TODO-list.git
cd TODO_list
```


👉 Step 2 Create virtual venv
```angular2html
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt

```

👉 Step 3 Start the app

```angular2html
python manage.py migrate
```

👉 Step 4 Start the project

```angular2html
python manage.py runserver
```

At this point, the app runs at http://127.0.0.1:8000/.

Link to this project

https://github.com/Paul-Maslov/TODO-list

Credential Username:
```angular2html
login: test_user
password: user12345
```
