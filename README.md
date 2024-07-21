Start up

To set up follow these 7 steps:

1: pipenv shell

2: pipenv install django=='4.1.3' autopep8=='2.0.0' pylint=='2.15.5' djangorestframework=='3.14.0' django-cors-headers=='3.13.0' pylint-django=='2.5.3'

3: Open VS Code and press ⌘SHIFTP (Mac), or CtrlSHIFTP (Windows) to open the Command Palette, and select "Python: Select Interpreter".
find the folder saying gearmaster-events-server

4: There should now be a .vscode folder in your directory. If there is not one, create it. Create/open the settings.json file and add the following lines:

{
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--django-settings-module=<folder name>.settings",
    ],
}

5: python manage.py migrate

6: Inside the .vscode create a file called launch.json. Paste the following code in that file.

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true,
            "autoReload":{
                "enable": true
            }
        }
    ]
}

7: python manage.py runserver
