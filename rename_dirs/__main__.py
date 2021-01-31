def main():
    import os
    path = input("enter full directory path: ")
    files = os.listdir(path)
    mainDirectorylist = list()

    for i in files:
        if i.startswith(".") == False:
            mainDirectorylist.append(i)
            filename = i.lower()
            if " " in filename:
                filename = filename.replace(" ", "_")
            if "-" in filename:
                filename = filename.replace("-", "_")
            confirmation = input(
                f"\n{mainDirectorylist[files.index(i)]} => {filename} (Y/n): ")
            if confirmation.lower() == "y" or "":
                os.rename(
                    f"{path}/{mainDirectorylist[files.index(i)]}", f"{path}/{filename}")
            else:
                continue

    print("Aight, I'm done!")
