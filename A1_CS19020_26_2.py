class FileManager:
    def readFromFile(self, filename=''):
        rec_lst=[]
        with open (filename,'a+') as f:
            f.seek(0)
            for record in f:
                rec=eval(record.strip())
                rec_lst+=[rec]
        return rec_lst  
    def saveToFile(self,filename,reclst):
        with open(filename, 'w+')as f:
            for record in reclst:
                f.write(str(record)+'\n')        
class Account:
    def __init__(self):
        self.account_record=[None,None,None]
    def setUsername(self,username):
        self.account_record[0]=username
    def setPassword(self,password):
        self.account_record[1]=password
    def setAddress(self,address):
        self.account_record[2]=address
    def PrintAccountDetails(self):
        print('USERNAME:',self.account_record[0],'\nPASSWORD:',self.account_record[1],'\nADDRESS:',self.account_record[2])
    def __str__(self):
        return str(self.account_record)
    
class AccountWork(FileManager):
    def __init__(self,filename):
        self.loadList(filename)
    def loadList(self,filename):    
        self.account_reclist=[]
        filelist=self.readFromFile(filename)
        for record in filelist:
            rec=Account()
            rec.setUsername(record[0])
            rec.setPassword(record[1])
            rec.setAddress(record[2])
            self.account_reclist.append(rec)
    @staticmethod
    def searchAccount(username,account_reclist):   #looks for the account in the account list then returns it + its index
        index=0
        for i in account_reclist:
            if i.account_record[0]==username:
                return i,index
            index+=1         
    @staticmethod            
    def checkUsername(username,account_reclist):    #checks whether username exists in the account list
        user_list=[]
        for i in account_reclist:
            user_list.append(i.account_record[0])
        if username in user_list:
              return True
        else:
            return False 
    @staticmethod
    def checkPassword(username,password,account_reclist):     #checks whether password matches username
        for i in account_reclist:
            if username in i.account_record and password in i.account_record:
                return True
    def viewDetails(self,user):                               
        acc=AccountWork.searchAccount(user,self.account_reclist)[0]
        print('\nACCOUNT INFORMATION:\n===================')
        acc.PrintAccountDetails()           
    def login(self):   
        while True:
            user=input('ENTER USERNAME:')
            self.userlogin=user.capitalize()
            if AccountWork.checkUsername(self.userlogin,self.account_reclist):
                while True:                    
                  pw=input('ENTER PASSWORD:')
                  if AccountWork.checkPassword(self.userlogin,pw,self.account_reclist):                    
                      return True
                  else:
                      print('Incorrect Password!')
                      while True:
                        try:
                           select=input('Would you like to try again(Enter  YES  or  No): ')
                           if select.lower()=='no':
                              return False
                           elif select.lower()=='yes':
                                print('TRY AGAIN:')
                                break
                           raise ValueError
                        except ValueError:
                          print('INVALID ENTRY!')
            else:
                print('Username does not exist!')
                while True:
                  try:
                     select=input('Would you like to try again (Enter  YES  or  No): ')
                     if select.lower()=='no':
                              return False
                     elif select.lower()=='yes':
                                print('TRY AGAIN:')
                                break
                     raise ValueError
                  except ValueError:
                          print('INVALID ENTRY!')                   
    def signUp(self,filename):
        rec=Account()
        while True:
            try:
              user=input('ENTER USERNAME:')
              if len(user)==0:
                        raise ValueError
              self.usersignup=user.capitalize()
              if self.checkUsername(self.usersignup,self.account_reclist)==False:
                rec.setUsername(self.usersignup)
                pw=input('ENTER PASSWORD:')
                if len(pw)==0:
                        raise ValueError
                rec.setPassword(pw)
                address=input('ENTER ADDRESS:')
                if len(address)==0:
                        raise ValueError
                rec.setAddress(address)
                self.account_reclist.append(rec)
                self.save_updateAccount(filename,self.account_reclist)             
                return True
              else:
                print('Username already in use!')
                while True:
                  try:
                    select=input('Would you like to SIGN UP again (Enter  YES  or  No ): ')
                    if select.lower()=='no':
                              return False
                    elif select.lower()=='yes':
                                print('TRY AGAIN:')
                                break
                    raise ValueError
                  except ValueError:
                          print('INVALID ENTRY!')
            except ValueError:
                          print('INVALID ENTRY!')
    def save_updateAccount(self,filename,accountlist):       #updates list
        FileManager.saveToFile(self,filename,accountlist)

class Usermenu:
    def __init__(self):
        self.account=AccountWork('A1_CS19020_26_7.txt')
        self.signingprocedure_u()
    def signingprocedure_u(self):
        print ('\nWELCOME USER!\nBefore continuing please select from the following options:')
        while True:
           choice=input('\nPress \'1\' to SIGN IN or \'2\' to SIGN UP:')
           if choice=='1':             
              if self.account.login():
                 self.name=self.account.userlogin
                 print ('Login Successfull!')
                 while True:
                    option=input('WOULD YOU LIKE TO VIEW YOUR ACCOUNT DETAILS?')
                    if option.lower()=='yes':
                       self.account.viewDetails(self.account.userlogin)
                       print('=======================\n')
                       break
                    elif option.lower()=='no':
                        return
                    else:
                        print('INVALID ENTRY')
                 break
              else:
                print('Login Unsuccessful!')
            
           elif choice=='2':
             if self.account.signUp('A1_CS19020_26_7.txt'):
               self.name=self.account.usersignup
               print ('Account Successfully Created!!')
               while True:
                 option=input('WOULD YOU LIKE TO VIEW YOUR ACCOUNT DETAILS?')
                 if option.lower()=='yes':
                   self.account.viewDetails(self.account.usersignup)
                   print('=======================\n')
                   break
                 elif option.lower()=='no':
                     return
                 else:
                   print('INVALID ENTRY')
               break
             else:
               print('Account couldn\'t be created :(')
           else: 
             print ('Invalid entry!')   
#u1=Usermenu()        
