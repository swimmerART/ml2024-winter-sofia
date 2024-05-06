class InputList:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def find_index(self, x):
        try:
            index = self.numbers.index(x) + 1
        except ValueError:
            index = -1
        return index


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
