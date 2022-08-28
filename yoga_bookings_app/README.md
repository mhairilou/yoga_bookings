# The requirements for the app and the technologies it uses
This project uses Flask and postgresql and python3.

# A project brief/a list of things the app can do
The app allows you to add, edit and view sessions, students and bookings. It has pages that display all sessions/classes and all students. You can also view more details by clicking "view". The 

# Step by step process of how to get the app working (including the command you would type into the terminal)
To set up the app, open a terminal (command + space on mac) and type:
 ```
dropdb yoga_bookings
createdb yoga_bookings
psql -d yoga_bookings -f db/yoga_bookings.sql
python3 console.py
flask run
```
on mac press command and click on the url (http://127.0.0.1:4999)
Go to your browser to view the app.

# Some instructions on navigating the app
The homepage will show you four options. The first two are drop-down menus, the second two are buttons. Click on an option to go to that page. When adding a new student or new class, fill in all the details on the form to avoid an error message. Use "view" to see more details about a student or session, "edit" to update, "delete" to remove and "book" to create a new booking for that student or session. Please note, students can not be removed. When a session is removed, the corresponding bookings will also be deleted. 
