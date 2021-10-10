import urllib.parse
import requests
import hashlib

#I import this module to put my data in a table.
from tabulate import tabulate

import datetime
from datetime import date
import calendar

main_api = "http://gateway.marvel.com/v1/public/characters?"
public_key = "32a0cf7c4c888e22ac183d71f08ccf00"
private_key = "48e949913a8b871911b212d6677ccfc57b8fc3d6"
timestamp = "1"
pre_hash = timestamp + private_key + public_key
result = hashlib.md5(pre_hash.encode())

# This variable I set up to have a title above my table later.
headers = ""

# With this code, I make the date. And it converts it to dd/mm/yy.
today = date.today()
date_1 = today.strftime("%d/%m/%Y")
# With this code, I make the today's day.
curr_date = date.today()
# With this code, I make the current time and month.
h_m = datetime.datetime.now()

print("=============================================================== ")
# With this code, I display the current time.
print("The time is now:  %s:%s:%s" % (h_m.hour, h_m.minute, h_m.second))
# With this code, I display the current date. And it converts it to dd/mm/yy.
print("Date:            ", date_1)
# With this code, I display the today's day.
print("Day of the week: ", calendar.day_name[curr_date.weekday()])
# With this code, I display the current month.
print("Month:           ", h_m.strftime('%B'))
print("===============================================================")

# With this code, I print the name of my app.
print("My name is Marvelverse.")
#This is a small while loop to check the user's input. That they enter a name and not a number.
while True:
    user = input("What is your name? ")
    if user.isalpha():
        break
    print("Please enter characters A-Z only.")
#Here you will find the code for a personalized banner.
print("                                               _ ")
print("                                              | |  ")
print("                _ __ ___   __ _ _ ____   _____| |")
print("               | '_ ` _ \ / _` | '__\ \ / / _ \ |")
print("               | | | | | | (_| | |   \ V /  __/ |")
print("               |_| |_| |_|\__,_|_|    \_/ \___|_|")
print("=============================================================== ")
print("        Welcome " + user + ", to the Marvel character database !            ")
print("=============================================================== \n")

answer = ""
question = ""

while answer != "Y" and answer != "y":
    answer = input("Are you looking for a Marvel character ? (Type Y/N) ")
    if answer == "N" or answer == "n":
        print(" \n=============================================================== ")
        print("How do I say goodbye? When I hardly had a chance to say hello?  ")
        print("=============================================================== ")
        question = input("Are you sure you don't want to look up a Marvel character? (Type Y/N) ")
        if question == "y" or question == "Y":
            # For a more enjoyable user experience, here I am printing a goodbye message.
            print("    __   __   __   __   __       ___ ")
            print("   / _` /  \ /  \ |  \ |__) \ / |__  ")
            print("   \__> \__/ \__/ |__/ |__)  |  |___ ")
            break
        elif question == "n" or question == "N":
            while answer == "Y" or answer == "y" and answer != "N" or answer != "n":
                name = input("Which Marvel character are you looking for ? (type quit to stop) ")
                if name == "quit" or name == "stop" or name == "q" or name == "s" or name == "STOP" or name == "QUIT":
                    break
                url = main_api + urllib.parse.urlencode(
                    {"name": name, "ts": timestamp, "apikey": public_key, "hash": result.hexdigest()})
                print("\n=============================================================== ")
                print("Information for developers")
                print("=============================================================== ")
                print("URL: " + url)
                json_data = requests.get(url, headers=headers).json()
                json_status = json_data["code"]
                if json_status == 200:
                    result_t = []
                    if json_data["data"]["total"] == 0:
                        print(name + " doesn't exist \n")
                    else:
                        print("API status: " + str(json_status))
                        print("---------------------------------------------------------------\n")
                        print("=============================================================== ")
                        print("Basic information about " + name )
                        print("===============================================================\n")
                        print("Name: " + name)
                        print("Description: " + str(json_data["data"]["results"][0]["description"]))
                        print("How many comics " + name + " appears in: " + str(
                            json_data["data"]["results"][0]["comics"]["available"]))
                        print("\nHere are a couple of comics " + name + " appears in. Enjoy!")
                        print("================================================================")
                        for each in json_data["data"]["results"][0]["comics"]["items"]:
                            result_t.append([each["name"]])
                        print(tabulate(result_t, headers=["Name"]))
                        print("================================================================\n")
                elif json_status == 409:
                    print("================================================================")
                    print("Status Code: " + str(
                        json_status) + "; Oops, something went wrong. Did you fill in a superhero name? Remember that you can only fill in a maximum of 100 characters!")
                    print("================================================================\n")
#This is the code if you choose the "Y" or "y" option directly. This is where the code repeats.
while answer == "Y" or answer == "y" and answer != "N" or answer != "n":
    name = input("Which Marvel character are you looking for ? (type quit to stop) ")
    if name == "quit" or name == "stop" or name == "q" or name == "s" or name == "STOP" or name == "QUIT":
        # For a more enjoyable user experience, here I am printing a goodbye message.
        print("    __   __   __   __   __       ___ ")
        print("   / _` /  \ /  \ |  \ |__) \ / |__  ")
        print("   \__> \__/ \__/ |__/ |__)  |  |___ ")
        break
    url = main_api + urllib.parse.urlencode({"name": name, "ts": timestamp, "apikey": public_key, "hash": result.hexdigest()})
    print("\n=============================================================== ")
    print("Information for developers")
    print("=============================================================== ")
    print("URL: " + url)
    json_data = requests.get(url, headers=headers).json()
    json_status = json_data["code"]
    if json_status == 200:
        result_t = []
        if json_data["data"]["total"] == 0:
            print(name + " doesn't exist\n")
        else:
            print("API status: " + str(json_status))
            print("---------------------------------------------------------------\n")
            print("=============================================================== ")
            print("Basic information about " + name)
            print("===============================================================\n")
            print("Name: " + name)
            print("Description: " + str(json_data["data"]["results"][0]["description"]))
            print("How many comics " + name + " appears in: " + str(json_data["data"]["results"][0]["comics"]["available"]))
            print("\nHere are a couple of comics " + name + " appears in. Enjoy!")
            print("================================================================")
            for each in json_data["data"]["results"][0]["comics"]["items"]:
                result_t.append([each["name"]])
            print(tabulate(result_t, headers=["Name"]))
            print("================================================================\n")
    elif json_status == 409:
        print("================================================================")
        print("Status Code: " + str(json_status) + "; Oops, something went wrong. ")
        print("Did you fill in a superhero name? Remember that you can only fill in a maximum of 100 characters!")
        print("================================================================")