## PRODUCTS

- A search-bar allows users to easily find the product they are looking for.
- By clicking on JEWELLERY on the main-nav-bar, categories will be displayed, so the user can easily access them. Every category, if clicked, will display its own products listed with an image, name and price.
- By clicking on  SORT PRODUCTS, the user can choose to sort the products by rate, price, category or to display all of the products.
- Every product displayed on the products page or on the categories page, can be accessed easily and the user can see that the product displays name, rating, category, price and description.
- User can easily add the product or to see the other products by clicking on the 'KEEP SHOPPING' button.
- User can add a product by clicking add a product and choose the quantity, this product will be added and displayed in the preview of the bag.
- By clicking in the preview of the bag "SECURE CHECKOUT" or by clicking on the bag icon, the user will be redirected to the bag.
- The bag will display the item with its own name, SKU number, and price.  Delivery price will be automatically calculated and a Grand Total price will be displayed.
- User can add or reduce the quantity of the product and then update the shopping bag or can delete the products in the bag. Also, by clicking to SHOW PRODUCTS button, the user can check products before making the order.
- If the user decides to go to the CHECKOUT will be redirected to the final checkout page. This page has two sections:

— One section displaying the order items,quantity, price, delivery price and grand total.

— One section displaying a form where the user needs to add its own personal informations, delivery informations and payment details.

- After filling up the form with user information and add card payment details user can process the payments by clicking the COMPLETE ORDER button and will be redirected to a success page with the order details and a preview toast will display SUCCESS for the order.

## CREATE A PROFILE

- User can create a profile by clicking on the user icon and will be redirected to a SIGN UP page.
- By filling up the form with Email, Username and Password, user will be registered to the website.
-







## VALIDATOR CHECKS

- [***CSS VALIDATOR***]
    - SUCCESS
    
- [*** JsHINT ***]
     - 	WARNING: 'template literal syntax' is only available in ES6 (use 'esversion: 6').
     -  WARNING: 'template literal syntax' is only available in ES6 (use 'esversion: 6').

- [*** PEP8 ***]
     - SUCCESS 

- [*** FLAKE8 ***]
     -  By using the following command I was able to check the problems across all the files.

     $ python3 - m flake8

      - " DJ01 Avoid using null=True on string-based fields such URLField." 
      - "imported but unused " ( I decide to leave this imports as are not affecting my code)
      - E501 line too long (83 > 79 characters) on setting.py ( I decided to not break the variables)

## BUGS & FUTURE FIXING 

- Impossible to load an image URL to Product Management as the image can be loaded locally.
- Favicon image couldn't load from AWS. 
