# XEPTION 


![Mockup](https://i.ibb.co/pnbKrsT/xeption-mockups.png)


[Live Website](https://xeption-ms4.herokuapp.com/)


# User Experience & User Interface

## Purpose

The concept of my Full-Stack Development Milestone is to create an E-commerce shop selling jewellery.  

The purpose of this project is to create an e-commerce platform for a small business that is selling jewellery by categories ( necklaces, rings, earrings, etc..). 

This Project is demostrating not only the understanding of Django & Python and combines it with HTML, CSS & Javascript, but also is demonstrating the understanding of an authentication mechanism, a payment method provider (Stripe) and the use of a relational database.

The app was built using GitHub and deployed to Heroku, with all of static files stored with AWS.

## DESIGN 

### Research

![Research](https://i.ibb.co/hWK1VSV/Progetto-senza-titolo.png)

### Colour Scheme

* For this concept of XEPTION E-commerce, I decided to use Nude Colors that are really pleasing and minimalist for the eye. 

* "According to color psychology, the nude color infers sentiments of warmth, solace, and security. It’s frequently portrayed as usual, practical, and ordinary, yet this tone of brown likewise be modern and sophisticated." - Gotodesigno.com

* The combinations of colors that I used it's:  

**#F7D4C8**

**#000000**

**#FFFFFF**

### Logo

I decided to create a simple minimalistic Logo by using Homemade Apple font from Google Fonts, that allows to have an improved visual polish and professional appearance. 

### Typography

- Poppins, serif
- Homemade Apple, cursive (Used also for the Main Logo)
- Prata, serif
- FontAwesome - Icons

## Database

To store the models needed for the project I used a Relational Database. I used SQLite in development that is comes by default by Django and Heroku Postgres in production. 

Choosing a Relation Database it was a good choice because it doesn't require any complex structuring and querying process, it's flexible, it makes the data to be non-repetitive and it gives easy access to data.

# Features

### RESPONSIVENESS

- Responsive on all device sizes, using Bootstrap grid system and media queries.

### Home

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

# Technologies

- HTML5
- CSS3
- JAVASCRIPT
- PYTHON
- DJANGO
- BOOTSTRAP 4.5.3
- GITHUB - Used for storing the project
- GIT - Used for Version Control
- BOTO3
- HEROKU
- GUNICORN -WSGI SERVER used to connect web server and web application
- PILLOW - Python Library used for saving images, opening and manipulating
- PSYCOPG2 - PostgreSQL database adapter
- AWS
- STRIPE - Used to setup the payments
- TEMP MAIL
- GOOGLE FONTS
- FONT AWESOME
- BALSAMIQ

# CREDITS

# CREDITS

# MEDIA

- Products Images were taken from NihaoJewellery
- Homepage Images were taken from Unspleash and PixaBay