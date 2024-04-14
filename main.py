
#Make a funtion that prints arrays
def arr_Printer(arr):
    for i in arr:
        print(i.capitalize())

#Start program
while True:
    print("-Theodore's Grocery Organizer-")

    #s_ is for the stock the "store" has
    s_greens = ["onion", "carrot", "leek", "potato", "tomato"]
    s_meats = ["beef", "chicken", "pork", "fish"]
    #Arrays for user selected items, including one for the non existing items in the store
    b_greens = []
    b_meats = []
    b_NA = []
    #Take input from user
    groceries = input("\nHi, what would you like to buy today?\n> ")
    #Separate user input into an array
    list = groceries.lower().split()
    #Check if elements are in stock
    for i in list:
        if i in s_greens:
            b_greens.append(i)
        elif i in s_meats:
            b_meats.append(i)
        else:
            b_NA.append(i)
    print("\nIn the Greens section we have:\n")
    arr_Printer(b_greens)
    print("\nIn the Meats section we have:\n")
    arr_Printer(b_meats)
    print("\nThis store does not sell:\n")
    arr_Printer(b_NA)
