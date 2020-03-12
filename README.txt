-----------
How to use:

Step 1, Download "input.txt" and "course selection redux.exe"
Step 2, input your course options
--------------------------------
Type in your class in the "input.txt" file under the following format:


§1: If a class has ONE time slot:

course_name, starting_time, ending_time, weekday, semesters

§2: If a class has TWO time slot:

course_name, starting_time_1(for 1st time slot), ending_time_1(for 1st time slot), weekday_1(for 1st time slot), starting_time_2(for 2nd time slot), ending_time_2(for 2nd time slot), weekday_2(for 2nd time slot), semesters


Note:
1. Please DO NOT include space in the course name i.e. DO NOT type "CCST 9017"
2. If you want to include sub-class, please use the same name for the course_name!!!
3. starting_time and ending_time must be typed in 24hr form so 08:30 -> type "0830" or 14:20 -> type "1420"
4. weekday must be an integers {0 = Mmonday | 1 = Tuesday | 2 = Wednesday | 3 = Thursday | 4 = Friday | 5 = Saturday} 
5. semesters must be an integers: 1 or 2

For example:
If we want to input "CCST9017" from 16:30 to 18:20 (Wed) in semester 1 (ONE time slot)

CCST9017, 1630, 1820, 2, 1


If we want to input "CCST9017" from 16:30 to 18:20 (Wed) and 11:30 to 14:20 (Thur) in semester 1 (TWO time slot)

CCST9017, 1630, 1820, 2, 1130, 1420, 3, 1

---------------------------------

Step 2, run the script.
Step 3, the sorted timetable should be printed out.

--------------

Devlog:

0.1.2 Add the day-off priority algorithm and minor Bug fix

0.1.1 Now accept a sub class with two time slot

0.1.0 Publish the basic script
