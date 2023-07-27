# let's import the thinker module 
import tkinter as tk

# let's see whats inside tk module
# print(dir(tk))

# Create the empty gui
root = tk.Tk()

# let's define functions
def add():
    print('Adding task to the list')
    
    # let's get the text written inside the entry widget
    data = entry.get()
    
    #let's check first if data is empty or not
    if data:
        
        # shift that text to listbox
        # arguments: index number (0 --> First element), data you want put
        # task_list.insert(0, data)
        task_list.insert(tk.END, data)
        
        #let's clean the empty widget
        entry.delete(0, tk.END)

def delete():
    print('Deleting task form the list')
    
    # let's delete the active element from the list
    task_list.delete(tk.ACTIVE)
    
# let's define its size
root.geometry('400x400')

# let's stop the resizing
root.resizable(width=False, height=False)

# let's change the title
root.title('To Do List')

# let's start adding components or widgets
# let's ad entry widget
entry = tk.Entry(root)
entry.pack(padx=30, pady=10, fill='x')

# let's add a button --> add task
# In command parameter, we only put the function name
add_button = tk.Button(root, text='Add Task', width=20, bg='black', fg='white', command=add)
add_button.pack()

# let's add the task list
task_list = tk.Listbox(root)
task_list.pack(fill='x', padx=20, pady=10)

# let's add one more button --> delete task
delete_button = tk.Button(root, text='Delete Task', width=20, bg='black',fg='white', command=delete)
delete_button.pack()

# let's use the mainloop
# it display's the GUI continuously
# it listens for any event on gui
root.mainloop()