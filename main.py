code = input("""Enter code\n""")
file = input("Enter your file\n")

with open(file, "a") as f:
    f.write(code)
    f.write("\n")
