# CollegeWall - Final Project CS50W

For my final project for CS50Web I created a note-taking app for university that let users organize their notes in terms and courses, apart from writing them on the app itself and customize it as if it were a CMS like WordPress. The technologies used for the development have been Django (Python), JavaScript, HTML, CSS and SQLite. The app is mobile responsive as required on the project specs.

### Features

The app has the following features:

* Term and course creation in order to easily organize and arrange your notes.
* Note taking editor that fully lets you customize the content of your notes just like WordPress.
* Dashboard page displaying the most recent notes taken.

### Files

The application consists of the following files to make possible the previous functionalities:

- requirements.txt: needed installations for the project to work.
- manage.py: django file to launch the app.

- STATIC: Contains all the JavaScript and CSS files.

- COLLEGEWALL: Django project folder that contains the general settings, urls and views.
    wsgi.py
    urls.py
    views.py
    serializers.py
    settings.py

- NOTES: App folder containing views, urls, forms, models for the app's logic.
    views.py
    tests.py
    urls.py
    serializers.py
    models.py
    apps.py
    admin.py
    context_processors.py
    forms.py
    MIGRATIONS

- TEMPLATES: HTML templates that display the UI
    base.html
    course_edit_delete.html
    course_list.html
    courses_of_term_edit_delete.html
    dashboard.html
    index.html
    note_update.html
    notes_edit_delete.html
    notes_list.html
    notes.html
    register.html
    term_edit_delete.html
    term.html
    test.html
    update_course.html
    update_term.html

