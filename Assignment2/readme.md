# DD2480 Group 28 CI Server

This is a CI Server for Python projects written by group 28 for the Software Engineering Fundamentals course at KTH. The server supports three core features of continuous integration:

<ol>
<li>syntax check: the CI server performs a syntax check on the Python code</li>
<li>automated tests: the CI server performs automated testing</li>
<li>notification: the CI server notifies the user of the CI results through email and on a webpage</li>
</ol>

## Contributions

Yen Chen:

<ul>
	<li>Syntax checking
	<li>Testing suite
</ul>
Joel Lützow:
<ul>
	<li>Git management
	<li>Testing Integration
</ul>
Aïssata Maiga:
<ul>
	<li>Proof of concept
	<li>Debugging control flow
</ul>
Gautam Mukesh Manek:
<ul>
	<li>Created frontend
	<li>Integrated backend
</ul>
Jacob Mimms:
<ul>
<li>Created test skeleton
<li>Setup Email functionality
</ul>

# SEMAT team assessment

<img src="resources/sematpicture.png" width="50%" height="50%">

We believe ourselves to be in state “Collaborating” as we are now functioning as a unit, with open communication and focus on achieving the mission. We have different ambition levels but are working together to help each other out. To reach the next level, we have to align ourselves a bit more to each others’ goals so we can balance the work more effectively.
More specifically, we are working on the following three points to reach "Performing":

<ul>
<li> The team continuously adapts to the changing context.
<li> Effective progress is being achieved with minimal avoidable backtracking and
reworking.
<li> Wasted work and the potential for wasted work are continuously identified and
eliminated.
</ul>
We expect to get there by experimenting a bit more with group constellations and continuing to build on our communication.

# Installation/ Usage

## Setting up the virtual environment

create a virtual environment in the directory using the command:

```
python -m venv env
```

navigate to the newly created env folder, and in the file env/bin/activate, add the lines:

```
export USER2480="EMAIL"
export PASS2480="PASSWORD"
```

where EMAIL and PASSWORD are the email/password combination of a gmail accout you wish to act as the web server notification email.

Activate the virtual environment by running the command:

```
source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies by running:

```
pip install -r requirements.txt
```

Finally, start the server by running

```
python3 start_server.py
```

## Setting up ngrok

In a new terminal, install ngrok using:

```
pip install ngrok
```

and run the command:

```
ngrok http 4567
```

copy the url of the form http://x-x-x-x-x.ngrok.io and navigate to the webhooks interface of the repo you wish to work with. Add the url as the Payload URL with '/github', and select the following options:

<img src="resources/github_webhook.png" width="50%" height="50%">
  
Once the webhook is added and the server is running, push events on github will trigger the CI suite!!

# Database

For the server and frontend to work, an SQLite3 database needs to run locally. Install SQLite3 `https://www.sqlite.org/download.html` and unzip the folder. Create the database by navigating to the same folder and running the following command from the terminal:

```
sqlite3 test.db
```

Navigate to the server and ensure the `SQLALCHEMY_DATABASE_URI` inside `server.py` is set to the path of the sqlite3 database.

# Syntax Check

## Implementation

1. The remote branch where the change has been made is cloned when our server is triggered by webhook
2. The syntax check is conducted on the branch with pylint

## Unit Test

1. Push the code with syntax error to a specific remote branch, and our server should report "Syntax Error!!"
2. Push a code without syntax error to a specific remote branch, and our server should report "Ready for testing!!"

# Automated Tests

## Implementation

1. The remote branch where the change has been made is cloned when our server is triggered by webhook
2. The test is conducted on the branch with pytest

## Unit Test

1. Push the code with test that shoud fail to a specific remote branch, and our server should report "Some tests are failed." after testing
2. Push the code with test that shoud success to a specific remote branch, and our server should report "All testcases are passed!!" after testing

# Frontend

## Setup

Install node package manager by following instructions listed in https://docs.npmjs.com/getting-started before continuing with the setup of the frontend application.

## Installing

After cloning the repository, run the following command from the terminal

```
cd Assignment2/src/build-fe
npm install
```

Create an `.env` file at the root of the `build-fe` subdirectory and add the following environment variable, which should point to your local ngrok url:

```
REACT_APP_SERVER_URL=YOUR_NGROK_URL
```

Following this, start the server using te following command:

```
npm start
```

This should launch the react application at `localhost:3000`. Before accessing the frontend, ensure that the server is running and the database has been setup.

# Browsable documentation

## Python

Run:

```
python -m pydoc -p 1234
```

The browsable documentation is visible on `localhost:1234`.
