#Creating Window
from tkinter import*


root=Tk()

#7.creating functions
def Addition():
    sum = int(first_Number.get()) + int(second_Number.get())
    #sum = 10 + 20
    # sum = 30 -> Datatype  : int  
    my_Result.set(sum)

#Creating window size and title
root.title("GUI Addition")
root.geometry("700x300")
my_Result = StringVar()

#Creating window labels
Label(root,text="Enter First Number:").grid(row=0,column=0)
Label(root,text="Enter Second Number:").grid(row=1,column=0)
Label(root,text="Addition is:").grid(row=2,column=0)

#Creating text boxes
first_Number = Entry(root)
first_Number.grid(row=0,column=1)
second_Number = Entry(root)
second_Number.grid(row=1,column=1)

#5.Creating a button for submitting
Button(root,text="Submit", command = Addition).grid(row=2,column=2)

#6.Result

Label(root, text="", textvariable=my_Result).grid(row=2, column=1)


mainloop()