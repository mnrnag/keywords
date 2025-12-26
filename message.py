import tkinter  as tk
from tkinter import messagebox

def info_box():
    messagebox.showinfo("Information","This is a information message")

def warning_box():
    messagebox.showinfo("Warning","This is a warning message")

def error_box():
    messagebox.showinfo("Error","A error has occured")


def question_box():
    response=messagebox.askquestion("Question","Do you like python")
    print("Response:",response)

def ok_cancel_box():
    response=messagebox.askokcancel("Comfirm","Do you wantto proceed")
    print("Response:",response)

def yes_no_box():
    response=messagebox.askyesno("Comfirm","Do you wantto save changes")
    print("Response:",response)

def retry_cancel_box():
    response=messagebox.askretrycancel("Retry","oporation failed,Retry?")
    print("Response:",response)

root=tk.Tk()
root.title('message box example')
root.geometry("300x400")

tk.Button(root, text="Show Info", command=info_box).pack(pady=5)

tk.Button(root, text="Show Warning", command=warning_box).pack(pady=5)

tk.Button(root, text="Show Error", command=error_box).pack(pady=5)

tk.Button(root, text="Ask Question", command=question_box).pack(pady=5)

tk.Button(root, text="Ask Ok Cancel", command=ok_cancel_box).pack(pady=5)

tk.Button(root, text="Ask Yes No", command=yes_no_box).pack(pady=5)

tk.Button(root, text="Ask Retry Cancel", command=retry_cancel_box).pack(pady=5)

root.mainloop()




