## MAYO

This is a web project for the Mentor A Youth (MAYO) initiative.

This project is still in development.

## Requirements
* Python (3.x)


## Quickstart
To set up this project on a local machine:

1. Ensure Python 3.4.x is installed on your machine.
2. (Optional) You may want to create a separate ``virtualenv``
3. Download and unzip or clone the project.
4. ``cd`` into the project directory.
5. Install the requirements with
    * ``pip install -r requirements/development.txt``
6. Copy example environment file with
    * ``cp env.example mayo/settings/.env``
7. Set up database with:
    * ``python manage.py makemigrations``
    * ``python manage.py migrate``
8. Runserver with
    * ``python manage.py runserver``
    * ``Go to http://127.0.0.1:8000``

## Contributors

[Abdulmajid Hamza](http://abdulmajid.com.ng)

## License

Creative Commons [(CC-NC-ND)](https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode)

