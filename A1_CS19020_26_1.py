from A1_CS19020_26_2 import Usermenu
from A1_CS19020_26_3 import Adminmenu
from A1_CS19020_26_5 import ManagerInterfaceProduct
from  A1_CS19020_26_4 import userInterfaceProduct
from A1_CS19020_26_6 import ShoppingHistory
class Interface:                                                          #Main Interface from which different menus are accessed 
    def __init__(self):
         print('\t=============================')
         print('\t              WELCOME TO ONLINE SHOP')
         print('\t=============================')
         while True:
            Interface.displayMainMenu()
            choice=input('Enter option number:')
            if choice=='1':
                Interface.UserMenu()
            elif choice=='2':
                Interface.ManagerMenu()
            else:
                print('Closing ONLINE SHOP........')
                print('\t============= THANK YOU FOR SHOPPING :) =============')
                break
    def displayMainMenu():
        print('\nMAIN MENU:')
        print('***************************')
        print('1. UserSection')
        print('2. AdminSection')
        print('Press anyother key to exit')
        print('***************************')

    def ManagerEditMenu(Ad):
      while True:
        print('=============================')
        print('\nADMIN EDIT MENU:')
        print('=============================')
        print('1. Edit Accounts\n2. Edit Products\n3. Display Shopping History\nPress any key to exit')
        print('=============================')
        choice=input()
        if choice=='1':
              print('\t--------ADMIN ACCOUNT MANAGEMENT--------')
              Ad.menu()
        elif choice=='2':
             ManagerInterfaceProduct()
        elif choice=='3':
             print('\t--------HISTORY DETAILS--------')
             print('***************************************************')
             h=ShoppingHistory()
             for user in h.history_rec:
                 h.viewShoppingHistory(user)
                 print('=============================\n')
        else:
            print('Closing Admin Management......')
            return
    def UserMenu():
        print('=============================')
        s=Usermenu()
        p=userInterfaceProduct()
        h=ShoppingHistory(s.name)
        if p.choice=='4':
            h.checkout()
        while True:
              print('Do you want to see the history details?',end='')
              opt=input()
              if opt.lower()=='no':
                 print('Have a nice day')
                 print('=============================')
                 return
              elif opt.lower()=='yes':
                check=h.checkUser()                           #checking if the user is new or he had from online shop before
                if check!=None:
                      h.viewShoppingHistory( h.checkUser()[0])
                      return
                elif  check==None:                     #if the user is new and has done no shopping then showing no history founded
                  print('No history founded')
                  return
              else:
                   print('Enter valid value\nEnter   YES   or   No  !  ')                 
    def ManagerMenu():
        print('=============================')
        print('\t---- Admin Department------')
        Ad=Adminmenu()
        Interface.ManagerEditMenu(Ad)

i1=Interface()      
