from tkinter import *
import serial
from time import sleep
import tkinter as tk
import webbrowser
from tkinter import filedialog
import time

#function to connect to device start code
def measures_window():
    bottom.delete('all')
    bottom.config(bg="#0C2C3C")
    bottom.create_text(40, 40, fill="red", font="Times 13", text="a")


def protocols_window():
    bottom.delete('all')
    bottom.config(bg="#0C2C3C")
    bottom.create_text(40, 40, fill="red", font="Times 13", text="b")


def configurations_window():
    bottom.delete('all')
    bottom.config(bg="#0C2C3C")
    bottom.create_text(40, 40, fill="red", font="Times 13", text="c")


def quick_logs_window():
    bottom.delete('all')
    bottom.config(bg="#0C2C3C")
    bottom.create_text(40, 40, fill="red", font="Times 13", text="d")


def help_window():
    window = tk.Toplevel(mb2, bg="#124057")
    window.geometry("400x400")
    window.resizable(0, 0)
    icon = PhotoImage(file='4.png')
    window.tk.call('wm', 'iconphoto', window._w, icon)
    help_frame = Frame(window, bg="#124057", width=400, height=400)
    help_frame.pack(side=TOP)
    help_frame.pack()

def about_window():
    bottom.delete('all')
    bottom.config(bg="#0C2C3C")
    bottom.create_text(40, 40, fill="red", font="Times 13", text="f")


def update_window():
    bottom.delete('all')
    bottom.config(bg="#0C2C3C")
    bottom.create_text(40, 40, fill="red", font="Times 13", text="e")


def saveas():
    filedialog.askopenfilename(initialdir="/",title = "Select file",filetypes = (("jpeg files"),("all files","*.*")))

timer = 0

def start():
    bottom.delete('all')
    bottom.config(bg = "#0C2C3C")
    bottom.create_text(40,40,fill="red",font="Times 13",text="nothing")
    while(ann()):
        time.after(1000,start())
        timer = timer+1


def callback():
    webbrowser.open_new("http://www.google.com")

def history():
    bottom.delete('all')
    bottom.config(bg="#0C2C3C")
    bottom.create_text(40, 40, fill="red", font="Times 13", text="f")


def analyzing():
    try:
        serial_port = serial.Serial(port='com8', baudrate=9600, timeout=10, parity=serial.PARITY_NONE, bytesize=serial.EIGHTBITS,
                                stopbits=serial.STOPBITS_ONE, xonxoff=False)
        serial_port.flushInput()
        print(serial_port.name)
        serial_port.write("\n".encode())
        serial_port.write("?".encode())
        bytes_to_read = serial_port.inWaiting()
        sleep(.5)
        data = serial_port.read(bytes_to_read).decode()
        print(data)
    except:
        print("[-] No data received")
    #serial_port
# the ending of the function to connect to device

def ann():
    console = serial.Serial(
        port='COM8',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=4
    )

    console.isOpen()
    console.inWaiting()

    input_data = console.read(225)
    print(input_data)


master = Tk()

master.geometry("700x560")
master.resizable(0, 0)


#master.overrideredirect(1)

master.title('Optimum RS')
icon = PhotoImage(file='4.png')

master.tk.call('wm','iconphoto',master._w,icon)

topframe = Frame(master,bg="#124057",width=700,height=47)
topframe.pack(side=TOP)
topframe.pack()

topframe1 = Frame(topframe,bg="#124057",width = 340,height = 47)

topframe1.grid()
#topframe2.grid()

e1 = Entry(topframe,bg="#0C2C3C",bd=0,foreground="#fff")
#e1.insert(16,"Search")

e1.grid(row=0, column=10,ipady=4,ipadx=40, pady=6,padx=15)
Button(topframe, text='Search',relief=RIDGE,bg="#124057",borderwidth=1,
                activebackground="#1F6A8F",activeforeground="white",foreground="#ffffff",compound=LEFT).grid(row=0,
                column=15, sticky=W, pady=6,padx=2,ipady=2.5,ipadx=7)


biz = Button(topframe, relief=RAISED,bg="#124057",borderwidth=0,
                activebackground="#1F6A8F",activeforeground="white",foreground="#ffffff").grid(row=0,column=5,padx=12,)

labelk=Label(topframe1, bg="#124057",width=50,height=2)
labelk.pack()


m = PanedWindow(orient=HORIZONTAL,bd=0,borderwidth=0,bg="#0C2C3C",sashwidth=0)
m.pack(fill=BOTH, expand=1)

top = Frame(m,bg="#124057",bd=0,borderwidth=0)
m.add(top)




mb = Menubutton(top, text="    File              ", relief=RAISED,bg="#124057",width=150,height=95,bd=0,borderwidth=0,direction="right",
                activebackground="#1F6A8F",activeforeground="white",foreground="#ffffff",compound=LEFT)

image = PhotoImage(file="file1.png")
mb.config(image=image)
mb.image = image


mb1 = Menubutton(top, text="     Analyze     ", relief=RAISED,bg="#124057",width=150,height=95,bd=0,borderwidth=0, direction="right",
                 activebackground="#1F6A8F",activeforeground="white",foreground="#ffffff",compound=LEFT)

image = PhotoImage(file="analyze.png")
mb1.config(image=image)
mb1.image = image

mb2 = Menubutton(top, text="      View        ", relief=RAISED,bg="#124057",width=150,height=95,bd=0, borderwidth=0, direction="right",
                 activebackground="#1F6A8F",activeforeground="white",foreground="#ffffff", compound=LEFT)
#1E6182
image = PhotoImage(file="view.png")
mb2.config(image=image)
mb2.image = image

mb3 = Menubutton(top, text="      Update  ", relief=RAISED,bg="#124057",width=150,height=95,bd=0,borderwidth=0, direction="right",
                 activebackground="#1F6A8F",activeforeground="white",foreground="#ffffff", compound=LEFT)

image = PhotoImage(file="update.png")
mb3.config(image=image)
mb3.image = image


mb4 = Menubutton(top, text="       Help    ", relief=RAISED,bg="#124057",width=150,height=95,bd=0,borderwidth=0, direction="right",
                 activebackground="#1F6A8F",activeforeground="white",foreground="#ffffff", compound=LEFT)

image = PhotoImage(file="seething.png")
mb4.config(image=image)
mb4.image = image


mb.menu = Menu(mb, tearoff=0,bg="#124057",fg="#ffffff",activebackground="#1F6A8F", foreground= "#fdfdfd",activeborderwidth=10,activeforeground="grey")
mb["menu"] = mb.menu


mb1.menu1 = Menu(mb1, tearoff=0,bg="#124057",fg="#ffffff",activebackground="#1F6A8F",activeborderwidth=10,activeforeground="grey")
mb1["menu"] = mb1.menu1

mb2.menu2 = Menu(mb2, tearoff=0,bg="#124057",fg="#ffffff",activebackground="#1F6A8F",activeborderwidth=10,activeforeground="grey")
mb2["menu"] = mb2.menu2

mb3.menu3 = Menu(mb3, tearoff=0,bg="#124057",fg="#ffffff",activebackground="#1F6A8F",activeborderwidth=10,activeforeground="grey")
mb3["menu"] = mb3.menu3

mb4.menu4 = Menu(mb4, tearoff=0,bd=0,bg="#124057",fg="#ffffff",activebackground="#1F6A8F",activeborderwidth=10,activeforeground="grey")
mb4["menu"] = mb4.menu4

mb.menu.add_command(label="     Save As                    ",command = saveas)

mb.menu.add_command(label="     Email                      ")
mb.menu.add_command(label="     History                    ",command = history)
mb.menu.add_command(label="     Exit                       ", command=ann)


mb1.menu1.add_command(label="   Start                      ",command = start)
mb1.menu1.add_command(label="   Stop                       ")
mb1.menu1.add_command(label="   Forward                    ")
mb1.menu1.add_command(label="   Backward  "
                            "                 ")
mb2.menu2.add_command(label="   Measures                   ", command=measures_window)
mb2.menu2.add_command(label="   Protocols                  ", command=protocols_window)
mb2.menu2.add_command(label="   Configurations             ", command=configurations_window)
mb2.menu2.add_command(label="   Quick Logs                 ", command=quick_logs_window)


#mb3.menu3.add_command(label="   Auto Update                ")
#mb3.menu3.add_command(label="   Ask every time             ")
mb3.menu3.add_command(label="   Update Options              ", command=update_window)


mb4.menu4.add_command(label="   Help                       ", command=help_window)
mb4.menu4.add_command(label="   Getting Started            ", command=callback)
mb4.menu4.add_command(label="   About                      ", command=about_window)

mb.pack()
mb1.pack()
mb2.pack()
mb3.pack()
mb4.pack()
#w.pack()

#the other frame
bottom = Canvas(m, bg="#0C2C3C",bd=0,borderwidth=0,highlightthickness=0)
m.add(bottom)

mainloop()