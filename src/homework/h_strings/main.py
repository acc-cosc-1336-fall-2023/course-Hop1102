#
from strings import get_hamming_distance, get_dna_complement

def display_menu():
    print("Menu:")
    print("1-Hamming Distance")
    print("2-DNA complement")
    print("3-Exit")

def option_1():
    dna1 = input("Enter the first DNA string: ")
    dna2 = input("Enter the second DNA string: ")
    distance = get_hamming_distance(dna1, dna2)
    print(f"The hamming distance between '{dna1}' and '{dna2}' is: {distance}")

def option_2():
    dna = input("Enter the DNA string: ")
    complement = get_dna_complement(dna)
    print(f"The complement of '{dna}' is: {complement}")

def main():
    while True: 
        display_menu()
        option = input("enter your choice(1, 2 or 3): ")

        if option == '1':
            option_1()
        elif option == '2':
            option_2()
        elif option == '3':
            break
        else:
            print("Invalid input")
        


