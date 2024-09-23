def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input.lower() == "done":
            break

        try:
            number = float(user_input)  # Allowing for decimal numbers
            numbers.append(number)
        except ValueError:
            print("Error: Please enter a valid number.")

    if numbers:
        maximum = max(numbers)
        minimum = min(numbers)
        print(f"Maximum: {maximum}, Minimum: {minimum}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
