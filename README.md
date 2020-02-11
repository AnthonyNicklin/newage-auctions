[![Build Status](https://travis-ci.org/AnthonyNicklin/newage-auctions.svg?branch=master)](https://travis-ci.org/AnthonyNicklin/newage-auctions)

# Newage Auctions

## Full Stack Web Development 

![NAA Logo](https://newageauctions.s3-eu-west-1.amazonaws.com/static/images/naa_logo.png)

## Table of Contents

1. [Aim](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#aim)
2. [UX](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#ux)
3. [Features](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#features)
4. [Database Schema](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#database-schema)
5. [Database Design](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#database-design)
6. [Technologies Used](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#technologies-used)
7. [Application Logic](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#application-logic)
8. [Testing](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#testing)
9. [Deployment](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#deployment)
10. [Credits](https://github.com/AnthonyNicklin/newage-auctions/tree/develop#credits)

## Aim

Auctions are exciting, fast-paced and fun but, getting to one can be a problem for some looking for the one-off or rare item they wish to add to their collection. Welcome to [Newage Auctions!](https://newage-auctions.herokuapp.com)

Bringing auctions into the connected digital age has solved the problem of busy private or commercial collectors not able to attend every auction they wish to be at. 

This web application is run and administered by the owner of the website who is the seller. All administrative tasks are carried out in the admin dashboard by the administrator only.

## UX

Starting with a mobile first design approach to this project I started creating mockups and wireframes for mobile and small screens. I then moved onto creating mockups and wireframes for medium and larger screens. The design of the site is clean and simple. Mockups and wireframes can be viewed via this link - [Mockups/wireframes](https://github.com/AnthonyNicklin/newage-auctions/tree/develop/mockups_wireframes).
Below are user stories that were conducted in order to gain clear goals that needed to be achieved for this website.

1. I want an online auction site.
2. I want to add, update and delete item listings.
3. I want a display to show all listings in a summarized view.
4. I want pagination.
5. I want a search engine for listings and auctions. 
6. I want to display a detailed item page for each item. 
7. I want customers to create, update, and delete their own accounts.
8. I want only logged in users to place bids.
9. I want a secure payment process.

The navigation bar is responsive having break points for smaller, medium and large screens. The navigation links disappear on screen widths below 992 pixels and a burger menu icon appears top left. When the burger icon is clicked, it brings a side navigation bar across from the left. The navigation bar is fixed to the top with a back to the top buttom that appears once a user scrolls down.

If a user is not authenticated on the site then 'Login' and 'Register' will populate the nav bar. If the site visitor is authenticated 'Account' replaces 'Login' and 'Register'.

When a user first visits the site they are presented with a landing picture and description of the website. The picture chosen helps to explain the digital concept of auctions and then a short description of the web application. Featured Lots gives the visitor a quick taste of the lots on offer. Presented with just an image and name in order to not clutter this important section. The bottom section has some easy on the eye images and some more content to help turn the visitor into a bidder.

Auctions, Lots, and Category summary pages show valid current Lots and Auctions. The UX concept here was less is more, executed by keeping the content inside the summary cards to a minimum. A search bar across the top of these pages ties in by giving the box a lighter, softer blue then the primary site colour.
Auction and Lots detail pages split the image and content apart giving each some breathing space. This breathing space makes digesting the information on the page easier and more appealing. A link at the top provides a way back to either summary page.

All forms for logging in, creating, updating, password reset etc and checkout have the same form design. Again, using the softer blue background to tie it in with the site and also help the input fields stand out. Messages are displayed at the top of the page to grab the users attention with corresponding colors to the event like red for errors, and green for success.

The shopping cart displays the items in the cart in a clean and decoupled way. This makes it easy for the user to see what they are going to purchase. Making the cart in a more table like format breaks from the mold of the summary pages, but still in keeping with the site. 

## Features

The list below shows all the added features that needed to be in place for the project to be fully functional. The features planned to be added in the future are listed in the “Future Features” section of this document.

### Features on this website are:

* Login - allows user to login 
* Sign Up - sign up new users
* Profile - edit, update, change the password or delete the account
* Asynchronous Tasks - running tasks periodically
* Featured Lots - allows users to navigate straight to lots that have been flagged by the site owner
* Auctions - shows summarized view of all auctions not expired
* Lots - shows summarized view of all valid lots 
* Categories - shows summarized view of all valid lots by category
* Site admin - Create, edit, delete auctions, lots and orders
* Payment - secure payment method using Stripe integration

### Future features

* Multiple lots in an auction
* Order history
* Wish list
* Notification system to alert when a user has been out bidded

## Database Schema

I chose to use PostgreSQL a relational database for this application. My reason for this is, links need to be created and maintained between objects.

![SQL Diagram](https://newageauctions.s3-eu-west-1.amazonaws.com/static/images/sql_diagram.png)

## Database Design

Relationships between tables are as follows:

* user and profile- one to one relationship as one record in the user table can be associated with only one profile;
* lot and auction - one to one relationship as one record in the lot table can be associated with only one auction;
* auction and bid - one to many relationships as an auction can have many bids;
* auction and user - one to many relationships as a user can be a winner of many auctions;
* auction and orderlintitem - one to many relationships as many auctions can be in an order;
* bid and user - one to many relationships as a user can bid as many times as he/she wishes;
* order to orderlineitem - one to many relationships as a order can have many items (auctions) in it.

## Technologies Used

Below are a list of the programming languages, technologies and frameworks used for this website.

* HTML5
* CSS3
* JavaScript
* Python
    * Server-side scripting language.
* [Celery](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
    * Run asynchronous tasks periodically.
* [Django 3.0](https://www.djangoproject.com/)
    * Python web application framework.
* Markdown
    * Used to write README.md file.
* [PostgreSQL](https://www.postgresql.org/)
    * Relational database used for the application database.
* [Bootstrap4.3.1 framework](https://getbootstrap.com/)
    * The web application uses the Bootstrap framework for it's grid system, page layout, button styling and responsive navigation bar.
* [Travis CI](https://travis-ci.org/) 
    * Continuous Integration and to help test functionality.
* [Visual Studio Code](https://code.visualstudio.com/)
    * Visual Studio Code was used as the IDE to write the web application.
* [Heroku](https://www.heroku.com/) 
    * Hosting platform the production site is hosted on.
* [AWS S3](https://aws.amazon.com/) 
    * For hosting static files for the web application.
* Python Virtual Environment
* [Marvel App](https://marvelapp.com/)
    * This was used to design and create the wireframes for this project.
* [Google Fonts](https://fonts.google.com/)
* Git
    * Version control.
* [Github](https://github.com/)	
    * Remote repository.
* Google Chrome Developer Tools
* Firefox Inspector
* [Google Docs](https://docs.google.com/)
    * Write the contents of the README.md file.
* [DBDiagram](https://dbdiagram.io/home) 
    * A relational database diagram design tool used to create the database schema.

## Application Logic

### Apps

#### Accounts
The accounts app holds all the logic for anything to do with user accounts. I utilized Django's built-in user authentication system and added extra functionality  by attaching profiles to each user account. 

#### Auction
Lots and auctions are created and processed within the auction app. All CRUD operations are handled within the admin dashboard. Authenticated users can use the bid form at the bottom of each auction to place a bid only if higher then the current bid.

A Celery beat is run every minute which fires a function to: 
* Set auction to expired if the time_ending is less than the current date and time.
* Find the winning bid and the user who placed this bid and set this user as the winning bidder. 

The Celery function lives in [tasks.py](https://github.com/AnthonyNicklin/newage-auctions/blob/master/auction/tasks.py) and the Celery beat can be found in the [settings.py](https://github.com/AnthonyNicklin/newage-auctions/blob/master/newageauctions/settings.py).

*Note to assessors, please use the following credentials in order to log into the admin dashboard: assessor / e3nod34LLer3

**Note to assessors, to ensure you are able to review the payment process fully I have created multiple user accounts with auctions already in user shopping carts. Please use the following accounts:
* James32  / kan34KJH34
* Ben343 / lajfKj343a
* Joun343 / kda793jKJ3
* Smithy23 / kdjnf98KJ33

From the date of submission I have staggered auctions to expire at different intervals from 2 days, 1 week, 2 weeks, 1 month and 2 months. You can amend the auction expiry times manually if required by logging into the admin dashboard > *Auction* > *Auctions* > Amend the time ending date and time and make sure the *Expired* checkbox is not ticked and *Paid* checkbox.

If at any point you require items to populate back into a users shopping cart, log into the admin dashboard. Under Auction click on *Auctions* > Choose a auction > Tick *Paid* and then select the user account to populate their shopping cart. Also ensure the *Expired* checkbox is ticked.

#### Cart
The cart app renders the users shopping cart and also lets them remove an item if they wish to not go through with the purchase.

#### Checkout
The Checkout app handles the payment process. I have integrated Stripe payments and used their API as a secure way to process payments. The server-side logic is held in the [views.py](https://github.com/AnthonyNicklin/newage-auctions/blob/master/checkout/views.py) and the client-side logic is in [static/js/stripe.js](https://github.com/AnthonyNicklin/newage-auctions/blob/master/static/js/stripe.js).

#### Home
Home renders the home page for now. I created a reusable app for the home page as future features will include more pages and features that will be added to this app.

#### Search
The search app holds the search logic for categories, search auctions and search lots bar. Auctions and lots use keywords to search and then display the results back. Categories are simply filtered by the category and then rendered on a categories page.

## Testing

I conducted testing across different platforms and web browsers in order to make sure the website looked great across each one. I also asked friends and family to test across their own devices and to give me honest opinions and feedback.

Platforms:

* Samsung Galaxy 8
    * Google Chrome
    * Firefox
    * Samsung web browser
* Ubuntu 18.0
    * Google Chrome
    * Firefox
* Windows 7
    * Google Chrome
    * Firefox
    * IE 11
* Kindle Fire
    * Amazon Silk

### Code Validation

* CSS - validated using the W3C CSS Validation Service - Jigsaw.
* HTML - validated using the W3C Markup Validation Service.
* JavaScript - validated using JSHint.

###  Manual Testing
Manual testing was conducted to ensure the user story objectives were achieved.

1. I want to add, update and delete item listings.
    * Login to admin dashboard
    * Click on 'Lot items' under 'Auctions'
    * Click 'add lot'. Fill out the form then click 'Save'
    * Click on the created lot. Amend fields then click 'Save'
    * Click on the radio button next to the lot. Select from the dropdown list 'Delete selected lot items' > Click 'Go'
2. I want a display to show all listings in a summarized view.
    * On Auctions, All Lots and Category pages
        * Navigate to each summary page using their respected links in the navigation bar
        * Check to see that items or auctions are displayed correctly in a summarized view
3. I want pagination.
    * On Auctions, All Lots, Categories, Bidding history
        * Navigate to each summary page using their respected links in the navigation bar
        * Ensure only 10 items are displayed on the page
        * Click next to view the next 10 items
        * Click previous to go back to the first 10 items
4. I want a search engine for listings and auctions. 
    * On Auctions, All Lots and Category pages
        * Navigate to each summary page using their respected links in the navigation bar
        * Check to see the search bar appears at the top of the page
        * Enter in a keyword and click 'Search'
        * Check the search results comes back with correct items
5. I want to display a detailed item page for each item.
    * Click on 'Lots' or a 'Category' from the dropdown in the navigation bar
    * Click on a lot summary tile
    * Lot detail page should render
6. I want customers to create, update, and delete their own accounts.
    * Click on 'Register'
        * Fill out the registration form and click 'Register'
    * Login and then click 'Account' then click on the users name that appears in the dropdown menu to view the profile
        * Amend fields and click 'Update'
        * Repeat then click 'Cancel'
    * Login and then click 'Account' > then click on the users name that appears in the dropdown menu to view the profile
        * Click 'Delete' then 'Delete' again on the modal
        * Try to log back in to see if the account has been deleted
7. I want only logged in users to place bids.
    * Ensure the user is not logged in
    * Click on 'Auctions' then click on an auction
    * Check and make sure the bid form is hidden
    * Login and navigate to an auction
    * Check the bid form is now viewable
    * Place a bid and check a success message appears and the current bid amount has changed
8. I want a secure payment process.
    * Login then navigate to 'Shopping Cart'
    * Scroll to the botton and click 'Checkout'
    * Fill out the form using Stripes Test card number 4242424242424242
    * Check to see is a success message appears.
    * Log into Stripe Account and check payment was process in the dashboard

### Automated Testing

Automated tests were written using the Django test framework and are located in 'testing' directory under each app. 

#### Test Directory Structure

* test_forms.py - forms are created and valid.
* test_models.py - test labels are assigned correctly and any conditions for the model are met.
* test_views.py - test the view returns the correct html page and any parameters.

### Continuous Integration

Throughout the development of the project after setting up Heroku, TRAVIS CI tool was utilised to ensure that the builds would be runnable on the Heroku application, the commands for this are contained within the Travis.yml file.

### Issues encountered

#### Running asynchronous tasks 
I required my web application to set auctions to expire and also populate user shopping carts via an automated process. I found when researching how this can be done not be as straightforward as one would think. However, Celery came to the rescue. The initial set up for local development was OK but, I ran into issues when trying to deploy to Heroku. Heroku requires additional dynos and configuration which at first upsetted the way it was working locally. 

#### Stripe client-side error messages
I have been unable to get stripe errors messages for errors that happen on the client-side to display. An example is, as this application uses the test api keys the card number 4242424242424242 will only work. When trying to submit another card number Stripes error messages are failing to display. After a lot of troubleshooting I have still been unable to overcome this but will continue to work on this problem.

Stripe client-side error messages is the only bug that has not been resolved due to time left on the course.

## Deployment

The web application was created using Visual Studio Code. Git was used for version control and pushed to a remote repository hosted on [Github](https://github.com/).

The web application is deployed using Heroku and can be viewed here - [Newage Auctions](https://newage-auctions.herokuapp.com)

The web application was built and tested locally and once near completion it was pushed to Heroku by linking the master git branch from the remote Github repository to the app created in Heroku. All changes pushed to the master Github branch automatically pushed to the production application in Heroku. 

To ensure additional features and testing was conducted before being pushed to the production environment in Heroku. I created a development branch in git. All changes were pushed with commits first to the development branch then once happy merged into the master branch. Then as mentioned this would automatically push to the production environment.

There are two differences between the development environment and the production environment. 

1. Development environment uses SQLite for its database where the production environment uses PostgreSQL.
2. Production environment DEBUG is set to False. Development DEBUG is set to TRUE.

Functions have been written in the setting.py file to recognise which environment the application is running on.

### How to deploy the code locally

If you wish to run this code locally then please follow the instructions below.

1. Download the code from the Github repository at [https://github.com/AnthonyNicklin/newage-auctions](https://github.com/AnthonyNicklin/newage-auctions).
2. Click on Clone or *download* then *Download ZIP*. This will download the code into a ZIP folder locally on your computer.
3. Uncompress the ZIP folder.
4. Create a virtual environment. Tutorial of how to create a virtual environment can be found here. [https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
5. Activate the virtual environment.
6. Install the necessary Python packages in the requirements.txt file.
    * `pip3 install -r requirements.txt`
7. Set environment variables. On MacOS and Linux add the following code to your /.bashrc or /.bash_profile files. For Windows, create a new folder within the top level of this project and create a file to add the code in.
```bash
# Environment variables for Django projects
export DB_USER=<DB admin username>
export DB_USER_PASSWORD=<DB user password>
export EMAIL_HOST_USER=<email address>
export EMAIL_HOST_PASSWORD=<email password>
export SECRET_KEY=<secret key>
export STRIPE_PUBLISHABLE=<stripe publishable key>
export STRIPE_SECRET=<stripe secret key>
export AWS_STORAGE_BUCKET_NAME=<AWS bucket name>
export AWS_ACCESS_KEY_ID=<AWS access key ID>
export AWS_SECRET_ACCESS_KEY=<AWD secret access key>
export CELERY_BROKER_URL=<celery broker URL>
export DEBUG=True
```
8. Create an AWS account by following these instructions. [https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
9. Create a AWS s3 bucket using these instructions. Make sure your bucket is set to public under the permissions tab. [https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
10. Install Rabbitmq message broker for MacOS or Linux. For Windows click [here](https://www.rabbitmq.com/install-windows.html) for detailed instructions.
    * Follow the installation steps [here](https://www.rabbitmq.com/#getstarted) for installing Rabbitmq.
    * Set local path `export PATH=$PATH:/usr/local/opt/rabbitmq/sbin`
    * You may need to add your hostname to /etc/hostfile if using a Mac
    * Type the following command into a terminal below to configure Rabbitmq.
    ```bash
    sudo rabbitmqctl add_user <user> <password>   
    sudo rabbitmqctl add_vhost <virtual host name>
    sudo rabbitmqctl set_user_tags <user> <tag>
    sudo rabbitmqctl set_permissions -p <virtual host name> <user>  ".*" ".*" ".*"
    ```
    * Check the Rabbitmq server is running `sudo rabbitmq status`
11. Install Celery for MacOS or Linux by following the steps below. For Windows, Celery does not support Windows. There are some work arounds like this from StackOverflow [https://stackoverflow.com/questions/37255548/how-to-run-celery-on-windows](https://stackoverflow.com/questions/37255548/how-to-run-celery-on-windows)
    * Start the worker with log lever on info. Only set the log level in development enviroment. `celery -A app.celery beat --loglevel=info`
    * Start Celery Beat with log lever on info. Only set the log level in a development environment. `celery -A app.celery beat --loglevel=info`

### Deploy to Heroku

This project was deployed to Heroku and uses Heroku for its production environment. Instructions are below on how to deploy this web application to a production environment in Heroku.

**Git must be installed onto your computer. Instructions for installing Git can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

**Heroku CLI must be installed in order to deploy to Heroku using these instructions. Please follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli) to download and install Heroku CLI. 

1. Open up Heroku and navigate to your dashboard.
2. Select 'New' > 'Create New App' and fill out the details required then hit 'Create App'.
3. Select 'Settings' > 'Reveal Config Vars'
    * Enter in the same environment variables that are in step 7 of deploying code locally.
4. Download the code from the Github repository [here](https://github.com/AnthonyNicklin/newage-auctions)
5. Click on Clone or *download* then *Download ZIP*. This will download the code into a ZIP folder locally on your computer.
6. Uncompress the ZIP folder.
7. Open up a terminal or cmd prompt and login into Heroku CLI.
    * `heroku login`
8. Check the app is present.
    * `heroku apps`
9. A Proflice has already been created for this project but make sure it is present. If for some reason it is not then follow the steps below to create one.
    * Procfile
        * In a terminal make sure you are in the root directory of the project then run `touch Profile`.
        * Add the following code to the Procfile 
        ```
        web: gunicorn newageauctions.wsgi:application
        worker: celery -A <your_app_name>.celery worker
        celery_beat: celery -A <your_app_name>.celery beat
        ```
10. Add a new git remote for Heroku.
    * `git remote add heroku git@heroku.comYOUR_APP_NAME.git`
11. Push to Heroku.
    * `git push heroku master`
12. Give Heroku a few minutes to get it all set up and then check the activity logs under the Activity tab in your Heroku dashboard.
13. Once the build is complete click on 'Open App' top right to see Newage Auctions in action.

### PostgreSQL on Heroku
 
To install and set up a PostgreSQL database follow the well document instructions provided by Heroku at [https://devcenter.heroku.com/articles/heroku-postgresql](https://devcenter.heroku.com/articles/heroku-postgresql).

### Celery on Heroku

You need to install the CloudAMQP add-on in order to install and run Rabbitmq in Heroku. Under the Resources tab click 'Find more add-ons' > 'Messaging and Queues' the click on 'CloudAMQP' > 'Install CloudAMQP'.

To test if Celery is setup correctly and working. Log into the Heroku CLI and run:
`heroku run celery -A <your_app_name>.celery worker --beat --loglevel=info`. The logs will display any errors when the functions and also let you know if they are successful. 

To enable or disable Celery under the Resources tab click on the edit icon next to 'celery_beat' and 'worker' > slide the button to enable > 'Confirm'.

## Credits

### Content 

Content written for lot items and auctions are completely fictional and not historic facts or were taken from various pages on [Wikipedia](https://www.wikipedia.org/). 

### Images

All images for this web application are being used under a free commercial license from Pixaby. Links to each image on the homepage are below.

* [Analytics](https://pixabay.com/illustrations/analytics-information-innovation-3088958/) (landing picture on homepage)
* [Empty cart](https://pixabay.com/illustrations/icon-shopping-cart-1001596/)
* [Empty search result](https://pixabay.com/vectors/seo-search-engine-optimization-1970475/)
* [Lighting bolt](https://pixabay.com/vectors/lightning-bolt-strike-lighting-303595/)
* [Read-only](https://pixabay.com/vectors/read-only-readonly-locked-lock-98443/)
* [Technology](https://pixabay.com/illustrations/technology-equipment-responsive-web-2468063/) (Device images icon)
* [Fun](https://pixabay.com/vectors/thumbs-up-good-thumb-hand-gesture-31663/)

All images for lot items are under free commercial license from Pixaby. 

### Favicon 

I used a Favicon and App Icon Generator online to create the Favicon for this web application. The web site I used was [Favicon.ico & App Icon Generator](https://www.favicon-generator.org/).

### Code

#### User Profiles
In order to expand Django’s built-in user authenication system I followed the tourial at [https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html) in order to add user profiles that where attached to the user account and created on user registraion. 

### Disclaimer

This is for educational use.