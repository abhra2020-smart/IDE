import random

username = input("What is your name?\n")
timesTheLoopWent = 0
whoWillBeFirst = random.randint(0, 1)
symbolAssigner = random.randint(0, 1)
symbol: str
cell = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]


# def whoWillGoFirst():
#     if whoWillBeFirst == 0:
#         print(f"{username} will go first")
#     elif whoWillBeFirst == 1:
#         print("I am first")


def assignSymbol():
    global symbol
    if symbolAssigner == 0:
        print("Your symbol is X")
        symbol = "X"
    else:
        print("Your symbol is O")
        symbol = "O"


print(f"Let's play some Tic Tac Toe, {username}")
# whoWillGoFirst()
print(f"{username} will go first")
assignSymbol()
print(f"{symbol} selected")
while not timesTheLoopWent == 9:
    coordinate = int(input("Enter the coordinate of your symbol:\n"))
    try:
        cell[coordinate-1] = symbol
        timesTheLoopWent += 1
        print(str(cell))
    except IndexError:
        print("Coordinate not in range.\nTry again.")
