-----------
How to use:

Step 1, Download "input.txt" and "course selection redux.exe"
Step 2, input your course options
--------------------------------
Type in your course sub class in the "input.txt" file under the following method:

course_name, starting_time (in 24hr form), ending_time (in 24hr form), weekday, semesters

Note:
1. Please DO NOT include space in the course name i.e. DO NOT type "CCST 9017"
2. If you want to include sub-class, please use the same name for the course_name!!!
3. starting_time and ending_time must be typed in 24hr form so 08:30 -> type "0830" or 14:20 -> type "1420"
4. weekday must be an integers {0 = Mmonday | 1 = Tuesday | 2 = Wednesday | 3 = Thursday | 4 = Friday | 5 = Saturday} 
5. semesters must be an integers: 1 or 2

For example:
If we want to input CCST9017 from 16:30 to 18:20 (Wed) in semester 1

CCST9017, 1630, 1820, 2, 1

---------------------------------

Step 3, run the script.
Step 4, the sorted timetable should be printed out.


--------------

Devlog:

0.1.0 Publish the basic script
