from tkinter import *
from datetime import datetime
import sqlite3
import os

root = Tk()
root.title('To Do App')
root.geometry("600x600")  # Size of root window to open when program runs
root.resizable(True, True)  # Allows user to resize the root window, if (False, False) size would be fixed.
root.config(bg = "lightblue")  # Changes background color of root window

frame = None  # Set to None so when show_frame function is run, it will change this variable. If function runs again, it will know to destroy previous frame before creating new frame.

# Functions
def add_task():
    """
    Adds the task entered by user on GUI into database. Deletes user's entry from the text box afterwards.
    """
    if task_entered.get() != "":  # Prevents the addition of "" as a task if user clicks "Click here to Add Task" button before entering anything.
        
        date_created = str(datetime.now()).strip()  # Gets current time and puts it into variable date_created to be stored as time task was created.
        status = "incomplete"  # Set as incomplete since assume at task creation it has not been completed yet.
        date_completed = "Pending"  # Set as pending for date completed is unknown still for task is assumed to not have been completed yet.

        # Connect to database and adds task to database. If database does not yet have a table to insert values, table is created.
        connection = sqlite3.connect('todo.db')
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO tasks VALUES (:task, :status, :date_created, :date_completed)",
                           {
                               'task': task_entered.get(),
                               'status': status,
                               'date_created': date_created,
                               'date_completed': date_completed
                            })
        except Exception as e:  # Handles error if same name file exists already but with different table.
            print("Error occurred with inserting values. todo.db file likely existed prior to run of this app, either delete current todo.db file or specify a new .db file to use in app")
        connection.commit()
        connection.close()
        
        task_entered.delete(0, END)  # Deletes task user entered in text box from the text box


def query(option):
    """
    Receives selected option from drop down in GUI as an argument.
    Fetches all tasks from database and depending on option passed in, creates a list of tasks.
    Calls function show_frame and passes the list of tasks to be displayed.
    """
    # Connect to database and fetch information from database
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute("SELECT *, oid FROM tasks")  # Retrieves data from database
    all_tasks = cursor.fetchall()  # fetchall() gets all of the retrieved data
    connection.commit()
    connection.close()

    tasks_to_show = []
    if option == options[0]:  # Selects for tasks that are 'incomplete' for 'status' since option[0] = "Tasks To Do"
        for i in all_tasks:
            if i[1] == "incomplete":
                tasks_to_show.append(i)
    elif option == options[1]:  # Selects for tasks that are 'complete' for 'status' since option[1] = "Completed Tasks"
        for i in all_tasks:
            if i[1] != "incomplete":
                tasks_to_show.append(i)
    elif option == options[2]:  # Selects all tasks since option[2] = "All tasks"
        tasks_to_show = all_tasks

    show_frame(tasks_to_show)


def show_frame(tasks_to_show):
    """
    Creates frame, and displays passed in tasks in the tasks_to_show list as buttons in the frame in the GUI.
    Also, if button of a task is clicked, show_options will be called and the task with task id will be passed.
    """
    global frame
    if frame is not None:
        frame.destroy()  # Destroys already existent frame, if not then when each option is selected in drop down menu and button "Click to View Tasks" is clicked, there will be overlapping frames.

    frame = Frame(root)
    frame.grid(row = 11, column = 1, columnspan = 2,pady = 10, sticky = 'w')

    task_list = []  # List of task names
    task_id_list = []  # List of oid (oid meaning object id are assigned everytime a task was added, so each task can be referenced by a unique oid
    for i in tasks_to_show:
        task_list.append(i[0])
        task_id_list.append(str(i[4]))
    
    for i,task in enumerate(task_list):
        task_id = task_id_list[i]  # task_list and task_id_list are ordered so same index elements in each list correspond to each other 
        task_button = Button(frame, text=task, command=lambda task=task, task_id=task_id: show_options(task,task_id))  #  Creates button with the task name obtained from task_list, and passes task and it's Id to show_options function
        task_button.grid(row = i, column = 0, sticky = "w")  # task=task, task_id=task_id must be included since if not, then for show_options funcion it will be the last task and task_id in the loop passed and not the current loop values.


def show_options(task_name, task_id):
    """
    Creates popup window and 4 widgets inside the popup which consist of a label, and three buttons (Mark Complete button, Task Information button, and Delete button)
    Each button calls a different function to complete task indicated by button name.
    """
    popup = Toplevel(frame)
    popup.title("Task Actions")

    label = Label(popup, text=f"Actions for Task: {task_name}")
    label.pack(pady=10)

    complete_button = Button(popup, text="Mark as Complete", command=lambda: mark_complete_confirmation(task_id, popup))
    complete_button.pack()

    info_button = Button(popup, text="Task Information", command=lambda: task_info(task_name, task_id, popup))
    info_button.pack()

    delete_button = Button(popup, text="Delete Task", command=lambda: delete_confirmation(task_id, popup))
    delete_button.pack()

    global option_buttons  # To reference outside of function when needing to disable all of the buttons so as to prevent repeated clicking which led to printing of the same buttons
    option_buttons = [complete_button, info_button, delete_button]
    
    popup.geometry(f"+{root.winfo_x() + 250}+{root.winfo_y() + 220}")  # Keeps popup to remain appearing in the same place. Before this addition, popup kept moving more southeast at each calling.


def mark_task_complete(task_id, popup):
    """
    Updates database to mark task complete.
    """
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    update_query = "UPDATE tasks SET status = ? WHERE oid = ?"
    cursor.execute(update_query, ("Complete", task_id))

    date_completed = str(datetime.now()).strip()
    update_query = "UPDATE tasks SET date_completed = ? WHERE oid = ?"
    cursor.execute(update_query, (date_completed, task_id))

    connection.commit()
    connection.close()

    popup.destroy()


def mark_complete_confirmation(task_id, popup):
    """
    Confirms if user wants to mark complete since currently the app does not have an option to reverse this.
    Creates two buttons where can choose not to mark complete which would just close the popup and no action taken,
    or mark complete and will call mark_task_complete function to update database.
    """
    for button in option_buttons:
        button['state'] = 'disabled'  # Disables buttons in the popup outside this function so user can only click the not_complete_button or completed_button
    
    label_for_confirmation = Label(popup, text="Are you sure?").pack(pady=10)
    
    not_complete_button = Button(popup, text="No, Do Not Mark Complete Yet", command=lambda: popup.destroy())
    not_complete_button.pack()

    completed_button = Button(popup, text="Yes, Task Complete!", command=lambda: mark_task_complete(task_id, popup))
    completed_button.pack()


def task_info(task_name,task_id, popup):
    """
    Creates popup which shows information from database.
    Connected and fetched data from database to be displayed in GUI.
    """
    popup = Toplevel(frame)
    popup.title("Task Information")

    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    select_query = "SELECT * FROM tasks WHERE oid = ?"
    cursor.execute(select_query, (int(task_id),))
    task_info_list = cursor.fetchone()  # Fetches one row from the database table
    
    label_for_task = Label(popup, text=f"Task: {task_name}").pack(pady=10)
    label_for_status = Label(popup, text=f"Status: {task_info_list[1]}").pack(pady=10)
    label_for_date_created = Label(popup, text=f"Date Created: {task_info_list[2]}").pack(pady=10)
    label_for_date_completed = Label(popup, text=f"Date Completed: {task_info_list[3]}").pack(pady=10)

    popup.geometry(f"+{root.winfo_x() + 250}+{root.winfo_y() + 220}")

    connection.commit()
    connection.close()


def delete_task(task_id, popup):
    """
    Deletes task from database.
    """
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()

    delete_query = "DELETE FROM tasks WHERE oid = ?"
    cursor.execute(delete_query, (task_id,))
    
    connection.commit()
    connection.close()

    popup.destroy()


def delete_confirmation(task_id, popup):
    """
    Confirms if user wants to delete since currently the app does not have an option to reverse this.
    Creates two buttons where can choose not delete which would just close the popup and no action taken,
    or delete and will call delete_task function to update database.
    """
    for button in option_buttons:
        button['state'] = 'disabled'
    
    label_for_confirmation = Label(popup, text="Are you sure?").pack(pady=10)
    
    do_not_delete_button = Button(popup, text="No, Do Not Delete", command=lambda: popup.destroy())
    do_not_delete_button.pack()

    confirm_delete_button = Button(popup, text="Yes, Delete Permanently", command=lambda: delete_task(task_id,popup))
    confirm_delete_button.pack()


# Create file for Database if needed:
file_exists = os.path.isfile('todo.db')  # Checks if the *.db file already exists.
connection = sqlite3.connect('todo.db')  # Connects to database.
cursor = connection.cursor()  # Create cursor which is necessary to perform any database actions.
if file_exists == False:
    cursor.execute("""CREATE TABLE tasks (task text, status text, date_created text, date_completed text)""")  # If file not yet existent, this will create it as well as the database table.

# Create Widgets for Root Window:
heading = Label(root, text = "To Do App")  # Label() Allows for text display on the GUI
heading.grid(row = 0, column = 0, padx = 10, pady = 20)  # padx and pady values used to add extra space around the label widget (padx for horizontally, pady for vertically) for aesthetics.

task_entered = Entry(root, width = 40)  # Entry() Creates text box to allow user to type in task on the GUI
task_entered.grid(row = 1, column = 1, sticky = 'w')  # sticky = 'w' to place text box as far to the left in the column.

task_label = Label(root, text = "Enter task:")
task_label.grid(row = 1, column = 0, padx = 5, sticky = 'e')  # 'e' used for far right placement in a column.

add_button = Button(root, text = "Click here to Add Task", command = add_task)  # Button() creates button for user to click. This add_button will call the function add_task when clicked.
add_button.grid(row = 2, column = 1, pady = 5, sticky = 'w')

options = ["Tasks To Do", "Completed Tasks", "All tasks"]  # List of options to be placed in drop down menu.
option_clicked = StringVar()  # tkinter variable created so as to be able to save value from drop down widget and use .set()
option_clicked.set("Tasks To Do")  # .set() sets "Tasks To Do" as default for drop_down menu.

drop_down = OptionMenu(root, option_clicked, *options)  # OptionMenu() Creates drop down menu.
drop_down.grid(row = 3, column = 0, pady = 10, padx = 5, sticky = 'e')

enter_option_button = Button(root, text = "Click to View Tasks", command = lambda: query(option_clicked.get()))  # lambda used when need to pass parameter to a function, here whatever was clicked in drop down will be sent to query function.
enter_option_button.grid(row = 3, column = 1, pady = 10, sticky = 'w')

# Save changes to database and end connection
connection.commit()  # Whenever a connection to a database is made, .commit() is used to save changes and .close() to end the connection. 
connection.close()


root.mainloop()
