#!/bin/python3

import tkinter
import datetime  # for log

"""
# TODO  list:
- [x] change icon. problem in tkinter, change to remove the icon
- [x] function packing
- [x] generate a usage record
"""

# thinter init
root = tkinter.Tk()
screenWidth, screenHeight = root.maxsize()

"""
input parameters by user -----
"""
# pomodoro
workTime = 25
restTime = 5

logFilename = "pomodoro.log"

# window size
windowWidth = 100
windowHeight = 40
windowX = 10
windowY = screenHeight - 60
"""
input parameters by user ----- End
"""

logFile = open(logFilename, 'a+')

# better to use gif image
# clock_icon_file = "clock.gif"

isWork = True
isStopped = False

# label show
tMin = workTime
tSec = 0


def set_label_time(label):
    if tSec >= 10 and tMin >= 10:
        label.config(text="{:d} : {:d}".format(tMin, tSec))
    elif tSec < 10 and tMin >= 10:
        label.config(text="{:d} : 0{:d}".format(tMin, tSec))
    elif tSec >= 10 and tMin < 10:
        label.config(text="0{:d} : {:d}".format(tMin, tSec))
    elif tSec < 10 and tMin < 10:
        label.config(text="0{:d} : 0{:d}".format(tMin, tSec))


# this function will be invoked every second
def update_label(label1):
    global tSec
    global tMin
    global isStopped
    global isWork

    tSec -= 1
    if tSec == -1:
        tSec = 59
        tMin -= 1

    if tMin != -1:
        set_label_time(label1)
        label1.after(1000, update_label, label1)

    else:
        isWork = not isWork
        isStopped = True
        label1["background"] = "#33FF00"

        if isWork is False:  # if stop from work mode
            logFile.write(str(datetime.datetime.now()) + " ")
            logFile.write(entry1.get())
            logFile.write("\n")
            logFile.flush()


# click the label for switch the working mode
def label_click(event):
    global tMin, tSec, isStopped
    global workTime, restTime, isWork
    label = event.widget

    if isStopped:
        if isWork:
            tMin = workTime
            tSec = 0
            label.after(1000, update_label, label)
            label["background"] = "gray85"
            isStopped = False
        else:
            tMin = restTime
            tSec = 0
            label.after(1000, update_label, label)
            label["background"] = "gray85"
            isStopped = False
    else:
        tMin = 0
        tSec = 0
        set_label_time(label)

        # give a mark if the pomodoro time is broken by click
        if isWork is True:
            logFile.write("p- ")


if __name__ == "__main__":

    # set the icon
    #    img = tkinter.PhotoImage(file=clock_icon_file)
    #    root.tk.call('wm', 'iconphoto', root._w, img)

    win_size = "{:d}x{:d}+{:d}+{:d}".format(windowWidth, windowHeight,
                                            windowX, windowY)
    root.geometry(win_size)
    root.wm_attributes("-topmost", 1)  # always on top
    root.title(" ")

    label1 = tkinter.Label(text="{:d} : 0{:d}".format(tMin, tSec))
    #                           (tMin, tSec), height=10, width=15)

    #    label1.grid(row=0, column=0, padx=1, pady=1)
    label1.pack()
    label1.bind("<Button-1>", label_click)

    entry1 = tkinter.Entry(root)
    #    entry1.grid(row=1, column=0, padx=1, pady=1)
    entry1.pack()

    # start timer
    label1.after(1000, update_label, label1)
    root.mainloop()
