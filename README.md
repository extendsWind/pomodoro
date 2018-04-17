# pomodoro 

![screenshot](app_screenshot.png)

![screenshot2](app_screenshot2.png)

A simple GUI app for pomodoro technech written by python3 with tkinter.

Just install the python dependence and run the .py file.

Dependence:

- tkinter for GUI
- pygame for playing sounds (only for sound version)


## No Sound Version

this version rely on tkinter and need two files, `pomodoro.pyw` and `clock.gif`, just run:

```
python pomodoro.pyw
```

- left click for switching between the work and rest mode.


## Sound Version 


` python pomodoro_sound.pyw` run the program.

simple operation:

- left click for switching between the work and rest mode.
- right click for turn on/off the sound.

The sound file can be changed, just change the corresponding file name and the working sound length(the sound is played repeatly, auto get the sound length has not been supported now). 

The sound version may cause high cpu usage for the bug of pygame in some linux distribution, which may be fixed by compile the pygame source. [Some reference](https://github.com/pygame/pygame/issues/331)

- Windows 10 is tested without the problem 
- Manjaro 16.08 has the problem.


## other

The timer can not pause for it may be unnecessary in pomodoro technech.
