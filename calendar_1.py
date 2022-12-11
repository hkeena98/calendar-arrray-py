"""
Author: Henry Keena
Version : 1.0
Date: 12/10/22
Description: Calendar 2D Practice Problem
"""

"""
Function: calendar_generator(weekday)
Parameter: weekday = Integer
Description: Function responsible for creating and outputting generator calendar
"""
def calendar_generator(weekday):
    # 'calendar' is the declaration of a 2D list
    calendar = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
    # Declares a counter for calendar lines
    calendar_line = 0
    # Declares a counter for individual calendar days
    day_counter = 0
    # Primary 'for' loop, which iterates through each list in the calendar
    for line in calendar:
        # With each iteration, the calendar line counter is increased
        calendar_line = calendar_line + 1
        # Secondary 'for' loop for iterating over individual spots in each line
        for x in range(len(line)):
            # 'if' statement that checks if current loop iteration is on the first line
            if calendar_line == 1:
                # if the calendar line is the first, checks to see if the current index is less than the input weekday
                if x < weekday:
                    # if the current index 'x', is less that weekday, it will skip to the next iteration
                    continue 
            # checks to see if the current day counter is greater than or equal to 31 (maximum day count)
            if day_counter >= 31:
                # if current day is greater than or equal to 31, breaks the loop
                break
            # if day counter is not greater than or equal to 31, executes the following code
            else:
                # day counter is incremented
                day_counter = day_counter + 1
                # day_fig, a string equivalent of day counter is made
                day_fig = str(day_counter)
                # if day counter is less than 10, formats the day_fig to have a '0' in it (ie. day_counter = 7, becomes '07')
                if day_counter < 10:
                    day_fig = "0"+day_fig
                # sets the current index of the calendar line to day_fig
                line[x] = day_fig
    # final 'for' loop that prints out the calendar
    for line in calendar:
        print(line)
    
"""
Function: main()
Desription: Main function for calling the other functions
"""
def main():
    # Welcome Print Statement
    print("Welcome to Calendar Generator\n")
    # Input function call for getting user to input a start day of the week
    weekday = int(input("Enter a Calendar Start Week Day(1 - 6): "))
    # Another print statement
    print("\nCalling Calendar Generator...\n")
    # Function Call to calendar_generator() 
    calendar_generator(weekday)

# Calls main()
if __name__ == "__main__":
    main()
