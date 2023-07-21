import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

# Vertex and color data
vertices = np.array([-0.5, -0.5, 0.0,  
                     0.5, -0.5, 0.0, 
                     0.0, 0.5, 0.0], dtype=np.float32)
                     
colors = np.array([1.0, 0.0, 0.0,  
                   0.0, 1.0, 0.0,
                   0.0, 0.0, 1.0], dtype=np.float32)

# Shader source code
vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

out vec3 v_color;

void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

fragment_src = """
# version 330
in vec3 v_color;
out vec4 out_color;

void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

# Initialize glfw  
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# Configure OpenGL context
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

# Create window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

glfw.make_context_current(window)

# Compile and link shaders
vertex_shader = OpenGL.GL.shaders.compileShader(vertex_src, GL_VERTEX_SHADER)
fragment_shader = OpenGL.GL.shaders.compileShader(fragment_src, GL_FRAGMENT_SHADER)
shader_program = OpenGL.GL.shaders.compileProgram(vertex_shader, fragment_shader)

# Vertex Array Object
VAO = glGenVertexArrays(1)
glBindVertexArray(VAO)

# Vertex Buffer Object
VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
glEnableVertexAttribArray(0) 
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

# Color Buffer Object
CBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, CBO)
glBufferData(GL_ARRAY_BUFFER, colors.nbytes, colors, GL_STATIC_DRAW)
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

glUseProgram(shader_program)

# Main render loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    
    glClearColor(0.2, 0.2, 0.2, 1) 
    glClear(GL_COLOR_BUFFER_BIT)

    glBindVertexArray(VAO)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)

# Terminate glfw
glfw.terminate()