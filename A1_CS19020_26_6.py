from A1_CS19020_26_2 import FileManager
from datetime import datetime
class ShoppingHistory:
    def __init__(self,user='None'):
          self.user_name=user
          self.loadCart()
          self.loadHistory()
    def loadHistory(self):
         self.history_rec=FileManager.readFromFile(self,'A1_CS19020_26_11.txt')
    def checkUser(self):
         for i in range(0, len(self.history_rec)):                                                #To check if the user is new or he had from online shop before
            n=self.user_name.capitalize()
            if n ==self.history_rec[i][0]:
               return self.history_rec[i],i
    def loadCart(self):
         self.cart=FileManager.readFromFile(self,'A1_CS19020_26_10.txt')          
    def checkout(self):                                                                            #To append information of cart and user to history
        now=datetime.now()
        dt_string=now.strftime('%d/%m/%Y %H:%M:%S')               #appending date and time 
        check=self.checkUser()
        if check!=None:
            cartwithtime=[]
            cartwithtime.append(self.cart)
            cartwithtime.append(dt_string)
            self.history_rec[self.checkUser()[1]][1].append(cartwithtime)
        elif check==None:
            new=[]
            new.append(self.user_name.capitalize())
            cartwithtime=[]
            cartwithtime.append(self.cart)
            cartwithtime.append(dt_string)
            new.append([cartwithtime])
            self.history_rec.append(new)
        FileManager.saveToFile(self,'A1_CS19020_26_11.txt',self.history_rec)
        
    def viewShoppingHistory(self,lst):
          print('\tUserName :',lst[0])
          temp='{name:20}{quantity:18}{price:23}'
          print('PRODUCTNAME        QUANTITY            PRICE(for 1 product)       ')
          print('-----------        --------            -----       \n')
          
          for history in lst[1]:
              print('DATE AND TIME:',history[1])
              for cart in history[0]:
                   strg=temp.format(name=cart[0],quantity=str(cart[2]),price=str(cart[1])+'Rs\=')
                   print(strg)
              print('\n')          
