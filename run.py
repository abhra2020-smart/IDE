file = input("Enter file name ")
with open(file, "rb") as f:
    code = f.read()
    exec(code)
