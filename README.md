# IKONIC EVENTS


## Table of Contents
* [Introduction](#Introduction)
* [Wireframes](#Wireframes)
* [Database Design](#Database-Design)
* [Features](#Features)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Project Creation](#Project-Creation)
    * [Heroku Deployment](#Deployment-To-Heroku)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Acknowledgements](#Acknowledgements)


## Introduction

## Wireframes

## Database Design

## Features

## Technologies
* [HTML](https://en.wikipedia.org/wiki/HTML)
	* This project uses HTML as the main language used to complete the structure of the Website.
* [CSS](https://en.wikipedia.org/wiki/CSS)
	* This project uses custom written CSS to style the Website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    * JS was used to load the toasts and to create the Stripe payments. It was also used for the refresh/scroll functionalty on the chatrooms.
* [Python](https://www.python.org/) 
    * This project was created using Python framework [Django](https://www.djangoproject.com/) following Model-View-Template design and 
* [DJANGO](https://www.djangoproject.com/)
    * Python framework the application was built on

## Testing

### Test Results

## Deployment

### Project Creation
To create this project I used the `git init` command in the terminal from VS Code.

I then used the `git add .` command followed by `git commit -m "Initial commit"` and was then prompted to create a new repository 
with the choices of public or private.

The following commands were used for version control throughout the project:

`git add <filename>` - This command was used to add files to the staging area before committing.

`git commit -m "commit message explaining the updates"` - This command was used to to commit changes to the local repository.

`git push` - This command is used to push all committed changes to the GitHub repository.


### Deployment to Heroku

**Create application:**
1. Navigate to Heroku.com and login.
1. Click on the new button.
1. Select create new app.
1. Enter the app name.
1. Select region.

**Set up connection to Github Repository:**

1. Click the deploy tab and select GitHub - Connect to GitHub.
1. A prompt to find a github repository to connect to will then be displayed.
1. Enter the repository name for the project and click search.
1. Once the repo has been found, click the connect button.


**Add PostgreSQL Database:**

1. Click the resources tab.
1. Under Add-ons seach for Heroku Postgres and then click on it when it appears.
1. Select Plan name Hobby Dev - Free and then click Submit Order Form.

**Set environment variables:**

1. Click on the settings tab and then click reveal config vars.
1. Variables added:<br>
    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    * DATABASE_URL
    * EMAIL_HOST_PASS
    * EMAIL_HOST_USER
    * SECRET_KEY
    * STRIPE_PRICE_ID
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET
    * USE_AWS

**Enable automatic deployment:**
1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Run Locally

1. Navigate to the GitHub [Repository](https://github.com/Daisy-McG/IKONIC-EVENTS).
1. Click the Code drop down menu.
1. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1. Open your developement editor of choice and open a terminal window in a directory of your choice.
1. Use the `git clone` command in terminal followed by the copied git URL.
1. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:
`pip install -r requirements.txt`

### Fork Project 

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point 
for your own idea. - Definition from [Github Docs](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).

1. Navigate to the GitHub Repository you want to fork.
1. On the top right of the page under the header, click the fork button.
1. This will create a duplicate of the full project in your GitHub Repository.

****
## Credits

### Acknowledgements

Developers:
* [Tanya](https://github.com/datonex)
* [Alaa](https://github.com/Hijazi-alaa)
* [Matt](https://github.com/Matthew-Hurrell)
* [Daisy](https://github.com/Daisy-McG)

Facillitator:
* [Jim](https://github.com/JimLynx)