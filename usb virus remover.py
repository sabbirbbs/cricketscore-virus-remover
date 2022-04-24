import os


virus_list = []

def scanDir(path):
    for item in os.scandir(path):
        print(f"Scanning dir {item}")
        if os.path.isdir(item):
            scanDir(item)
        elif item.is_file():
            size = os.path.getsize(item)
            if size == 4048:#File Size in bytes
                print(item)
                virus_list.append(item)


for item in os.scandir("D:\\"):#Pendrive Address
    if os.path.isdir(item):
        scanDir(item)
    elif item.is_file():
        size = os.path.getsize(item)
        if size == 4048:
            print(item)
            virus_list.append(item)


print("*"*20)
for virus in virus_list:
    #os.remove(virus)#To Remove the virus
    print(virus)

