try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print("sample.txt not found. Please run the write program first.")
