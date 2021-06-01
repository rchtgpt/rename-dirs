def main():

    def one(filename):
        capitalizeWords(filename)
        filename = joinWithSpaces(filename)
        return filename

    def two(filename):
        capitalizeWords(filename)
        filename = joinWithDashes(filename)
        return filename

    def three(filename):
        filename[0] = filename[0].capitalize()
        filename = joinWithDashes(filename)
        return filename

    def four(filename):
        capitalizeWords(filename)
        filename = joinWithUnderscores(filename)
        return filename

    def five(filename):
        lowercaseWords(filename)
        filename = joinWithSpaces(filename)
        return filename

    def six(filename):
        lowercaseWords(filename)
        filename = joinWithDashes(filename)
        return filename

    def seven(filename):
        lowercaseWords(filename)
        filename = joinWithUnderscores(filename)
        return filename

    def capitalizeWords(filename):
        for i in filename:
            filename[filename.index(i)] = i.capitalize()
        return filename

    def lowercaseWords(filename):
        for i in filename:
            filename[filename.index(i)] = i.lower()
        return filename

    def joinWithSpaces(new_name):
        new_name = " ".join(new_name)
        return new_name

    def joinWithUnderscores(new_name):
        new_name = "_".join(new_name)
        return new_name

    def joinWithDashes(new_name):
        new_name = "-".join(new_name)
        return new_name

    import os
    path = input("Enter full directory path: ")
    format = int(input('Choose the name format:\n1. Example File.txt\n2. Example-File.txt\n3. Example-file.txt\n4. Example_File.txt\n5. example file.txt\n6. example-file.txt\n7. example_file.txt\n\nEnter a number: '))
    files = os.listdir(path)
    mainDirectorylist = list()
    final_filename = str()

    for file in files:
        if file.startswith(".") == False and "." in file:
            mainDirectorylist.append(file)

    for visibleFile in mainDirectorylist:
        filename=str()
        if " " in visibleFile or "-" in visibleFile or "_" in visibleFile:
            if " " in visibleFile:
                filename = visibleFile.split()
            if "-" in visibleFile:
                filename = visibleFile.split('-')
            if "_" in visibleFile:
                filename = visibleFile.split("_")
        else:
            filename = visibleFile.split()

        while ("" in filename):
            filename.remove("")

        if type(format) == int:
            if format == 1:
                final_filename = one(filename)
            elif format == 2:
                final_filename = two(filename)
            elif format == 3:
                final_filename = three(filename)
            elif format == 4:
                final_filename = four(filename)
            elif format == 5:
                final_filename = five(filename)
            elif format == 6:
                final_filename = six(filename)
            elif format == 7:
                final_filename = seven(filename)
            else:
                print('Enter a number from 1 to 7')
                break
        else:
            print('Enter a number from 1 to 7')
            break

        confirmation = input(
            f"\n{visibleFile} => {final_filename} (Y/n): "
            )
        if confirmation.lower() == "y" or "":
            os.rename(
                f"{path}/{visibleFile}", f"{path}/{final_filename}")
        else:
            continue

    print("\nI'm done! the files have been renamed.")