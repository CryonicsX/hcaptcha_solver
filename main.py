import pymongo
import random
import random
import array
import pymongo
import sys
import json
import time



conf = json.loads(open('config.json', 'r', encoding='utf-8').read())


myclient = pymongo.MongoClient(conf["mongourl"])


mydb = myclient["mydatabase"] 


mycol = mydb["PasswordManager"]


print(
"""                                       
 _____                             _    _____                         
|  _  |___ ___ ___ _ _ _ ___ ___ _| |  |     |___ ___ ___ ___ ___ ___ 
|   __| .'|_ -|_ -| | | | . |  _| . |  | | | | .'|   | .'| . | -_|  _|
|__|  |__,|___|___|_____|___|_| |___|  |_|_|_|__,|_|_|__,|_  |___|_|    (Developed by CryonicX)
                                                         |___|
[1]: Generates Password
[2]: Records the password you enter into the database
[3]: List the passwords saved in the database
[4]: It Shows The Password That The Media You Entered Has Saved To The Database
[5]: Resets the database
[Q]: quit
"""
)


NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    
    
CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    
    
UPCHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']   
    
    
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    
    
COMBINED_LIST = NUMBER + UPCHARACTERS + CHARACTERS  + SYMBOLS
    
    
rand_digit = random.choice(NUMBER)
    
    
rand_upper = random.choice(UPCHARACTERS)
    
    
rand_lower = random.choice(CHARACTERS)
    
    
rand_symbol = random.choice(SYMBOLS)
    
    
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


cryonicx = input("choose: ")


if cryonicx == "1":
    MAX_LEN = input('How many characters do you want your password to be? ')
    if MAX_LEN != int:
        try:
            print('Password length must be numbers.')
            time.sleep(2.4)
            quit()
        except Exception as e:
            print(e)


    
    MEDİA =  input('Where will you use this password? ')

    
    for x in range(int(MAX_LEN) - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    
    password = ""
    
    
    for x in temp_pass_list:
            password = password + x
    
    db = input('Do you want to save the password to the Database?(yes/no): ')

    if db != str:
        try:
            print('Yes and no only.')
            time.sleep(2.4)
            quit()
        except Exception as e:
            print(e)

    
    if db == "yes" or "y":
        try:
            mydict = {"Media":str(MEDİA),"Password":str(password) } 
            
            mycol.insert_one(mydict)
            print(f"Password has been created for [{MEDİA}] || password: \n{password} ")
        except Exception as e:
            print(f"Error : {e}")

    else:
        print(f"Password has been created for [{MEDİA}] || password: \n{password} \n(not saved in database)")


if cryonicx == "2":
    try:
        pass2 = input('Enter the password you want to save: ')
        MEDİA =  input('Where will you use this password? ')
        mydict = {"Media":MEDİA,"Password":pass2 }
        mycol.insert_one(mydict) 
        print('Saved to the database.')
    except Exception as e:
        print(f"Error : {e}")



if cryonicx == "3":
    try:
        for x in mycol.find({},{ "_id": 0,  "Password": 1 ,"Media":2}):
            data = x["Password"]
            data2 = x["Media"]
            print(f"Media Name: {data2} | Password: {data}")
    except Exception as e:
        print(f"Error : {e}")



if cryonicx == "4":
        rar = input('Enter the Name of the Media You Want to Find in the Database: ')
        try:
            for x in mycol.find({},{ "_id": 0,  "Password": 1 ,"Media":2}): 
                data = x["Password"]
                data2 = x["Media"]
                if rar in x['Media']:
                    print(f"Found in {data2} database. password: {data} ")
                else:
                    print('Data not found.')
        except Exception as e:
            print(f"Error : {e}")



if cryonicx == "5":
    try:
        x = mycol.delete_many({})
        print(x.deleted_count, "password deleted")
    except Exception as e:
        print(f"Error : {e}")


if cryonicx == "Q" or "quit" or "q" or "QUİT":
    try:
        quit()
    except Exception as e:
        print(f"Error : {e}")

