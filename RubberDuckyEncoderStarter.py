import os,platform,sys
from time import sleep

ChosenPayload = ""
Payloads = []
index = 0
AllowedInputs = []

red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'


def CheckOSandDo(Function):
    System = platform.system()
    if System == "Windows":
        if Function == "Clear":
            os.system("cls")
        elif Function == "DownloadJavaEncoder":
            os.system("powershell (new-object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/hak5darren/USB-Rubber-Ducky/master/Encoder/encoder.jar','encoder.jar')")
    elif System == "Linux":
        if Function == "Clear":
            os.system("clear")
        elif Function == "DownloadJavaEncoder":
            os.system("wget https://raw.githubusercontent.com/hak5darren/USB-Rubber-Ducky/master/Encoder/encoder.jar")
    elif System == "Darwin" or System == "macOS":
        if Function == "Clear":
            os.system("clear")
        elif Function == "DownloadJavaEncoder":
            os.system("curl -O https://raw.githubusercontent.com/hak5darren/USB-Rubber-Ducky/master/Encoder/encoder.jar")
    else:
        if Function == "Clear":
            if System == "":
                print(red("** This Script is not tested on this Operating System and might crash!!"))
            else:
                print(red("** This script is not tested on " + System + " and might crash!!"))
        elif Function == "DownloadJavaEncoder":
            if System == "":
                print(red("** This Script is not tested on this Operating System and might crash!!"))
            else:
                print(red("** This script is not tested on " + System + " and might crash!!"))
        return
    
def Load():
    CheckOSandDo("Clear")
    global ChosenPayload 
    global Payloads
    global index
    ChosenPayload = ""
    Payloads = []
    index = 0
    print("")
    print("")
    print("                                                             ")
    sleep(0.1)
    print("                                                             ")
    sleep(0.1)
    print("                                             " + yellow("&&&&&&&&&") + "       ")
    sleep(0.1)
    print("                                            " + yellow("&&&&&&") + " " + yellow("(*&&") + "      ")
    sleep(0.1)
    print("                                          " + yellow("(&&&&&&&&") + "  " + yellow("/&&") + "     ")
    sleep(0.1)
    print("                                         " + yellow("*&&&&&&&&&&&&&&") + "     ")
    sleep(0.1)
    print("                                         " + yellow(".&&&&&&&&&&&&&&&&&(") + " ")
    sleep(0.1)
    print("                                           " + yellow(".&&&&&&&&&&&&&&&.") + " ")
    sleep(0.1)
    print("                                              " + yellow("&&&&&&&&&&") + "     ")
    sleep(0.1)
    print("                        "+yellow("&&/")+ " " + yellow("*") + "               "+yellow(".&&&&&&&&&&&&/")+"   ")
    sleep(0.1)
    print("                          " + yellow("&,&") + "  " + yellow(".&..&&&&&&") + red("USB") + yellow("&") + red("Rubber") + yellow("&") + red("Ducky") + yellow("&*") + "  ")
    sleep(0.1)
    print("                           " + yellow("(/(#/&&&") + " " + yellow("/&&&&&") + red("Encoder") + yellow("&") + red("Starter") + yellow("&&") + "  ")
    sleep(0.1)
    print("                              " + yellow("(..,&&&,") + " " + yellow(".&&&") + red("By:") + yellow("&") + red("Mina") + yellow("&") + red("Magdy") + yellow("&") + "   ")
    sleep(0.1)
    print("                             " + yellow("&&") + " " + yellow(".&") + "         " + yellow("&&&&&&&&&&&&&&&") + "   ")
    sleep(0.1)
    print("                            " + yellow("&*") + " " + yellow("*&(") + "          " + yellow("&&&&&&&&&&&&(") + "    ")
    sleep(0.1)
    print("                                                             ")
    sleep(0.1)
    print("                                                             ")
    print(chr(10) + chr(10) + yellow("                         USB Rubber Ducky Encoder Starter") + chr(10) + green("                                 By: Mina Magdy" + chr(10) + "                       https://github.com/minamagdyshehata") + chr(10) + chr(10))
    ShowPayloads()

def ShowPayloads():
    global Payloads
    global index
    global AllowedInputs
    Payloads = []
    index = 0
    AllowedInputs = []
    print(green("## Your Payloads are: " + chr(10))) 
    Files = os.listdir (".")
    for x in range (0,len(Files)):
        if Files[x].endswith(".txt" )or Files[x].endswith(".txT") or Files[x].endswith(".tXt") or Files[x].endswith(".tXT")  or Files[x].endswith(".Txt")  or Files[x].endswith(".TxT")  or Files[x].endswith(".TXt")  or Files[x].endswith(".TXT"):
            Payloads.append(Files[x])
    index = len(Payloads)
    if index == 0:
        print(red("** No Payloads were found!!") + chr(10) + green("*** Place your Payloads in the same Directory then Restart this script..") + chr(10))
        ExitScript()
    if index > 0:
        for x in range (1,index + 1):
            print (green("--[" + str(x) + "]") + " : " + Payloads[x-1])
    print (red("--[" + str(index + 1) + "]" + " : To Exit..."))
    for x in range (1,index+2):
        AllowedInputs.append(x)
    ChoosePayload()
    
def ChoosePayload():
    global ChosenPayload
    global Payloads
    global index
    global AllowedInputs
    ChosenPayload = ""
    RenameRequired = 0
    if sys.version_info[0] >= 3: ChosenPayload = input(chr(10) + green("*** Please choose an option : "))
    elif sys.version_info[0] == 2: ChosenPayload = raw_input(chr(10) + green("*** Please choose an option : "))
    
    
    while ChosenPayload not in str(AllowedInputs) or ChosenPayload == "":
        print(chr(10) + red("** Wrong input, please try again..") + chr(10))
        print(green("*** Allowed Inputs are: " + str(AllowedInputs)))
        if sys.version_info[0] >= 3: ChosenPayload = input(chr(10) + green("*** Please choose an option : "))
        elif sys.version_info[0] == 2: ChosenPayload = raw_input(chr(10) + green("*** Please choose an option : "))
    ChosenPayload = int(ChosenPayload)    
    if ChosenPayload == index + 1: ExitScript()
    for x in range(0,len(Payloads[ChosenPayload-1])-4):
        if (65 <= ord(Payloads[ChosenPayload-1][x]) and ord(Payloads[ChosenPayload-1][x]) <= 90) or (48 <= ord(Payloads[ChosenPayload-1][x]) and ord(Payloads[ChosenPayload-1][x]) <= 57) or (97 <= ord(Payloads[ChosenPayload-1][x]) and ord(Payloads[ChosenPayload-1][x]) <= 122):
            if RenameRequired == 1:
                RenameRequired = 1
            else:
                RenameRequired = 0
        else:
            RenameRequired = 1        
    if RenameRequired == 0:
        CheckOSandDo("Clear")
        EncodePayload(Payloads[ChosenPayload-1])
    elif RenameRequired == 1:
        CheckOSandDo("Clear")
        RenamePayload()
    ShowPayloads()
        
def ExitScript():
    if sys.version_info[0] >= 3: Terminate = input(red(chr(10) + "** Please Press Enter to Exit.."))
    elif sys.version_info[0] == 2: Terminate = raw_input(red(chr(10) + "** Please Press Enter to Exit.."))
    print (chr(10) + green("*** Thank You for using:" + chr(10) + "*** USB Rubber Ducky Encoder Starter") + chr(10))
    print (yellow("      _      _      _      USB       _      _      _"))
    sleep(0.1)
    print (yellow("   __(.)< __(.)> __(.)=   Rubber   =(.)__ <(.)__ >(.)__"))
    sleep(0.1)
    print (yellow("   \___)  \___)  \___)    Ducky!    (___/  (___/  (___/ " + chr(10)))
    sleep(0.1)
    print (chr(10) + red("** Rubber Ducky Encoder Starter script will terminate in 1.5 seconds..") + chr(10) + chr(10))
    sleep(1.5)
    sys.exit()

def EncodePayload(PayloadName):
    global ChosenPayload
    global Payloads
    if os.path.isfile(PayloadName) == False:
        print(chr(10) + red("** Payload was not found!!!") + chr(10))
        return
    print (chr(10) + "*** Your choice is " + green(PayloadName) + chr(10) + "*** Your encoded Payload will be created as " + green(PayloadName[:len(PayloadName) - 4] + "inject.bin"))
    print(red("** Please remember to remane the encoded Payload to ") + green("inject.bin") + red(" before using it.") + chr(10) + green("*** Enjoy!!...") + chr(10))
    if os.path.isdir("./DuckyEncodedPayloads") == False:
        print(red("** DuckyEncodedPayloads Directory doesn't exist..."))
        os.makedirs(r"DuckyEncodedPayloads")
        print(green("*** DuckyEncodedPayloads successfully created...") + chr(10))
    if os.path.isfile("encoder.jar") == False:
        print(chr(10) + red("** Java Encoder was not found!!"))
        print(green("*** Downloading encoder.jar.....") + chr(10))
        CheckOSandDo("DownloadJavaEncoder")
        if os.path.isfile("encoder.jar") == False:
            print(red(chr(10) + "** Download Failed!!"))
            print(red("** Please Check your Internet Connection or Download Java Encoder manually from:") + chr(10) + green("*** https://github.com/hak5darren/USB-Rubber-Ducky/blob/master/Encoder/encoder.jar") + chr(10) + red("** Then Restart  this script..") + chr(10))
            ExitScript()
        else:
            print(chr(10) + green("*** encoder.jar Downloaded Successfully...." + chr(10)))
    os.system("java -jar encoder.jar -i " + PayloadName + " -o ./DuckyEncodedPayloads/" + PayloadName[:len(PayloadName) - 4] + "inject.bin")
    if os.path.isfile("./DuckyEncodedPayloads/" + PayloadName[:len(PayloadName) - 4] + "inject.bin") == True:
        print(green(chr(10) + "*** Done!!..Please check the DuckyEncodedPayloads Directory.." + chr(10)))
    else:
        print(red(chr(10) + "** Encoding Failed!!..Please make sure Java is installed..." + chr(10)))

def RenamePayload():
    global ChosenPayload
    global Payloads
    RENAMEDPayload = ""
    print (chr(10) + "** Your choice is " + red(Payloads[ChosenPayload-1]))
    print(chr(10) + red("** The Chosen Payload name contains a space or a special character and will raise an Error!!"))
    for x in range(0,len(Payloads[ChosenPayload-1])-4):
        if (65 <= ord(Payloads[ChosenPayload-1][x]) and ord(Payloads[ChosenPayload-1][x]) <= 90) or (48 <= ord(Payloads[ChosenPayload-1][x]) and ord(Payloads[ChosenPayload-1][x]) <= 57) or (97 <= ord(Payloads[ChosenPayload-1][x]) and ord(Payloads[ChosenPayload-1][x]) <= 122):
            RENAMEDPayload += Payloads[ChosenPayload-1][x]
    RENAMEDPayload += "RENAMED"
    while os.path.isfile(RENAMEDPayload + ".txt"):
        RENAMEDPayload += "RENAMED"
    RENAMEDPayload = RENAMEDPayload + ".txt"
    os.rename(Payloads[ChosenPayload-1],RENAMEDPayload)     
    print(green(chr(10) + "*** Your Payload was Rename " + RENAMEDPayload) + chr(10))
    EncodePayload(RENAMEDPayload)

Load()
