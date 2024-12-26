def Display_items(items):
    print('Menu List:',items)

def Add_Items(items):
    newitem = input('Enter the Item to be Added :')
    items.append(newitem)
    print('Added List:',items)

def Update_Items(items):
    exist_item=input('Enter the item:')
    new_item=input('Enter New Item:')
    food = items.index(exist_item)
    items[food]=new_item
    print('Updated_Menu:',items)

def Delete_Items(items):
    rem=input('Enter the Item to Remove:')
    items.remove(rem)
    print('List After removal:',items)


def main():
    menu=['Idly','Dosa','Briyani','Shawarma']
    print('1.Display Item')
    print('2.Add item')
    print('3.Update item')
    print('4.Delete item')

    options=int(input('Enter Number:'))
    if(options==1):
        Display_items(menu)
    elif(options==2):
        Add_Items(menu)
    elif(options==3):
        Update_Items(menu)
    elif(options==4):
        Delete_Items(menu)
    else:
        print('invalid Number')

if __name__ == "__main__":
    main()

