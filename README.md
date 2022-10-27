# Team4 Software Engineering

Chess puzzle game
- Pygame (Python Framework)

## Pre-requisites
- git
- python3
- docker
- docker-compose

## Running the docker containers locally

> Note: if you are on linux all docker commands may need to run with sudo before

- `docker-compose up -d` - will start the postgres and pgadmin instances locally
    - postgres - binds to localhost 5432
    - pgadmin - binds to localhost 8080

## Stopping the docker containers locally

> Note: doing so will delete all the data, TODO: enable persistent data using docker volumes

- `docker-compose down`

## Running the database test script

- `python3 db.py` - creates some example tables (to be deleted later)

## Seeing the data in the database

1. Browse to localhost:8080
1. Enter `admin@admin.com` (or whatever is in the docker-compose.yml file)
1. Enter `example` for the password (or whatever is in the docker-compose.yml file)
1. Add a new server
    1. Give a name 
    1. On connection tab enter:
        1. host: chess_db
        1. user: postgres
        1. password: example
        1. database: postgres
1. Navigate to Database -> Public -> Schemas -> Tables -> vendors (if it does not exist, run the database test script which creates the table)
1. Left click on the table, and select View rows


HOW TO UPDATE:

git clone -b <BRANCH_NAME> https://github.com/h3its/Team4-ChessPuzzleGame.git      --> This will pull the current code from the branch you are aiming at

git init --> after your code is copied you must create a local git repo on your system to start commiting changes

##THE VIRTUAL ENVIORNMENT

if your virtual enviornment is not setup run the following:

python -m venv      --> This will create a virtual enviornment to install your dependencies

###Activate the Virtual Enviornment IMPORTANT
You must make sure the virtual enviornment is running before installing your dependencies!

mac: source venv/bin/activate

windows: venv\Scripts\activate

Then run:
pip install -r requirements.txt

Now:
git remote add origin https://github.com/h3its/Team4-ChessPuzzleGame.git     --> This will add the github repo as your remote repository

git push --set-upstream origin <YOUR_BRANCH_NAME>   --> This will push your changes to YOUR INDIVIDUAL BRANCH on github, we will merge these changes individually into the main code base.

Now you should be able to see the changes you committed on github

Shane is updating this...
