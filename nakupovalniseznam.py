
shopping_list = []

while True:
    answer = raw_input("Do you wish to add items to your cart? yes or no: ")

    if answer == "yes":
        item = raw_input("add items: ")
        shopping_list.append(item)

    elif answer == "no":
         break


print "Your shopping list for today is: ", shopping_list

