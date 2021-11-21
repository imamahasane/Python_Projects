class Library:
    def __init__(self, blist, bname):
        self.bkList = blist
        self.bkName = bname
        self.storeDict = {}
        
    def show_book(self):
        print("My library has these books right now: {self.bname}")
        for book in self.bkList:
            print(book)
        
    
    def credit_book(self, user, book):
        if book in self.bkList.keys():
            self.storeDict.update({book:user})
            print("Book store has updated. You can take the book now")
            
        else:
            print("Book is already being used by {self.storeDict[book]}")
    
    
    def add_book(self, book):
        self.bkList.append(book)
        print("Book has been added to the book blist")
    
    
    def return_book(self, book):
        self.storeDict.pop(book)
    
    
if __name__ == "__main__":
    main_library = Library(["Himu somogro", "Python", "ML", "ML_Python", "7th havit of life"])
    
    while(True):
        print("Welcome to the Ahasan's library.")
        print("=============================")
        print("1. Show Book List")
        print("2. Credit The Book")
        print("3. Add The Book")
        print("4. Return The Book")
        print("=============================")
        
        user_input = input("Please Enter Your Choice to continue: ")
        if user_input not in ['1', '2', '3', '4']:
            print("=============================")
            print("Your input is wrong. Please enter a valid option.")
            print("=============================")
            continue
        
        else:
            user_input = int(user_input)
        
        
        if user_input == 1:
            main_library.show_book()
            
        elif user_input == 2:
            book = input("Enter the book name, you want to credit: ")
            user = input("Enter your name: ")
            main_library.credit_book(user, book)
        
        elif user_input == 3:
            book = input("Enter the book name, you want to add: ")
            main_library.add_book(book)
        
        elif user_input == 4:
            book = input("Enter the book name, you want to return: ")
            main_library.return_book(book)
        
        else:
            print("Worng answer. Please try again.")
        
        user_input2 = None
        while (user_input2 != "c"  and user_input2 != "q"):
            user_input2 = input("Press 'q' to quit or 'c' to continue: \n")
            
            if user_input2 == "q":
                exit()
                
            elif user_input2 == "c":
                continue
            
            else:
                print("Invalid answer.")
                continue
            
            
        
        
        