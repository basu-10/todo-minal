# todo-minal
ToDo-minal - The ToDo terminal

Why log out of the terminal for some simple todo tasks and alerts/reminders?

This small app aims to be at your fingertips... err, your terminal, and shows your todos from any day.

Here are the rules:
Week starts at Monday.

Enter 'today'       OR 't'      to see todays todos
Enter 'tomorrow'    OR 'tm'     to see tomorrows todos
Enter 'yesterday'   OR 'y'      to see yesterdays todos
Enter 'week'        OR 'w'      to see current weeks todos
Enter 'week next'   OR 'w +1'   to see the todo of each day in next week
Enter 'week 1' to see the todo of each day in week 1 of this month. 
    ('week 2', 'week 3', 'week 4', 'week 5' are valid while, numbers greater than 5 are not valid)
    ('week2' is same as 'week 2' and 'w2')



This is how you install:

1. Download
$ wget -O todo-minal.py https://raw.githubusercontent.com/basu-10/todo-minal/main/main.py

3. Install
$ sudo mkdir /usr/local/todo_minal/ # create the folder
$ sudo cp todo-minal.py /usr/local/todo_minal/ # copy contents to folder

5. Create alias to enable lanuching by just entering todo.
Open the .bashrc file with root privileegs($ sudo nano ~/.bashrc) and append the following line:
alias todo="python3 /usr/local/todo-minal/try1.py" 
