# 1. Activate Environment in Powershell:

`cd .\.venv\Scripts\`
`activate.ps1`

# To run:

`python manage.py runserver`

# Create DB superuser:

`python manage.py createsuperuser`

# Converting Class models through ORM into DB tables:
Once the model is defined in the 'Models.py' file we can proceed with.
`python manage.py makemigrations`
`python manage.py migrate`

Just by the ongoing app, go to 'admin.py' and add the model that can be displayed.

# Using Django shell for creating and querying data:

`python manage.py shell`

The class shall be imported first as follows:
`from notes.models import Notes`
Create a variable to store the information. Note that 'Notes' is the class we're querying.
`mynote = Notes.objects.get(pk='1')`
We can access the attributes by typing:
`mynote.title`
Or querying all the objects with, that will return a Queryset "List on steroids"
`Notes.objects.all()`
*Create notes* from shell:
`new_note = Notes.objects.create(title="Second note", text="This is a second note")`
*Filter notes*
`Notes.objects.filter(title__startswith="My")`
*Exclude filter notes*
`Notes.objects.exclude(text__icontains="Django")`
*Concatenate filter*
`Notes. objects. filter(text__icontains='Django').exclude(title__icontains='Django')`
*Users*
`from django.contrib.auth.models import User`
`user = User.objects.get(pk=1)`
`user`

# How to handle auth on class based views
With mixing class we can add additional features

## Notes:
Every app must be mentioned in the 'settings.py from the MAIN app'

# Users in Django

![Alt text](.venv/Scripts/photos/User.png?raw=true "getUserInShell")

