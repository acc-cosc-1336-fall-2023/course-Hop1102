#
def print_menu():
    print('Menu: ')
    print('1- Get p-distance matrix')
    print('2- Exit')

def main():
    while True:
        print_menu()
        choice = input('Enter your choice: ')
        
        if choice == '1':
            num_strings = int(input('Enter the number of DNA strings: '))
            strings = []
            for i in range(num_strings):
                dna_string = list(input(f'Enter DNA string {i+1} (without spaces): '))
                strings.append(dna_string)

            result = get_p_distance_matrix(strings)
            print('Resulting p distance matrix: ')
            for row in result:
                print(''.join(f'{val:.5f}' for val in row))

        elif choice == '2':
            print('Exiting now. Bye.')
            break

        else:
            print('Invalid') 
