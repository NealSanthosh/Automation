import pyautogui
import time
import random
import os

def openChrome ():
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

def openVSCode ():
    os.startfile("C:/Users/admin\AppData/Local/Programs/Microsoft VS Code/Code.exe")

def chooseTasks (n):
    print("Opening " + n)

    if n == "1":
        openChrome()
        print("Chrome Opened")
    elif n == "2":
        openVSCode()
        print("Chrome Opened")
    
    print("Finished")

print("1 : Open Chrome")
print("2 : Open VSCode")

x = input("Input : ")

chooseTasks(x)
