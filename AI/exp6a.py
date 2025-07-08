def img(fourg, threeg):
    def display(gallons, capacity):
        if gallons == 0:
            return "0"  # Empty
        elif gallons == capacity:
            return str(capacity)  # Full (4 or 3)
        elif gallons == 2:
            return "2"  # Goal of 2 gallons
        else:
            return "X"  # Some other amount, unknown

    fourg_display = display(fourg, 4)
    threeg_display = display(threeg, 3)

    print("\n")
    print("|  |      ")
    print("|  |  |  |")
    print("|  |  |  |")
    print(f"({fourg_display}) , ({threeg_display})")
    print("\n")

fourg = 0
threeg = 0

print("Welcome")
count = 10
while count != 0:
    print("Select 1: Fill 4-gallon jug")
    print("Select 2: Fill 3-gallon jug")
    print("Select 3: Empty 4-gallon jug")
    print("Select 4: Empty 3-gallon jug")
    print("Select 5: Pour 3-gallon jug into 4-gallon jug")
    print("Select 6: Pour 4-gallon jug into 3-gallon jug")
    n = int(input("Enter your choice: "))

    if n == 1:
        if fourg == 4:
            print("4-gallon jug is already full")
        else:
            fourg = 4
            print("4-gallon jug filled")
        img(fourg, threeg)

    elif n == 2:
        if threeg == 3:
            print("3-gallon jug is already full")
        else:
            threeg = 3
            print("3-gallon jug filled")
        img(fourg, threeg)

    elif n == 3:
        fourg = 0
        print("4-gallon jug emptied")
        img(fourg, threeg)

    elif n == 4:
        threeg = 0
        print("3-gallon jug emptied")
        img(fourg, threeg)

    elif n == 5:
        transfer = min(threeg, 4 - fourg)
        fourg += transfer
        threeg -= transfer
        print("3-gallon jug poured into 4-gallon jug")
        img(fourg, threeg)

    elif n == 6:
        transfer = min(fourg, 3 - threeg)
        fourg -= transfer
        threeg += transfer
        print("4-gallon jug poured into 3-gallon jug")
        img(fourg, threeg)

    # Check for the win condition in the 4-gallon jug
    if fourg == 2:
        print("Congratulations! You win! There are 2 gallons in the 4-gallon jug.")
        img(fourg, threeg)
        break

    # Check for the goal condition in the 3-gallon jug
    if threeg == 2:
        print("Goal Reached! There are 2 gallons in the 3-gallon jug.")
        img(fourg, threeg)
        break

    count -= 1

# Check if count has reached 0
if count == 0:
    print("Limit reached, you lose! Try again.")
