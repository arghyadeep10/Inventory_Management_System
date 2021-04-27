# Inventory_Management_System
This Inventory Management System, written in Python (and using SQLite3 database) allows a warehouse to manage and maintain its inventory, monitor its products, their stock quantity, its list of suppliers and distributor, and also past records of supplies, receivals and damages.

<h1>PROJECT DOCUMENTATION</h1>

PROJECT NAME: Inventory Management System <br>
LANGUAGE USED: Python <br>
PROJECT TYPE: Command Line Interface <br>
AUTHOR NAME: Arghyadeep Acharya <br>

### PROJECT STATS: <br>
Number of lines: 4193 <br>
Number of utility functions: 32 <br>
Number of driver functions : 1 (the main() function) <br>
Database Used: sqlite3 <br>
Database Type: SQL (and permanent database) <br>


### HOW TO INITIATE/RUN PROJECT:
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

Note: The main_prog.py file runs on the basis of command line arguments. This was a first version of this project. However later I discovered that 
it can be difficult to run a program with command line arguments inside an IDE when user clicks the run button inside their IDE and doesn't use the
command line/terminal. Hence I have created a new version. This file is called main_prog_IDE_version.py

After you clone the Inventory_Management_System project to your computer, you can open the project using your preferred IDE and then go to Debug
Properties. There inside General setting go to option of startup file and enter "main_prog_IDE_version.py". Now when you click the run button,
your IDE will run this file "main_prog_IDE_version.py" instead of "main_prog.py"
This new version skips the command line arguments and provides you with the following menu:

>Welcome <br>
>Choose from the below options to continue: <br>
>1.Generate database <br>
>2.Use system <br>
>Q.Exit <br> <br>
>Enter your choice: <br>

Here again, if you are using the system for the first time, then press 1, and if you are using it from 2nd time onwards then press 2. 

Note: This program allows you to print details that get displayed on your screen (Terminal/Command Line Interface). For example when you
view the details of a product/item in the system, the program gives you the option to print these details in .txt file. These files are stored 
inside separate folders (directories) inside the Inventory_Management_System folder (directory). All these separate folders contain one 
blank text file.

These folders are :

> distributor_details/ : stores all the printouts relating to distributor details

> supplier_details/ : stores all the printouts relating to supplier details

> user_details/ : stores all the printouts relating to user details (user refers to the person currently logged in the system)

> product_details/ : stores all the printouts relating to products

> receival_details/ : stores all the printouts relating to product receivals

> supply_details/ : stores all the printouts relating to product suppplies

> product_transac_details/ : stores all the printouts relating to supplies, receivals and damage/expiry for a particular product

> damage_expiry_details/ : stores all the printouts relating to product damage and expiry records


### ABOUT THE PROJECT:
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

> hash_fun(plaintext): Enables hashing of a plaintext password to a ciphertext for added data security.
The database contains only the hashed passwords.

> hash_compare(pswdd,ciphertext): Compares the plaintext entered by the user with the ciphertext stored in
the database. If they match entry into system is allowed.

> login(): Allows a Warehouse Employee who has an account in the Inventory Management System to login.

> create_account(): Allows a Warehouse Employee to create a new account in the system.

> create_product(): Allows creation of a product/item in the system. When a product is created, its stock qty is
set to 0 by default.

> view_user_details(user_ID): Allows user to view his/her profile details.

> edit_user_details(user_ID): Allows user to edit his/her profile details (including password but not the
  user ID).

> view_product(): To view the details of a product/item. Search can be performed on the basis of Item Code or
Item Name

> edit_product(): To edit the details of a product/item (except the Item Code and the Stock Qty)

> create_supplier(): To create a new supplier profile

> create_distributor(): To create a new distributor profile

> view_supplier(): To view details of an existing supplier (Search can be performed on the basis of Supplier ID
or Supplier Name)

> view_distributor(): To view details of an existing Distributor (Search can be performed on the basis of
Distributor ID or Distributor Name)

> edit_supplier(): To edit details of a supplier (except the Supplier ID)

> edit_distributor(): To edit details of a distributor (except the distributor ID)

> receive_shipment(): To receive a shipment from a supplier

> supply_shipment(): To supply a shipment to a distributor

> damaged_or_expired(): To add a record of a product damage/expiry

Note: Only 3 functions can alter the stock qty of a product/item. They are receive_shipment(), supply_shipment(),
and damaged_or_expired()

> view_past_transactions(): This is the a menu function that allows user the access of all of the below
functions. This function basically opens the MENU that provides user with various methods of viewing past records

> view_all_past_receivals(): To view all past product receivals

> view_all_past_supply(): To view all past product supplies

> past_receivals_interval(): To view past product receivals in a given time interval

> past_supply_interval(): To view past product supplies in a given time interval

> all_past_product_transactions(): To view all past transactions/records of a product. This
includes all past receivals, supplies and damage/expiry of that product

> all_past_product_transactions_interval(): To view past transactions/records of a product in a
given time interval. This includes all past receivals, supplies and damage/expiry of that product

> view_all_transactions_supplier(): To view all past receivals from a particular supplier

> view_all_transactions_distributor(): To view all past supplies to a particular distributor

> view_transactions_supplier_interval(): To view past receivals from a particular supplier in a given time
interval

> view_transactions_distributor_interval(): To view past supplies to a particular distributor in a given time
interval

> view_all_damages(): To view all the past product damages and expiry for all products

> view_damage_product(): To view past product damages for a particular product

> view_damage_product_interval(): To view past product damages for a particular product in a given time
interval


Disclaimer:
This Project and all of its components is for educational purposes only.
All the names, IDs and content that have been shown in this project/video explanations for
this project are all fictitious. They are just for the sake of demonstration of the project.
