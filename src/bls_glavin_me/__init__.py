import random

version = '0.1'

def generate_random_number(storage):
    random_number = random.randint(100000, 999999)
    storage.add(random_number)
    return random_number


def verification_number(storage, input_number):
    if input_number in storage:
        storage.clear()
        return True
    return False


def generated_number_manager(storage):
    random_number = generate_random_number(storage)
    log("", f"Generated number: {random_number}")


def verfication_manager(storage):
    if not storage:
        log("", "No number has been generated yet. Please generate a number first.")
        return

    try:
        user_input = int(input("Enter the 6-digit number to verify: "))
        if verification_number(storage, user_input):
            print("Verification successful! The list of numbers is cleared.")
        else:
            log("","Verification failed. Number not found.")
    except ValueError:
        log("", "Invalid input. Please enter a 6-digit number.")


def exit_program():
    log("", "Exiting the program. Goodbye!")
    return False

def log(tag, message):
    if not tag:
        tag = "System"
    print(f'[{tag}] {message}')



def main():
    generated_numbers = set()
    is_running = True

    log('', f'Current version: {version}')


    while is_running:
        print("\nChoose an option:")
        print("1. Generate a 6-digit random number")
        print("2. Verify a number")
        print("3. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                generated_number_manager(generated_numbers)
            case "2":
                verfication_manager(generated_numbers)
            case "3":
                is_running = exit_program()
            case _:
                log("", "Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
