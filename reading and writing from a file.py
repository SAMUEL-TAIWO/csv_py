fileName = "Tresure.csv"
# WRITE = "w"
# APPEND = "a"
# READWRITE ="w+"
# MyFile = open(fileName,"w+")
# MyFile.write("FEYI,21\n")
# MyFile.write("TUMILARA,30\n")
# MyFile.write("Taiwo")
# MyFile.close()
# print("file written succesfully")
# r = read a file
# w = write to the file
# a = append to the existing file content
# b = open a binary file

#a CSV file contains data separated by a character usually a coma
fileName="i.csv"
data = [  ]
name = "  "
while name != "DONE":
    name = input("ENTER FILE INFORMATION:(INPUT DONE WHEN NO MORE NAMES IS ADDED):")
    data.append(name)
    data.sort()
WRITE = "w"
APPEND = "a"
READWRITE ="w+"
MyFile = open(fileName,mode=READWRITE )
data = ", ".join(name)
MyFile.write(data)
MyFile.close()
MyFile = open(fileName,mode = READWRITE)
MyFile.write("susan,39\n")
MyFile.write("chris,50")
MyFile.close()
print("file written succesfully")

#HOW TO READ A FILE WITH CODE
#you right click on pycharm, then sth will be displaying down on the icon
#click on the file icon and open new, after open text document and change the name to any name of your choice.
#after changing the name , open the folder and it will ope in form of a note pad
#write the the stuffs you want to write on it and  and go to your pycharm and write the code to open it
animalFile = open("tesmania.txt","r")
fileContent = animalFile.read()
print(animalFile)

# HOW TO READ A FILE WITH CODE
# you right click on pycharm, then sth will be displaying down on the icon
# click on the file icon and open new, after open text document and change the name to any name of your choice.
# after changing the name , open the folder and it will ope in form of a note pad
# #write the the stuffs you want to write on it and  and go to your pycharm and write the code to open it
import csv

with open("tesmania.txt", "r") as animalFile:
    allrowslist = csv.reader(animalFile)
    for currentrows in allrowslist:
        print(":".join(currentrows))
        for currentphrase in currentrows:
            print(currentphrase)

# CHANGING THE FORMATING AND THE WAY IT PRINTS OUT THE LIST I.E[ CHANGE THE SQUARE BRACKET]:
# YOU can use join function to format your output i.e  (",".join(files))


animalFile = open("tesmania.txt", "r")
# TO READ THE FIRST LINE/READ FILE LINE BY LINE
firstanimal = animalFile.readline()
print(firstanimal)
secondanimal = animalFile.readline()
print(secondanimal)
# TO READ THE SECOND LINE
fileContent = animalFile.readline()
print(fileContent)
# USING THE READERS FUNCTIONS TO RETURN ALL ROWS FROM THE FILE INTO A LIST
# To open and read our csv
# challenge:reading from file
import csv

filename = "wode.txt"
READ = "r"
with open(filename, mode=READ) as MyCsvFile:
    readfromfile = csv.reader(MyCsvFile)
    for currentread in readfromfile:
        print(":".join(currentread))

# THE CHALLENGE CAN ALSO BE CODED AS
import csv

with open("wode.txt", "r") as MyCsvFile:
    readfromfile = csv.reader(MyCsvFile)
    for currentread in readfromfile:
        print(":".join(currentread))























