# Islamic-Charity-Portal-Aus-WebApp
Python/Javascript web application providing a directory/portal for zakaat and charity organisations located in Australia, highlighting key features of the charities

## Technology
This project is built on top of React(TypeScript), Flask and Postgresql.
Additionally MaterialUI is used for React components

---

## To contribute:
Start by navigating to a folder in a terminal/cmd of your choice then run:

`git clone https://github.com/aaadam3042/Islamic-Charity-Portal-AUS-WebApp.git`

---

### Frontend:

1. Ensure that npm is installed via this link: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
2. Run npm install in terminal in the frontend directory
3. Start contributing!
4. To test: run the backend, and then run `npm start` in the frontend directory

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
6. To test routes, run `python server.py` or similar

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

---

#### **Database:**

Contributers are required to set up a local postgresql database to test the application.

1. Download postgresql from the following page: https://www.postgresql.org/download/
2. Install postgresql and set up and start a server using the installed postgresql application (Keep the server running while developing)
3. Install requirements using (while in `/backend/`):
`pip install -r requirements.txt`
4. Create a new file called `.env`. The path should be `/backend/src/server/.env` (Don't need to create new if it already exists)
5. Add the following line to .env: `'DATABASE_URL='postgresql://localhost:[db port]/[db name]'`, where `db port` and `db name` refer to the values of the database you just set up. Details can be found on your running instance of the postgres server
6. Using a terminal in `src/server/` run `flask db migrate` to apply any database changes
7. Start contributing!

**When changing the database schema:** Ensure that you run `flask db migrate -m "[Your message here]"`, then `flask db migrate` to apply, before commiting to git 

**Image locations:** Images are stored in the database as a string representing their URL. The images themselves are to be stored in `servers/charities/upload/images` for charity organisation images.

**Database Schema:**

| User          |                  |     
| ------------- | ---------------- |     
| id: int       | Primary key      |     
| email: str    | Unique, NOT NULL |     
| isAdmin: bool | NOT NULL         |     


| Charity            |                  |
| ------------------ | ---------------- |
| id: int            | Primary key      |
| name: str          | Unique, NOT NULL |
| logoURL: str       | NOT NULL         |
| storefrontURL: str | NULLABLE         |
| adminFees: bool    | NULLABLE         |
| distribution: bool | NULLABLE         |


| Contact        |                       |
| -------------- | --------------------- |
| id: int        | Primary key           |
| charityID: int | Foreign Key, NOT NULL |
| type: str      | NOT NULL, NOT NULL    |
| value: str     | NULLABLE, NOT NULL    |


| Category  |                  |
| --------- | ---------------- |
| id: int   | Primary key      |
| name: str | Unique, NOT NULL |


| CharityCategory  |              |
| ---------------- | -----------  |
| charityID: int   | Foreign Key  |
| categoryID: int  | Foreign Key  |

| Location       |             |
| -------------- | ----------- |
| id: int        | Primary Key |
| charityID: int | Foreign Key |
| Street: str    | Foreign Key |
| Suburb: str    | Foreign Key |
| State: str     | Foreign Key |
