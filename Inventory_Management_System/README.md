PROJECT DOCUMENTATION

PROJECT NAME: Inventory Management System
LANGUAGE USED: Python
PROJECT TYPE: Command Line Interface
AUTHOR NAME: Arghyadeep Acharya

PROJECT STATS:
Number of lines: 4193
Number of utility functions: 32
Number of driver functions : 1 (the main() function)
Database Used: sqlite3
Database Type: SQL (and permanent database)


HOW TO INITIATE/RUN PROJECT:
Install Python 3 on your machine
Open Terminal in your machine
  1. Clone the project and store it in your computer
  2. Using the command line on Windows, Mac or Linux, firstly navigate to the directory where the clone of
     this project is stored by using the cd command.
  3. Once your are in the project library :

        > If you are using for the first time you need to generate the database for storing all your data.
          To do that run the following command on your terminal:
          $ python main_prog.py generate

        > If your database has been created, you can now start using the system. Run the following command
          to initiate the system:
          $ python main_prog.py use


ABOUT THE PROJECT:
In many parts of the world, shops and businesses still use manual methods to store their inventory data. However
storing inventory data is one of the things that is most suited for computers. Using a computer program to store
this data has a lot of benefits:

 1. Faster Data Entry
 2. No Data Redundancy or Duplicacy
 3. Faster Data Retrieval
 4. Efficient Data Sharing
 5. Specifying access rights to employees (i.e not everyone can access the inventory data, only those with
    a valid account in the inventory management system can)
 6. Modularity and Addition of new features as and when required.


I am completely new to the Python Programming language and have been learning about it for the past 2 weeks or so.
Creating this project was a nice way for me to solidify my learning experience into real world software.
The entire source code has been written in a single file called main_prog.py
Multiple files haven't been created because the program primarily consists of utility functions that facilitate
the CRUD operations of the database, hence multiple files just makes it uneccessarily harder to navigate.
To maintain a high level of modularity I have tried to break down the program to as many utility functions as I
could. The proram consists of 32 utility functions that are run by 1 driver function (the main() function)

The program uses command line arguments to set the mode. There are two modes:

 1. Generate Mode: This mode allows the administrator to create the database and all its associated tables
                   for the first time. Once the generate command has been used, it should not be reused until
                   and unless the old database has been deleted.

 2. Use Mode: This mode allows the warehouse employees to access the inventory management system and access and
              and update data.


In the real world, a basic Warehouse has 3 components

    1. Receiving shipment of a product/item from a Supplier
    2. Supplying shipment of a product/item to a Distributor
    3. Managing the inventory
        A. Creating new products/items
        B. Viewing details of a product/item including its current qty in the warehouse
        C. Viewing past product receivals and supplies records/transactions
        D. Creating new Supplier Profiles
        E. Creating new Distributor Profiles
        F. Viewing and Editing Supplier Profiles
        G. Viewing and Editing Distributor Profiles
        H. Adding record of product damage/expiry

All the above functionality and more can be done using the system.

There are 3 primary ways that can alter the stock of an item in the warehouse
 1. Receiving shipment (This increases the stock Qty of that item)
 2. Supplying shipment (This decreases the stock Qty of that item)
 3. Damage/Expiry of an item while it is stored in warehouse
    (This decreases the stock Qty of that item)


DETAILS Regarding the Utility Functions:

hash_fun(plaintext): Enables hashing of a plaintext password to a ciphertext for added data security.
The database contains only the hashed passwords.

hash_compare(pswdd,ciphertext): Compares the plaintext entered by the user with the ciphertext stored in
the database. If they match entry into system is allowed.

login(): Allows a Warehouse Employee who has an account in the Inventory Management System to login.

create_account(): Allows a Warehouse Employee to create a new account in the system.

create_product(): Allows creation of a product/item in the system. When a product is created, its stock qty is
set to 0 by default.

view_user_details(user_ID): Allows user to view his/her profile details.

edit_user_details(user_ID): Allows user to edit his/her profile details (including password but not the
  user ID).

view_product(): To view the details of a product/item. Search can be performed on the basis of Item Code or
Item Name

edit_product(): To edit the details of a product/item (except the Item Code and the Stock Qty)

create_supplier(): To create a new supplier profile

create_distributor(): To create a new distributor profile

view_supplier(): To view details of an existing supplier (Search can be performed on the basis of Supplier ID
or Supplier Name)

view_distributor(): To view details of an existing Distributor (Search can be performed on the basis of
Distributor ID or Distributor Name)

edit_supplier(): To edit details of a supplier (except the Supplier ID)

edit_distributor(): To edit details of a distributor (except the distributor ID)

receive_shipment(): To receive a shipment from a supplier

supply_shipment(): To supply a shipment to a distributor

damaged_or_expired(): To add a record of a product damage/expiry

Note: Only 3 functions can alter the stock qty of a product/item. They are receive_shipment(), supply_shipment(),
and damaged_or_expired()

view_past_transactions(): This is the a menu function that allows user the access of all of the below
functions. This function basically opens the MENU that provides user with various methods of viewing past records

view_all_past_receivals(): To view all past product receivals

view_all_past_supply(): To view all past product supplies

past_receivals_interval(): To view past product receivals in a given time interval

past_supply_interval(): To view past product supplies in a given time interval

all_past_product_transactions(): To view all past transactions/records of a product. This
includes all past receivals, supplies and damage/expiry of that product

all_past_product_transactions_interval(): To view past transactions/records of a product in a
given time interval. This includes all past receivals, supplies and damage/expiry of that product

view_all_transactions_supplier(): To view all past receivals from a particular supplier

view_all_transactions_distributor(): To view all past supplies to a particular distributor

view_transactions_supplier_interval(): To view past receivals from a particular supplier in a given time
interval

view_transactions_distributor_interval(): To view past supplies to a particular distributor in a given time
interval

view_all_damages(): To view all the past product damages and expiry for all products

view_damage_product(): To view past product damages for a particular product

view_damage_product_interval(): To view past product damages for a particular product in a given time
interval


Disclaimer:
This Project and all of its components is for educational purposes only.
All the names, IDs and content that have been shown in this project/video explanations for
this project are all fictitious. They are just for the sake of demonstration of the project.
