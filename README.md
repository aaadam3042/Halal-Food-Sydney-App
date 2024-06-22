# Halal Food Sydney
Python/Javascript web application providing a directory of halal location in
Sydeny, Australia.

## Technology
This project is built on top of React, Flask and Postgresql.
Additionally Material UI and tailwind is used to speed up development.

---

## Mockups
These are some basic mockups for some pages. Design is not final.


![Mockups](https://github.com/aaadam3042/Halal-Food-Sydney-App/assets/69839172/e387b90d-98be-4499-b70d-d7032993491d)

---

## To contribute:
Start by navigating to a folder in a terminal/cmd of your choice then run:

`git clone https://github.com/aaadam3042/Halal-Food-Sydney-App.git`

---

### Frontend:

1. Ensure that npm is installed via this link: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
2. Ensure that react-native dependencies are installed as per documentation: https://reactnative.dev/docs/environment-setup
3. Run `npm install` in terminal in the frontend directory
4. Start contributing!
5. To test: run the backend, and then run `npm start` in the frontend directory

---

### Backend:

#### **Flask App:**

1. Navigate to the backend directory in terminal
`cd backend`
2. Setup a virtual environment
```
virtualenv venv
source venv/bin/activate
```
3. Ensure that python is running from the virtual environment
`which python3`
OR
`which python`.
Output should be directory ending in `venv/bin/python3` or similar
4. Install requirements using:
`pip install -r requirements.txt`
5. Start contributing!
6. To manually test routes by running the server, run `python app.py` or similar, then make relevant calls

**If using an IDE:** Make sure to set the interpreter to the one located `venv/bin/python3`

**Troubleshooting:** 
If using MacOS and the interpreter does not seem to be set correctly, it is likely that this is due to symlinks. A solution would be to use a different interpreter which has all the requirements installed. This can be done by installing the requirements file on any python version and then setting it as the version to be used by the interpreter.

**When commiting changes:** If adding dependencies to the codebase run:
`pip freeze > requirements.txt`
**Note:** Ensure the correct interpreter is used on the terminal running this command

---

#### **Backend Tests:**

**Making tests:**

Ensure all routes have tests associated with them before making a pull request. 
Tests are to be located in `src/tests/` and all files should end in _tests.py.

Routes in seperate files should also have a seperate file for tests, however these files should be located directly in the `tests/` directory. For e.g:

`src/server/admin/routes.py` -> `src/tests/admin_tests.py`

**Running tests:**

Run tests with the following line in terminal: `pytest` 

**Troubleshooting:**

If pytest fails due to a module error, try:

MacOS/Linux: `export PYTHONPATH=/Absoulte/path/to/backend/src/server `

Windows: `set PYTHONPATH=C:\Absolute\path\to\backend\src\server`


To ensure that the path has been set, run `echo $PYTHONPATH`

---

#### **Database:**

Contributers are required to set up a local postgresql database to test the application.

1. Download postgresql from the following page: https://www.postgresql.org/download/
2. Install postgresql and set up and start a server using the installed postgresql application (Keep the server running while developing)
3. Install requirements using (while in `/backend/`):
`pip install -r requirements.txt`
4. Create a new file called `.env`. The path should be `/backend/src/server/.env` (Don't need to create new if it already exists)
5. Add the following line to .env: `DATABASE_URL='postgresql://localhost:[db port]/[db name]'`, where `db port` and `db name` refer to the values of the database you just set up. Details can be found on your running instance of the postgres server
6. Using a terminal in `src/server/` run `flask db migrate` to apply any database changes
7. Start contributing!

**When changing the database schema:** Ensure that you run `flask db migrate -m "[Your message here]"`, then `flask db upgrade` to apply, before commiting to git 

If flask db commands don't work, try applying the PYTHONPATH commands in the backend test section.

**Image locations:** Images are stored in ...
