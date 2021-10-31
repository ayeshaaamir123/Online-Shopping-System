from A1_CS19020_26_2 import FileManager
class ManagerInterfaceProduct:
    def __init__(self):
      PMM= ProductManagement()                                                        #object of class ProductManagement is instantiated (composition)
      print('\t--------ADMIN PRODUCT MANAGEMENT--------')
      while True:
        print('************************************')
        print('MENU:\n1: Add products to stock\n2:Remove items from stock\n3:Show stock available\n4:UpdateStock\nPress ANY key to Exit ')
        print('************************************')
        choice=input('Enter an option: ')
        if choice=='1':
           while True:
              choice=input('Press \'e\' to exit or ANY KEY to continue ----ADDING PRODUCTS TO STOCK----: ')
              if choice=='e' or choice=='E':
                  break
              else:
                  try:
                    product=input('Enter product name')
                    if len(product)==0:
                        raise ValueError
                    PMM.addProduct(product)
                  except ValueError:
                      print('Enter valid name')     
        elif choice=='2':
              PMM. removeProduct (PMM.product_rec )
        elif choice=='3':
            print('\t--------PRODUCT DETAILS--------')
            PMM.printProduct(PMM.product_rec)
        elif choice=='4':
          PMM. saveProduct('A1_CS19020_26_9.txt',PMM.product_rec) #updates the changes made in the productlist
          print('STOCK UPDATED SUCCESSFULLY!-----')
        else:
            print('Closing Admin Product Management......') 
            break
class Product(list):
    def setProductName(self,product):
         self.append(product)
    def setPrice(self,price):
        self.append(price)                                                                                      #Product(class) used in Product Management class to set and print products easily
    def setQuantity(self,quantity):
        self.append(quantity)
    def PrintProductWithPrice(self,item):
        temp='{name:20}{quantity:18}{price:23}\n'
        dis= temp.format(name=item[0],quantity=str(item[2]),price=(str(item[1])+'Rs/='))
        return dis      
class ProductManagement:
    def __init__(self):
        self.LoadProductList('A1_CS19020_26_9.txt')
    @staticmethod                 
    def search(name,product_rec):                                                    #making search() a static method to make it handy to be use in the code where needed
        n=name.capitalize()
        for i in range(0, len(product_rec)):
            if n == product_rec[i][0]:
                return i
    def addProduct(self,product):
             pre_product=ProductManagement.search(product, self.product_rec)
             if pre_product!=None:
               print('PRODUCT available already enter amount to increase the quantity of product')
               while True:
                   try:                                                                                                                           #using try except block to avoid program termination and to put some checks
                       quan=int(input('Enter quantity of product to be added: '))
                       if quan<=0:
                           print('Try Quantity greater than zero!')
                           raise ValueError
                       self.product_rec[pre_product][2]+=quan
                       print('QUANTITY ADDED SUCCESSFULLY')                               
                       break
                   except ValueError:
                           print('Enter an integer value!')
             else:
              p=Product()
              p.setProductName(product.capitalize())
              while True:
                try:
                 print('Enter price of one(1)',product.capitalize(),': ',end='')   
                 price=float(input())
                 if price<=0:
                     raise ValueError
                 p.setPrice(price)
                 break
                except ValueError:
                   print('Enter a valid value!')
              while True:
                try:
                      print('Enter quantity of',product,': ',end='')
                      quantity=int(input())
                      if quantity<=0:
                        print('Try Quantity greater than zero!')  
                        raise ValueError
                      p.setQuantity(quantity)
                      self.product_rec.append(p)
                      break
                except:
                    print('Enter an valid value!')
    def removeProduct(self, lst):
      while True:
          try:
            self.remove=input('Enter product name of product to be removed: ')
            if len(self.remove)==0:
                raise ValueError
            product_remove=ProductManagement.search(self.remove,lst)
            if product_remove!=None:
                print('You want to remove whole product or some quantity of it?')
                self.choice=input('Press 1 for removing whole product and 2 for changing the quantity only')
                if self.choice=='1':
                    lst.pop(product_remove)
                    print('PRODUCT REMOVED SUCCESSFULLY')     
                    break
                elif self.choice=='2':
                   while True:
                     try:
                       self.amount=int(input('Enter quantity of product to be removed'))    
                       if self.amount<=0:
                          print('Try Quantity greater than zero!')                                                            #If the value of quantity entered is less than or equal to zero then it should ask to enter quantity again  
                          raise ValueError
                       if lst[product_remove][2]<self.amount:
                           print('Quantity Entered is greater than previously available quantity')
                           raise ValueError
                       lst[product_remove][2]-=self.amount
                       print('QUANTITY REMOVED SUCCESSFULLY')     
                       return
                     except ValueError:
                         print('Enter valid Amount!!')
                else:
                    print('Invalid ENTRY!!')
            else:
                 print('Invalid product entered!!!\nPRODUCT NOT PRESENT!')                                #If product not present in stock then it show this error statement  
                 raise ValueError()
          except ValueError:
               print('Enter valid Product!')
    def saveProduct(self,filename,lst):
       FileManager.saveToFile(self,filename,lst)
    def printProduct(self,lst):
        strg='PRODUCTNAME        QUANTITY            PRICE(for 1 product)       \n'
        for element in lst:
              strg+=element.PrintProductWithPrice(element)
        print(strg)
    def LoadProductList(self,filename):
            self.product_rec=[]
            filelist=FileManager.readFromFile(self,filename)
            for product_list in filelist:
              p = Product()
              p.setProductName(product_list[0])
              p.setPrice(product_list[1])
              p.setQuantity(product_list[2])
              self.product_rec.append(p)
            return self.product_rec
##m1= ManagerInterfaceProduct()
