#
import dictionary 

#def print_menu():
    #print('Menu: ')
    #print('1- Get p-distance matrix')
    #print('2- Exit')
#def main():
    #while True:
       # print_menu()
        #choice = input('Enter your choice: ')
        #if choice == '1':
            #num_strings = int(input('Enter the number of DNA strings: '))
           # strings = []
           # for i in range(num_strings):
           #     dna_string = list(input(f'Enter DNA string {i+1} (without spaces): '))
           #     strings.append(dna_string)
            #result = get_p_distance_matrix(strings)
           # print('Resulting p distance matrix: ')
           # for row in result:
           #     print(''.join(f'{val:.5f}' for val in row))
     #   elif choice == '2':
         #   print('Exiting now. Bye.')
         #   break
       # else:
       #     print('Invalid') 

def display_menu():
    print('Inventory Menu')
    print('1- Add or Update Item')
    print('2- Delete Item')
    print('3- Exit')

def add_update_item():
    widget_name = input("Enter the widget name: ")
    quantity = int(input("Enter the quantity: "))
    dictionary.add_inventory(inventory, widget_name, quantity)
    print(f"{widget_name} with quantity {quantity} was added/updated.")

def deleted_item():
    widget_name = input("Enter the widget name to delete: ")
    result = dictionary.remove_inventory_widget(inventory, widget_name)
    print (result)
    
inventory = {} 

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_update_item()
    elif choice == '2':
        deleted_item()
    elif choice == '3':
        print("Exiting the program")
        break
    else:
        print("Invalid entry") 



