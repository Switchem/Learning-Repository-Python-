import random

MAX_LINES = 3  # <-- in all caps because this is a constant value, something that's not going to change
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # ^ the reason this will work because if they bet on one line, then you're going to go up to one line but not include it. meaning line will be equal to zero
        symbol = columns[0][line]
        # ^ reason for using columns zero is because we have all of the columns, not all of the rows. it's a bit complicated. So you need to look at the first column because that's where the first symbols are always going to be for each row and then get whatever line were on.
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
                # ^ reason for breaking is if we found one of the symbols is not equal to the previous symbol or equal to all of the symbols that should be in the row, then we just break out of the fault.
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # when using items it gives you a key and value associated with a dictionary
        for _ in range(symbol_count):
            # ^ _(underscore) = an anonymous variable, so whenever you loop through something but you don't actually care abo the counter that iteration value, then you just put an underscore so you don't have an unused variable
            all_symbols.append(symbol)

    # ^ This is a nested list, which each of these nested lists id going to represent the values in our call
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # ^ you want a copy or else the variables are going to mess up the data

        for _ in range(rows):
            # ^ loop through the number of values needed to generate, which is equal to the number of rows in the slot machine
            value = random.choice(current_symbols)
            # ^ this value right here is random not choice and it's from the current_symbols variable, which picks a random value
            current_symbols.remove(value)
            # ^ current_symbols, so it doesn't pick it again
            column.append(value)
            # ^ we add the value to the column

        columns.append(column)
        # ^ this adds the column to the column list

    return columns
# ^ this whole lines of code is picking a random value for each row in the columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            # ^ what this does is give the index(0, 1, 2, 3) aswell as the item
            if i != len(columns) - 1:
                # ^ reason for checking if I is not equal to the line of columns - 1 is the maximum index there is to access an element in the columns list
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
# For every row I looped through every column, and for every column you only print the current row that you're on


def deposit():
    # a function to define a deposit
    while True:
        # it's a while loop so it's going to continue until it breaks
        amount = input("What would you like to deposit? $")
        # ^ this is the amount you want to deposit
        if amount.isdigit():
            # ^ where you enter you deposit or Money, and if it is a digit it's going to convert to a integer
            amount = int(amount)
            if amount > 0:
                # ^ this checks if the number is greater than 0, which would be a vaild amount
                break  # <-- this 'break' breaks the while loop the continue to the next line of code, if the value is greater than cero
            else:
                print("Amount must be greater than 0.")
        else:
            # if you did not enter a number this will tell prompt you to enter a number, this while continue until we get a number
            print("Please enter a number.")

    return amount  # <-- return the amount or you can just use it later on


def get_number_of_lines():
    while True:
        # it's a while loop so it's going to continue until it breaks
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # ^ added the Max lines inside of the string, converting it into a string because if you add two strings together, they get squished together. But if it was a number there would be a exception in the program
        if lines.isdigit():
            # ^ where you enter you deposit or Money, and if it is a digit it's going to convert to a integer
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                # ^ I want to check if a value is inbetween two values, meaning if my lines is greater than or equal to one and is less tahn or equal to the maximum lines, then I'm okay, I can break.
                break  # <-- this 'break' breaks the while loop the continue to the next line of code, if the value is greater than cero
            else:
                print("Enter a vaild number of lines.")
        else:
            # if you did not enter a number this will tell prompt you to enter a number, this while continue until we get a number
            print("Please enter a number.")

    return lines  # <-- return the amount or you can just use it later on


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
                # ^ putting f before the string and use curly braces to change any variable to a string automatically IF it can be converted
        else:
            print("Please enter number.")
    return amount


def spin(balence):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet >= balence:
            print(
                f"you do not have enought to bet that amount, your current balence is ${balence}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    # ^ so what this is it's called the splat operator or the unpack operator, and it's going to pass every single line from this winning line's to this print function.
    return winnings - total_bet


def main():
    balence = deposit()
    while True:
        print(f"Current balence is ${balence}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balence += spin(balence)

    print(f"You left with ${balence}")


main()
