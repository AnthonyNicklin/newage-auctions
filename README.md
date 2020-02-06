[![Build Status](https://travis-ci.org/AnthonyNicklin/newage-auctions.svg?branch=master)](https://travis-ci.org/AnthonyNicklin/newage-auctions)

# Newage Auctions

## Full Stack Web Development 

![NAA Logo](https://github.com/AnthonyNicklin/newage-auctions/blob/develop/static/images/naa_logo.png)

## Table of Contents

1. Aim
2. UX
3. Features
4. Database Schema
5. Database Design
6. Technologies Used
7. Testing
8. Deployment
9. Credits

## Aim

Auctions are exciting, fast-paced and fun but, getting to one can be a problem for some looking for the one-off or rare item to add to your collection. Welcome to [Newage Auctions!](newage-auctions.herokuapp.com)

Bringing auctions into the connected digital age has solved the problem of busy private and commercial collectors not able to attend every auction they wish to be at. 

The site is run and administered by the owner of the website who is the seller. All administrative tasks are carried out in the admin dashboard by the administrator only.

## UX

Starting with a mobile first design approach to this project I started creating mockups and wireframes for mobile and small screens. I then moved onto creating mockups and wireframes for medium and larger screens. The design of the site is clean and simple. Mockups and wireframes can be viewed via this link - Mockups/wireframes.
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

The navigation bar is responsive having break points for smaller, medium and large screens. The navigation links disappear on screen width below 992 pixels and a burger menu icon appears top left. When the burger icon is clicked, it brings a side navigation bar across from the left. The navigation bar is fixed to the top and follows the use down the page for ease of navigation.

If a user is not authenticated on the site then Login and Register will populate the nav bar. If the site visitor is authenticated Account will be replace Login and Register.

When a user first visits the site they are presented with a landing picture and description of the website. The picture chosen helps to explain the digital concept of auctions and then a short description of the web application. Featured Lots gives the visitor a quick taste of the lots on offer. Presented with just an image and name in order to not clutter this important section. Last section has some easy on the eye images and some more content to help turn the visitor into a bidder.

Auctions, Lots, and category summary pages show valid current Lots and Auctions. The UX concept here was less is more, executed by keeping the content inside the summary cards to a minimum. A search bar across the top of these pages ties in by giving the box a lighter, softer blue then the primary site colour.
Auction and Lots detail pages split the image and content apart giving each some breathing space. This breathing space makes digesting the information on the page easier and more appealing. A link at the top provides a way back to either summary page.

All forms for logging in, creating, updating, password reset etc and checkout have the same form design. Again, using the softer blue background to tie it in with the site and also help the input fields stand out. Messages are displayed at the top of the page to grab the users attention with corresponding colors to the event like red for errors, and green for success.

The shopping cart displays the items in the cart in a clean and decoupled way. This makes it easy for the user to see what they are going to purchase. Making the cart in a more table like format breaks from the mold of the summary pages, but still in keeping with the site. 

## Features

The list below shows all the added features that needed to be in place for the project to be fully functional. The features planned to be added in the future are listed in the “Future Features” section of this document.

### Features on this website are:

* Login - allows user to login 
* Sign Up - sign up new users
* Profile - edit, update, change the password or delete profile
* Asynchronous Tasks - running tasks periodically
* Featured Lots - allows users to navigate straight to lots that have been flagged but the site owner
* Auctions - shows summarized view of all auctions not expired
* Lots - shows summarized view of all valid lots 
* Categories - shows summarized view of all valid lots by category
* Site admin - Create, edit, delete auctions, lots and orders
* Payment - secure payment method

### Future features

* Multiple lots in an auction
* Order history
* Notification system to alert when a user has been out bidded

## Database Schema

I chose to use PostgreSQL a relational database for this application. My reason for this is links need to be created and maintained between objects.

![SQL Diagram](https://github.com/AnthonyNicklin/newage-auctions/blob/develop/static/images/sql_diagram.png)

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
* Celery
    * Run asynchronous tasks periodically.
* Django 3.0
    * Python web application framework.
* Markdown
    * Used to write README.md file.
* PostgreSQL
    * Relational database used for the application database.
* Bootstrap4.3.1 framework
    * The web application uses the Bootstrap framework for it's grid system, page layout, button styling and responsive navigation bar.
* Travis CI 
    * Continuous Integration and to help test functionality.
* Visual Studio Code
    * Visual Studio Code was used as the IDE to write the web application.
* Heroku 
    * Hosting platform the production site is hosted on.
* AWS S3 
    * For hosting static files for the web application.
* Python Virtual Environment
* Marvel App
    * This was used to design and create the wireframe for this project.
* Google Fonts
* Git
    * Version control.
* Github	
* Remote repository
* Google Chrome Developer Tools.
* Firefox Inspector
* Google Docs
    * Write the contents of the README.md file.
* DBDiagram 
    * A relational database diagram design tool used to create the database schema.

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
* Windows 10
    * Google Chrome
    * Firefox
    * Microsoft Edge
    * IE 11
* Kindle Fire
    * Amazon Silk

### Code Validation


CSS - validated using the W3C CSS Validation Service - Jigsaw.
HTML - validated using the W3C Markup Validation Service.
JavaScript - validated using JSHint.

###  Manual Testing
Manual testing was conducted to ensure the user story objectives were achieved.

1. I want to add, update and delete item listings.
    a. Login to admin dashboard
    b. Click on Lot items under Auctions
    c. Click add lot. Fill out the form then click Save
    d. Click on the created lot. Amend fields then click Save
    e. Click on the radio button next to the lot. Select from the dropdown list 'Delete selected lot items'. Click Go.
2. I want a display to show all listings in a summarized view.
    a. On Auctions, All Lots and Category pages
        i. Navigate to each summary page using their respected nav bar links
        ii. Check to see that items or auctions are displayed correctly in a summarized view
3. I want pagination.
    a. On Auctions, All Lots, Categories, Bidding history
        i. Navigate to each summary page using their respected nav bar links
        ii. Ensure only 10 items are displayed on the page
        iii. Click next to view the next 10 items
        iv. Click previous to go back to the first 10 items
4. I want a search engine for listings and auctions. 
    a. On Auctions, All Lots and Category pages
        i. Navigate to each summary page using their respected nav bar links
        ii. Check to see the search bar appears at the top of the page
        iii. Enter in a keyword and click search
        iv. Check the search results comes back with correct items
5. I want to display a detailed item page for each item.
    a. Click on Lots or a category from the dropdown
    b. Click on a lot summary tile
    c. Lot detail page should render
6. I want customers to create, update, and delete their own accounts.
    a. Click on Register
        i. Fill out the registration form and submit
    b. Login and then click Account > name to view profile
        i. Amend fields and click Update
        ii. Repeat then click cancel
    c. Login and then click Account > name to view profile
        i. Click delete then delete again on the modal
        ii. Try to log in to see if account has been deleted
7. I want only logged in users to place bids.
    a. Ensure the user is not logged in
    b. Click on Auctions then click on an auction
    c. Check and make sure the bid form is hidden
    d. Login and navigate to an auction
    e. Check a bid form is now viewable
8. I want a secure payment process.
    a. Stripe integrations tested

### Automated Testing

Automated tests were written and are located in the tests directory of each app.

## Deployment

## Credits

### Disclaimer

This is for educational use.