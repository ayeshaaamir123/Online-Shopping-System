class userInterfaceProduct:
    def __init__(self):
      print('\t-------PRODUCT IN ONLINE SHOP--------')
      print('\t=============================\n')
      p=Order()                                                             #when object of Order class is instantiated all the available products with price and quantity are printed
      print('\n\t--------PLACE YOUR ORDER--------')
      print('YOUR CART IS READY!')
      while True: 
              choice=input('Press \'e\' to exit or ANY KEY to continue: ')
              if choice=='e' or choice=='E':
                  break
              else:
                   try:
                    product=input('Enter PRODUCT NAME to be added in the Cart: ')
                    if len(product)==0:
                        raise ValueError
                    p.AddToCart(product)
                   except ValueError:
                      print('Enter valid name!')
      while True:
        print('************************************')
        print('MENU\n1: Add more items to Cart\n2: Remove items from the cart\n3: Show Items in cart\n4: CheckOut\nPress ANY key to Exit')
        print('************************************')
        self.choice=input('Enter an option: ')
        if self.choice=='1':
            while True:
                  try:
                    product=input('Enter PRODUCT NAME to be added in the Cart:')
                    if len(product)==0:
                        raise ValueError
                    p.AddMoreToCart(product)
                    break 
                  except ValueError:
                      print('Enter valid name!')
        elif self.choice=='2':
           p. removeFromCart()
        elif self.choice=='3':
           print('\t----ITEMS IN CART-----')
           p.printPurchasedProduct()
           p.TotalPrice()
        elif self.choice=='4':
          p.savePurchasedProduct()                                     #saving the Purchased products in a file 
          print('Order placed successfully')
          print('\t----ORDERED ITEMS------')
          p.printPurchasedProduct()
          p.TotalPrice()
          break
        else:
           break
from A1_CS19020_26_5 import  ProductManagement,Product
class Order:
    def __init__(self):
        self.product_cart=[]                                                                                                #Using ManageProduct class in Order class as most of the coding was same 
        self.PM = ProductManagement()
        self.PM.printProduct(self.PM.product_rec)
    def AddToCart(self,product): 
       p = Product()
       while True:
             add_product = self.PM.search(product, self.PM.product_rec)
             pre_product = self.PM.search(product, self.product_cart)
             if add_product == None:                                                     #If the product user want to buy is not present in stock 
                  print('Invalid product entered!!')
                  product=input('Enter product name again!')
             elif add_product != None:
                p.setProductName(self.PM.product_rec[add_product][0])
                while True:
                  try:                                                                                                                      #using try except block to avoid program termination and to put some checks
                     quan = int(input('Enter quantity of product: '))
                     if quan> self.PM.product_rec[add_product][2]:
                        print('SORRY!!,STOCK NOT AVAILABLE IN REQUIRED QUANTITY---')      
                        print('Quantity availabe: ', self.PM.product_rec[add_product][2])
                        return
                     if quan<=0:
                         print('Try Quantity greater than zero!')  
                         raise ValueError
                     if pre_product != None:                                                                              #If the item is already present in the cart then only its quantity is increased
                            self.product_cart[pre_product][2] += quan
                            return
                     else:
                      self.PM.product_rec[add_product][2] -= quan                   
                      p.setPrice(self.PM.product_rec[add_product][1])
                      p.setQuantity(quan)
                      self.product_cart.append(p)
                      return             
                  except ValueError:
                      print('Enter Valid Value!')                           
    def AddMoreToCart(self,add_product):                                         
       pre_product = self.PM.search(add_product, self.product_cart)                      #If user has added  a product in the cart that is already available in the cart
       if pre_product != None:
          print('PRODUCT AVAILABLE ALREADY! ')
          while True:
              try:             
                quan = int(input('Enter quantity of product to be added: '))
                if quan<=0:
                         print('Try Quantity greater than zero!')  
                         raise ValueError
                self.product_cart[pre_product][2] += quan
                self.PM.product_rec[pre_product][2] -= quan
                print('QUANTITY ADDED SUCCESSFULLY!!')
                return
              except ValueError:
                  print('Enter valid value!')
       else:
            self.AddToCart(add_product)                                               #If new product is added
    def removeFromCart(self):
            self.PM.removeProduct(self.product_cart)
            if self.PM.choice=='2':
                rem_product = self.PM.search(self.PM.remove, self.PM.product_rec)            
                self.PM.product_rec[rem_product][2] +=self.PM.amount
    def TotalPrice(self):
        totalPrice=0                                                                                                   #Calculating total price
        for element in self.product_cart:
             totalPrice+=element[1]*element[2]
        self.PM.saveProduct('A1_CS19020_26_9.txt',self.PM.product_rec)    
        print('\tTotal price of your products is:', totalPrice,'Rs/=')
    def printPurchasedProduct(self):
         self.PM.printProduct(self.product_cart)
    def savePurchasedProduct(self):
        self.PM.saveProduct('A1_CS19020_26_10.txt',self.product_cart)

##u1=userInterfaceProduct()

