#Ask the user to input a month and day.
month = input("Please enter the month: ").lower()
day = int(input("Please enter a day: "))

#Make lists of all the months, then make seperate lists to classify each month to a time period.
months = ['january','february','march','april','may','june','july','august','september','october','november','december']
spring = ['january','february','march','april']
summer = ['may','june','july','august']
fall = ['august','september','october','november','december']
winter = ['december','january']


#Make an if statement to check if the month and date given is a real/valid value.
if month in months and day < 31 and day >= 1:
    #Include an if-else statement to check for months without 31 days.
    if month == ['september','april','june','november'] and day == 31:
        print(f"{month.title()} {day}is an invalid date.")
    #Checks if an invalid date for february was entered.
    elif month == 'february' and day > 29:
        print(f"{month.title()} {day}is an invalid date.")
    else:
        #Prints out the academic time period for the given month and day by checking if the month is in a specific list and under a specific number
        if month in spring[0] and day >= 8 or month in spring and day <= 31:
            print(f"{month.title()} {day} is during GSU's spring semester.")
        elif month in summer[0] and day <31 or month in summer[1] and day <=31 or month in summer[2] and day <=31 or month in summer[3] and 1< day <=20:
            print(f"{month.title()} {day} is during GSU's summer break.")
        elif month in fall[0] and day >= 21 or month in fall[1] and day <=31 or month in fall[2] and day <=31 or month in fall[3] and day <=31 or month in fall[4] and day <= 12:
            print(f"{month.title()} {day} is during GSU's fall semester")
        else:
            print(f"{month.title()} {day} is during GSU's winter break.")
else:
    #Tell the user the date/month is invalid
    print(f"{month.title()} {day} is an invalid date.")