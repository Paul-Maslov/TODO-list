"# TODO-list" 

Site for managing the performance of personal tasks.
The TODO List is actually a notebook in which a person sets tasks and records their implementation.
Tasks are automatically sorted by their due dates, taking into account the completion marker
Button Complete if a task is not done and Undo if a task is done, this button changes the status
of the task to the opposite and redirects to home page.

✨ Images of the project

Home page

![image](https://user-images.githubusercontent.com/112548104/233767194-ec8463fe-e824-42cc-ba33-e3c8ccd56ee2.png)

Tag page

![image](https://user-images.githubusercontent.com/112548104/233767243-9911b2da-eecd-4783-9dd4-6508d6b95847.png)


✨ Initialization

👉 Step 1 - Download the code from the GH repository (using GIT)

```
git@github.com:Paul-Maslov/TODO-list.git
cd todo_list
```

👉 Step 2 Set Up for Windows

```
virtualenv env
.\env\Scripts\activate
pip3 install -r requirements.txt
```

👉 Step 3 Set Up Database

```
python manage.py makemigrations
python manage.py migrate
```

👉 Step 4 Start the app

```
python manage.py runserver
```

At this point, the app runs at http://127.0.0.1:8000/.

👉 Step 5 Create superuser

```
python manage.py createsuperuser
```

Link to this project

https://github.com/Paul-Maslov/TODO-list


