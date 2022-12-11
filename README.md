# calendar-arrray-py
2D Calendar Generation Function Practice Problem

PRACITCE PROBLEM PROMPT:

Define a function that, given a 'weekday' and a number of 'days', returns a 2D list to represent a 
calendar month. The 'weekday' is an integer between '0' (Sunday) and '6' (Saturday) and is the 
weekday on which the first day of the month falls. The number of 'days' indicates the number of 
days in the month, i.e. 28, 29, 30, 31. The 2D list returned should include 7 columns (one for each
day of the week) and a sufficient number of rows to include all of the days of the month. All days 
should be represented as strings padded out to two characters, including "emoty" days.
For Example, a month that begins on a 'Tuesday' (weekday = 2) and includes 31 days:

['  ', '  ', '01', '02', '03', '04', '05']
['06', '07', '08', '09', '10', '11', '12']
['13', '14', '15', '16', '17', '18', '19']
['20', '21', '22', '23', '24', '25', '26']
['27', '28', '29', '30', '31', '  ', '  ']

