from module5_mod import InputList 

def main():
    N = int(input("Please enter the length of the list: "))
    if N <= 0:
        print("The number should be a positive integer.")
        return

    num_list = InputList()

    print("Enter", N, "numbers:")
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        num_list.add_number(num)

    X = int(input("Search Number: "))

    index = num_list.find_index(X)
    print("Result index:", index)


if __name__ == "__main__":
    main()
