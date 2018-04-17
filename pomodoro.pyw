import tkinter


"""
# TODO  list:
- [x] change icon. problem in tkinter, change to remove the icon
- [x] function packing
- generate a usage record
"""

"""
input parameters by user
"""
# pomodoro
workTime = 25
restTime = 5

# better to use gif image
clock_icon_file = "clock.gif"

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
        label1["background"] = "#FF8C00"


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


if __name__ == "__main__":

    # thinter init
    root = tkinter.Tk()

    # set the icon
    img = tkinter.PhotoImage(file=clock_icon_file)
    root.tk.call('wm', 'iconphoto', root._w, img)

    screenWid, screenHeight = root.maxsize()
    win_size = "200x30+70+%d" % (screenHeight - 100)
    root.geometry(win_size)
    root.wm_attributes("-topmost", 1)  # always on top
    root.title(" ")

    label1 = tkinter.Label(text="{:d} : 0{:d}".format
                           (tMin, tSec), height=10, width=15)
    label1.pack()
    label1.bind("<Button-1>", label_click)

    # start timer
    label1.after(1000, update_label, label1)
    root.mainloop()
