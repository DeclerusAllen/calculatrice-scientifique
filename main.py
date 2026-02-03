def main():
    def sumnumber(number1, number2):
        return number1 + number2

    def get_valid_number(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("invalid input, please enter numeric values.")

    number1 = get_valid_number("enter the first number: ")
    number2 = get_valid_number("enter the second number: ")

    print("the result is: ", sumnumber(number1, number2))

if __name__ == "__main__":
    main()