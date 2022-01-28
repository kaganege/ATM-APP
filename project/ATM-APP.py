#•••••••••••••••••••••••••• Used Modules••••••••••••••••••••••••••#  
import os
from sys import exit
from time import sleep
from datetime import datetime
from randomPassword import RandPass
""" randomPassword.py is a module I created for create Random passwords. You can examine this."""

#-------------------------------Error Block Function-----------------------------------------#
def error_block(query, keyfunc):
    while True:
        try:
            value = keyfunc(input(query))
            return value
        except Exception:
            print('-'*50)
            print("Please enter a correct value")
            print('-'*50)    
""" Error Block function created for shorting the debugging process, by @kadir014 user.
 His GitHub: https://github.com/kadir014 """
 
 #Usage Example: x = error_block("Input content: ", int)  [this mean, the input must be an integer.]


#################### Atm Class ####################

class Atm:
#------------------------------- __init__ Function-----------------------------------------#     
    def __init__(self):
        print ("ATM APP - Main Menu ")
        print("•"*50)
        
#| >>> A dictionary for user datas :   
#--> There are some pre-filled account datas. You can set them.     
        self.accounts =  {
        "names" : ["tom", "Martin", "Amanda", "Carl"] ,
        "passwords" : ["12345678" , "martin.account", "thatsmycard", "carlbuthewantbeelon"] ,
        "card_numbers" : [ "1111 1111 1111 1111", "2222 2222 2222 2222", "3333 3333 3333 3333", "4444 4444 4444 4444"],
        "create_date" : ["21/01/2022 16:52:40", "20/06/2021 16:52:40", "06/05/2021 10:02:21", "15/05/2020 15:19:11"], 
        "budgets" : [0,0,0,0]
}       

#| >>> Letters and some characters for avoid to user enter letters and characters to inside card number:
        self.chracters_and_letters = [
        
"A","B", "C", "D" , "E", "F", "G" ,"H",  "I" , "J",  "K", "L" ,  "M", "N" , "O" , "P"  ,"R", "S", "T", "U", "V", "W", "X", "Y",  "Z", #--> capital letters
        
"a", "b", "c", "d", "e" , "f", "g","h", "i", "j","k", "l", "m", "n", "o" , "p", "r","s","t","u","v", "w",  "x", "y" , "z", #--> small letters
 
 "#" , "*", "-", "+", "=", "_" , "(", ")" , "~", ":" , ";" , "!", "?", "@" , "<", ">" , "/", " '\' ", "|" , "{", "}", "$", "€", "&", "[", "]", " ' "  #--> some  characters
  
]
       
        


#------------------------------------Main Menu Function------------------------------------# 

    def main_menu(self):
#| >>> Main menu input:
        choice = error_block("""
Welcome to the ATM app:
1 --- Add a new account
2 --- Login your account and see your account infos, make operations
3 --- Exit from ATM app
         
 ~~> Selection: """ , int)
 
        if choice == 1 :
           os.system("cls") if os.name == "nt" else os.system("clear") #this one line if-else statement, clears the terminal screen by os module we imported above.
           self.add_account()
              
        if choice == 2:
           os.system("cls") if os.name == "nt" else os.system("clear")
           self.logging_account()
       
        if choice ==3:
            print("-"*50)
            print("You quited from app.")
            exit()

#| >>> Else statement:                        
        else:
            print("-"*50)
            print("--> The entered value must be 1,2 or 3. Try again.")
            sleep(2)
            os.system("cls") if os.name == "nt" else os.system("clear")
            self.main_menu()
            
 
         
#-------------------------------Account Adding Function-----------------------------------------# 
    def add_account(self):
#| >>> Name and Name conditions :    
             print ("Adding Account")
             print("•"*50)
             
             name = input("Enter your name for your new account: ")
          
             while len(name) < 2: 
               print ("--> Your name must be least 2 character. Try again.")
               print ("-"*50)
               name = input("Your name: ")
               
             print(">>> Name successfuly saved." )
             sleep(2) #--> we imported that ''sleep" from time module above
             print ("-"*50)
             
#| >>> Password and Password conditions:             
             selection = input("Specify a password: Random or Custom password?\n--- '1' for Custom Password\n--- '2' for Random Password\n\n Selection: ")
             
             if selection == "1":
                print ("-"*50)
                for i in self.chracters_and_letters : #--> this is a list in __init__ function
                         print ("--> Please enter only number as card number. Don't use any letter or another foreign character. Also card number must be 19 character (with spaces). Don't forget the spaces.")    
                         card_number = input("Card number: ")         
                                
                password = input("Create your password (least 8 character) : ")             
                while len(password) < 8 or " " in password:
                    print("--> Password must be least 8 character and mustn't contain any space. Try again.")
                    print ("-"*50)         
                    password = input("Password: ")
                    
                print(">>> Password successfuly saved." )
                sleep(2)
                print ("-"*50)         
                     
             else:     
                  print(" \n>>> You selected random password. Your random password is : ")             
                  
                  object = RandPass() #--> we imported that from "randomPassword" module above.
                  password = object.random_password()
                  
                  print("(Don't forget this ! )")
                  sleep(2)
                  print ("-"*50)  
                  
#| >>> Card Number and Card Number conditions:                   
             card_number = input("And enter your card number: ")
                          
             while len(card_number) != 19:
                 print("--> Wrong card number. Please try again. (ex:0123 4567 8900 0000)")
                 print ("-"*50)  
                 card_number = input("Card number: ")
             
             
             for i in self.chracters_and_letters : #--> this is a list in __init__ function
                  while i  in card_number or  len(card_number) != 19:
                         print ("\n--> Please enter only number as card number. Don't use any letter or another foreign character. Also card number must be 19 character (with spaces). Don't forget the spaces. (ex:0123 4567 8900 0000)")    
                         card_number = input("Card number: ")
                         
             print(">>> Card number successfully saved.")
             sleep(2)
             print ("-"*50)  
                         
           
#| >>> Saving all informations to "accounts" dictionary:          
             self.accounts["names"].append(name)
             self.accounts["passwords"].append(password)
             self.accounts["card_numbers"].append(card_number)

             now = datetime.now()
             self.accounts["create_date"].append(now.strftime(r"%d/%m/%Y %H:%M:%S"))
             self.accounts["budgets"].append(0) #--> We're adding a budget per every account. 
             
#| >>> Returning to main menu::    
             confirmation = input(">>> Your new account created. Click enter for return to menu: ")
             os.system("cls") if os.name == "nt" else os.system("clear") 
             self.main_menu()

#---------------------------------Logging Account Function---------------------------------------#             
    def logging_account(self): 
             print ("Logging to Account")
             print("•"*50)
             
#| >>> Name, password and card_number input and verification:             
             self.name = input("Name: ")         
             self.password = input ("Password: ")
             self.card_number = input("Card Number: ")

             if self.name in self.accounts["names"]:  #--> Main if
                   self.name_index = self.accounts["names"].index(self.name)
                   self.password_index = self.accounts["passwords"][self.name_index]
                   cardNumber_index = self.accounts["card_numbers"][self.name_index]
                

                   print ("-"*50) 

                   if self.password == self.password_index  and self.card_number == cardNumber_index : #--> Sub if
                      print('>>> Access confirmed. Logging to account, please wait...')
                   
                      sleep(2)
                      os.system("cls") if os.name == "nt" else os.system("clear")
                      self.account_information_operation()
                   
                   else:  #--> Sub else   
                       while self.password != self.password_index or self.card_number != cardNumber_index:
                          print("--> Password or card number is invalid. Please try again enter the password and card number.") 
                          self.password = input ("Password: ")
                          self.card_number = input("Card Number: ")
                       
                   print ("-"*50) 
                   print(">>> Acces confirmed. Logging to account, please wait...") #--> When user entered true the passeword and card_number, the while loop will end.
                   
                   sleep(2) 
                   os.system("cls") if os.name == "nt" else os.system("clear")  
                   self.account_information_operation()
                  
             else: #--> Main else
                  print ("-"*50)   
                  print("--> There is no such user. Returning to menu.")  
                  sleep(2)
               
                  os.system("cls") if os.name == "nt" else os.system("clear")             
                  self. main_menu()
               
#---------------------------------Account Information Function---------------------------------------#   
    def account_information_operation(self):             
#| >>> Account infromation:      
             print ("Account Information and Account Operations")
             print("•"*50)
             
             print (f"Welcome {self.accounts['names'][self.name_index]} ! In here, you can see your account informations and  you can make various operation on your account. ")
             print("-"*50)

             print(f"""
Informations         
--- Name: {self.accounts["names"][self.name_index]}
--- Password: {self.accounts["passwords"][self.name_index]}
--- Card Number: {self.card_number}
--- Create Date: {self.accounts["create_date"][self.name_index]}
--- Budget in Your Card: {self.accounts["budgets"][self.name_index]} $  
""")
             print("-"*50)

# -->  the expression **self.accounts["budgets"][self.name index]**,  is accessing to budget of account. ("**", sign is only for highlighting expression.)

#| >>> Making operations on account:              
             account_operations = error_block("""
Operations
1 --- Budget operations 
2 --- Change account password
3 --- Change account name
4 --- Money transfer
5 --- Log out
6 --- Delete account

Selection: """, int)

#| >>> Account operations conditions             
             if account_operations == 1: 
                 os.system("cls") if os.name == "nt" else os.system("clear")
                 self.budget_operations() 
                 
             if account_operations == 2:
                 os.system("cls") if os.name == "nt" else os.system("clear")
                 self.changing_password()
                 
             if account_operations == 3:
                 os.system("cls") if os.name == "nt" else os.system("clear")
                 self.changing_name()
                 
             if account_operations == 4:
                 os.system("cls") if os.name == "nt" else os.system("clear")
                 self.money_transfer()                 

#| >>> Logging Out condition                                        
             if account_operations == 5:
                 os.system("cls") if os.name == "nt" else os.system("clear")
                 print ("Log Out")
                 print("•"*50)                                 
                 confirm = error_block("Are you sure for log out? Type 1 for confirm, 0 for cancel: ",int)
                                   
                 if confirm == 1:
                     print("-"*50)
                     print(">>> Logged out. Returning to main menu...")
                     sleep(2)                     
                     os.system("cls") if os.name == "nt" else os.system("clear")
                     self.main_menu() 
                 else:
                     os.system("cls") if os.name == "nt" else os.system("clear")
                     self.account_information_operation() 

#| >>> Deleting account condition                                          
             if account_operations == 6:         
                 os.system("cls") if os.name == "nt" else os.system("clear")
                 print ("Delete Account")
                 print("•"*50)             
                 confirm = error_block("Are you sure for delete your account? Type 1 for confirm, 0 for cancel: ",int)
                 if confirm == 1:
                     self.accounts["names"].remove(self.accounts["names"][self.name_index])
                     self.accounts["passwords"].remove(self.accounts["passwords"][self.name_index])
                     self.accounts["card_numbers"].remove(self.accounts["card_numbers"][self.name_index])
                     self.accounts["budgets"].remove(self.accounts["budgets"][self.name_index])
                     self.accounts["create_date"].remove(self.accounts["create_date"][self.name_index])                    
                     print("-"*50)
                     
                     print(">>> Account deleted. Returning to main menu...")                     
                     sleep(2.5)                     
                     
                     os.system("cls") if os.name == "nt" else os.system("clear")
                     self.main_menu() 
                     
                 else:
                     os.system("cls") if os.name == "nt" else os.system("clear")
                     self.account_information_operation()  
                 
#| >>> Main else statement:          
             else:
                print("-"*50)
                print("--> The entered value must be between 1-6.Try again.")
                sleep(2)
                os.system("cls") if os.name == "nt" else os.system("clear")
                self.account_information_operation()                 
                                  
       
#---------------------------------Budget Operations Function---------------------------------------#         
    def  budget_operations(self): 
                print ("Budget Operations")
                print("•"*50)
                
                budget = self.accounts["budgets"][self.name_index]
                deposit_or_withdraw = error_block(
f"""The budget in your card: {budget} $ 
1 --- Deposit money
2 --- Withdraw money                
3 --- Back                 

Selection: """, int)
    
  
#| >>> Depositing money input and debug:               
                if deposit_or_withdraw == 1:
                    os.system("cls") if os.name == "nt" else os.system("clear") 
                    print ("Depositing Money")
                    print("•"*50)
                                
                    deposit_money =  error_block(f"Budget : {budget} $ \nEnter the money value  ​you want deposit to budget (Only enter a number, if you want return budget operations menu, type 1): ", int)
                    if deposit_money == 1:
                          print("Returning budget operations menu...")
                          sleep(2)
                          os.system("cls") if os.name == "nt" else os.system("clear") 
                          self.budget_operations()

                    while deposit_money <= 0 or deposit_money> 100000:
                             print("\n--> You can't deposit 0$ or a negative value. And you can deposit max 100.000 $ . Try again.")
                             print("-"*50)
                             deposit_money =  int(input("Enter the money value  ​you want deposit to budget (Only enter a number, if you want return budget operations menu, type 1): "))
                                                 
                    
#| >>> Increasing budget according to the deposit_money input and showing new budget amount: 
                    self.accounts["budgets"][self.name_index] +=  deposit_money
                
                    print(f"\n>>> New budget amount on your account:{self.accounts['budgets'][self.name_index]} $")
                    sleep(2)
                
                    os.system("cls") if os.name == "nt" else os.system("clear")
                    self.budget_operations()
                
#| >>> Withdrawing money input and debug:                
                if deposit_or_withdraw == 2:
                    os.system("cls") if os.name == "nt" else os.system("clear") 
                    print ("Withdrawing  Money")
                    print("•"*50)
                 
                    withdraw_money =  error_block(f"Budget : {budget} $\nEnter the money value  ​you want withdraw from budget (Only enter a number, if you want return budget operations menu, type 1): ", int)
                    if withdraw_money == 1:
                          print("Returning budget operations menu...")
                          sleep(2)
                          os.system("cls") if os.name == "nt" else os.system("clear") 
                          self.budget_operations()

                    while withdraw_money <= 0 or withdraw_money> budget:
                          print("\n--> You can't withdraw 0$ or a negative value. And you can't withdraw more money the amount in  budget. Try again.")
                          print("-"*50)
                          withdraw_money =  int(input("Enter the money value  ​you want withdraw from budget (Only enter a number, if you want return budget operations menu, type 1): "))
                        
                      
                      
#| >>> Decreasing  budget according to the withdraw_money input and showing new budget amount: 
                    self.accounts["budgets"][self.name_index] -=  withdraw_money
                
                    print(f"\n>>> New budget amount on your account:{self.accounts['budgets'][self.name_index]} $")
                    sleep(2)
                
                    os.system("cls") if os.name == "nt" else os.system("clear")
                    self.budget_operations()
                                    
                if deposit_or_withdraw == 3:
                   print("-"*50)
                   print("Returning to account ınformation and account operations field...")
                   
                   sleep(2)
                   os.system("cls") if os.name == "nt" else os.system("clear")
                   self.account_information_operation() 

                else: 
                   print("-"*50)
                   print("--> The entered value must be between 1-3.Try again.")
                   sleep(2)
                   os.system("cls") if os.name == "nt" else os.system("clear")
                   self.budget_operations()

                   
                
#---------------------------------Changing Password Function---------------------------------------#                
    def changing_password(self):
           print ("Changing Password")
           print("•"*50)
           
           print(f">>> Your current password: {self.accounts['passwords'][self.name_index]}") 
           #-->  the expression **self.accounts["password"][self.name index]**,  is accessing to password of account.
           print("•"*50)
           
#| >>>  Random or custom password selection:       
           change_pass = input("Enter your new password (type 'random' for random password): ")
           
           if change_pass == "random" or  change_pass == "Random":    
                  print ("\nRandom password is :")
                  
                  object = RandPass() 
                  change_pass = object.random_password()
          
                  print("(Don't forget your new random password ! )")
                  print ("-"*50)  
         
#| >>> Checking new custom password:         
           else:           
               while len(change_pass) < 8 or " " in change_pass:
                         print("--> Password must be least 8 character and mustn't contain any space. Try again.")
                         print ("-"*50)         
                         change_pass = input("Password: ")
 
#| >>> Saving new password to dictionary:                   
           self.accounts["passwords"][self.name_index] = change_pass
  
           print(">>> New password successfuly saved." )
           print ("-"*50)        
           sleep(2)
            
           os.system("cls") if os.name == "nt" else os.system("clear")
           self.account_information_operation()
   
          
            
#---------------------------------Changing Name Function---------------------------------------#                
    def changing_name(self):
           print ("Changing Account Name")
           print("•"*50)
           
           print(f">>> Your current account name : {self.accounts['names'][self.name_index]}")
           #-->  the expression **self.accounts["names"][self.name index]**,  is accessing to name of account.
           print("•"*50)
           change_name = input("Enter your new account name: ")
           
           
#| >>> Checking new password:           
           while len(change_name) < 2: 
               print ("--> Your new name must be least 2 character. Try again.")
               print ("-"*50)
               change_name = input("Your name: ")
                    
#| >>> Saving new name to dictionary:        
           self.accounts["names"][self.name_index] = change_name
           
           print(">>> New name successfuly saved." )
           print ("-"*50)
           sleep(2)
             
           os.system("cls") if os.name == "nt" else os.system("clear")
           self.account_information_operation()
                    

                                        
#---------------------------------Money Transfer Function---------------------------------------#                                                                                 
    def money_transfer(self):
           print ("Money Transfer")
           print("•"*50)    
           print ("Users: ")
           print ("-"*5)

#| >>> Listing all users:                  
           for i in self.accounts["names"]:                      
                      print(f"~~ {i}")

#| >>> Determining the user and amount of money to be sent also getting the send date:    
           print ("-"*50)                                     
           print(f">>> Budget in Your Card: {self.accounts['budgets'][self.name_index]} $ \n")            
           
           enter_name =  input("Please enter the name of user you want to send money (be careful for spaces): ")               
           money_amount = error_block("\nNow enter the money amount you want to send (only number): " ,int)
           
           current_time = datetime.now()
           send_date = current_time.strftime(r"%d/%m/%Y %H:%M:%S")

#| >>> Confirmation the transaction                       
           confirmation = error_block(f""" 
Confirm the Transaction
--- Sender : {self.accounts["names"][self.name_index]}
--- Receiver : {enter_name}
--- Amount of Money to be Sent : {money_amount} $
--- Send Date : {send_date}

Type 1 for confirm, type 0 for cancel:  """, int)

#| >>> Conditions will be , if transaction was confirmed:
           if confirmation == 1:         
               while money_amount > self.accounts['budgets'][self.name_index]:  #--> Comparing monay amount with budget
                   print("\n--> Amount of money to be sent can't be more from budget. Please enter a suitable value. Or type '0' for cancel the transaction.")
                   print("-"*50)
                   money_amount = error_block("Enter the suitable money amount you want to send (only number): " ,int)
                   
                   if money_amount == 0:
                       print("-"*50)
                       print("Returning to back...")
                       os.system("cls") if os.name == "nt" else os.system("clear")
                       self.account_information_operation()

#| >>> Checking if the name is in the list:                                      
               if enter_name in self.accounts["names"] : 
                       while enter_name == self.accounts["names"][self.name_index]: #--> If user tries send the money to himself, this loop to move in
                           print("-"*50)
                           print("--> You can't send money to yourself. Please try again.")
                           enter_name =  input("\nEnter the name of user you want to send money (be careful for spaces if there is): ")

                       while not enter_name in self.accounts["names"]: #--> When user entered firstly him/herself name, s/he can enter to this condition and if user enters a name there isn't, this while loop will be activated.
                           print(f"\nThere isn't any user named  '{enter_name}'. Try again.")   
                           enter_name =  input("\nEnter the name of user you want to send money (be careful for spaces if there is): ")
                       self.accounts["budgets"][self.name_index] -= money_amount #--> Decreasing current account budget
                       
                       new_name_index = self.accounts["names"].index(enter_name) #--> New name index for acesing the selected user 
                       self.accounts["budgets"][new_name_index] +=  money_amount  #--> Increasing selected user's budget                    
                       
                       
                       print("-"*50)
                       print(f">>> {money_amount} $ sent to {enter_name}. Now budget in your card: {self.accounts['budgets'][self.name_index]} $ ")
                       input("\nClick enter for return to back: ")
                       os.system("cls") if os.name == "nt" else os.system("clear")
                       self.account_information_operation()
                       
#| >>> Checking if the name is not in the list:                                          
               else: 
                   choice = error_block(f"\n--> There isn't any user named  '{enter_name}'. Type 0 for back, type 1 for try again:  " , int)
                   if choice == 1:
                      os.system("cls") if os.name == "nt" else os.system("clear")
                      self.money_transfer()                                           
                   else:
                     os.system("cls") if os.name == "nt" else os.system("clear")                                                                                       
                     self.account_information_operation()           
                                                                                                
#| >>> Condition will be , if transaction wasn't confirmed:                                                            
           else:
                print ("-"*50)
                print("Transaction cancelled, returning to back...")
                sleep(2)
                os.system("cls") if os.name == "nt" else os.system("clear")
                self.account_information_operation()                   
                
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
#| >>> The object of Atm class                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
object = Atm()
while True:  #--> An infinite while loop for run the app regularly
   object.main_menu()
  
  


#|--- made by @dolpsoft  
#|--- GitHub : github.com/dolpsoft
#|--- Twitter : twitter.com/dolpsoft,
#|--- Reach Me : rekld26@gmail.com
