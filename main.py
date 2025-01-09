# nexessary imports to acsess api, webbrowser, and dates
import requests
import webbrowser
from datetime import datetime
import calendar

# API Url being associated to a variable
url = "https://api.nasa.gov/planetary/apod"

# Get the current date based on your computer
current_Y = int(datetime.now().strftime('%Y')) # Gets your computers current year
current_M = int(datetime.now().strftime('%m')) #                             month
current_D = int(datetime.now().strftime('%d')) #                             day

suf = "" # establish a suffix variable
if 10 <= current_D % 100 <= 20: # Assigns 'th' to suf to all numbers read with 'th, special case handeled for 11-13
        suf = 'th' 
else:
    suf = {1: 'st', 2: 'nd', 3: 'rd'}.get(current_D % 10, 'th') # applies the special suffixes for 1-3 and and variation using 1-3 (excpet 11-13)

day = f"{current_D}{suf}" # Formats the suffix together with the day to make a string instead of a tuple

month_name = calendar.month_name[current_M] # gets the name of the current month

current = f"{month_name} {day}, {str(current_Y)}" # Creats a formated current day to be used later

# Create code for user to interact with the program
print("Welcome to Nasa's APOD!.\n") # introduction
print("Note, Apod only supports dates from June 20th, 1995 - " + current + "\n") # uses the current date to list all the dates avalible
while True: 
  
    inpSee = input("Enter 'exit' to leave, anything else to continue: ") # asks the user if they want to searrch for a picture or leave

    if inpSee.lower() == 'exit': # If user apllies exit the loop ends and conclusion message prints
        print("Thank you, hope you enjoyed your time here!\n")
        break

  
    else:
      
        inpD = input("\nEnter the day of your picture: ") # takes user input on the day they want
        inpD = inpD.zfill(2) # formats the data to include 2 integers (in case the user enters a digit 1-9 without a leading 0)

        inpM = input("\nEnter the Month of your picture: ") # takes user input on the month they want
        inpM = inpM.zfill(2) # formats the data to include 2 integers (in case the user enters a digit 1-9 without a leading 0)

        inpY = int(input("\nEnter the year of your picture: ")) # takes user input on the year they want
        if (95 <= inpY <= 99): # if the user enters a year from 1995-1999 without the leading 2 digits, they are added
            inpY += 1900
        elif (00 <= inpY <= current_Y): # if the user enters a year from 2000-2025 without the leading 2 digits, they are added
            inpY += 2000
        
        inpDirty = str(inpY) + "-" + inpM + "-" + inpD # concatonate all the inputs
        inp = inpDirty.replace(" ", "") # clean any uncessary spaces the user might have added



        params = {
            "api_key": "DEMO_KEY",  # Demo key but can be changed with your custom key
            "date": inp    # Specific date for the APOD
        }

        response = requests.get(url, params=params) # Get the requested fata from the API

        if response.status_code == 200:
            data = response.json()
            pic_url = data.get("url")
            pic_title = data.get("title")
            pic_explanation = data.get("explanation")

            # Create an HTML file to display the information
            html_content = f"""
            <html>
                <head>
                    <title>{pic_title}</title>
                </head>
                <body>
                    <h1>{pic_title}</h1>
                    <img src="{pic_url}" alt="{pic_title}" style="max-width: 100%; height: auto;">
                    <p>{pic_explanation}</p>
                </body>
            </html>
            """

            # Save the HTML file
            with open("apod.html", "w") as file:
                file.write(html_content)

            # Open the HTML file in the default browser
            webbrowser.open("apod.html")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
        print("") # Create a space for readability
