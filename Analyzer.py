##Analyzer

import numpy as np

arr = None

while True:
    print("\n=========Numpy Menu======")
    print("1. Create Array")
    print("2. Add Number")
    print("3. Multiply Array")
    print("4. Sort Array")
    print("5. Find Sum and Average")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter size array: "))
        elements = list(map(int , input("Enter elements: ").split()))
        arr = np.array(elements)
        print("Array:", arr)

    elif choice == 2:
        if arr is None:
            print("Create array first!")
        else:
            num = int(input("enter number to add: "))
            print("Result:", arr + num)

    elif choice == 3:
        if arr is None:
            print("Create array first!")
        else:
            num = int(input("Enter number to multiply: "))
            print("Rsult:", arr * num)

    elif choice == 4:
        if arr is None:
            print("create array first!")
        else:
            print("Sorted array:", np.sort(arr))

    elif choice == 5:
        if arr is None:
            print("Create array first!")
        else:
            print("Sum =", np.sum(arr))
            print("Average =", np.mean(arr))

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

