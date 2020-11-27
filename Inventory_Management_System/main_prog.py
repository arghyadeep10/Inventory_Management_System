
import sqlite3
import sys
import datetime


#to generate the database and all the tables for the first time the user needs to type "generate" after
#entering the file name.

if len(sys.argv) != 2 or (len(sys.argv) == 2 and (sys.argv[1] != "generate" and sys.argv[1] != "use")) :
    print("Correct Usage: $ python main_prog.py generate OR $ python main_prog.py use")
    exit(1)

#program executes this part if "generate" is used after $ python main_prog.py which indicates
#the database is being setup for the first time.
if len(sys.argv) == 2:
    if sys.argv[1] == "generate":
        #Create the database
        conn_db = sqlite3.connect('stock_management.db')
        cur = conn_db.cursor()
        #Create the table for storing Employee data
        cur.execute("create table employee (user_id text primary key, name text, age int, email text, phone text, address text, pswd text);")
        #Create the table for storing Supplier data
        cur.execute("create table supplier (supplier_id text primary key, name text, email text, phone text, address text, type text);")
        #Create the table for storing Distributor data
        cur.execute("create table distributor (distributor_id text primary key, name text, email text, phone text, address text, type text);")
        #Create the Product table for storing various products
        cur.execute("create table product (item_code text primary key, item_name text, item_weight real, item_price real, item_type text, item_stock_qty int, item_brand text);")
        #Create Shipment Receivals Table
        cur.execute("create table shipment_receival (slno int primary key, date_of_receival date, supplier_id text, supplier_name text, item_code text, item_name, stock_qty_prior int, qty_received int, stock_qty_after int, rate real, total_price real );")
        #Create Shipment Supply Table
        cur.execute("create table shipment_supply (slno int primary key, date_of_supply date, distributor_id text, distributor_name text, item_code text, item_name, stock_qty_prior int, qty_supplied int, stock_qty_after int, rate real, total_price real );")
        #Creating a Print Document Counter Table
        cur.execute("create table printer (slno int);")
        #Creating a Damaged_Expired Table
        cur.execute("create table damaged_expired (slno int primary key, date_of_record date, item_code text, item_name text, stock_qty_prior int, qty_damaged int, stock_qty_after int, damagedORexpired text, notes text, rate real, damage_worth real);")
        cur.execute("insert into printer values (?)",[0])
        conn_db.close()
        exit(0)

#Program starts here when an employee uses the database

# main() function Begins here
def main():
    x = "1"

    while x != "Q":

        print()
        print("*************** WELCOME TO STOCK MANAGEMENT SYSTEM ***************")

        print(" ------------------------------------------------------------------")
        print("|                            MENU                                  |")
        print(" ------------------------------------------------------------------")
        print("| 1. Create a new User Account                                     |")
        print(" ------------------------------------------------------------------")
        print("| 2. Login                                                         |")
        print(" ------------------------------------------------------------------ ")
        print("| Q. Exit                                                          |")
        print(" ------------------------------------------------------------------ ")

        welcome_window = input(">> Kindly enter your choice: ")

        if welcome_window == "1":
            create_account()

        elif welcome_window == "2":
            log_res, user_ID = login()

            if log_res == True: #The Login is Successful, so the user can continue

                y = "1"

                while y != "Q" :

                    print(" ------------------------------------------------------------------")
                    print("|                            MENU                                  |")
                    print(" ------------------------------------------------------------------")
                    print("| 1.  Create a new Product                                         |")
                    print(" ------------------------------------------------------------------")
                    print("| 2.  View Product Details                                         |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 3.  Edit Product Details                                         |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 4.  Edit User Profile Details                                    |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 5.  Create a new Supplier                                        |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 6.  Create a new Distributor                                     |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 7.  View Supplier Details                                        |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 8.  View Distributor Details                                     |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 9.  Edit Supplier Details                                        |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 10. Edit Distributor Details                                     |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 11. Receive shipment of a product/consignment                    |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 12. Supply shipment of a product/consignment                     |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 13. View all past Records                                        |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 14. View User Details                                            |")
                    print(" ------------------------------------------------------------------ ")
                    print("| 15. Product Damage/Expiry Record Entry                           |")
                    print(" ------------------------------------------------------------------ ")
                    print("| Q.  Exit                                                         |")
                    print(" ------------------------------------------------------------------ ")

                    master_menu = input(">> Kindly enter your choice: ")

                    if master_menu == "1":
                        create_product()
                    elif master_menu == "2":
                        view_product()
                    elif master_menu == "3":
                        edit_product()
                    elif master_menu == "4":
                        edit_user_details(user_ID)
                    elif master_menu == "5":
                        create_supplier()
                    elif master_menu == "6":
                        create_distributor()
                    elif master_menu == "7":
                        view_supplier()
                    elif master_menu == "8":
                        view_distributor()
                    elif master_menu == "9":
                        edit_supplier()
                    elif master_menu == "10":
                        edit_distributor()
                    elif master_menu == "11":
                        receive_shipment()
                    elif master_menu == "12":
                        supply_shipment()
                    elif master_menu == "13":
                        view_past_transactions()
                    elif master_menu == "14":
                        view_user_details(user_ID)
                    elif master_menu == "15":
                        damaged_or_expired()
                    elif master_menu == "Q" or master_menu == "q" or master_menu.lower() == "exit":
                        y = "Q"

                    else:
                        print(">> Incorrect Input. Please try again")


        elif welcome_window == 'Q' or welcome_window == "q" or welcome_window.lower() == "exit" :
            x = "Q"
            print(">> Goodbye !")
            exit(0)

        else:
            print(">> Incorrect Input. Please try again")

    exit(0)

# main() function Ends here

#All utility functions begin from here
#Hash Function (Converts a plaintext to ciphertext)
def hash_fun(plaintext):
    key = "YTNSHKVEFXRBAUQZCLWDMIPGJO"
    ciphertext = ""
    for j in plaintext:
        if ord(j)>=65 and ord(j)<=90:
            p = j
            j = key[ord(p)-65]
            ciphertext += j
        elif ord(j)>=97 and ord(j)<=122:
            p = j.upper()
            ch = key[ord(p)-65]
            j = ch.lower()
            ciphertext += j
        else :
            ciphertext += j

    return ciphertext


#Checks whether password entered by user is correct by comparing it against the ciphertext stored in database
def hash_compare(pswdd,ciphertext) : #pswdd is the password entered by the user and ciphertext is the ciphertexted password for that person stored in database
    if hash_fun(plaintext = pswdd) == ciphertext :
        return True
        exit(0)
    else:
        return False
        exit(1)


def login():
    userID = input("| User ID > ")
    pswdd = input("| Passoword > ")

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    #first we need to check whether this user ID exists in system or not
    count_array= cur.execute("select count(*) from employee where user_id = ?;",[userID]).fetchone()
    if count_array[0] != 1:
        print(">> The User ID entered by you is incorrect or it doesn't exist in system ")
        return False, userID
        exit(1)

    array = cur.execute("select pswd from employee where user_id = ?;",[userID]).fetchone()
    ciphertext = array[0]

    conn_db.close()

    res = hash_compare(pswdd,ciphertext)

    if res == True:
        print(">> Login SUCCESSFUL ")
        return True, userID
        exit(0)

    else:
        print(">> Login Failed. The User ID or Password entered maybe incorrect ")
        return False, userID
        exit(1)


#Create Account Function
def create_account():
    name = input("| Name > ")
    age = input("| Age > ")
    email = input("| Email > ")
    address = input("| Address > ")
    phone = input("| Phone > ")
    password = input("| Password > ")
    confirm_password = input("| Confirm Password > ")

    if password == confirm_password:
        #to generate user ID for this employee
        #Connect to the database
        conn_db = sqlite3.connect('stock_management.db')
        cur = conn_db.cursor()

        current_employee_count = cur.execute("select count(*) from employee;").fetchone() #this returns an array of type (x,) where x is the count(*) value
        new_number = str(current_employee_count[0]+1) #current_employee_count[0] gives us the first element x in the array (x,) where x is the count(*) value
        user_id = "EMPUSER{}".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        print(">> Your user account has been SUCCESSFULLY Created")
        print(f">> Your user id is : {user_id}")

        #enter this data into the employee table
        password = hash_fun(plaintext = password) #The plaintext password gets converted to ciphertext

        cur.execute("insert into employee (user_id, name, age, email, phone, address, pswd) values (?,?,?,?,?,?,?);",(user_id,name,age,email,phone,address,password))

        conn_db.commit()
        conn_db.close()
        return True;
        exit(0)

    else:
        print(">> Password and Confirm Password do not match. Try again later")
        return False;
        exit(1)

#Create Account Function
def create_product():
    item_name = input("| Name of item > ")
    item_weight = input("| Weight of item > ")
    item_price = input("| Price of item > ")
    item_type = input("| Item Type > ")
    item_stock_qty = 0
    item_brand = input("| Brand of Item > ")


    #to generate item_code for this product
    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    current_product_count = cur.execute("select count(*) from product;").fetchone() #this returns an array of type (x,) where x is the count(*) value
    new_number = str(current_product_count[0]+1) #current_product_count[0] gives us the first element x in the array (x,) where x is the count(*) value
    item_code = "ITMCD{}".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

    print(">> The product has been SUCCESSFULLY Created")
    print(f">> The item code of the product is : {item_code}")

    #enter this data into the employee table

    cur.execute("insert into product (item_code, item_name, item_weight, item_price, item_type, item_stock_qty, item_brand) values (?,?,?,?,?,?,?);",(item_code, item_name, item_weight, item_price, item_type, item_stock_qty, item_brand))

    conn_db.commit()
    conn_db.close()
    return True;
    exit(0)

def view_user_details(user_ID):

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    array = cur.execute("select * from employee where user_id = (?)",[user_ID]).fetchall()

    user_id = array[0][0]
    name = array[0][1]
    age = array[0][2]
    email = array[0][3]
    phone = array[0][4]
    address = array[0][5]
    pswd = array[0][6]

    print("  ------------------------------------------------------------------")
    print(" |                         USER DETAILS                             |")
    print("  ------------------------------------------------------------------")
    print(f"| User ID  : {user_id}")
    print(f"| Name     : {name}")
    print(f"| Age      : {age}")
    print(f"| Email ID : {email}")
    print(f"| Phone    : {phone}")
    print(f"| Address  : {address}")
    print("  ------------------------------------------------------------------")

    print()
    op = input(">> Do you wish to download these details in a text file (Y/N)")

    if op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "user_details/user_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "user_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')
        file.write("  ------------------------------------------------------------------\n")
        file.write(" |                         USER DETAILS                             |\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write(f"| User ID  : {user_id}\n")
        file.write(f"| Name     : {name}\n")
        file.write(f"| Age      : {age}\n")
        file.write(f"| Email ID : {email}\n")
        file.write(f"| Phone    : {phone}\n")
        file.write(f"| Address  : {address}\n")
        file.write("  ------------------------------------------------------------------\n")
        file.close()

        print(f">> The user details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory user_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    if op.lower() != 'y' and op.lower() != 'n':
        print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()
    return True;
    exit(0)

def edit_user_details(user_ID):

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    array = cur.execute("select * from employee where user_id = (?)",[user_ID]).fetchall()

    user_id = array[0][0]
    name = array[0][1]
    age = array[0][2]
    email = array[0][3]
    phone = array[0][4]
    address = array[0][5]
    pswd = array[0][6]

    print("  ------------------------------------------------------------------")
    print(" |                         USER DETAILS                             |")
    print("  ------------------------------------------------------------------")
    print(f"| User ID  : {user_id}")
    print(f"| Name     : {name}")
    print(f"| Age      : {age}")
    print(f"| Email ID : {email}")
    print(f"| Phone    : {phone}")
    print(f"| Address  : {address}")
    print("  ------------------------------------------------------------------")

    choice = "1"

    while choice != "Q":
        print(" ------------------------------------------------------------------")
        print("|                   USER DETAILS EDITING MENU                      |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Edit Name                                                    |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Edit Age                                                     |")
        print(" ------------------------------------------------------------------ ")
        print("| 3.  Edit Email ID                                                |")
        print(" ------------------------------------------------------------------ ")
        print("| 4.  Edit Phone                                                   |")
        print(" ------------------------------------------------------------------ ")
        print("| 5.  Edit Address                                                 |")
        print(" ------------------------------------------------------------------ ")
        print("| 6.  Edit password                                                |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------ ")

        while choice != "Q":

            choice = input(">> Kindly enter your choice: ")

            if choice == "1":
                name = input(">> Enter new name: ")
                cur.execute("update employee set name = (?) where user_id = (?)",(name,user_ID))
                print(">> Name successfully updated")
            elif choice == "2":
                age = input(">>Enter new age: ")
                cur.execute("update employee set age = (?) where user_id = (?)",(age,user_ID))
                print(">> Age successfully updated")
            elif choice == "3":
                email = input(">> Enter new email ID: ")
                cur.execute("update employee set email = (?) where user_id = (?)",(email,user_ID))
                print(">> Email ID successfully updated")
            elif choice == "4":
                phone = input(">> Enter new Phone number: ")
                cur.execute("update employee set phone = (?) where user_id = (?)",(phone,user_ID))
                print(">> Phone Number successfully updated")
            elif choice == "5":
                address = input("Enter new Address: ")
                cur.execute("update employee set address = (?) where user_id = (?)",(address,user_ID))
                print(">> Address successfully updated")
            elif choice == "6":
                pswd = input("Enter new Password: ")
                confirm_pswd = input("Confirm Password: ")

                if pswd == confirm_pswd:
                    pswd = hash_fun(pswd)
                    cur.execute("update employee set pswd = (?) where user_id = (?)",(pswd,user_ID))
                    print(">> Password successfully updated")

                else:
                    print(">> Password and Confirm Password do not match. Please try again")

            elif choice == "Q" or choice == "q" or choice.lower() == "exit":
                choice = "Q"

            else:
                print(">> Incorrect Option entered ")

    conn_db.commit()
    conn_db.close()
    return True;
    exit(0)


def view_product():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                     VIEW PRODUCT/ITEM MENU                       |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by Item Code                                          |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by Item Name                                          |")
        print(" ------------------------------------------------------------------ ")
        print("| 3.  View all Items                                               |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            item_code = input("Enter Item Code: ")

            ar = cur.execute("select count(*) from product where item_code = (?)",[item_code]).fetchone()
            count_ = ar[0]

            if count_ == 1:

                array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

                item_code = array[0][0]
                item_name = array[0][1]
                item_weight = array[0][2]
                item_price = array[0][3]
                item_type = array[0][4]
                item_stock_qty = array[0][5]
                item_brand = array[0][6]

                print("  ------------------------------------------------------------------")
                print(" |                      ITEM/PRODUCT DETAILS                        |")
                print("  ------------------------------------------------------------------")
                print(f"| Item Code       : {item_code}")
                print(f"| Item Name       : {item_name}")
                print(f"| Item Weight     : {item_weight}")
                print(f"| Item Price      : {item_price}")
                print(f"| Item Type       : {item_type}")
                print(f"| Item Stock Qty  : {item_stock_qty}")
                print(f"| Brand Name      : {item_brand}")
                print("  ------------------------------------------------------------------")

                print()
                op = input(">> Do you wish to download these details in a text file (Y/N)")

                if op.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "product_details/product_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "product_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                         PRODUCT DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| Item Code       : {item_code}\n")
                    file.write(f"| Item Name       : {item_name}\n")
                    file.write(f"| Item Weight     : {item_weight}\n")
                    file.write(f"| Item Price      : {item_price}\n")
                    file.write(f"| Item Type       : {item_type}\n")
                    file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
                    file.write(f"| Brand Name      : {item_brand}\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.close()

                    print(f">> The product details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory product_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                    if op.lower() != 'y' and op.lower() != 'n':
                        print(">> Incorrect Choice entered")

            else:
                print(">> Incorrect Product ID entered, or Product doesn't exist in system")


        elif choice == "2":
            name_of_item = input("Enter Item Name (Case insensitive): ")

            name_of_item = name_of_item.lower()

            ar_ = cur.execute("select count(*) from product where lower(item_name) = (?)", [name_of_item]).fetchone()
            count_t = ar_[0]

            if count_t == 1:

                ar = cur.execute("select item_code from product where lower(item_name) = (?)", [name_of_item]).fetchone()
                item_code = ar[0]

                array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

                item_code = array[0][0]
                item_name = array[0][1]
                item_weight = array[0][2]
                item_price = array[0][3]
                item_type = array[0][4]
                item_stock_qty = array[0][5]
                item_brand = array[0][6]

                print("  ------------------------------------------------------------------")
                print(" |                      ITEM/PRODUCT DETAILS                        |")
                print("  ------------------------------------------------------------------")
                print(f"| Item Code       : {item_code}")
                print(f"| Item Name       : {item_name}")
                print(f"| Item Weight     : {item_weight}")
                print(f"| Item Price      : {item_price}")
                print(f"| Item Type       : {item_type}")
                print(f"| Item Stock Qty  : {item_stock_qty}")
                print(f"| Brand Name      : {item_brand}")
                print("  ------------------------------------------------------------------")

                print()
                op = input(">> Do you wish to download these details in a text file (Y/N)")

                if op.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "product_details/product_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "product_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                         PRODUCT DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| Item Code       : {item_code}\n")
                    file.write(f"| Item Name       : {item_name}\n")
                    file.write(f"| Item Weight     : {item_weight}\n")
                    file.write(f"| Item Price      : {item_price}\n")
                    file.write(f"| Item Type       : {item_type}\n")
                    file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
                    file.write(f"| Brand Name      : {item_brand}\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.close()

                    print(f">> The product details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory product_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                    if op.lower() != 'y' and op.lower() != 'n':
                        print(">> Incorrect Choice entered")

            else:
                print(">> Incorrect product name entered or product doesn't exist in system")

        elif choice == "3":

            #obtaining the current_time when the user is executing this command
            current_time = datetime.datetime.now()

            count_array = cur.execute("select count(*) from product").fetchone()
            count = count_array[0]

            print(f">> There are currently {count} product(s) in the system as of {current_time}.")

            master_display = cur.execute("select * from product").fetchall()

            for i in range(0,count):
                print(f"****************** Product {i+1} ********************")
                print(f"Item Code           : {master_display[i][0]}")
                print(f"Item Name           : {master_display[i][1]}")
                print(f"Item Weight         : {master_display[i][2]}")
                print(f"Item Price          : {master_display[i][3]}")
                print(f"Item Type           : {master_display[i][4]}")
                print(f"Item Stock Quantity : {master_display[i][5]}")
                print(f"Item Brand Name     : {master_display[i][6]}")
                print(f"***************************************************")
                print()

            print()
            op = input(">> Do you wish to download these details in a text file (Y/N)")

            if op.lower() == "y":
                new_ar = cur.execute("select slno from printer").fetchone()
                new_number_int = new_ar[0]
                new_number = str(new_number_int)
                filename = "product_details/product_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                filename_without_path = "product_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                file = open(filename,'w')

                file.write(f">> There are currently {count} product(s) in the system as of {current_time}.\n\n")

                file.write("----------------- DEATAILS OF ALL PRODUCTS -------------------\n\n")

                for i in range(0,count):
                    file.write(f"****************** Product {i+1} ********************\n")
                    file.write(f"Item Code           : {master_display[i][0]}\n")
                    file.write(f"Item Name           : {master_display[i][1]}\n")
                    file.write(f"Item Weight         : {master_display[i][2]}\n")
                    file.write(f"Item Price          : {master_display[i][3]}\n")
                    file.write(f"Item Type           : {master_display[i][4]}\n")
                    file.write(f"Item Stock Quantity : {master_display[i][5]}\n")
                    file.write(f"Item Brand Name     : {master_display[i][6]}\n")
                    file.write(f"*****************************************************\n")
                    file.write("\n\n")

                file.write("-------------------------------------------------------------\n")
                file.close()

                print(f">> The product details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory product_details/ ")
                new_number_int += 1
                new_number = str(new_number_int)
                cur.execute("update printer set slno = (?)",[new_number])
                conn_db.commit()

            if op.lower() != 'y' and op.lower() != 'n':
                print(">> Incorrect Choice entered")


        elif choice == "Q" or choice == "q" or choice.lower == "exit":
            choice = "Q"

        else:
            print(">> Incorrect choice entered")


    conn_db.commit()
    conn_db.close()
    return True;
    exit(0)

def edit_product():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                     VIEW PRODUCT/ITEM MENU                       |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by Item Code                                          |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by Item Name                                          |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            item_code = input("Enter Item Code: ")

            array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

            item_code = array[0][0]
            item_name = array[0][1]
            item_weight = array[0][2]
            item_price = array[0][3]
            item_type = array[0][4]
            item_stock_qty = array[0][5]
            item_brand = array[0][6]

            print("  ------------------------------------------------------------------")
            print(" |                      ITEM/PRODUCT DETAILS                        |")
            print("  ------------------------------------------------------------------")
            print(f"| Item Code       : {item_code}")
            print(f"| Item Name       : {item_name}")
            print(f"| Item Weight     : {item_weight}")
            print(f"| Item Price      : {item_price}")
            print(f"| Item Type       : {item_type}")
            print(f"| Item Stock Qty  : {item_stock_qty}")
            print(f"| Brand Name      : {item_brand}")
            print("  ------------------------------------------------------------------")

            k = "1"

            while k != "Q":

                print(" ------------------------------------------------------------------")
                print("|                   ITEM DETAILS EDITING MENU                      |")
                print(" ------------------------------------------------------------------")
                print("| 1.  Edit Item Name                                               |")
                print(" ------------------------------------------------------------------")
                print("| 2.  Edit Item Weight                                             |")
                print(" ------------------------------------------------------------------ ")
                print("| 3.  Edit Item Price                                              |")
                print(" ------------------------------------------------------------------ ")
                print("| 4.  Edit Item Type                                               |")
                print(" ------------------------------------------------------------------ ")
                print("| 5.  Edit Item Brand                                              |")
                print(" ------------------------------------------------------------------ ")
                print("| Q.  Exit                                                         |")
                print(" ------------------------------------------------------------------ ")

                k = input(">> Kindly enter your choice: ")

                if k == "1":
                    item_name = input(">> Enter new Item Name: ")
                    cur.execute("update product set item_name = (?) where item_code = (?)",(item_name,item_code))
                    print(">> Item Name successfully updated")
                elif k == "2":
                    item_weight = input(">> Enter new Item Weight: ")
                    cur.execute("update product set item_weight = (?) where item_code = (?)",(item_weight,item_code))
                    print(">> Item Weight successfully updated")
                elif k == "3":
                    item_price = input(">> Enter new Item Price: ")
                    cur.execute("update product set item_price = (?) where item_code = (?)",(item_price,item_code))
                    print(">> Item Price successfully updated")
                elif k == "4":
                    item_type = input(">> Enter new Item Type: ")
                    cur.execute("update product set item_type = (?) where item_code = (?)",(item_type,item_code))
                    print(">> Item Type successfully updated")
                elif k == "5":
                    item_brand = input(">> Enter new Item Brand Name: ")
                    cur.execute("update product set item_brand = (?) where item_code = (?)",(item_brand,item_code))
                    print(">> Item Brand Name successfully updated")

                elif k == "Q" or k == "q" or k.lower() == "exit":
                    k = "Q"

                else:
                    print(">> Incorrect Choice entered ")


        elif choice == "2":
            name_of_item = input("Enter Item Name (Case insensitive): ")

            name_of_item = name_of_item.lower()

            ar = cur.execute("select item_code from product where lower(item_name) = (?)", [name_of_item]).fetchone()
            item_code = ar[0]

            array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

            item_code = array[0][0]
            item_name = array[0][1]
            item_weight = array[0][2]
            item_price = array[0][3]
            item_type = array[0][4]
            item_stock_qty = array[0][5]
            item_brand = array[0][6]

            print("  ------------------------------------------------------------------")
            print(" |                      ITEM/PRODUCT DETAILS                        |")
            print("  ------------------------------------------------------------------")
            print(f"| Item Code       : {item_code}")
            print(f"| Item Name       : {item_name}")
            print(f"| Item Weight     : {item_weight}")
            print(f"| Item Price      : {item_price}")
            print(f"| Item Type       : {item_type}")
            print(f"| Item Stock Qty  : {item_stock_qty}")
            print(f"| Brand Name      : {item_brand}")
            print("  ------------------------------------------------------------------")

            k = "1"

            while k != "Q":

                print(" ------------------------------------------------------------------")
                print("|                   ITEM DETAILS EDITING MENU                      |")
                print(" ------------------------------------------------------------------")
                print("| 1.  Edit Item Name                                               |")
                print(" ------------------------------------------------------------------")
                print("| 2.  Edit Item Weight                                             |")
                print(" ------------------------------------------------------------------ ")
                print("| 3.  Edit Item Price                                              |")
                print(" ------------------------------------------------------------------ ")
                print("| 4.  Edit Item Type                                               |")
                print(" ------------------------------------------------------------------ ")
                print("| 5.  Edit Item Brand                                              |")
                print(" ------------------------------------------------------------------ ")
                print("| Q.  Exit                                                         |")
                print(" ------------------------------------------------------------------ ")

                k = input(">> Kindly enter your choice: ")

                if k == "1":
                    item_name = input(">> Enter new Item Name: ")
                    cur.execute("update product set item_name = (?) where item_code = (?)",(item_name,item_code))
                    print(">> Item Name successfully updated")
                elif k == "2":
                    item_weight = input(">> Enter new Item Weight: ")
                    cur.execute("update product set item_weight = (?) where item_code = (?)",(item_weight,item_code))
                    print(">> Item Weight successfully updated")
                elif k == "3":
                    item_price = input(">> Enter new Item Price: ")
                    cur.execute("update product set item_price = (?) where item_code = (?)",(item_price,item_code))
                    print(">> Item Price successfully updated")
                elif k == "4":
                    item_type = input(">> Enter new Item Type: ")
                    cur.execute("update product set item_type = (?) where item_code = (?)",(item_type,item_code))
                    print(">> Item Type successfully updated")
                elif k == "5":
                    item_brand = input(">> Enter new Item Brand Name: ")
                    cur.execute("update product set item_brand = (?) where item_code = (?)",(item_brand,item_code))
                    print(">> Item Brand Name successfully updated")

                elif k == "Q" or k == "q" or k.lower() == "exit":
                    k = "Q"

                else:
                    print(">> Incorrect Choice entered ")


        elif choice == "Q" or choice == "q" or choice.lower == "exit":
            choice = "Q"

        else:
            print(">> Incorrect choice entered")


    conn_db.commit()
    conn_db.close()
    return True;
    exit(0)


def create_supplier():
    print(">> Welcome to Create Supplier Menu")
    print()

    name = input("| Supplier Name > ")
    email = input("| Email > ")
    phone = input("| Phone > ")
    address = input("| Address > ")
    sup_type = input("| Supplier Type > ")


    #to generate supplier_id for this supplier
    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    current_supplier_count = cur.execute("select count(*) from supplier;").fetchone() #this returns an array of type (x,) where x is the count(*) value
    new_number = str(current_supplier_count[0]+1) #current_supplier_count[0] gives us the first element x in the array (x,) where x is the count(*) value
    supplier_id = "SUPLR{}".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

    print(">> The Supplier Profile has been SUCCESSFULLY Created")
    print(f">> The Supplier Code is : {supplier_id}")

    #enter this data into the employee table

    cur.execute("insert into supplier (supplier_id, name, email, phone, address, type) values (?,?,?,?,?,?);",(supplier_id, name, email, phone, address, sup_type))

    conn_db.commit()
    conn_db.close()
    return supplier_id;
    exit(0)


def create_distributor():
    print(">> Welcome to Create Distributor Menu")
    print()

    name = input("| Distributor Name > ")
    email = input("| Email > ")
    phone = input("| Phone > ")
    address = input("| Address > ")
    dis_type = input("| Distributor Type > ")


    #to generate distributor_id for this distributor
    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    current_distributor_count = cur.execute("select count(*) from distributor;").fetchone() #this returns an array of type (x,) where x is the count(*) value
    new_number = str(current_distributor_count[0]+1) #current_distributor_count[0] gives us the first element x in the array (x,) where x is the count(*) value
    distributor_id = "DISTR{}".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

    print(">> The Distributor Profile has been SUCCESSFULLY Created")
    print(f">> The Distributor Code is : {distributor_id}")

    #enter this data into the employee table

    cur.execute("insert into distributor (distributor_id, name, email, phone, address, type) values (?,?,?,?,?,?);",(distributor_id, name, email, phone, address, dis_type))

    conn_db.commit()
    conn_db.close()
    return distributor_id;
    exit(0)


def view_supplier():
    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                        VIEW SUPPLIER MENU                        |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by supplier ID                                        |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by supplier Name                                      |")
        print(" ------------------------------------------------------------------ ")
        print("| 3.  View all suppliers                                           |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            supplier_id = input("Enter supplier ID: ")

            ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

                supplier_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                        SUPPLIER DETAILS                          |")
                print("  ------------------------------------------------------------------")
                print(f"| supplier ID     : {supplier_id}")
                print(f"| supplier Name   : {name}")
                print(f"| Email ID        : {email}")
                print(f"| Phone           : {phone}")
                print(f"| Address         : {address}")
                print(f"| supplier Type   : {type_}")
                print("  ------------------------------------------------------------------")

                print()
                op = input(">> Do you wish to download these details in a text file (Y/N)")

                if op.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "supplier_details/supplier_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "supplier_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                        SUPPLIER DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| supplier ID     : {supplier_id}\n")
                    file.write(f"| supplier Name   : {name}\n")
                    file.write(f"| Email ID        : {email}\n")
                    file.write(f"| Phone           : {phone}\n")
                    file.write(f"| Address         : {address}\n")
                    file.write(f"| supplier Type   : {type_}\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.close()

                    print(f">> The supplier details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory supplier_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                    if op.lower() != 'y' and op.lower() != 'n':
                        print(">> Incorrect Choice entered")

            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")




        elif choice == "2":
            name_of_supplier = input("Enter supplier Name (Case insensitive): ")

            name_of_supplier = name_of_supplier.lower()

            ar = cur.execute("select supplier_id from supplier where lower(name) = (?)", [name_of_supplier]).fetchone()
            supplier_id = ar[0]

            ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

                supplier_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                         SUPPLIER DETAILS                         |")
                print("  ------------------------------------------------------------------")
                print(f"| supplier ID     : {supplier_id}")
                print(f"| supplier Name   : {name}")
                print(f"| Email ID        : {email}")
                print(f"| Phone           : {phone}")
                print(f"| Address         : {address}")
                print(f"| supplier Type   : {type_}")
                print("  ------------------------------------------------------------------")

                print()
                op = input(">> Do you wish to download these details in a text file (Y/N)")

                if op.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "supplier_details/supplier_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "supplier_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                        SUPPLIER DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| supplier ID     : {supplier_id}\n")
                    file.write(f"| supplier Name   : {name}\n")
                    file.write(f"| Email ID        : {email}\n")
                    file.write(f"| Phone           : {phone}\n")
                    file.write(f"| Address         : {address}\n")
                    file.write(f"| supplier Type   : {type_}\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.close()

                    print(f">> The supplier details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory supplier_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                    if op.lower() != 'y' and op.lower() != 'n':
                        print(">> Incorrect Choice entered")


            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")


        elif choice == "3":
            count_array = cur.execute("select count(*) from supplier").fetchone()
            count = count_array[0]

            master_display = cur.execute("select * from supplier").fetchall()

            for i in range(0,count):
                print(f"***************** Supplier {i+1} *******************")
                print(f"supplier ID   : {master_display[i][0]}")
                print(f"supplier Name : {master_display[i][1]}")
                print(f"Email ID      : {master_display[i][2]}")
                print(f"Phone         : {master_display[i][3]}")
                print(f"Address       : {master_display[i][4]}")
                print(f"supplier Type : {master_display[i][5]}")
                print(f"***************************************************")
                print()
                print()

            print()
            op = input(">> Do you wish to download these details in a text file (Y/N)")

            #obtaining the current_time when the user is executing this command
            current_time = datetime.datetime.now()

            if op.lower() == "y":
                new_ar = cur.execute("select slno from printer").fetchone()
                new_number_int = new_ar[0]
                new_number = str(new_number_int)
                filename = "supplier_details/supplier_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                filename_without_path = "supplier_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                file = open(filename,'w')

                file.write(f">> There are currently {count} supplier(s) in the system as of {current_time}.\n\n")

                file.write("----------------- DEATAILS OF ALL SUPPLIERS -------------------\n\n")

                for i in range(0,count):
                    file.write(f"***************** Supplier {i+1} *******************\n")
                    file.write(f"supplier ID   : {master_display[i][0]}\n")
                    file.write(f"supplier Name : {master_display[i][1]}\n")
                    file.write(f"Email ID      : {master_display[i][2]}\n")
                    file.write(f"Phone         : {master_display[i][3]}\n")
                    file.write(f"Address       : {master_display[i][4]}\n")
                    file.write(f"supplier Type : {master_display[i][5]}\n")
                    file.write(f"***************************************************\n")

                    file.write("\n\n")

                file.write("-------------------------------------------------------------\n")
                file.close()

                print(f">> The suppliers details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory supplier_details/ ")
                new_number_int += 1
                new_number = str(new_number_int)
                cur.execute("update printer set slno = (?)",[new_number])
                conn_db.commit()

            if op.lower() != 'y' and op.lower() != 'n':
                print(">> Incorrect Choice entered")




        elif choice == "Q" or choice == "q" or choice.lower == "exit":
            choice = "Q"

        else:
            print(">> Incorrect choice entered")

    conn_db.commit()
    conn_db.close()




def view_distributor():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                     VIEW DISTRIBUTOR MENU                        |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by distributor ID                                     |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by distributor Name                                   |")
        print(" ------------------------------------------------------------------ ")
        print("| 3.  View all distributors                                        |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            distributor_id = input("Enter distributor ID: ")

            ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

                distributor_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                      DISTRIBUTOR DETAILS                         |")
                print("  ------------------------------------------------------------------")
                print(f"| distributor ID     : {distributor_id}")
                print(f"| distributor Name   : {name}")
                print(f"| Email ID           : {email}")
                print(f"| Phone              : {phone}")
                print(f"| Address            : {address}")
                print(f"| distributor Type   : {type_}")
                print("  ------------------------------------------------------------------")

                print()
                op = input(">> Do you wish to download these details in a text file (Y/N)")

                if op.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "distributor_details/distributor_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "distributor_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                       DISTRIBUTOR DETAILS                        |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| distributor ID     : {distributor_id}\n")
                    file.write(f"| distributor Name   : {name}\n")
                    file.write(f"| Email ID           : {email}\n")
                    file.write(f"| Phone              : {phone}\n")
                    file.write(f"| Address            : {address}\n")
                    file.write(f"| distributor Type   : {type_}\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.close()

                    print(f">> The distributor details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory distributor_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                    if op.lower() != 'y' and op.lower() != 'n':
                        print(">> Incorrect Choice entered")


            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")


        elif choice == "2":
            name_of_distributor = input("Enter distributor Name (Case insensitive): ")

            name_of_distributor = name_of_distributor.lower()

            ar = cur.execute("select distributor_id from distributor where lower(name) = (?)", [name_of_distributor]).fetchone()
            distributor_id = ar[0]

            ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

                distributor_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                      DISTRIBUTOR DETAILS                         |")
                print("  ------------------------------------------------------------------")
                print(f"| distributor ID     : {distributor_id}")
                print(f"| distributor Name   : {name}")
                print(f"| Email ID           : {email}")
                print(f"| Phone              : {phone}")
                print(f"| Address            : {address}")
                print(f"| distributor Type   : {type_}")
                print("  ------------------------------------------------------------------")

                print()
                op = input(">> Do you wish to download these details in a text file (Y/N)")

                if op.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "distributor_details/distributor_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "distributor_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                       DISTRIBUTOR DETAILS                        |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| distributor ID     : {distributor_id}\n")
                    file.write(f"| distributor Name   : {name}\n")
                    file.write(f"| Email ID           : {email}\n")
                    file.write(f"| Phone              : {phone}\n")
                    file.write(f"| Address            : {address}\n")
                    file.write(f"| distributor Type   : {type_}\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.close()

                    print(f">> The distributor details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory distributor_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                    if op.lower() != 'y' and op.lower() != 'n':
                        print(">> Incorrect Choice entered")



            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")


        elif choice == "3":
            count_array = cur.execute("select count(*) from distributor").fetchone()
            count = count_array[0]

            master_display = cur.execute("select * from distributor").fetchall()

            for i in range(0,count):
                print(f"*************** Distributor {i+1} *****************")
                print(f"distributor ID   : {master_display[i][0]}")
                print(f"distributor Name : {master_display[i][1]}")
                print(f"Email ID         : {master_display[i][2]}")
                print(f"Phone            : {master_display[i][3]}")
                print(f"Address          : {master_display[i][4]}")
                print(f"distributor Type : {master_display[i][5]}")
                print(f"***************************************************")
                print()

            print()
            op = input(">> Do you wish to download these details in a text file (Y/N)")

            #obtaining the current_time when the user is executing this command
            current_time = datetime.datetime.now()

            if op.lower() == "y":
                new_ar = cur.execute("select slno from printer").fetchone()
                new_number_int = new_ar[0]
                new_number = str(new_number_int)
                filename = "distributor_details/distributor_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                filename_without_path = "distributor_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                file = open(filename,'w')

                file.write(f">> There are currently {count} distributor(s) in the system as of {current_time}.\n\n")

                file.write("--------------- DEATAILS OF ALL DISTRIBUTORS ---------------\n\n")

                for i in range(0,count):
                    file.write(f"***************** distributor {i+1} *******************\n")
                    file.write(f"distributor ID   : {master_display[i][0]}\n")
                    file.write(f"distributor Name : {master_display[i][1]}\n")
                    file.write(f"Email ID      : {master_display[i][2]}\n")
                    file.write(f"Phone         : {master_display[i][3]}\n")
                    file.write(f"Address       : {master_display[i][4]}\n")
                    file.write(f"distributor Type : {master_display[i][5]}\n")
                    file.write(f"***************************************************\n")

                    file.write("\n\n")

                file.write("-------------------------------------------------------------\n")
                file.close()

                print(f">> The distributors details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory distributor_details/ ")
                new_number_int += 1
                new_number = str(new_number_int)
                cur.execute("update printer set slno = (?)",[new_number])
                conn_db.commit()

            if op.lower() != 'y' and op.lower() != 'n':
                print(">> Incorrect Choice entered")


        elif choice == "Q" or choice == "q" or choice.lower == "exit":
            choice = "Q"

        else:
            print(">> Incorrect choice entered")

    conn_db.commit()
    conn_db.close()





def edit_supplier():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                       EDIT SUPPLIER MENU                         |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by supplier ID                                        |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by supplier Name                                      |")
        print(" ------------------------------------------------------------------ ")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            supplier_id = input("Enter supplier ID: ")

            ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

                supplier_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                        SUPPLIER DETAILS                          |")
                print("  ------------------------------------------------------------------")
                print(f"| supplier ID     : {supplier_id}")
                print(f"| supplier Name   : {name}")
                print(f"| Email ID        : {email}")
                print(f"| Phone           : {phone}")
                print(f"| Address         : {address}")
                print(f"| supplier Type   : {type_}")
                print("  ------------------------------------------------------------------")

                choice = "Q"

            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")


        elif choice == "2":
            name_of_supplier = input("Enter supplier Name (Case insensitive): ")

            name_of_supplier = name_of_supplier.lower()

            ar = cur.execute("select supplier_id from supplier where lower(name) = (?)", [name_of_supplier]).fetchone()
            distributor_id = ar[0]

            ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

                supplier_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                        SUPPLIER DETAILS                          |")
                print("  ------------------------------------------------------------------")
                print(f"| supplier ID     : {supplier_id}")
                print(f"| supplier Name   : {name}")
                print(f"| Email ID        : {email}")
                print(f"| Phone           : {phone}")
                print(f"| Address         : {address}")
                print(f"| supplier Type   : {type_}")
                print("  ------------------------------------------------------------------")

                choice = "Q"

            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")


        else:
            print(">> Incorrect choice entered")



    k = "1"

    while k != "Q":

        print(" ------------------------------------------------------------------")
        print("|                 SUPPLIER DETAILS EDITING MENU                    |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Edit supplier Name                                           |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Edit supplier email                                          |")
        print(" ------------------------------------------------------------------ ")
        print("| 3.  Edit supplier phone                                          |")
        print(" ------------------------------------------------------------------ ")
        print("| 4.  Edit supplier address                                        |")
        print(" ------------------------------------------------------------------ ")
        print("| 5.  Edit supplier type                                           |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------ ")

        k = input(">> Kindly enter your choice: ")

        if k == "1":
            name = input(">> Enter new supplier Name: ")
            cur.execute("update supplier set name = (?) where supplier_id = (?)",(name, supplier_id))
            print(">> supplier Name successfully updated")
        elif k == "2":
            email = input(">> Enter new email ID: ")
            cur.execute("update supplier set email = (?) where supplier_id = (?)",(email, supplier_id))
            print(">> supplier email successfully updated")
        elif k == "3":
            phone = input(">> Enter new phone number: ")
            cur.execute("update supplier set phone = (?) where supplier_id = (?)",(phone, supplier_id))
            print(">> supplier phone successfully updated")
        elif k == "4":
            address = input(">> Enter new address: ")
            cur.execute("update supplier set address = (?) where supplier_id = (?)",(address, supplier_id))
            print(">> supplier address successfully updated")
        elif k == "5":
            type_ = input(">> Enter new supplier type: ")
            cur.execute("update supplier set type = (?) where supplier_id = (?)",(type_,supplier_id))
            print(">> supplier type successfully updated")

        elif k == "Q" or k == "q" or k.lower() == "exit":
            k = "Q"

        else:
            print(">> Incorrect Choice entered ")

    conn_db.commit()
    conn_db.close()



def edit_distributor():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                     EDIT DISTRIBUTOR MENU                        |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by distributor ID                                     |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by distributor Name                                   |")
        print(" ------------------------------------------------------------------ ")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            distributor_id = input("Enter distributor ID: ")

            ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

                distributor_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                      DISTRIBUTOR DETAILS                         |")
                print("  ------------------------------------------------------------------")
                print(f"| distributor ID     : {distributor_id}")
                print(f"| distributor Name   : {name}")
                print(f"| Email ID           : {email}")
                print(f"| Phone              : {phone}")
                print(f"| Address            : {address}")
                print(f"| distributor Type   : {type_}")
                print("  ------------------------------------------------------------------")

                choice = "Q"

            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

        elif choice == "2":
            name_of_distributor = input("Enter distributor Name (Case insensitive): ")

            name_of_distributor = name_of_distributor.lower()

            ar = cur.execute("select distributor_id from distributor where lower(name) = (?)", [name_of_distributor]).fetchone()
            distributor_id = ar[0]

            ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
            count = ar[0]

            if count == 1:

                array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

                distributor_id = array[0][0]
                name = array[0][1]
                email = array[0][2]
                phone = array[0][3]
                address = array[0][4]
                type_ = array[0][5]

                print("  ------------------------------------------------------------------")
                print(" |                      DISTRIBUTOR DETAILS                         |")
                print("  ------------------------------------------------------------------")
                print(f"| distributor ID     : {distributor_id}")
                print(f"| distributor Name   : {name}")
                print(f"| Email ID           : {email}")
                print(f"| Phone              : {phone}")
                print(f"| Address            : {address}")
                print(f"| distributor Type   : {type_}")
                print("  ------------------------------------------------------------------")

                choice = "Q"

            else:
                print(">> Incorrect ID entered or ID doesn't exist in system. Try again")



        else:
            print(">> Incorrect choice entered")


    k = "1"

    while k != "Q":

        print(" ------------------------------------------------------------------")
        print("|                DISTRIBUTOR DETAILS EDITING MENU                  |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Edit distributor Name                                        |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Edit distributor email                                       |")
        print(" ------------------------------------------------------------------ ")
        print("| 3.  Edit distributor phone                                       |")
        print(" ------------------------------------------------------------------ ")
        print("| 4.  Edit distributor address                                     |")
        print(" ------------------------------------------------------------------ ")
        print("| 5.  Edit distributor type                                        |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------ ")

        k = input(">> Kindly enter your choice: ")

        if k == "1":
            name = input(">> Enter new distributor Name: ")
            cur.execute("update distributor set name = (?) where distributor_id = (?)",(name, distributor_id))
            print(">> distributor Name successfully updated")
        elif k == "2":
            email = input(">> Enter new email ID: ")
            cur.execute("update distributor set email = (?) where distributor_id = (?)",(email, distributor_id))
            print(">> distributor email successfully updated")
        elif k == "3":
            phone = input(">> Enter new phone number: ")
            cur.execute("update distributor set phone = (?) where distributor_id = (?)",(phone, distributor_id))
            print(">> distributor phone successfully updated")
        elif k == "4":
            address = input(">> Enter new address: ")
            cur.execute("update distributor set address = (?) where distributor_id = (?)",(address, distributor_id))
            print(">> distributor address successfully updated")
        elif k == "5":
            type_ = input(">> Enter new distributor type: ")
            cur.execute("update distributor set type = (?) where distributor_id = (?)",(type_,distributor_id))
            print(">> distributor type successfully updated")

        elif k == "Q" or k == "q" or k.lower() == "exit":
            k = "Q"

        else:
            print(">> Incorrect Choice entered ")

    conn_db.commit()
    conn_db.close()


def receive_shipment():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    ar = cur.execute("select count(*) from shipment_receival").fetchone()
    count = ar[0]
    count += 1

    print(">> Receive Shipment Portal")

    date_of_receival = input("| Date of Receival (in yyyy-mm-dd format) > ")
    supplier_id = input("| Supplier ID > ")

    ar_1 = cur.execute("select count(*) from supplier where supplier_id = (?);",[supplier_id]).fetchone()
    count_1 = ar_1[0]

    if count_1 == 1:

        ar_2 = cur.execute("select name from supplier where supplier_id = (?);",[supplier_id]).fetchone()
        supplier_name = ar_2[0]
        item_code = input("| Item Code > ")

        ar_3 = cur.execute("select count(*) from product where item_code = (?);",[item_code]).fetchone()
        count_3 = ar_3[0]

        if count_3 == 1:
            ar_4 = cur.execute("select item_name from product where item_code = (?);",[item_code]).fetchone()
            item_name = ar_4[0]

            ar_5 = cur.execute("select item_stock_qty from product where item_code = (?);",[item_code]).fetchone()
            stock_qty_prior = ar_5[0]

            qty_received = input("| Enter Qty > ")

            qty_received = int(qty_received)

            stock_qty_after = stock_qty_prior + qty_received

            rate = input("| Enter Rate >")

            total_price = input("| Enter Total Price >")

            cur.execute("insert into shipment_receival values (?,?,?,?,?,?,?,?,?,?,?);",(count,date_of_receival,supplier_id,supplier_name,item_code,item_name,stock_qty_prior,qty_received,stock_qty_after,rate,total_price))
            cur.execute("update product set item_stock_qty = (?) where item_code = (?)",(stock_qty_after,item_code))

            conn_db.commit()

            print(">> Shipment Received Successfully ")



    conn_db.commit()
    conn_db.close()


def supply_shipment():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    ar = cur.execute("select count(*) from shipment_supply").fetchone()
    count = ar[0]
    count += 1

    print(">> Supply Shipment Portal")

    date_of_receival = input("| Date of Supply (in yyyy-mm-dd format) > ")
    distributor_id = input("| Distributor ID > ")

    ar_1 = cur.execute("select count(*) from distributor where distributor_id = (?);",[distributor_id]).fetchone()
    count_1 = ar_1[0]

    if count_1 == 1:

        ar_2 = cur.execute("select name from distributor where distributor_id = (?);",[distributor_id]).fetchone()
        distributor_name = ar_2[0]
        item_code = input("| Item Code > ")

        ar_3 = cur.execute("select count(*) from product where item_code = (?);",[item_code]).fetchone()
        count_3 = ar_3[0]

        if count_3 == 1:
            ar_4 = cur.execute("select item_name from product where item_code = (?);",[item_code]).fetchone()
            item_name = ar_4[0]

            ar_5 = cur.execute("select item_stock_qty from product where item_code = (?);",[item_code]).fetchone()
            stock_qty_prior = ar_5[0]

            qty_supplied = input("| Enter Qty > ")

            qty_supplied = int(qty_supplied)

            stock_qty_after = stock_qty_prior - qty_supplied

            rate = input("| Enter Rate >")

            total_price = input("| Enter Total Price >")

            cur.execute("insert into shipment_supply values (?,?,?,?,?,?,?,?,?,?,?);",(count,date_of_receival,distributor_id,distributor_name,item_code,item_name,stock_qty_prior,qty_supplied,stock_qty_after,rate,total_price))
            cur.execute("update product set item_stock_qty = (?) where item_code = (?)",(stock_qty_after,item_code))

            conn_db.commit()

            print(">> Shipment Supplied Successfully ")



    conn_db.commit()
    conn_db.close()


def damaged_or_expired():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    ar = cur.execute("select count(*) from damaged_expired").fetchone()
    count = ar[0]
    count += 1

    print(">> Shipment Damage and Expiry Portal")

    date_of_record = input("| Date of Record (in yyyy-mm-dd format) > ")

    item_code = input("| Item Code > ")

    ar_3 = cur.execute("select count(*) from product where item_code = (?);",[item_code]).fetchone()
    count_3 = ar_3[0]

    if count_3 == 1:
        ar_4 = cur.execute("select item_name from product where item_code = (?);",[item_code]).fetchone()
        item_name = ar_4[0]

        ar_5 = cur.execute("select item_stock_qty from product where item_code = (?);",[item_code]).fetchone()
        stock_qty_prior = ar_5[0]

        qty_damaged = input("| Enter Qty Damaged or Expired > ")

        qty_damaged = int(qty_damaged)

        stock_qty_after = stock_qty_prior - qty_damaged

        rate = input("| Enter Rate >")

        damage_worth = input("| Enter Total Damage Worth >")

        print("Select Type :")
        print("1. Damaged")
        print("2. Expired")

        opp = input(">> Enter choice: ")

        if opp == "1":
            damagedORexpired = "Damaged"
        elif opp == "2":
            damagedORexpired = "Expired"
        else:
            print(">> Incorrect Choice Entered")

        notes = input("Notes and Comments regarding the damage/expiry: ")


        cur.execute("insert into damaged_expired values (?,?,?,?,?,?,?,?,?,?,?);",(count,date_of_record,item_code,item_name,stock_qty_prior,qty_damaged,stock_qty_after,damagedORexpired,notes,rate,damage_worth))
        cur.execute("update product set item_stock_qty = (?) where item_code = (?)",(stock_qty_after,item_code))

        conn_db.commit()

        print(">> Shipment Damage/Expiry Report Added Successfully ")



    conn_db.commit()
    conn_db.close()




def view_past_transactions():

    select = "1"

    while select != "Q":

        print(">>Welcome to Past Transactions Menu")

        print(" ------------------------------------------------------------------")
        print("|                            MENU                                  |")
        print(" ------------------------------------------------------------------")
        print("| 1. View all Past Receivals                                       |")
        print(" ------------------------------------------------------------------")
        print("| 2. View all Past Supplies                                        |")
        print(" ------------------------------------------------------------------ ")
        print("| 3. View Past Receivals in a time interval                        |")
        print(" ------------------------------------------------------------------ ")
        print("| 4. View Past Supplies in a time interval                         |")
        print(" ------------------------------------------------------------------ ")
        print("| 5. View all Transactions for a particular product/item           |")
        print(" ------------------------------------------------------------------ ")
        print("| 6. View Transactions for a particular product in a time interval |")
        print(" ------------------------------------------------------------------ ")
        print("| 7. View all Transactions for a supplier                          |")
        print(" ------------------------------------------------------------------ ")
        print("| 8. View Transactions for a supplier in a time interval           |")
        print(" ------------------------------------------------------------------ ")
        print("| 9. View all Transactions for a distributor                       |")
        print(" ------------------------------------------------------------------ ")
        print("| 10.View Transactions for a distributor in a time interval        |")
        print(" ------------------------------------------------------------------ ")
        print("| 11.View all past damages/expiry                                  |")
        print(" ------------------------------------------------------------------ ")
        print("| 12.View all damages for a particular product                     |")
        print(" ------------------------------------------------------------------ ")
        print("| 13.View damages for a product in a time interval                 |")
        print(" ------------------------------------------------------------------ ")
        print("| Q. Exit                                                          |")
        print(" ------------------------------------------------------------------ ")

        select = input(">> Enter your choice: ")

        if select == "1":
            view_all_past_receivals()
        elif select == "2":
            view_all_past_supply()
        elif select == "3":
            past_receivals_interval()
        elif select == "4":
            past_supply_interval()
        elif select == "5":
            all_past_product_transactions()
        elif select == "6":
            past_product_transactions_interval()
        elif select == "7":
            view_all_transactions_supplier()
        elif select == "8":
            view_transactions_supplier_interval()
        elif select == "9":
            view_all_transactions_distributor()
        elif select == "10":
            view_transactions_distributor_interval()
        elif select == "11":
            view_all_damage()
        elif select == "12":
            view_damage_product()
        elif select == "13":
            view_damage_product_interval()
        elif select.lower() == "q" or select.lower() == "exit" :
            select = "Q"

        else:
            print(">> Incorrect Choice entered. Try again")



def view_all_past_receivals():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    data = cur.execute("select * from shipment_receival ;").fetchall()
    count_ = cur.execute("select count(*) from shipment_receival ;").fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of Receival:          {data[i][1]}")
        print(f"| Supplier ID:               {data[i][2]}")
        print(f"| Supplier Name:             {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Received:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "receival_details/receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of Receival         : {data[i][1]}\n")
            file.write(f"| Supplier ID              : {data[i][2]}\n")
            file.write(f"| Supplier Name            : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Received             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The receival details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory receival_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()


def view_all_past_supply():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    data = cur.execute("select * from shipment_supply ;").fetchall()
    count_ = cur.execute("select count(*) from shipment_supply ;").fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of supply:            {data[i][1]}")
        print(f"| Distributor ID:            {data[i][2]}")
        print(f"| Distributor Name:          {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Supplied:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "supply_details/supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of supply           : {data[i][1]}\n")
            file.write(f"| Distributor ID           : {data[i][2]}\n")
            file.write(f"| Distributor Name         : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Supplied             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The supply details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory supply_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()




def all_past_product_transactions():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                   SEARCH PRODUCT/ITEM MENU                       |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by Item Code                                          |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by Item Name                                          |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            item_code = input("Enter Item Code: ")

            ar = cur.execute("select count(*) from product where item_code = (?)",[item_code]).fetchone()
            count_ = ar[0]

            if count_ == 1:

                array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

                item_code = array[0][0]
                item_name = array[0][1]
                item_weight = array[0][2]
                item_price = array[0][3]
                item_type = array[0][4]
                item_stock_qty = array[0][5]
                item_brand = array[0][6]

                print("  ------------------------------------------------------------------")
                print(" |                      ITEM/PRODUCT DETAILS                        |")
                print("  ------------------------------------------------------------------")
                print(f"| Item Code       : {item_code}")
                print(f"| Item Name       : {item_name}")
                print(f"| Item Weight     : {item_weight}")
                print(f"| Item Price      : {item_price}")
                print(f"| Item Type       : {item_type}")
                print(f"| Item Stock Qty  : {item_stock_qty}")
                print(f"| Brand Name      : {item_brand}")
                print("  ------------------------------------------------------------------")

                print()

                print(">> All past transactions for this product ")

                print("--> All past product receivals")
                arr = cur.execute("select count(*) from shipment_receival where item_code = (?);", [item_code]).fetchone()
                count_2 = arr[0]

                master_array = cur.execute("select * from shipment_receival where item_code = (?);", [item_code]).fetchall()


                for i in range(0,count_2):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Receival: {master_array[i][1]} ")
                    print(f"Supplier ID: {master_array[i][2]}")
                    print(f"Supplier Name: {master_array[i][3]}")
                    print(f"Stock Qty Prior: {master_array[i][6]}")
                    print(f"Qty Received: {master_array[i][7]}")
                    print(f"Stock Qty After: {master_array[i][8]}")
                    print(f"Rate: {master_array[i][9]}")
                    print(f"Total Price of Shipment: {master_array[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()


                print()
                print("****************************************************************************")

                print("--> All past product supplies")
                arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?);", [item_code]).fetchone()
                count_22 = arr2[0]

                master_array2 = cur.execute("select * from shipment_supply where item_code = (?);", [item_code]).fetchall()


                for i in range(0,count_22):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Supply: {master_array2[i][1]} ")
                    print(f"Distributor ID: {master_array2[i][2]}")
                    print(f"Distributor Name: {master_array2[i][3]}")
                    print(f"Stock Qty Prior: {master_array2[i][6]}")
                    print(f"Qty Supplied: {master_array2[i][7]}")
                    print(f"Stock Qty After: {master_array2[i][8]}")
                    print(f"Rate: {master_array2[i][9]}")
                    print(f"Total Price of Shipment: {master_array2[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")
                print("--> All past product damages/expiry")
                arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)", [item_code]).fetchone()
                count_23 = arr3[0]

                master_array3 = cur.execute("select * from damaged_expired where item_code = (?)", [item_code]).fetchall()


                for i in range(0,count_23):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Damage Record: {master_array3[i][1]} ")
                    print(f"Stock Qty Prior: {master_array3[i][4]}")
                    print(f"Qty Received: {master_array3[i][5]}")
                    print(f"Stock Qty After: {master_array3[i][6]}")
                    print(f"Damaged/Expired: {master_array3[i][7]}")
                    print(f"Notes regarding the damage/expiry: {master_array3[i][8]}")
                    print(f"Rate: {master_array3[i][9]}")
                    print(f"Total Damage worth: {master_array3[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")

                print()
                result = input(">> Do you want to print these details in a .txt file ? (Y/N)")

                if result.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "product_transac_details/product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                         PRODUCT DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| Item Code       : {item_code}\n")
                    file.write(f"| Item Name       : {item_name}\n")
                    file.write(f"| Item Weight     : {item_weight}\n")
                    file.write(f"| Item Price      : {item_price}\n")
                    file.write(f"| Item Type       : {item_type}\n")
                    file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
                    file.write(f"| Brand Name      : {item_brand}\n")
                    file.write("  ------------------------------------------------------------------\n")

                    file.write(">> All past transactions for this product \n\n")

                    file.write("****************************************************************************\n")

                    file.write("--> All past product receivals\n")
                    arr = cur.execute("select count(*) from shipment_receival where item_code = (?);", [item_code]).fetchone()
                    count_2 = arr[0]

                    master_array = cur.execute("select * from shipment_receival where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_2):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Receival: {master_array[i][1]} \n")
                        file.write(f"Supplier ID: {master_array[i][2]}\n")
                        file.write(f"Supplier Name: {master_array[i][3]}\n")
                        file.write(f"Stock Qty Prior: {master_array[i][6]}\n")
                        file.write(f"Qty Received: {master_array[i][7]}\n")
                        file.write(f"Stock Qty After: {master_array[i][8]}\n")
                        file.write(f"Rate: {master_array[i][9]}\n")
                        file.write(f"Total Price of Shipment: {master_array[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")


                    file.write("\n")
                    file.write("****************************************************************************\n")

                    file.write("--> All past product supplies\n")
                    arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?);", [item_code]).fetchone()
                    count_22 = arr2[0]

                    master_array2 = cur.execute("select * from shipment_supply where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_22):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Supply: {master_array2[i][1]} \n")
                        file.write(f"Distributor ID: {master_array2[i][2]}\n")
                        file.write(f"Distributor Name: {master_array2[i][3]}\n")
                        file.write(f"Stock Qty Prior: {master_array2[i][6]}\n")
                        file.write(f"Qty Supplied: {master_array2[i][7]}\n")
                        file.write(f"Stock Qty After: {master_array2[i][8]}\n")
                        file.write(f"Rate: {master_array2[i][9]}\n")
                        file.write(f"Total Price of Shipment: {master_array2[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")
                    file.write("--> All past product damages/expiry\n")
                    arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)", [item_code]).fetchone()
                    count_23 = arr3[0]

                    master_array3 = cur.execute("select * from damaged_expired where item_code = (?)", [item_code]).fetchall()


                    for i in range(0,count_23):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Damage Record: {master_array3[i][1]} \n")
                        file.write(f"Stock Qty Prior: {master_array3[i][4]}\n")
                        file.write(f"Qty Received: {master_array3[i][5]}\n")
                        file.write(f"Stock Qty After: {master_array3[i][6]}\n")
                        file.write(f"Damaged/Expired: {master_array3[i][7]}\n")
                        file.write(f"Notes regarding the damage/expiry: {master_array3[i][8]}\n")
                        file.write(f"Rate: {master_array3[i][9]}\n")
                        file.write(f"Total Damage worth: {master_array3[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")



                    file.close()

                    print(f">> The product details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory product_transac_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                if result.lower() != 'y' and result.lower() != 'n':
                    print(">> Incorrect Choice entered")



            else:
                print(">> Incorrect Product ID entered, or Product doesn't exist in system")




        elif choice == "2":
            name_of_item = input("Enter Item Name (Case insensitive): ")

            name_of_item = name_of_item.lower()

            ar_ = cur.execute("select count(*) from product where lower(item_name) = (?)", [name_of_item]).fetchone()
            count_t = ar_[0]

            if count_t == 1:

                f = 1
                ar = cur.execute("select item_code from product where lower(item_name) = (?)", [name_of_item]).fetchone()
                item_code = ar[0]

                array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

                item_code = array[0][0]
                item_name = array[0][1]
                item_weight = array[0][2]
                item_price = array[0][3]
                item_type = array[0][4]
                item_stock_qty = array[0][5]
                item_brand = array[0][6]

                print("  ------------------------------------------------------------------")
                print(" |                      ITEM/PRODUCT DETAILS                        |")
                print("  ------------------------------------------------------------------")
                print(f"| Item Code       : {item_code}")
                print(f"| Item Name       : {item_name}")
                print(f"| Item Weight     : {item_weight}")
                print(f"| Item Price      : {item_price}")
                print(f"| Item Type       : {item_type}")
                print(f"| Item Stock Qty  : {item_stock_qty}")
                print(f"| Brand Name      : {item_brand}")
                print("  ------------------------------------------------------------------")

                print()

                print(">> All past transactions for this product ")

                print("--> All past product receivals")
                arr = cur.execute("select count(*) from shipment_receival where item_code = (?);", [item_code]).fetchone()
                count_2 = arr[0]

                master_array = cur.execute("select * from shipment_receival where item_code = (?);", [item_code]).fetchall()


                for i in range(0,count_2):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Receival: {master_array[i][1]} ")
                    print(f"Supplier ID: {master_array[i][2]}")
                    print(f"Supplier Name: {master_array[i][3]}")
                    print(f"Stock Qty Prior: {master_array[i][6]}")
                    print(f"Qty Received: {master_array[i][7]}")
                    print(f"Stock Qty After: {master_array[i][8]}")
                    print(f"Rate: {master_array[i][9]}")
                    print(f"Total Price of Shipment: {master_array[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()


                print()
                print("****************************************************************************")

                print("--> All past product supplies")
                arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?);", [item_code]).fetchone()
                count_22 = arr2[0]

                master_array2 = cur.execute("select * from shipment_supply where item_code = (?);", [item_code]).fetchall()


                for i in range(0,count_22):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Supply: {master_array2[i][1]} ")
                    print(f"Distributor ID: {master_array2[i][2]}")
                    print(f"Distributor Name: {master_array2[i][3]}")
                    print(f"Stock Qty Prior: {master_array2[i][6]}")
                    print(f"Qty Supplied: {master_array2[i][7]}")
                    print(f"Stock Qty After: {master_array2[i][8]}")
                    print(f"Rate: {master_array2[i][9]}")
                    print(f"Total Price of Shipment: {master_array2[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")
                print("--> All past product damages/expiry")
                arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)", [item_code]).fetchone()
                count_23 = arr3[0]

                master_array3 = cur.execute("select * from damaged_expired where item_code = (?)", [item_code]).fetchall()


                for i in range(0,count_23):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Damage Record: {master_array3[i][1]} ")
                    print(f"Stock Qty Prior: {master_array3[i][4]}")
                    print(f"Qty Received: {master_array3[i][5]}")
                    print(f"Stock Qty After: {master_array3[i][6]}")
                    print(f"Damaged/Expired: {master_array3[i][7]}")
                    print(f"Notes regarding the damage/expiry: {master_array3[i][8]}")
                    print(f"Rate: {master_array3[i][9]}")
                    print(f"Total Damage worth: {master_array3[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")

                print()
                result = input(">> Do you want to print these details in a .txt file ? (Y/N)")

                if result.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "product_transac_details/product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                         PRODUCT DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| Item Code       : {item_code}\n")
                    file.write(f"| Item Name       : {item_name}\n")
                    file.write(f"| Item Weight     : {item_weight}\n")
                    file.write(f"| Item Price      : {item_price}\n")
                    file.write(f"| Item Type       : {item_type}\n")
                    file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
                    file.write(f"| Brand Name      : {item_brand}\n")
                    file.write("  ------------------------------------------------------------------\n")

                    file.write(">> All past transactions for this product \n\n")

                    file.write("****************************************************************************\n")

                    file.write("--> All past product receivals\n")
                    arr = cur.execute("select count(*) from shipment_receival where item_code = (?);", [item_code]).fetchone()
                    count_2 = arr[0]

                    master_array = cur.execute("select * from shipment_receival where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_2):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Receival: {master_array[i][1]} \n")
                        file.write(f"Supplier ID: {master_array[i][2]}\n")
                        file.write(f"Supplier Name: {master_array[i][3]}\n")
                        file.write(f"Stock Qty Prior: {master_array[i][6]}\n")
                        file.write(f"Qty Received: {master_array[i][7]}\n")
                        file.write(f"Stock Qty After: {master_array[i][8]}\n")
                        file.write(f"Rate: {master_array[i][9]}\n")
                        file.write(f"Total Price of Shipment: {master_array[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")


                    file.write("\n")
                    file.write("****************************************************************************\n")

                    file.write("--> All past product supplies\n")
                    arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?);", [item_code]).fetchone()
                    count_22 = arr2[0]

                    master_array2 = cur.execute("select * from shipment_supply where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_22):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Supply: {master_array2[i][1]} \n")
                        file.write(f"Distributor ID: {master_array2[i][2]}\n")
                        file.write(f"Distributor Name: {master_array2[i][3]}\n")
                        file.write(f"Stock Qty Prior: {master_array2[i][6]}\n")
                        file.write(f"Qty Supplied: {master_array2[i][7]}\n")
                        file.write(f"Stock Qty After: {master_array2[i][8]}\n")
                        file.write(f"Rate: {master_array2[i][9]}\n")
                        file.write(f"Total Price of Shipment: {master_array2[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")
                    file.write("--> All past product damages/expiry\n")
                    arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)", [item_code]).fetchone()
                    count_23 = arr3[0]

                    master_array3 = cur.execute("select * from damaged_expired where item_code = (?)", [item_code]).fetchall()


                    for i in range(0,count_23):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Damage Record: {master_array3[i][1]} \n")
                        file.write(f"Stock Qty Prior: {master_array3[i][4]}\n")
                        file.write(f"Qty Received: {master_array3[i][5]}\n")
                        file.write(f"Stock Qty After: {master_array3[i][6]}\n")
                        file.write(f"Damaged/Expired: {master_array3[i][7]}\n")
                        file.write(f"Notes regarding the damage/expiry: {master_array3[i][8]}\n")
                        file.write(f"Rate: {master_array3[i][9]}\n")
                        file.write(f"Total Damage worth: {master_array3[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")



                    file.close()

                    print(f">> The product details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory product_transac_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                if result.lower() != 'y' and result.lower() != 'n':
                    print(">> Incorrect Choice entered")



            else:
                print(">> Incorrect product name entered or product doesn't exist in system")


        elif choice.lower() == "q" or choice.lower() == "exit":
            choice = "Q"

        else:
            print(">> Incorrect Choice Entered")



    conn_db.commit()
    conn_db.close()


def past_product_transactions_interval():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    f = 0
    choice = "1"

    while choice != "Q":

        print(" ------------------------------------------------------------------")
        print("|                   SEARCH PRODUCT/ITEM MENU                       |")
        print(" ------------------------------------------------------------------")
        print("| 1.  Search by Item Code                                          |")
        print(" ------------------------------------------------------------------")
        print("| 2.  Search by Item Name                                          |")
        print(" ------------------------------------------------------------------ ")
        print("| Q.  Exit                                                         |")
        print(" ------------------------------------------------------------------")

        choice = input(">> Enter your choice: ")

        if choice == "1":
            item_code = input("Enter Item Code: ")

            ar = cur.execute("select count(*) from product where item_code = (?)",[item_code]).fetchone()
            count_ = ar[0]

            start_date = input(">> Enter Starting Date for Interval (yyyy-mm-dd): ")
            end_date = input(">> Enter Ending Date for Interval (yyyy-mm-dd): ")


            if count_ == 1:

                array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

                item_code = array[0][0]
                item_name = array[0][1]
                item_weight = array[0][2]
                item_price = array[0][3]
                item_type = array[0][4]
                item_stock_qty = array[0][5]
                item_brand = array[0][6]

                print("  ------------------------------------------------------------------")
                print(" |                      ITEM/PRODUCT DETAILS                        |")
                print("  ------------------------------------------------------------------")
                print(f"| Item Code       : {item_code}")
                print(f"| Item Name       : {item_name}")
                print(f"| Item Weight     : {item_weight}")
                print(f"| Item Price      : {item_price}")
                print(f"| Item Type       : {item_type}")
                print(f"| Item Stock Qty  : {item_stock_qty}")
                print(f"| Brand Name      : {item_brand}")
                print("  ------------------------------------------------------------------")

                print()
                print(">> All past transactions for this product in the given time interval")

                print("****************************************************************************")

                print("--> Product receivals")
                arr = cur.execute("select count(*) from shipment_receival where item_code = (?) and date_of_receival >= (?) and date_of_receival <= (?) ;", (item_code,start_date,end_date)).fetchone()
                count_2 = arr[0]

                master_array = cur.execute("select * from shipment_receival where item_code = (?) and date_of_receival >= (?) and date_of_receival <= (?);", (item_code,start_date,end_date)).fetchall()


                for i in range(0,count_2):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Receival        : {master_array[i][1]} ")
                    print(f"Supplier ID             : {master_array[i][2]}")
                    print(f"Supplier Name           : {master_array[i][3]}")
                    print(f"Stock Qty Prior         : {master_array[i][6]}")
                    print(f"Qty Received            : {master_array[i][7]}")
                    print(f"Stock Qty After         : {master_array[i][8]}")
                    print(f"Rate                    : {master_array[i][9]}")
                    print(f"Total Price of Shipment : {master_array[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()


                print()
                print("****************************************************************************")

                print("--> Product supplies")
                arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?)  and date_of_supply >= (?) and date_of_supply <= (?);", (item_code,start_date,end_date)).fetchone()
                count_22 = arr2[0]

                master_array2 = cur.execute("select * from shipment_supply where item_code = (?) and date_of_supply >= (?) and date_of_supply <= (?);", (item_code,start_date,end_date)).fetchall()


                for i in range(0,count_22):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Supply          : {master_array2[i][1]} ")
                    print(f"Distributor ID          : {master_array2[i][2]}")
                    print(f"Distributor Name        : {master_array2[i][3]}")
                    print(f"Stock Qty Prior         : {master_array2[i][6]}")
                    print(f"Qty Supplied            : {master_array2[i][7]}")
                    print(f"Stock Qty After         : {master_array2[i][8]}")
                    print(f"Rate                    : {master_array2[i][9]}")
                    print(f"Total Price of Shipment : {master_array2[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")


                print("--> Past product damages/expiry")
                arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)  and date_of_record >= (?) and date_of_record <= (?)", (item_code,start_date,end_date)).fetchone()
                count_23 = arr3[0]

                master_array3 = cur.execute("select * from damaged_expired where item_code = (?)  and date_of_record >= (?) and date_of_record <= (?)", (item_code,start_date,end_date)).fetchall()


                for i in range(0,count_23):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Damage Record               : {master_array3[i][1]} ")
                    print(f"Stock Qty Prior                     : {master_array3[i][4]}")
                    print(f"Qty Received                        : {master_array3[i][5]}")
                    print(f"Stock Qty After                     : {master_array3[i][6]}")
                    print(f"Damaged/Expired                     : {master_array3[i][7]}")
                    print(f"Notes regarding the damage/expiry   : {master_array3[i][8]}")
                    print(f"Rate                                : {master_array3[i][9]}")
                    print(f"Total Damage worth                  : {master_array3[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")

                print()
                result = input(">> Do you want to print these details in a .txt file ? (Y/N)")

                if result.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "product_transac_details/product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                         PRODUCT DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| Item Code       : {item_code}\n")
                    file.write(f"| Item Name       : {item_name}\n")
                    file.write(f"| Item Weight     : {item_weight}\n")
                    file.write(f"| Item Price      : {item_price}\n")
                    file.write(f"| Item Type       : {item_type}\n")
                    file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
                    file.write(f"| Brand Name      : {item_brand}\n")
                    file.write("  ------------------------------------------------------------------\n")

                    file.write(">> Past transactions for this product in below time interval \n\n")
                    file.write(f"Start Date : {start_date}\n")
                    file.write(f"End Date   : {end_date}\n\n")

                    file.write("****************************************************************************\n")
                    file.write("--> Past product receivals\n")
                    arr = cur.execute("select count(*) from shipment_receival where item_code = (?);", [item_code]).fetchone()
                    count_2 = arr[0]

                    master_array = cur.execute("select * from shipment_receival where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_2):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Receival           : {master_array[i][1]} \n")
                        file.write(f"Supplier ID                : {master_array[i][2]}\n")
                        file.write(f"Supplier Name              : {master_array[i][3]}\n")
                        file.write(f"Stock Qty Prior            : {master_array[i][6]}\n")
                        file.write(f"Qty Received               : {master_array[i][7]}\n")
                        file.write(f"Stock Qty After            : {master_array[i][8]}\n")
                        file.write(f"Rate                       : {master_array[i][9]}\n")
                        file.write(f"Total Price of Shipment    : {master_array[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")


                    file.write("\n")
                    file.write("****************************************************************************\n")

                    file.write("--> Past product supplies\n")
                    arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?);", [item_code]).fetchone()
                    count_22 = arr2[0]

                    master_array2 = cur.execute("select * from shipment_supply where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_22):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Supply             : {master_array2[i][1]} \n")
                        file.write(f"Distributor ID             : {master_array2[i][2]}\n")
                        file.write(f"Distributor Name           : {master_array2[i][3]}\n")
                        file.write(f"Stock Qty Prior            : {master_array2[i][6]}\n")
                        file.write(f"Qty Supplied               : {master_array2[i][7]}\n")
                        file.write(f"Stock Qty After            : {master_array2[i][8]}\n")
                        file.write(f"Rate                       : {master_array2[i][9]}\n")
                        file.write(f"Total Price of Shipment    : {master_array2[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")

                    file.write("--> Past product damages/expiry\n")
                    arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)", [item_code]).fetchone()
                    count_23 = arr3[0]

                    master_array3 = cur.execute("select * from damaged_expired where item_code = (?)", [item_code]).fetchall()


                    for i in range(0,count_23):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Damage Record              : {master_array3[i][1]} \n")
                        file.write(f"Stock Qty Prior                    : {master_array3[i][4]}\n")
                        file.write(f"Qty Received                       : {master_array3[i][5]}\n")
                        file.write(f"Stock Qty After                    : {master_array3[i][6]}\n")
                        file.write(f"Damaged/Expired                    : {master_array3[i][7]}\n")
                        file.write(f"Notes regarding the damage/expiry  : {master_array3[i][8]}\n")
                        file.write(f"Rate                               : {master_array3[i][9]}\n")
                        file.write(f"Total Damage worth                 : {master_array3[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")



                    file.close()

                    print(f">> The product details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory product_transac_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                elif result.lower() == 'n':
                    pass

                elif result.lower() != 'y' or result.lower() != 'n':
                    print(">> Incorrect Choice Entered")


            else:
                print(">> Incorrect Product ID entered, or Product doesn't exist in system")


        elif choice == "2":
            name_of_item = input("Enter Item Name (Case insensitive): ")

            name_of_item = name_of_item.lower()

            ar_ = cur.execute("select count(*) from product where lower(item_name) = (?)", [name_of_item]).fetchone()
            count_t = ar_[0]

            if count_t == 1:

                ar = cur.execute("select item_code from product where lower(item_name) = (?)", [name_of_item]).fetchone()
                item_code = ar[0]

                array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

                item_code = array[0][0]
                item_name = array[0][1]
                item_weight = array[0][2]
                item_price = array[0][3]
                item_type = array[0][4]
                item_stock_qty = array[0][5]
                item_brand = array[0][6]

                print("  ------------------------------------------------------------------")
                print(" |                      ITEM/PRODUCT DETAILS                        |")
                print("  ------------------------------------------------------------------")
                print(f"| Item Code       : {item_code}")
                print(f"| Item Name       : {item_name}")
                print(f"| Item Weight     : {item_weight}")
                print(f"| Item Price      : {item_price}")
                print(f"| Item Type       : {item_type}")
                print(f"| Item Stock Qty  : {item_stock_qty}")
                print(f"| Brand Name      : {item_brand}")
                print("  ------------------------------------------------------------------")

                print()

                print(">> All past transactions for this product in the given time interval")

                print("****************************************************************************")

                print("--> Product receivals")
                arr = cur.execute("select count(*) from shipment_receival where item_code = (?) and date_of_receival >= (?) and date_of_receival <= (?) ;", (item_code,start_date,end_date)).fetchone()
                count_2 = arr[0]

                master_array = cur.execute("select * from shipment_receival where item_code = (?) and date_of_receival >= (?) and date_of_receival <= (?);", (item_code,start_date,end_date)).fetchall()


                for i in range(0,count_2):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Receival        : {master_array[i][1]} ")
                    print(f"Supplier ID             : {master_array[i][2]}")
                    print(f"Supplier Name           : {master_array[i][3]}")
                    print(f"Stock Qty Prior         : {master_array[i][6]}")
                    print(f"Qty Received            : {master_array[i][7]}")
                    print(f"Stock Qty After         : {master_array[i][8]}")
                    print(f"Rate                    : {master_array[i][9]}")
                    print(f"Total Price of Shipment : {master_array[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()


                print()
                print("****************************************************************************")

                print("--> Product supplies")
                arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?)  and date_of_supply >= (?) and date_of_supply <= (?);", (item_code,start_date,end_date)).fetchone()
                count_22 = arr2[0]

                master_array2 = cur.execute("select * from shipment_supply where item_code = (?) and date_of_supply >= (?) and date_of_supply <= (?);", (item_code,start_date,end_date)).fetchall()


                for i in range(0,count_22):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Supply          : {master_array2[i][1]} ")
                    print(f"Distributor ID          : {master_array2[i][2]}")
                    print(f"Distributor Name        : {master_array2[i][3]}")
                    print(f"Stock Qty Prior         : {master_array2[i][6]}")
                    print(f"Qty Supplied            : {master_array2[i][7]}")
                    print(f"Stock Qty After         : {master_array2[i][8]}")
                    print(f"Rate                    : {master_array2[i][9]}")
                    print(f"Total Price of Shipment : {master_array2[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")


                print("--> Past product damages/expiry")
                arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)  and date_of_record >= (?) and date_of_record <= (?)", (item_code,start_date,end_date)).fetchone()
                count_23 = arr3[0]

                master_array3 = cur.execute("select * from damaged_expired where item_code = (?)  and date_of_record >= (?) and date_of_record <= (?)", (item_code,start_date,end_date)).fetchall()


                for i in range(0,count_23):
                    print(f"----------------------- Transaction {i+1} -----------------------")
                    print(f"Date of Damage Record               : {master_array3[i][1]} ")
                    print(f"Stock Qty Prior                     : {master_array3[i][4]}")
                    print(f"Qty Received                        : {master_array3[i][5]}")
                    print(f"Stock Qty After                     : {master_array3[i][6]}")
                    print(f"Damaged/Expired                     : {master_array3[i][7]}")
                    print(f"Notes regarding the damage/expiry   : {master_array3[i][8]}")
                    print(f"Rate                                : {master_array3[i][9]}")
                    print(f"Total Damage worth                  : {master_array3[i][10]}")
                    print("-----------------------------------------------------------------")
                    print()

                print()
                print("****************************************************************************")

                print()
                result = input(">> Do you want to print these details in a .txt file ? (Y/N)")

                if result.lower() == "y":
                    new_ar = cur.execute("select slno from printer").fetchone()
                    new_number_int = new_ar[0]
                    new_number = str(new_number_int)
                    filename = "product_transac_details/product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
                    filename_without_path = "product_transac_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

                    file = open(filename,'w')

                    #obtaining the current_time when the user is executing this command
                    current_time = datetime.datetime.now()

                    file.write(" -------------------------------------------------------------------\n")
                    file.write(f"| Date and Time of Printing: {current_time}\n")
                    file.write(" -------------------------------------------------------------------\n\n")

                    file.write("  ------------------------------------------------------------------\n")
                    file.write(" |                         PRODUCT DETAILS                          |\n")
                    file.write("  ------------------------------------------------------------------\n")
                    file.write(f"| Item Code       : {item_code}\n")
                    file.write(f"| Item Name       : {item_name}\n")
                    file.write(f"| Item Weight     : {item_weight}\n")
                    file.write(f"| Item Price      : {item_price}\n")
                    file.write(f"| Item Type       : {item_type}\n")
                    file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
                    file.write(f"| Brand Name      : {item_brand}\n")
                    file.write("  ------------------------------------------------------------------\n")

                    file.write(">> Past transactions for this product in below time interval \n\n")
                    file.write(f"Start Date : {start_date}\n")
                    file.write(f"End Date   : {end_date}\n\n")

                    file.write("****************************************************************************\n")
                    file.write("--> Past product receivals\n")
                    arr = cur.execute("select count(*) from shipment_receival where item_code = (?);", [item_code]).fetchone()
                    count_2 = arr[0]

                    master_array = cur.execute("select * from shipment_receival where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_2):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Receival           : {master_array[i][1]} \n")
                        file.write(f"Supplier ID                : {master_array[i][2]}\n")
                        file.write(f"Supplier Name              : {master_array[i][3]}\n")
                        file.write(f"Stock Qty Prior            : {master_array[i][6]}\n")
                        file.write(f"Qty Received               : {master_array[i][7]}\n")
                        file.write(f"Stock Qty After            : {master_array[i][8]}\n")
                        file.write(f"Rate                       : {master_array[i][9]}\n")
                        file.write(f"Total Price of Shipment    : {master_array[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")


                    file.write("\n")
                    file.write("****************************************************************************\n")

                    file.write("--> Past product supplies\n")
                    arr2 = cur.execute("select count(*) from shipment_supply where item_code = (?);", [item_code]).fetchone()
                    count_22 = arr2[0]

                    master_array2 = cur.execute("select * from shipment_supply where item_code = (?);", [item_code]).fetchall()


                    for i in range(0,count_22):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Supply             : {master_array2[i][1]} \n")
                        file.write(f"Distributor ID             : {master_array2[i][2]}\n")
                        file.write(f"Distributor Name           : {master_array2[i][3]}\n")
                        file.write(f"Stock Qty Prior            : {master_array2[i][6]}\n")
                        file.write(f"Qty Supplied               : {master_array2[i][7]}\n")
                        file.write(f"Stock Qty After            : {master_array2[i][8]}\n")
                        file.write(f"Rate                       : {master_array2[i][9]}\n")
                        file.write(f"Total Price of Shipment    : {master_array2[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")

                    file.write("--> Past product damages/expiry\n")
                    arr3 = cur.execute("select count(*) from damaged_expired where item_code = (?)", [item_code]).fetchone()
                    count_23 = arr3[0]

                    master_array3 = cur.execute("select * from damaged_expired where item_code = (?)", [item_code]).fetchall()


                    for i in range(0,count_23):
                        file.write(f"----------------------- Transaction {i+1} -----------------------\n")
                        file.write(f"Date of Damage Record              : {master_array3[i][1]} \n")
                        file.write(f"Stock Qty Prior                    : {master_array3[i][4]}\n")
                        file.write(f"Qty Received                       : {master_array3[i][5]}\n")
                        file.write(f"Stock Qty After                    : {master_array3[i][6]}\n")
                        file.write(f"Damaged/Expired                    : {master_array3[i][7]}\n")
                        file.write(f"Notes regarding the damage/expiry  : {master_array3[i][8]}\n")
                        file.write(f"Rate                               : {master_array3[i][9]}\n")
                        file.write(f"Total Damage worth                 : {master_array3[i][10]}\n")
                        file.write("-----------------------------------------------------------------\n")
                        file.write("\n")

                    file.write("\n")
                    file.write("****************************************************************************\n")



                    file.close()

                    print(f">> The product details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory product_transac_details/ ")
                    new_number_int += 1
                    new_number = str(new_number_int)
                    cur.execute("update printer set slno = (?)",[new_number])
                    conn_db.commit()

                elif result.lower() == 'n':
                    pass

                elif result.lower() != 'y' and result.lower() != 'n':
                    print(">> Incorrect Choice entered")


            else:
                print(">> Incorrect product name entered or product doesn't exist in system")


        elif choice.lower() == "q" or choice.lower() == "exit":
            choice = "Q"

        else:
            print(">> Incorrect option selected")



    conn_db.commit()
    conn_db.close()


def past_receivals_interval():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(">> Kindly enter the time interval ")
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    print()
    print()

    data = cur.execute("select * from shipment_receival where date_of_receival >= (?) and date_of_receival <= (?);", (start_date, end_date)).fetchall()
    count_ = cur.execute("select count(*) from shipment_receival where date_of_receival >= (?) and date_of_receival <= (?) ;", (start_date, end_date)).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of Receival:          {data[i][1]}")
        print(f"| Supplier ID:               {data[i][2]}")
        print(f"| Supplier Name:             {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Received:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "receival_details/receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("Time Interval for the below the Transactions:\n")
        file.write(f"Start Date: {start_date}\n")
        file.write(f"End Date: {end_date}\n")

        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of Receival         : {data[i][1]}\n")
            file.write(f"| Supplier ID              : {data[i][2]}\n")
            file.write(f"| Supplier Name            : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Received             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The receival details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory receival_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()


def past_supply_interval():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(">> Kindly enter the time interval ")
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    print()
    print()


    data = cur.execute("select * from shipment_supply  where date_of_supply >= (?) and date_of_supply <= (?);", (start_date, end_date)).fetchall()
    count_ = cur.execute("select count(*) from shipment_supply  where date_of_supply >= (?) and date_of_supply <= (?) ;", (start_date, end_date)).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of supply:            {data[i][1]}")
        print(f"| Distributor ID:            {data[i][2]}")
        print(f"| Distributor Name:          {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Received:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "supply_details/supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("Time Interval for the below the Transactions:\n")
        file.write(f"Start Date: {start_date}\n")
        file.write(f"End Date: {end_date}\n\n")


        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of supply           : {data[i][1]}\n")
            file.write(f"| Distributor ID           : {data[i][2]}\n")
            file.write(f"| Distributor Name         : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Received             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The supply details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory supply_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()



def view_all_transactions_supplier():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(" ------------------------------------------------------------------")
    print("|                        VIEW SUPPLIER MENU                        |")
    print(" ------------------------------------------------------------------")
    print("| 1.  Search by supplier ID                                        |")
    print(" ------------------------------------------------------------------")
    print("| 2.  Search by supplier Name                                      |")
    print(" ------------------------------------------------------------------ ")
    print("| 3.  View all suppliers                                           |")
    print(" ------------------------------------------------------------------ ")
    print("| Q.  Exit                                                         |")
    print(" ------------------------------------------------------------------")

    choice = input(">> Enter your choice: ")

    if choice == "1":
        supplier_id = input("Enter supplier ID: ")

        ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

            supplier_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                        SUPPLIER DETAILS                          |")
            print("  ------------------------------------------------------------------")
            print(f"| supplier ID     : {supplier_id}")
            print(f"| supplier Name   : {name}")
            print(f"| Email ID        : {email}")
            print(f"| Phone           : {phone}")
            print(f"| Address         : {address}")
            print(f"| supplier Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "2":
        name_of_supplier = input("Enter supplier Name (Case insensitive): ")

        name_of_supplier = name_of_supplier.lower()

        ar = cur.execute("select supplier_id from supplier where lower(name) = (?)", [name_of_supplier]).fetchone()
        supplier_id = ar[0]

        ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

            supplier_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                         SUPPLIER DETAILS                         |")
            print("  ------------------------------------------------------------------")
            print(f"| supplier ID     : {supplier_id}")
            print(f"| supplier Name   : {name}")
            print(f"| Email ID        : {email}")
            print(f"| Phone           : {phone}")
            print(f"| Address         : {address}")
            print(f"| supplier Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "Q" or choice == "q" or choice.lower == "exit":
        choice = "Q"

    else:
        print(">> Incorrect choice entered")



    data = cur.execute("select * from shipment_receival where supplier_id = (?);", [supplier_id]).fetchall()
    count_ = cur.execute("select count(*) from shipment_receival where supplier_id = (?) ;", [supplier_id]).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of Receival:          {data[i][1]}")
        print(f"| Supplier ID:               {data[i][2]}")
        print(f"| Supplier Name:             {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Received:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "receival_details/receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("  ------------------------------------------------------------------\n")
        file.write(" |                        SUPPLIER DETAILS                          |\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write(f"| supplier ID     : {supplier_id}\n")
        file.write(f"| supplier Name   : {name}\n")
        file.write(f"| Email ID        : {email}\n")
        file.write(f"| Phone           : {phone}\n")
        file.write(f"| Address         : {address}\n")
        file.write(f"| supplier Type   : {type_}\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write("\n\n")

        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of Receival         : {data[i][1]}\n")
            file.write(f"| Supplier ID              : {data[i][2]}\n")
            file.write(f"| Supplier Name            : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Received             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The receival details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory receival_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()


def view_transactions_supplier_interval():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(" ------------------------------------------------------------------")
    print("|                        VIEW SUPPLIER MENU                        |")
    print(" ------------------------------------------------------------------")
    print("| 1.  Search by supplier ID                                        |")
    print(" ------------------------------------------------------------------")
    print("| 2.  Search by supplier Name                                      |")
    print(" ------------------------------------------------------------------ ")
    print("| 3.  View all suppliers                                           |")
    print(" ------------------------------------------------------------------ ")
    print("| Q.  Exit                                                         |")
    print(" ------------------------------------------------------------------")

    choice = input(">> Enter your choice: ")

    if choice == "1":
        supplier_id = input("Enter supplier ID: ")

        ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

            supplier_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                        SUPPLIER DETAILS                          |")
            print("  ------------------------------------------------------------------")
            print(f"| supplier ID     : {supplier_id}")
            print(f"| supplier Name   : {name}")
            print(f"| Email ID        : {email}")
            print(f"| Phone           : {phone}")
            print(f"| Address         : {address}")
            print(f"| supplier Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "2":
        name_of_supplier = input("Enter supplier Name (Case insensitive): ")

        name_of_supplier = name_of_supplier.lower()

        ar = cur.execute("select supplier_id from supplier where lower(name) = (?)", [name_of_supplier]).fetchone()
        supplier_id = ar[0]

        ar = cur.execute("select count(*) from supplier where supplier_id = (?)",[supplier_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from supplier where supplier_id = (?)",[supplier_id]).fetchall()

            supplier_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                         SUPPLIER DETAILS                         |")
            print("  ------------------------------------------------------------------")
            print(f"| supplier ID     : {supplier_id}")
            print(f"| supplier Name   : {name}")
            print(f"| Email ID        : {email}")
            print(f"| Phone           : {phone}")
            print(f"| Address         : {address}")
            print(f"| supplier Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "Q" or choice == "q" or choice.lower == "exit":
        choice = "Q"

    else:
        print(">> Incorrect choice entered")


    print()
    print(">> Kindly enter the time interval ")
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    print()
    print()



    data = cur.execute("select * from shipment_receival where supplier_id = (?) and date_of_receival >= (?) and date_of_receival <= (?);", (supplier_id, start_date, end_date)).fetchall()
    count_ = cur.execute("select count(*) from shipment_receival where supplier_id = (?) and date_of_receival >= (?) and date_of_receival <= (?) ;", (supplier_id, start_date, end_date)).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of Receival:          {data[i][1]}")
        print(f"| Supplier ID:               {data[i][2]}")
        print(f"| Supplier Name:             {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Received:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "receival_details/receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "receival_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("  ------------------------------------------------------------------\n")
        file.write(" |                        SUPPLIER DETAILS                          |\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write(f"| supplier ID     : {supplier_id}\n")
        file.write(f"| supplier Name   : {name}\n")
        file.write(f"| Email ID        : {email}\n")
        file.write(f"| Phone           : {phone}\n")
        file.write(f"| Address         : {address}\n")
        file.write(f"| supplier Type   : {type_}\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write("\n\n")

        file.write("Time Interval for the below the Transactions:\n")
        file.write(f"Start Date: {start_date}\n")
        file.write(f"End Date: {end_date}\n")


        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of Receival         : {data[i][1]}\n")
            file.write(f"| Supplier ID              : {data[i][2]}\n")
            file.write(f"| Supplier Name            : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Received             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The receival details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory receival_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()



def view_all_transactions_distributor():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(" ------------------------------------------------------------------")
    print("|                      VIEW DISTRIBUTOR MENU                       |")
    print(" ------------------------------------------------------------------")
    print("| 1.  Search by distributor ID                                     |")
    print(" ------------------------------------------------------------------")
    print("| 2.  Search by distributor Name                                   |")
    print(" ------------------------------------------------------------------ ")
    print("| 3.  View all distributors                                        |")
    print(" ------------------------------------------------------------------ ")
    print("| Q.  Exit                                                         |")
    print(" ------------------------------------------------------------------")

    choice = input(">> Enter your choice: ")

    if choice == "1":
        distributor_id = input("Enter distributor ID: ")

        ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

            distributor_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                      DISTRIBUTOR DETAILS                         |")
            print("  ------------------------------------------------------------------")
            print(f"| Distributor ID     : {distributor_id}")
            print(f"| Distributor Name   : {name}")
            print(f"| Email ID           : {email}")
            print(f"| Phone              : {phone}")
            print(f"| Address            : {address}")
            print(f"| Distributor Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "2":
        name_of_distributor = input("Enter distributor Name (Case insensitive): ")

        name_of_distributor = name_of_distributor.lower()

        ar = cur.execute("select distributor_id from distributor where lower(name) = (?)", [name_of_distributor]).fetchone()
        distributor_id = ar[0]

        ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

            distributor_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                      DISTRIBUTOR DETAILS                         |")
            print("  ------------------------------------------------------------------")
            print(f"| Distributor ID     : {distributor_id}")
            print(f"| Distributor Name   : {name}")
            print(f"| Email ID           : {email}")
            print(f"| Phone              : {phone}")
            print(f"| Address            : {address}")
            print(f"| Distributor Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "Q" or choice == "q" or choice.lower == "exit":
        choice = "Q"

    else:
        print(">> Incorrect choice entered")



    data = cur.execute("select * from shipment_supply where distributor_id = (?);", [distributor_id]).fetchall()
    count_ = cur.execute("select count(*) from shipment_supply where distributor_id = (?) ;", [distributor_id]).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of supply:            {data[i][1]}")
        print(f"| Distributor ID:            {data[i][2]}")
        print(f"| Distributor Name:          {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Received:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "supply_details/supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("  ------------------------------------------------------------------\n")
        file.write(" |                        DISTRIBUTOR DETAILS                        |\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write(f"| Distributor ID     : {distributor_id}\n")
        file.write(f"| Distributor Name   : {name}\n")
        file.write(f"| Email ID        : {email}\n")
        file.write(f"| Phone           : {phone}\n")
        file.write(f"| Address         : {address}\n")
        file.write(f"| Distributor Type   : {type_}\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write("\n\n")

        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of supply           : {data[i][1]}\n")
            file.write(f"| Distributor ID           : {data[i][2]}\n")
            file.write(f"| Distributor Name         : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Received             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The supply details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory supply_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()


def view_transactions_distributor_interval():

    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(" ------------------------------------------------------------------")
    print("|                      VIEW DISTRIBUTOR MENU                       |")
    print(" ------------------------------------------------------------------")
    print("| 1.  Search by distributor ID                                     |")
    print(" ------------------------------------------------------------------")
    print("| 2.  Search by distributor Name                                   |")
    print(" ------------------------------------------------------------------ ")
    print("| 3.  View all distributors                                        |")
    print(" ------------------------------------------------------------------ ")
    print("| Q.  Exit                                                         |")
    print(" ------------------------------------------------------------------")

    choice = input(">> Enter your choice: ")

    if choice == "1":
        distributor_id = input("Enter distributor ID: ")

        ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

            distributor_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                      DISTRIBUTOR DETAILS                         |")
            print("  ------------------------------------------------------------------")
            print(f"| Distributor ID     : {distributor_id}")
            print(f"| Distributor Name   : {name}")
            print(f"| Email ID           : {email}")
            print(f"| Phone              : {phone}")
            print(f"| Address            : {address}")
            print(f"| Distributor Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "2":
        name_of_distributor = input("Enter distributor Name (Case insensitive): ")

        name_of_distributor = name_of_distributor.lower()

        ar = cur.execute("select distributor_id from distributor where lower(name) = (?)", [name_of_distributor]).fetchone()
        distributor_id = ar[0]

        ar = cur.execute("select count(*) from distributor where distributor_id = (?)",[distributor_id]).fetchone()
        count = ar[0]

        if count == 1:

            array = cur.execute("select * from distributor where distributor_id = (?)",[distributor_id]).fetchall()

            distributor_id = array[0][0]
            name = array[0][1]
            email = array[0][2]
            phone = array[0][3]
            address = array[0][4]
            type_ = array[0][5]

            print("  ------------------------------------------------------------------")
            print(" |                      DISTRIBUTOR DETAILS                         |")
            print("  ------------------------------------------------------------------")
            print(f"| Distributor ID     : {distributor_id}")
            print(f"| Distributor Name   : {name}")
            print(f"| Email ID           : {email}")
            print(f"| Phone              : {phone}")
            print(f"| Address            : {address}")
            print(f"| Distributor Type   : {type_}")
            print("  ------------------------------------------------------------------")

        else:
            print(">> Incorrect ID entered or ID doesn't exist in system. Try again")

    elif choice == "Q" or choice == "q" or choice.lower == "exit":
        choice = "Q"

    else:
        print(">> Incorrect choice entered")


    print()
    print(">> Kindly enter the time interval ")
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    print()
    print()



    data = cur.execute("select * from shipment_supply where distributor_id = (?) and date_of_supply >= (?) and date_of_supply <= (?);", (distributor_id, start_date, end_date)).fetchall()
    count_ = cur.execute("select count(*) from shipment_supply where distributor_id = (?) and date_of_supply >= (?) and date_of_supply <= (?) ;", (distributor_id, start_date, end_date)).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f" ----------------------- Transaction {i+1} -----------------------")
        print(f"| Date of supply:            {data[i][1]}")
        print(f"| Distributor ID:            {data[i][2]}")
        print(f"| Distributor Name:          {data[i][3]}")
        print(f"| Item Code:                 {data[i][4]}")
        print(f"| Item Name:                 {data[i][5]}")
        print(f"| Stock Qty Prior:           {data[i][6]}")
        print(f"| Qty Received:              {data[i][7]}")
        print(f"| Stock Qty After:           {data[i][8]}")
        print(f"| Rate:                      {data[i][9]}")
        print(f"| Total Price:               {data[i][10]}")
        print(f" -----------------------------------------------------------------")
        print()


    print()
    print_op = input(">> Do you wish to print these details a .txt file ? (Y/N)")

    if print_op.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "supply_details/supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "supply_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("  ------------------------------------------------------------------\n")
        file.write(" |                        DISTRIBUTOR DETAILS                        |\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write(f"| Distributor ID     : {distributor_id}\n")
        file.write(f"| Distributor Name   : {name}\n")
        file.write(f"| Email ID        : {email}\n")
        file.write(f"| Phone           : {phone}\n")
        file.write(f"| Address         : {address}\n")
        file.write(f"| Distributor Type   : {type_}\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write("\n\n")

        file.write("Time Interval for the below Transactions:\n")
        file.write(f"Start Date: {start_date}\n")
        file.write(f"End Date: {end_date}\n")


        for i in range(0,count):

            file.write(f" ----------------------- Transaction {i+1} -----------------------\n")
            file.write(f"| Date of supply           : {data[i][1]}\n")
            file.write(f"| Distributor ID           : {data[i][2]}\n")
            file.write(f"| Distributor Name         : {data[i][3]}\n")
            file.write(f"| Item Code                : {data[i][4]}\n")
            file.write(f"| Item Name                : {data[i][5]}\n")
            file.write(f"| Stock Qty Prior          : {data[i][6]}\n")
            file.write(f"| Qty Received             : {data[i][7]}\n")
            file.write(f"| Stock Qty After          : {data[i][8]}\n")
            file.write(f"| Rate                     : {data[i][9]}\n")
            file.write(f"| Total Price              : {data[i][10]}\n")
            file.write(f" -----------------------------------------------------------------\n")
            file.write("\n")


        print(f">> The supply details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory supply_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    elif print_op.lower() != 'y' and print_op.lower() != 'n':
            print(">> Incorrect Choice entered")


    conn_db.commit()
    conn_db.close()



def view_all_damage():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print("****************** ALL PAST PRODUCT DAMAGE/EXPIRY ******************")

    data = cur.execute("select * from damaged_expired;").fetchall()
    count_ = cur.execute("select count(*) from damaged_expired;").fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f"------------------- Record {i+1} -------------------")
        print(f"Date of Record      : {data[i][1]}")
        print(f"Item Code           : {data[i][2]}")
        print(f"Item Name           : {data[i][3]}")
        print(f"Stock Qty Prior     : {data[i][4]}")
        print(f"Qty Damaged         : {data[i][5]}")
        print(f"Stock Qty After     : {data[i][6]}")
        print(f"Damaged or Expired  : {data[i][7]}")
        print(f"Notes               : {data[i][8]}")
        print(f"Rate                : {data[i][9]}")
        print(f"Total Damage Worth  : {data[i][10]}")


    print("********************************************************************")

    print()
    result = input(">> Do you want to print these details in a .txt file ? (Y/N)")

    if result.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "damage_expiry_details/damage_expiry_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "damage_expiry_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("****************** ALL PAST PRODUCT DAMAGE/EXPIRY ******************\n\n")


        for i in range(0,count):

            file.write(f"------------------- Record {i+1} -------------------\n")
            file.write(f"Date of Record      : {data[i][1]}\n")
            file.write(f"Item Code           : {data[i][2]}\n")
            file.write(f"Item Name           : {data[i][3]}\n")
            file.write(f"Stock Qty Prior     : {data[i][4]}\n")
            file.write(f"Qty Damaged         : {data[i][5]}\n")
            file.write(f"Stock Qty After     : {data[i][6]}\n")
            file.write(f"Damaged or Expired  : {data[i][7]}\n")
            file.write(f"Notes               : {data[i][8]}\n")
            file.write(f"Rate                : {data[i][9]}\n")
            file.write(f"Total Damage Worth  : {data[i][10]}\n")


        file.write("\n")
        file.write("********************************************************************\n\n")


        file.close()

        print(f">> The damage/expiry details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory damage_expiry_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    if result.lower() != 'y' and result.lower() != 'n':
        print(">> Incorrect Choice entered")



    conn_db.commit()
    conn_db.close()



def view_damage_product():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(" ------------------------------------------------------------------")
    print("|                     VIEW PRODUCT/ITEM MENU                       |")
    print(" ------------------------------------------------------------------")
    print("| 1.  Search by Item Code                                          |")
    print(" ------------------------------------------------------------------")
    print("| 2.  Search by Item Name                                          |")
    print(" ------------------------------------------------------------------ ")
    print("| 3.  View all Items                                               |")
    print(" ------------------------------------------------------------------ ")
    print("| Q.  Exit                                                         |")
    print(" ------------------------------------------------------------------")

    choice = input(">> Enter your choice: ")

    if choice == "1":
        item_code = input("Enter Item Code: ")

        ar = cur.execute("select count(*) from product where item_code = (?)",[item_code]).fetchone()
        count_ = ar[0]

        if count_ == 1:

            array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

            item_code = array[0][0]
            item_name = array[0][1]
            item_weight = array[0][2]
            item_price = array[0][3]
            item_type = array[0][4]
            item_stock_qty = array[0][5]
            item_brand = array[0][6]

            print("  ------------------------------------------------------------------")
            print(" |                      ITEM/PRODUCT DETAILS                        |")
            print("  ------------------------------------------------------------------")
            print(f"| Item Code       : {item_code}")
            print(f"| Item Name       : {item_name}")
            print(f"| Item Weight     : {item_weight}")
            print(f"| Item Price      : {item_price}")
            print(f"| Item Type       : {item_type}")
            print(f"| Item Stock Qty  : {item_stock_qty}")
            print(f"| Brand Name      : {item_brand}")
            print("  ------------------------------------------------------------------")

            print()


        else:
            print(">> Incorrect Product ID entered, or Product doesn't exist in system")


    elif choice == "2":
        name_of_item = input("Enter Item Name (Case insensitive): ")

        name_of_item = name_of_item.lower()

        ar_ = cur.execute("select count(*) from product where lower(item_name) = (?)", [name_of_item]).fetchone()
        count_t = ar_[0]

        if count_t == 1:

            ar = cur.execute("select item_code from product where lower(item_name) = (?)", [name_of_item]).fetchone()
            item_code = ar[0]

            array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

            item_code = array[0][0]
            item_name = array[0][1]
            item_weight = array[0][2]
            item_price = array[0][3]
            item_type = array[0][4]
            item_stock_qty = array[0][5]
            item_brand = array[0][6]

            print("  ------------------------------------------------------------------")
            print(" |                      ITEM/PRODUCT DETAILS                        |")
            print("  ------------------------------------------------------------------")
            print(f"| Item Code       : {item_code}")
            print(f"| Item Name       : {item_name}")
            print(f"| Item Weight     : {item_weight}")
            print(f"| Item Price      : {item_price}")
            print(f"| Item Type       : {item_type}")
            print(f"| Item Stock Qty  : {item_stock_qty}")
            print(f"| Brand Name      : {item_brand}")
            print("  ------------------------------------------------------------------")

            print()

        else:
            print(">> Incorrect product name entered or product doesn't exist in system")


    print("****************** PAST PRODUCT DAMAGE/EXPIRY ******************")

    data = cur.execute("select * from damaged_expired where item_code = (?);", [item_code]).fetchall()
    count_ = cur.execute("select count(*) from damaged_expired where item_code = (?);", [item_code]).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f"------------------- Record {i+1} -------------------")
        print(f"Date of Record      : {data[i][1]}")
        print(f"Item Code           : {data[i][2]}")
        print(f"Item Name           : {data[i][3]}")
        print(f"Stock Qty Prior     : {data[i][4]}")
        print(f"Qty Damaged         : {data[i][5]}")
        print(f"Stock Qty After     : {data[i][6]}")
        print(f"Damaged or Expired  : {data[i][7]}")
        print(f"Notes               : {data[i][8]}")
        print(f"Rate                : {data[i][9]}")
        print(f"Total Damage Worth  : {data[i][10]}")


    print("****************************************************************")

    print()
    result = input(">> Do you want to print these details in a .txt file ? (Y/N)")

    if result.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "damage_expiry_details/damage_expiry_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "damage_expiry_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("  ------------------------------------------------------------------\n")
        file.write(" |                         PRODUCT DETAILS                          |\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write(f"| Item Code       : {item_code}\n")
        file.write(f"| Item Name       : {item_name}\n")
        file.write(f"| Item Weight     : {item_weight}\n")
        file.write(f"| Item Price      : {item_price}\n")
        file.write(f"| Item Type       : {item_type}\n")
        file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
        file.write(f"| Brand Name      : {item_brand}\n")
        file.write("  ------------------------------------------------------------------\n\n")


        file.write("****************** PAST PRODUCT DAMAGE/EXPIRY ******************\n\n")


        for i in range(0,count):

            file.write(f"------------------- Record {i+1} -------------------\n")
            file.write(f"Date of Record      : {data[i][1]}\n")
            file.write(f"Item Code           : {data[i][2]}\n")
            file.write(f"Item Name           : {data[i][3]}\n")
            file.write(f"Stock Qty Prior     : {data[i][4]}\n")
            file.write(f"Qty Damaged         : {data[i][5]}\n")
            file.write(f"Stock Qty After     : {data[i][6]}\n")
            file.write(f"Damaged or Expired  : {data[i][7]}\n")
            file.write(f"Notes               : {data[i][8]}\n")
            file.write(f"Rate                : {data[i][9]}\n")
            file.write(f"Total Damage Worth  : {data[i][10]}\n")
            file.write(f"----------------------------------------------------\n")


        file.write("\n")
        file.write("****************************************************************\n\n")


        file.close()

        print(f">> The damage/expiry details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory damage_expiry_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    if result.lower() != 'y' and result.lower() != 'n':
        print(">> Incorrect Choice entered")



    conn_db.commit()
    conn_db.close()



def view_damage_product_interval():

    #Connect to the database
    conn_db = sqlite3.connect('stock_management.db')
    cur = conn_db.cursor()

    print(" ------------------------------------------------------------------")
    print("|                     VIEW PRODUCT/ITEM MENU                       |")
    print(" ------------------------------------------------------------------")
    print("| 1.  Search by Item Code                                          |")
    print(" ------------------------------------------------------------------")
    print("| 2.  Search by Item Name                                          |")
    print(" ------------------------------------------------------------------ ")
    print("| 3.  View all Items                                               |")
    print(" ------------------------------------------------------------------ ")
    print("| Q.  Exit                                                         |")
    print(" ------------------------------------------------------------------")

    choice = input(">> Enter your choice: ")

    if choice == "1":
        item_code = input("Enter Item Code: ")

        ar = cur.execute("select count(*) from product where item_code = (?)",[item_code]).fetchone()
        count_ = ar[0]

        if count_ == 1:

            array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

            item_code = array[0][0]
            item_name = array[0][1]
            item_weight = array[0][2]
            item_price = array[0][3]
            item_type = array[0][4]
            item_stock_qty = array[0][5]
            item_brand = array[0][6]

            print("  ------------------------------------------------------------------")
            print(" |                      ITEM/PRODUCT DETAILS                        |")
            print("  ------------------------------------------------------------------")
            print(f"| Item Code       : {item_code}")
            print(f"| Item Name       : {item_name}")
            print(f"| Item Weight     : {item_weight}")
            print(f"| Item Price      : {item_price}")
            print(f"| Item Type       : {item_type}")
            print(f"| Item Stock Qty  : {item_stock_qty}")
            print(f"| Brand Name      : {item_brand}")
            print("  ------------------------------------------------------------------")

            print()


        else:
            print(">> Incorrect Product ID entered, or Product doesn't exist in system")


    elif choice == "2":
        name_of_item = input("Enter Item Name (Case insensitive): ")

        name_of_item = name_of_item.lower()

        ar_ = cur.execute("select count(*) from product where lower(item_name) = (?)", [name_of_item]).fetchone()
        count_t = ar_[0]

        if count_t == 1:

            ar = cur.execute("select item_code from product where lower(item_name) = (?)", [name_of_item]).fetchone()
            item_code = ar[0]

            array = cur.execute("select * from product where item_code = (?)",[item_code]).fetchall()

            item_code = array[0][0]
            item_name = array[0][1]
            item_weight = array[0][2]
            item_price = array[0][3]
            item_type = array[0][4]
            item_stock_qty = array[0][5]
            item_brand = array[0][6]

            print("  ------------------------------------------------------------------")
            print(" |                      ITEM/PRODUCT DETAILS                        |")
            print("  ------------------------------------------------------------------")
            print(f"| Item Code       : {item_code}")
            print(f"| Item Name       : {item_name}")
            print(f"| Item Weight     : {item_weight}")
            print(f"| Item Price      : {item_price}")
            print(f"| Item Type       : {item_type}")
            print(f"| Item Stock Qty  : {item_stock_qty}")
            print(f"| Brand Name      : {item_brand}")
            print("  ------------------------------------------------------------------")

            print()

        else:
            print(">> Incorrect product name entered or product doesn't exist in system")


    print(">>Kindly enter the start and end date of your interval")
    start_date = input("Start Date (yyy-mm-dd): ")
    end_date = input("End Date (yyy-mm-dd): ")


    print("****************** PAST PRODUCT DAMAGE/EXPIRY ******************")

    data = cur.execute("select * from damaged_expired where item_code = (?) and date_of_record >= (?) and date_of_record <= (?);", (item_code, start_date, end_date)).fetchall()
    count_ = cur.execute("select count(*) from damaged_expired where item_code = (?) and date_of_record >= (?) and date_of_record <= (?);", (item_code, start_date, end_date)).fetchone()

    count = count_[0]

    for i in range(0,count):

        print(f"------------------- Record {i+1} -------------------")
        print(f"Date of Record      : {data[i][1]}")
        print(f"Item Code           : {data[i][2]}")
        print(f"Item Name           : {data[i][3]}")
        print(f"Stock Qty Prior     : {data[i][4]}")
        print(f"Qty Damaged         : {data[i][5]}")
        print(f"Stock Qty After     : {data[i][6]}")
        print(f"Damaged or Expired  : {data[i][7]}")
        print(f"Notes               : {data[i][8]}")
        print(f"Rate                : {data[i][9]}")
        print(f"Total Damage Worth  : {data[i][10]}")


    print("****************************************************************")

    print()
    result = input(">> Do you want to print these details in a .txt file ? (Y/N)")

    if result.lower() == "y":
        new_ar = cur.execute("select slno from printer").fetchone()
        new_number_int = new_ar[0]
        new_number = str(new_number_int)
        filename = "damage_expiry_details/damage_expiry_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used
        filename_without_path = "damage_expiry_details_file{}.txt".format(new_number.zfill(4)) #zfill is used for padding. So 25 is converted to 0025 if zfill(4) is used

        file = open(filename,'w')

        #obtaining the current_time when the user is executing this command
        current_time = datetime.datetime.now()

        file.write(" -------------------------------------------------------------------\n")
        file.write(f"| Date and Time of Printing: {current_time}\n")
        file.write(" -------------------------------------------------------------------\n\n")

        file.write("  ------------------------------------------------------------------\n")
        file.write(" |                         PRODUCT DETAILS                          |\n")
        file.write("  ------------------------------------------------------------------\n")
        file.write(f"| Item Code       : {item_code}\n")
        file.write(f"| Item Name       : {item_name}\n")
        file.write(f"| Item Weight     : {item_weight}\n")
        file.write(f"| Item Price      : {item_price}\n")
        file.write(f"| Item Type       : {item_type}\n")
        file.write(f"| Item Stock Qty  : {item_stock_qty}\n")
        file.write(f"| Brand Name      : {item_brand}\n")
        file.write("  ------------------------------------------------------------------\n\n")

        file.write("Time Interval for the below Records:\n")
        file.write(f"Start Date: {start_date}\n")
        file.write(f"End Date: {end_date}\n")


        file.write("****************** PAST PRODUCT DAMAGE/EXPIRY ******************\n\n")


        for i in range(0,count):

            file.write(f"------------------- Record {i+1} -------------------\n")
            file.write(f"Date of Record      : {data[i][1]}\n")
            file.write(f"Item Code           : {data[i][2]}\n")
            file.write(f"Item Name           : {data[i][3]}\n")
            file.write(f"Stock Qty Prior     : {data[i][4]}\n")
            file.write(f"Qty Damaged         : {data[i][5]}\n")
            file.write(f"Stock Qty After     : {data[i][6]}\n")
            file.write(f"Damaged or Expired  : {data[i][7]}\n")
            file.write(f"Notes               : {data[i][8]}\n")
            file.write(f"Rate                : {data[i][9]}\n")
            file.write(f"Total Damage Worth  : {data[i][10]}\n")
            file.write(f"----------------------------------------------------\n")


        file.write("\n")
        file.write("****************************************************************\n\n")


        file.close()

        print(f">> The damage/expiry details have been successfully printed in the file {filename_without_path} and it is downloaded inside the directory damage_expiry_details/ ")
        new_number_int += 1
        new_number = str(new_number_int)
        cur.execute("update printer set slno = (?)",[new_number])
        conn_db.commit()

    if result.lower() != 'y' and result.lower() != 'n':
        print(">> Incorrect Choice entered")



    conn_db.commit()
    conn_db.close()



# All utility functions end here
main()
