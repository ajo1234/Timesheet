import json
import os
import chromedriver_autoinstaller

def CheckForChromeDriver():
    chromedriver_autoinstaller.install()

def CheckIfFileExists():
    return os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + "/Data.json")

def WriteFile():
    data = {}
    data["time"] = []
    time = []

    username = str(input("Enter username"))
    password = str(input("Enter password")) 
    
    taskCount = int(input("Enter number of elements: "))
    
    for index in range(0, taskCount):
        print("Enter time for task" + str(index+1) + ": ")
        ele = str(input())
        time.append(ele)
        
    data["time"].append({
        'Username':username,
        'Password':password,
        'Time':time
    })
    print(data["time"])
    
    try:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/Data.json", "w") as write_file:
            json.dump(data["time"], write_file)
    except Exception as e:
        print(e)
    k=input("Press any key to exit") 


CheckForChromeDriver()
if(CheckIfFileExists()):
    os.system("python "+ os.path.dirname(os.path.abspath(__file__)) + "/Automate.py 1")
else:
    WriteFile()
