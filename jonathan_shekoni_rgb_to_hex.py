"""
Name:Jonathan Shekoni
Program Description: Takes user inputted rgb code and converts it to hex code, looping until the user quits the program.
"""

#Create quit phrases for exiting loop
quit_phrases = ['quit', 'q']
def RGB_to_Hex(RGB):
    #Calculate the hex code for each colors
    red_0 = RGB['red'] % 16
    if red_0 == 10:
            red_0 = 'A'
    elif red_0 == 11:
            red_0 = 'B'
    elif red_0 == 12:
            red_0 = 'C'
    elif red_0 == 13:
            red_0 = 'D'
    elif red_0 == 14:
            red_0 = 'E'
    elif red_0 == 15:
            red_0 = 'F'
    red_1 = (RGB['red'] // 16)
    
    blue_0 = RGB['blue'] % 16

    if blue_0 == 10:
            blue_0 = 'A'
    elif blue_0 == 11:
            blue_0 = 'B'
    elif blue_0 == 12:
            blue_0 = 'C'
    elif blue_0 == 13:
            blue_0 = 'D'
    elif blue_0 == 14:
            blue_0 = 'E'
    elif blue_0 == 15:
            blue_0 = 'F'
    blue_1 = (RGB['blue'] // 16) 
    
    green_0 = RGB['green'] % 16

    if green_0 == 10:
            green_0 = 'A'
    elif green_0 == 11:
            green_0 = 'B'
    elif green_0 == 12:
            green_0 = 'C'
    elif green_0 == 13:
            green_0 = 'D'
    elif green_0 == 14:
            green_0 = 'E'
    elif green_0 == 15:
            green_0 = 'F'
    green_1 = (RGB['green'] // 16) 
        
    #Create final hex code string and return 
    hex_code = f"#{red_1}{red_0}{green_1}{green_0}{blue_1}{blue_0}"
    return hex_code


print("RGB to Hex Converter")
while True:
    #Quit if quit phrase is entered
    red_input = input("Enter the Red Color Value: ")
    if red_input.lower() in quit_phrases:
        break
    green_input = input("Enter the Green Color Value: ")
    if green_input.lower() in quit_phrases:
        break
    blue_input = input("Enter the Blue Color Value: ")
    if blue_input.lower() in quit_phrases:
        break
    
    #Create dictionary that takes colors rgb number as input
    colors = {
        'red': int(red_input),
        'blue': int(blue_input),
        'green': int(green_input),
    }
    
    hex = RGB_to_Hex(colors)
    print(f"\nHex Value: {hex}\n")
