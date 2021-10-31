from A1_CS19020_26_2 import AccountWork
class ManageAccount(AccountWork): 
    def __init__(self,filename):
        super().__init__(filename)  #loads admin list
    def changeDetails(self):
        choice=input('ENTER USERNAME OF THE ACCOUNT YOU WANT TO CHANGE:')
        if AccountWork.checkUsername(choice.capitalize(),self.account_reclist)==True:
           index=AccountWork.searchAccount(choice.capitalize(),self.account_reclist)[1]
           acc=AccountWork.searchAccount(choice.capitalize(),self.account_reclist)[0]
           print('\nWOULD YOU LIKE TO MAKE CHANGES TO:\n1.USERNAME\n2.PASSWORD\n3.ADDRESS:')
           select=input('ENTER AN OPTION: ')
           if select=='1':
             while True:
               try: 
                   user=input('ENTER NEW USERNAME:')
                   if len(user)==0:
                        raise ValueError
                   if AccountWork.checkUsername(user.capitalize(),self.account_reclist)==False:
                      acc.setUsername(user.capitalize())
                      break
                   else:
                     print('Username already in use!')
                     while True:
                      try:
                           option=input('Would you like to try again:')
                           if option.lower()=='no':
                              return False
                           elif option.lower()=='yes':
                                print('\nTRY AGAIN:')
                                break
                           raise ValueError
                      except ValueError:
                          print('INVALID ENTRY!')
               except ValueError:
                          print('INVALID ENTRY!')  
           elif select=='2':
               while True:
                   try:
                     pw=input('ENTER NEW PASSWORD:')
                     if len(pw)==0:
                        raise ValueError
                     acc.setPassword(pw)
                     break
                   except ValueError:
                          print('INVALID ENTRY!')   
           elif select=='3':
                while True:
                  try:
                     address=input('ENTER NEW ADDRESS:')
                     if len(address)==0:
                        raise ValueError
                     acc.setAddress(address)
                     break
                  except ValueError:
                          print('INVALID ENTRY!')  
           else:
            print('Invalid Entry!')
            return
           print ('NEW DETAILS:\n================')
           acc.PrintAccountDetails()
           print('\n')
           self.account_reclist[index]=acc
           self.save_updateAccount('A1_CS19020_26_8.txt',self.account_reclist)
        else:
            print('Username does not exist!')
    def removeAccount(self):
        while True:            
           username=input('ENTER USERNAME OF THE ACCOUNT YOU WANT TO REMOVE:')
           if AccountWork.checkUsername(username.capitalize(),self.account_reclist)==False:
             print('Account does not exist!')
             while True:
                 select=input('Would you like to try again?')
                 if select.lower()=='yes':
                     print('TRY AGAIN:')
                     break
                 elif select.lower()=='no':
                     return
                 else:
                     print('INVALID ENTRY!')                  
           else:
             index=AccountWork.searchAccount(username.capitalize(),self.account_reclist)[1]
             self.account_reclist.pop(index)
             self.save_updateAccount('A1_CS19020_26_8.txt',self.account_reclist)
             print('ACCOUNT SUCCESSFULLY REMOVED!')
             return
    def viewDetails(self,user):                                              #=====================overriding viewDetails  from AccountWork
        choice=input('\nPress \'1\' to view your own account OR \'2\' to view all accounts:')
        if choice=='1':
            AccountWork.viewDetails(self,user)
        elif choice=='2':
            index=1
            for i in self.account_reclist:
                print('==================\n')
                print('ACCOUNT '+str(index)+':')
                i.PrintAccountDetails()
                index+=1
        else:
            print('INVALID ENTRY')
class Adminmenu:
    def __init__(self):
        self.account=ManageAccount('A1_CS19020_26_8.txt')
        self.signingprocedure_a()      
    def signingprocedure_a(self):
        print('\nWELCOME ADMIN!\nPLEASE SIGN IN BEFORE CONTINUING:')
        if self.account.login():
            print('WELCOME!')            
    def menu(self):
       while True:
         print('************************************')
         print('MENU:\n1.ADD AN ACCOUNT\n2.CHANGE ACCOUNT INFORMATION\n3.VIEW ACCOUNT INFORMATION\n4.REMOVE ACCOUNT\n\'e\' to exist:')
         print('************************************')
         select=input('SELECT AN OPTION: ')
         if select=='1':
             if self.account.signUp('A1_CS19020_26_8.txt'):
                print('ACCOUNT SUCCESSFULLY ADDED') 
             else:
                 ('ACCOUNT COULD NOT BE MADE')
         
         elif select=='2':
             self.account.changeDetails()
         elif select=='3':
            self.account.viewDetails(self.account.userlogin)
         elif select=='4':
             self.account.removeAccount()
         elif select=='e':
             print('Closing Admin Account Management......')
             break
         else:
            print('Invalid entry!')

##a1=Adminmenu()
##a1.menu()
