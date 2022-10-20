# Team4 Software Engineering

Chess puzzle game
- Pygame (Python Framework)

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

my change to push