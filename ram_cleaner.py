from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import tkinter as tk
import os


def getpwd():
    password = tk.simpledialog.askstring("Password", "Enter sudo password:", show='*')
    return password


def clear(i):
    password = getpwd()
    bool=1
    os.system("sync")
    if i == 1:
        command = 'sudo sh -c "echo  1 > /proc/sys/vm/drop_caches"'
        bool=os.system("echo %s|sudo -S %s" % (password, command))

    elif i == 2:
        command = 'sudo sh -c "echo  2 > /proc/sys/vm/drop_caches"'
        bool=os.system("echo %s|sudo -S %s" % (password, command))

    elif i == 3:
        command = 'sudo sh -c "echo  3 > /proc/sys/vm/drop_caches"'
        bool=os.system("echo %s|sudo -S %s" % (password, command))

    if bool == 0:
        messagebox.showinfo("Success","Ram freed")

    else:
        messagebox.showerror("Error", "The password you entered is incorrect, Please try again")


def showinfo(num):
    if num == 1:
        messagebox.showinfo("Information","Page cache,sometimes also called disk cache,is a transparent cache for the pages originating from a secondary storage device such as a hard disk drive (HDD) or a solid-state drive (SSD)")
    elif num == 2:
        messagebox.showinfo("Information", "It will clear pagecache,dentries and inode on RAM read from disk")
    elif num == 3:
        messagebox.showinfo("Information","Dentries is a data structure which represents a directory or a folder and The inode (index node) is a data structure in a Unix-style file system that describes a file-system object such as a file or a directory")
    else:
        return


myapp = Tk()

myapp.configure(background="#191919")
myapp.title("Ram cleaner")
myapp.geometry("600x450+631+290")

Button1 = Button(myapp)
Button1.place(relx=0.083, rely=0.822, height=24, width=120)
Button1.configure(command=lambda: clear(1), background="#d6d6d6")
Button1.configure(text="Clear PageCache")

Button2 = Button(myapp)
Button2.place(relx=0.39, rely=0.822, height=24, width=125)
Button2.configure(command=lambda: clear(3), background="#d6d6d6")
Button2.configure(text="Clear All")

Button3 = Button(myapp)
Button3.place(relx=0.70, rely=0.822, height=24, width=150)
Button3.configure(command=lambda: clear(2), background="#d6d6d6")
Button3.configure(text="Clear dentries and inodes")

Button4 = Button(myapp)
Button4.place(relx=0.15, rely=0.889, height=24, width=25)
Button4.configure(command=lambda: showinfo(1), background="#FFFF66")
Button4.configure(text="?")
Button4.configure(cursor="question_arrow")

Button5 = Button(myapp)
Button5.place(relx=0.47, rely=0.889, height=24, width=25)
Button5.configure(command=lambda: showinfo(2), background="#FFFF66")
Button5.configure(text="?")
Button5.configure(cursor="question_arrow")

Button6 = Button(myapp)
Button6.place(relx=0.8, rely=0.889, height=24, width=25)
Button6.configure(command=lambda: showinfo(3), background="#FFFF66")
Button6.configure(text="?")
Button6.configure(cursor="question_arrow")

Label1 = Label(myapp)
Label1.place(relx=0.35, rely=0.689, height=21, width=170)
Label1.configure(text="Your current RAM usage")
Label1.config(bg='#191919', fg='white')

Frame1 = Frame(myapp)
Frame1.place(relx=0.067, rely=0.022, relheight=0.63374, relwidth=0.875)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
wid = Frame1.winfo_id()

messagebox.showwarning("Warning","Ram and CPU status is shown using htop command in xterm terminal. If don't have htop and xterm,The app won't work properly, Install them and try again")
result=messagebox.askyesno("Requirements","Do you have Htop and xterm installed")
if result != 1:
    myapp.destroy()
    exit()

os.system('xterm -into %d -geometry 90x190 -sb "htop" &' % wid)
myapp.mainloop()


