import tkinter
import time
from pygame import mixer

"""
# TODO  list:
- [X] change icon
- [X] function packing
- [ ] record usage
"""


"""
input parameters by user
"""
tickFile = "tick.wav"
tickSoundLength = 24  # second
remindFile = "remind.wav"

workTime = 25
restTime = 5

clock_icon_file = "clock.gif"  # better to use gif image
# logFilename = "pomodoro.log"

"""
input parameters by user ----- End
"""

# logFile = open(logFilename, 'a+')


# for sound
soundStartTime = 0
isPlaySound = True

# for a bug in pygame, pygame installed by pip may cause high
# cpu usage in some linux distribution
mixer.init()
tickSound = mixer.Sound("tick.wav")
remindSound = mixer.Sound("remind.wav")

# pomodoro
isWork = True
isStopped = False

# label show
tMin = 0
tSec = 0


# length of sound is needed
def play_tick_sound(length):
    global soundStartTime
    if soundStartTime == 0:
        soundStartTime = time.time()
        tickSound.play()
    if tickSound.get_volume() == 0:
        tickSound.set_volume(100)
    now_time = time.time()
    if now_time - soundStartTime >= length - 1:
        soundStartTime = 0


def stop_tick_sound():
    tickSound.set_volume(0)


def set_label_time(label):
    if tSec >= 10 and tMin >= 10:
        label.config(text="{:d} : {:d}".format(tMin, tSec))
    elif tSec < 10 and tMin >= 10:
        label.config(text="{:d} : 0{:d}".format(tMin, tSec))
    elif tSec >= 10 and tMin < 10:
        label.config(text="0{:d} : {:d}".format(tMin, tSec))
    elif tSec < 10 and tMin < 10:
        label.config(text="0{:d} : 0{:d}".format(tMin, tSec))


def update_label(label1):
    global tSec
    global tMin
    global isStopped
    global isWork
    global isPlaySound

    tSec -= 1
    if tSec == -1:
        tSec = 59
        tMin -= 1

    if tMin != -1:
        set_label_time(label1)
        label1.after(1000, update_label, label1)
        if isPlaySound and isWork:
            play_tick_sound(tickSoundLength)

    else:
        isWork = not isWork
        isStopped = True
        stop_tick_sound()
        if isPlaySound:
            remindSound.play()
        label1["background"] = "#FF8C00"


# to close the sound
def label_click(event):
    global isPlaySound
    global tickSound
    global remindSound
    isPlaySound = not isPlaySound

    if isPlaySound:
        play_tick_sound(24)
    else:
        stop_tick_sound()


def label_right_click(event):
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

    root = tkinter.Tk()

    # set the icon
    img = tkinter.PhotoImage(file=clock_icon_file)
    root.tk.call('wm', 'iconphoto', root._w, img)

    screenWid, screenHeight = root.maxsize()
    win_size = "200x30+70+%d" % (screenHeight - 100)
    root.geometry(win_size)
    root.wm_attributes("-topmost", 1)  # always on top
    root.title(" ")
    # root.minsize(200, 30)

    Label1 = tkinter.Label(text="0{:d} : 0{:d}".format(tMin, tSec),
                           height=10, width=15)
    Label1.pack()
    Label1.bind("<Button-3>", label_click)
    Label1.bind("<Button-1>", label_right_click)

    isWork = True
    tMin = workTime
    Label1.after(1000, update_label, Label1)

    root.mainloop()
