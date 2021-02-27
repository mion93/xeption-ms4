# XEPTION 


![Mockup](https://i.ibb.co/pnbKrsT/xeption-mockups.png)


[Live Website](https://xeption-ms4.herokuapp.com/)


# User Experience & User Interface

## PURPOSE

The concept of my Full-Stack Development Milestone is to create an E-commerce shop selling jewellery.  

The purpose of this project is to create an e-commerce platform for a small business that is selling jewellery by categories ( necklaces, rings, earrings, etc..). 

This Project is demostrating not only the understanding of Django & Python and combines it with HTML, CSS & Javascript, but also is demonstrating the understanding of an authentication mechanism, a payment method provider (Stripe) and the use of a relational database.

The app was built using GitHub and deployed to Heroku, with all of static files stored with AWS.

## DESIGN 

### RESEARCH

![Research](https://i.ibb.co/hWK1VSV/Progetto-senza-titolo.png)

### COLOUR SCHEMA

* For this concept of XEPTION E-commerce, I decided to use Nude Colors that are really pleasing and minimalist for the eye. 

* "According to color psychology, the nude color infers sentiments of warmth, solace, and security. It’s frequently portrayed as usual, practical, and ordinary, yet this tone of brown likewise be modern and sophisticated." - Gotodesigno.com

* The combinations of colors that I used it's:  

**#F7D4C8**

**#000000**

**#FFFFFF**

### LOGO

I decided to create a simple minimalistic Logo by using Homemade Apple font from Google Fonts, that allows to have an improved visual polish and professional appearance. 

![Logo](https://i.ibb.co/kJ9rVCm/xeptionlogo.png)

### TYPHOGRAPHY

- Poppins, serif
- Homemade Apple, cursive (Used also for the Main Logo)
- Prata, serif
- FontAwesome - Icons

## USER STORIES & TESTING

Users stories were tested as shown below:

![User Stories](https://i.ibb.co/YWj09bb/user-stories.png)


## Database

To store the models needed for the project I used a Relational Database. I used SQLite in development that is comes by default by Django and Heroku Postgres in production. 

Choosing a Relation Database it was a good choice because it doesn't require any complex structuring and querying process, it's flexible, it makes the data to be non-repetitive and it gives easy access to data.

# Features


### HOME

- Hero Image with a button that links to all products.
- Category Listings of categories of products of the e-commerce.
- About Us section that displays brand informations.
- Container that displays advantages of choosing XEPTION.
- Instagram section - with a link to Instagram Page.
- Footer Section displaying payment informations, main links to the page, newsletter.

### PRODUCTS

- Sort & Filter functionality to allow users to find the products they are looking for.
- Card Listing to display the products (Image, Name, Price).
- Scroll to top button.
- Edit and delete product for Admin User.
- Keep Shopping button to return to products page.

### PRODUCT DETAIL

- Display Name, image, price and description of the product.
- Edit and delete products for Admin user.
- Quantity selector for incrementing and reducing the quantity of the product.
- Add to bag button, that adds the product to a the bag and to the bag preview.

### SHOPPING BAG

- Display products with the functionality of updating the quantity and delete links.
- Before Delivery cost, Delivery cost and Grand Total cost.
- Amount left to spend for free delivery.
- Keep shopping button.
- Secure checkout button.

### CHECKOUT & CHECKOUT SUCCESS

- Crispy forms used for formatting.
- Forms used to display delivery informations and payments.
- If User is logged in, there is an option to save the info.
- Checkout form, if informations are saved in the account, is prefilled.
- Form Validation.
- Loading Overlay while processing the payment.
- Stripe Payment functionality used for card transaction management.
- Checkout Succed displays that the order has been processed and display the order details.

### PRODUCT MANAGEMENT ( ADD, EDIT & DELETE FUNCTIONALITY)

- Forms for adding a new product.
- Products can be edited via a prefilled form, that shows the preview of the existing or selected image.

### FUTURE IMPLEMENTATIONS

- Newsletter Page
- Contact Form


# Wireframes 

I choose Balsamiq for the planning of the desktop and mobile version of Xeption e-commerce. 
Wireframes can be found [here](readme/wireframes/)

# Technologies

## LANGUAGES
- [**HTML5**](https://en.wikipedia.org/wiki/HTML5)
- [**CSS3**](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [**JavaScript**](https://www.javascript.com/)
- [**Python**](https://www.python.org/)

## LIBRARIES, FRAMEWORKS & PROGRAMS

- [**Django**](https://www.djangoproject.com/)
  - Python Web Framework used to build the app.

- [**Bootstrap 4.5.3**](https://getbootstrap.com/)
  - Used for styling the website and used for creating a responsive design template.

- [**GitHub**](https://github.com/)
  - GitHub is used to store the project code during development.

- [**Git**](https://git-scm.com/)
  - Used for version control.

- [**Boto3**](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  - Allows Python to talk to AWS SDK so you can store data in S3 buckets .

- [**Heroku Postgres**](https://www.heroku.com/postgres)
  - Database from Heroku used to store the data

- [**Django-crispy-forms**](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
  - Allows style and HTML control of Django template form displays.

- [**Heroku**](https://www.heroku.com/)
  - Heroku is the app platform the project was deployed to.

- [**gunicorn**](https://gunicorn.org/)
  - WSGI SERVER used to connect web server and web application.

- [**pillow**](https://pypi.org/project/Pillow/2.2.1/)
  - Python Library used for saving images, opening and manipulating.

- [**psycopg2**](https://pypi.org/project/psycopg2/) 
  - PostgreSQL database adapter.

- [**AWS**](https://aws.amazon.com/)
  -  - A cloud-based storage service used to store static and, media files.

- [**Stripe**](https://stripe.com/gb)
  - Stripe was used to deal with payments.

- [**Google fonts**](https://fonts.google.com/)
  - Google fonts were used to import the fonts into the CSS file which is used on all pages throughout the project.

- [**Font Awesome 4.7.0**](https://fontawesome.com/)
  - Font Awesome was used for all icons on site. 

- [**Balsamiq**](https://balsamiq.cloud/)
  - Balsamiq was used to create the wireframes.

# **Deployment**

#### Deploy to Heroku

The project was deployed to Heroku with all static and media files stored on a Amazon S3 bucket. Automatic deployment  was enabled in Heroku to ensure deloyed app is automatically up to date with the GitPod repository.

This project also requires a `Gmail Account` with an app secret password, to allow emails to be sent to users. Sign up for a Gmail account [here](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp)

The site also utilises Stripe, the documentation for which can be found [here](https://stripe.com/docs)

<details>
<summary>Deploying to Heroku</summary>
<p>

> **Note:** Before following the below steps ensure you have already created your new repo in Github.

1. Log in (or Register) to [Heroku](https://www.heroku.com/) and from your dashboard click 'new' > 'create new app'.

2. Enter your 'App name' and choose the appropriate region, then click 'Create app'.

3. Then on the 'Resources' tab, search and add on the Heroku Postgres database.

4. To use Postgres, install dj_database_url, and psycopg2 in the project terminal using the following commands;

    `$ pip3 install dj_database_url`

    `$ pip3 install psycopg2-binary`

5. Freeze the requirements to ensure Heroku installs all the apps requirements when deployed using the following command;

    `$ pip3 freeze > requirements.txt`

6. To migrate to the Postgres, go to settings.py and add the following import;

    `import dj_database_url`

   Then down in the databases setting comment out the default configuration and replace the default database with a call to dj_database_url.parse and give it the database URL from Heroku which can be found under the Heroku app setting config vars.

7. Apply all migrations using the following command;

    `$ python3 manage.py migrate`

    After migrations have been applied you will need to reupload the fixtures to the heroku database using. 

    `$ python3 manage.py loaddata categories`
    `$ python3 manage.py loaddata products`
    
    Your database should now be set up on heroku, when looking at the deloyed site you will notice a noticeable slow download speed which will improve later in the process. 

8. Create a superuser to log in with using the following command;

    `$ python3 manage.py createsuperuser`

9. Go to the Settings tab on Heroku, scroll to the 'Config Vars' section, and click 'Reveal Config Vars'. 

   Enter the variables (key and value) contained in your gitpod environment setting. The keys are listed below and values are inputted by the user.

| Key               | Value               |
|-------------------|---------------------|
| AWS_ACCESS_KEY_ID | To be added by user |
| AWS_SECRET_KEY_ID | To be added by user |
| DATABASE_URL      | To be added by user |
| EMAIL_HOST_PASS   | To be added by user |
| EMAIL_HOST_USER   | To be added by user |
| SECRET_KEY        | To be added by user |
| STRIPE_PUBLIC_KEY | To be added by user |
| STRIPE_SECRET_KEY | To be added by user |
| STRIPE_WH_SECRET  | To be added by user |

10. Install gunicorn using the following command;

    `$ pip3 install gunicorn`
    and then:

    `$ pip3 freeze > requirements.txt`


11. Create a Procfile and add:

    `web: gunicorn xeption.wsgi:application`

    This tells Heroku to create a web dyno which will run gunicorn and serve the Django app.

   
12. Then you need to temporarily disable collectstatic to ensure that Heroku won't collect static files on deployment. This is done by adding the below variable;

    | DISABLE_COLLECTSTATIC  | 1 |

13. Add the hostname of Heroku app to allowed hosts in settings.py

14. Now you can commit all the changes and push to GitHub;

    `$ git add .`
    `$ git commit -m <'your commit message'>`
    `$ git push`

    If you created your app on the website you will need to initialize your Heroku git remote using the following command;

    `$ heroku git:remote -a xeption`

    Then use the following command to push to Heroku;

    `$ git push heroku master`

</p>
</details>

<details>
<summary>Deploying AWS Static and Media files</summary>
<p>

The project uses Amazon Web Services s3,a cloud-based storage service, to store static and media files.

1. Create an account by navigating to [aws.amazon.com](https://aws.amazon.com/) and clicking create an AWS account. Fill in your email and password, and a username for your account, and select continue.

2. Now on the account type page, select personal and fill out the required information, click create an account and continue.

3. Next you will be asked to enter a credit card number which will be used for billing if we go above the free usage limits. Beyond this, you'll be asked a couple more verification questions then once all required information is confirmed your account will be created.

   > **Note**: For this project, I didn't go anywhere near the usage limits but keep in mind that AWS is not free if you go above the free usage limits.

4. Now you can navigate back to [aws.amazon.com](https://aws.amazon.com/) and sign-in to your account.

5. Navigate to AWS management console under my account and using the 'find services' search bar, find s3.

6. Now open s3 and create a new bucket to store all your files.

- Enter a name for your bucket

- Select a region (select your geographically closest region)

- Uncheck block all public access and acknowledge that the bucket will be public.

- Click create bucket and your bucket should be created.

7. Now click into your new bucket and set some settings;

- On the properties tab and turn on static website hosting.

- On the permissions tab 

  - Paste in a **CORS Configuration** to set up the required access between your Heroku app and this s3 bucket. Copy the code below supplied by CodeInstitute;

        [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
        ]

  - In the **Bucket Policy** tab, select policy generator
    - Policy type is 's3 bucket policy'
    - Allow all principles using a *
    - Actions is 'GetObject'
    - Add in your ARN (found on previous page)
    - Click 'Add statement' then 'Generate policy'
    - Copy the policy code and paste it into the bucket policy editor

       > **Note:** To allow access to all resources in this bucket add a slash star onto the end of the resource key.
    
    - Click save

  - In the **Access Control List** tab, under the Public Access section, set the list objects permission to everyone.

8. Create a user to access the bucket created.

- Search for a new service 'IAM'
- Now open IAM, navigate to 'groups' and click 'Create new group'
- Create a policy by navigating to 'policies' and click 'Create policy'
- Go JSON tab and click 'import managed policy'
  - Search for s3 and then import the s3 full access policy.
    - Replace resource value '*' with your bucket ARN from the bucket policy page;

    "Resource": [
        "arn:aws:s3:::xeption-ms4",
        "arn:aws:s3:::xeption-ms4/*"
    ]

  - Click 'Review policy', give it a name and a description and click 'Create policy'

9. Attach the policy to the group you created.
- Navigate to 'groups', select the group you created and on permissions tab select 'Attach policy'.
- Search for the policy you created, select it and click 'Attach policy'.

- Now to create the user, navigate to 'users' and click 'Add user'
  - Add username, select programmatic access and click 'Next'
  - Add user to a group by selecting the group you created and click 'Next' then click through to the end and click 'Create user'
  - Now download the CSV file which will contain this users access key and secret access key

10. To connect to Django, head to your project and install two new packages then freeze them into your requirements.txt;
  - $ pip3 install boto3
  - $ pip3 install django-storages
  - $ pip3 freeze > requirements.txt

11. In settings, add 'storages' to installed apps.

12. To connect Jdango to s3 add the below settings in settings.py which will tell it which bucket it should be communicating with;

        if 'USE_AWS' in os.environ:
            AWS_STORAGE_BUCKET_NAME = 'xeption-ms4'
            AWS_S3_REGION_NAME = 'eu-west-2'
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'


13. Create a file called custom_storages.py and add the content below;

        from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage


        class StaticStorage(S3Boto3Storage):
            location = settings.STATICFILES_LOCATION


        class MediaStorage(S3Boto3Storage):
            location = settings.MEDIAFILES_LOCATION

    Then in settings.py add the below:

        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
</p>
</details>

<details>
<summary>Setting up Automatic Deployment to Heroku</summary>
<p>

1. From the Heroku deploy tab, select the Deployment method 'GitHub'.

2. On the 'Connect to GitHub' section make sure your GitHub profile is displayed then add your repository name and click 'Search'.

3. Your repo should now be displayed below, click 'Connect' to connect to this app.

4. Go to the Deploy tab on Heroku and under the Automatic deployment section, click 'Enable Automatic Deploys'. Then under Manual deploy click 'Deploy Branch'.

   - Heroku will now receive the code from GitHub and start building the app using the required packages.
   - Once built you will receive the message 'Your app was successfully deployed' and you can click 'View' to launch your new app.

</details>


<details>
<summary>Accessing the Project Code</summary>
<p>
    Forking allows you to create a copy of the original repository and propose changes to the repository owner via a pull request.
</p>
</details>

<details>
<summary>Forking the GitHub Repository</summary>
<p>

1. Log in to GitHub and locate the GitHub Repository. Xeption repository can be found [here](https://github.com/mion93/xeption-ms4)

2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.

3. You should now have a copy of the original repository in your GitHub account.

</p>
</details>


<details>
<summary>To run the code locally</summary>

From GitHub, click on the "Clone" button.

Choose "Download Zip" (The download starts).

After the download is complete, open the zip folder by double clicking to access created page.

Set up a virtual environment if you have not already done so.

Activate your virtual environment, please see the Python Documentation on virtual environments for further instructions.

Install any required module and freeze them into requirements.txt.

Create a new file env.py at the base directory.

Copy all your secret keys from settings.py and paste into env.py file.

Then complete the process by running migration, createsuperuser, preload products and tags, then runserver.

Finally, ensure to run the following command whenever changes are made to static files.

                    ```
                    python3 manage.py collectstatic
                    ```
</details>


# Testing

- Testing file can be found [here](readme/testing/testing.md)

## RESPONSIVENESS

- Responsive on all device sizes, using Bootstrap grid system and media queries.
- The website has been tested across multiple screen sizes using Google Chrome developer tools for a range of screen sizes, portrait and landscape, including:

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro

## BROWSER COMPATIBILITY
The live website, hosted on gitpages, has been opened and tested on multiple browsers for responsives and intended appearance. Browers tested included:

- Google Chrome
- Safari
- Microsoft Edge
- Internet Explorer
- Firefox
- Opera
- Overall the website worked well and appeared as intended on different sizes across different browsers.

## CREDITS & MEDIA

- Products Images were taken from ***NihaoJewellery***.
- Homepage Images were taken from ***Unspleash*** and ***PixaBay***.
- StackOverflow 

## ACNOWLEDGEMENTS

My Mentor Gerard Mcbride for his continuous support throughout the project.

The tutors from Code Institute (Stephe, Igor, Johann and Alan).

Slack Community of Code Institute.
