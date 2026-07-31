program_name = "quick sort"

with open("myown.py", "r") as file:
    found = False

    for line in file:

        if line.strip() == f"#{program_name}":
            found = True

        elif found and line.startswith("#"):
            break

        if found:
            print(line, end="")