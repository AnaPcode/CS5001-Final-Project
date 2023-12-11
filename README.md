# Final Project Report

* Student Name: Anastasia Pupo
* Github Username: AnaPcode
* Semester: Fall 2023
* Course: CS 5001



## Description 
General overview of the project, what you did, why you did it, etc. 

  This project is a to do app GUI that keeps track of tasks. I created the GUI using Tkinter where a user can enter and delete tasks. Furthermore, the tasks and changes will be saved in the SQLite database and therefore this project to do app will be able to access the updated list of tasks at each run.
  I chose this project as I was interested in learning how to build a user interface and believed using Tkinter will both help me practice programming in Python as well as introduce me to creating GUIs. I was able to build the GUI through learning about tkinter from watching the youtube video by freeCodeCamp (https://www.youtube.com/watch?v=YXPyB4XeYLA) and applying the concepts learned from the video.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

- A key feature of this project is the utilization of the database SQLite3 as to be able to store tasks and edit information from the GUI interface.
- The user can also choose to display tasks in three ways: Display Tasks To Do, Completed Tasks, and All Tasks.
- Another added feature is when creating a task, the date is recorded, and when a task is marked complete, the completion date is recorded.

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

Download to_do_app.py and run the file. 
A user interface will appear. At the first run of this app, no tasks have been entered and therefore using the drop down menu to select whether to view "All tasks", "Completed Tasks", or "Tasks To Do" and clicking "Click to View Tasks" will not display anything.
To enter a task, type into the text box next to "Enter task:", the task to be entered. Then when done, click "Click here to Add Task". More tasks can be entered in this same way. Note if user presses "Click here to Add Task" and the text box is empty "", then no task is added.
To view the tasks just entered, choose from the drop down menu which tasks to be seen and then press "Click to View Tasks". Buttons with the name of each task will appear. When clicking the button, a popup appears containing three buttons: "Mark as Complete", "Task Information", and "Delete Task". 
If user presses, "Mark as Complete", the popup will then ask user "Are you sure" and gives the option of clicking two buttons: "No, Do Not Mark Complete" and "Yes, Task Complete!". If select "No, Do Not Mark Complete", then popup will close and no changes to tasks. However, if "Yes, Task Complete!" is pressed, then task will be marked complete and popup will close. To see the change, can select in drop down menu the "Completed Tasks" Option and press "Click to View Tasks" which will update the tasks displayed in the GUI.
Similar to "Mark as Complete", "Delete Task" operates in the same way except it will delete the task and therefore when refreshing the list of tasks on the GUI by clicking "Click to View Tasks", the task will not be found under any drop down menu option.
Lastly, if the user presses "Task Information", this will provide information on the status of the task (complete or incomplete), date task was created in the form of year-month-day time, and date task was completed ("Pending" if task is incomplete or date in the format year-month-day time if task is complete).

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

- The only requirement to run this project is to have Python installed.
However, though already likely met, please download the Python file into a directory that does not already contain a "todo.db" file, else error message will appear for this project app is intended to create the "todo.db" file when first run.
Optional is downloading DB Browser for SQLite at https://sqlitebrowser.org/. DB Browser for SQLite can open .db files where can confirm the project's GUI is editing and saving tasks into the todo.db file.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 



### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

  A continual challenge in this project was finding that the GUI was not doing as I intended and trying to fix the errors. For example, when I first built the GUI, I had everything set up to retrieve information by name of the task. It was not until I entered a task in the text box that was already entered. This is when I found that, any actions such as delete and mark complete, I did to one of the tasks with a duplicate name, the same will occur to the other even though I submitted the tasks at different times. I was able to change my code to use the oid (object id) instead of name of the task to be able to now enter duplicate tasks.
  Throughout building the GUI, it was a struggle to find how everything should fit together, for example, to find where to code for a popup to close and open was often by trial and error. It was actually through struggling with this, I found I can add labels buttons to an existant popup which I implemented for asking if the user was sure if they wanted to delete or mark a task complete. However, another issue occurred by doing this in that the user was able to click either the mark complete or delete button again which printed the asking if user was sure and the two buttons following again. To resolve this error, I was able to figure out a way to disable all of those previous buttons so if user cannot click Mark complete or Delete again and is only left with the two given buttons on whether to indeed mark complete or delete a task.

## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

Link to video showing a project run: https://youtu.be/8yNreIvFSlc

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_

  I tested my code through running the GUI frequently while writing the program and seeing if it performs the actions I intended. Furthermore, opening the todo.db file in DB Browser for SQLite to compare if my GUI displays data representative of what is shown in the table in the todo.db file.

## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

- Fix bug of when task is completed, mark complete buttons still work. No changes to database however I think better to disable those buttons.
- A vertical scrolling bar within the frame that holds the task buttons. As the list of tasks increases, the GUI will currently not be able to show all the task buttons and hence will limit the utility of the app for there would be tasks that are unreachable unless the current viewable tasks are deleted to make space. Viewing online resources, it appears tkinter Canvas() widget can be used to accomplish this.
- I think rather than having the “Click to View Tasks” button and clicking it after choosing an option in the drop down menu or to just refresh a change made to in the database, I think I’d like to try to change it to where there is no “Click to View Tasks” button and instead what’s chosen in the drop down menu will automatically show as well as when any changes in database made that the tasks list buttons shown will be refreshed automatically.
- Allow users to specify a .db file to use. Currently, the code specifies a .db file. If the file is not found in the same directory as the app code, then it will create the file with the already provided name and for all subsequent uses of the app, it will update this file. However if a .db file with the same name specified in the code existed before running of this app, there likely will be an error. This could be prevented if the user specifies a new .db file to use.
- Make the GUI more visually appealing for example by changing some fonts, font sizes, colors. Also, for when a task is entered and has many characters, for the text box to wrap around the characters so all can be seen in the text box in the GUI. As well as for the Task Information popup, to change how the Date is shown where I will most likely consider removing the seconds or at least truncating the seconds to a whole number.
- Create a way for the user to edit the task after adding. This can be added as a feature in the popup that appears when a task is clicked. For example, if the user misspelled a task and clicked enter, currently there is no way to change it. Instead the user would need to delete that task, then enter and submit the task again.
- Add a feature that allows for the deletion of all or many tasks at once, currently the tasks in the GUI can only be deleted one by one.
- Add a feature that allows for the user to choose what tasks appear by specifying date. For example, the user only wants to see all tasks that were created today and ignore any from previous days. A calendar may be incorporated for this.
- Currently, when the program is first run and the .db file is empty, all the widgets still work on the GUI which can be clicked but nothing will be shown since there are no tasks in the database. An improvement can be to put out a message somewhere when it comes to clicking when there are no tasks entered yet to display No Tasks to View.
- Instead of permanently deleting tasks, somehow export the deleted task to a different file and in the GUI be able to reference this file to show deleted tasks.
- If user enters "       " (lots of spaces) to not consider that as a task, and therefore not to add as a task.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

  I feel I learned how to write code that is more robust and understandable for others to follow. Before this course, I did have some past experience with Python however I now know I did not write code with good design. For example, I used to often include a lot of code into one function and often had repeats of code. Furthermore, I rarely ever commented and did not have in mind to write in a way for others to be able to follow along easily. Learning to write code that others understand and practicing how to program alongside others are two key takeaways I feel I will take with me from this course. 
  I do feel I can improve when it comes to design as I still struggle with writing code efficiently and think often times there is most likely a better way to execute the same action. I do feel with practice and continuing to learn different methods that my programming will improve with time.
