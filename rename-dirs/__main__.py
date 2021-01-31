import os
path = input("enter full directory path: ")
files = os.listdir(path)
mainDirectorylist = list()
counter = 0

for i in files:
    if i.startswith(".") == False:
        mainDirectorylist.append(i)
        filename = i.lower()
        if " " in filename:
            filename = filename.replace(" ", "_")
        if "-" in filename:
            filename = filename.replace("-", "_")
        confirmation = input(
            f"\n{mainDirectorylist[counter]} => {filename} (Y/n): ")
        if confirmation != "n" or "N":
            os.rename(
                f"{path}/{mainDirectorylist[counter]}", f"{path}/{filename}")
        else:
            continue
        counter += 1

print("Aight, I'm done!")

"""
# sample input: /Users/rachitgupta/Documents
"""
