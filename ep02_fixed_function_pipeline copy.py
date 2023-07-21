import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos


# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# make the context current
glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)

glClearColor(0, 0.1, 0.1, 1)

# the main application loop
while not glfw.window_should_close(window):
    #Poll for keyboard and mouse events, and then call the appropriate functions.
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    ct = glfw.get_time()  # returns the elapsed time, since init was called

    #Resets the identity matrix. 
    # This is important because OpenGL multiplies all positions and rotations through the current matrix. 
    # If the current matrix is not reset, then the results of the rendering operation will be unpredictable.
    glLoadIdentity()
    
    glScale(abs(sin(ct)), abs(sin(ct)), 1)
    #Rotates 45 degrees on the z-axis
    glRotatef(sin(ct) * 45, 0, 0, 1)
    #Translates the position of the object(the current matrix) by a specified amount.
    #Typically used to move objects around in the scene. 
    # It can also be used to create illusions of depth and perspective.
    glTranslatef(sin(ct), cos(ct), 0)

    glDrawArrays(GL_TRIANGLES, 0, 3)
    #Swaps the front and back buffers to display the rendered content on screen
    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()