# Unit 0 Project: Animation

## Intial Contents
This is the starter code for [Project 0: Animation](http://cs.fablearn.org/courses/cs9/unit00/project).
Here's what is included:

- `README.md` You're looking at it, or at least the formatted version. (Click "raw" to see the unformatted version.) Every project has a README explaining what it is.
- `project.py` When this is run, it should draw your project. (If your project is well-organized, there might not be much code in `project.py`. Instead, it might import functions from other modules.)
- `settings.py` This is where you will store your settings for your animation. Feel free to add more settings to further parameterize your project.

## Modules
The modules in this project include:
1. helpers.py
Useful functions created by Chris Proctor that was provided alongside the starter code. The functions I used include fly, no_delay, and restore_state_when_finished. These functions allow me to move the turtle to different places as well as allow my animation to run.

2. misc.py
Miscellaneous functions to assist with my animation. These functions allow me to set the background in different frames in my animation(sky_background, ts_color, and ts_background), print different words(words and ts_words), and position the turtle for different objects(k_positioning and a_positioning)

3. object.py
Draw the object that I will use for my animation. In object.py, there is the function apple which draws an apple with a customizable size, function knife which draws a knife with a customizable size, as well as knife_in_apple which uses the two previously mentioned objects drawn together to create an illusion that the knife is inside the apple.

4. project.py
Draws the animation using the different functions imported from the modules. When this file is run, the animation will be drawn.

## Settings
The settings that I use for my animations. This allows me to customize the total number of frames, number of repeats, sleeptime(time between each frame), and the size of the turtle screen.

## How to use
To run my animation, simply go into the folder named project-animation-bobotime1 and run the project.py file.
