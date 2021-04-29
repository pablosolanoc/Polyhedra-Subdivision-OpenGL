import glfw
from OpenGL.GL import  *
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from update import update_figure

vertex_src = """
# version 330 core

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

out vec3 v_color;

uniform mat4 rotation;

void main()
{
        gl_Position = rotation * vec4(a_position, 1.0);
        v_color = a_color;
}
"""

fragment_src = """
# version 330 core


in vec3 v_color;
out vec4 out_color;

void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

def get_new_figure(vertices_array, indices_array, vertices, indices, flag):
    vertices_array, indices_array = update_figure(vertices_array, indices_array)

    # print(vertices)
    # print(indices)
    # vertices = [-0.5257311121191336, 0.0, 0.8506508083520399, 0.5257311121191336, 0.0, 0.5257311121191336, -0.5257311121191336, 0.0, 0.8506508083520399, 0.5257311121191336, 0.0, -0.8506508083520399, 0.0, 0.8506508083520399, 0.5257311121191336, 0.0, 0.8506508083520399, -0.5257311121191336, 0.0, -0.8506508083520399, 0.5257311121191336, 0.0, -0.8506508083520399, -0.5257311121191336, 0.8506508083520399, -0.5257311121191336, 0.0, -0.8506508083520399, 0.5257311121191336, 0.0, 0.8506508083520399, 0.5257311121191336, 0.0, -0.8506508083520399, 0.5257311121191336, 0.0, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204, -0.5257311121191337, 0.0, 0.85065080835204]

    # indices_array = [0, 1, 4, 0, 4, 9, 9, 4, 5, 4, 8, 5, 4, 1, 8, 8, 1, 10, 8, 10, 3, 5, 8, 3, 5, 3, 2, 2, 3, 7, 7, 3, 10, 7, 10, 6, 7, 6, 11, 11, 6, 0, 0, 6, 1, 6, 10, 1, 9, 11, 0, 9, 2, 11, 9, 5, 2, 7, 11, 2]

    vertices = np.array(vertices_array, dtype=np.float32)
    indices = np.array(indices_array, dtype=np.uint32)

    # glClearBufferData(GL_ELEMENT_ARRAY_BUFFER, GL_RGBA32I, GL_INT, GL_INT, vertices)
    # glDeleteBuffers(1, EBO);
    # print(indices.nbytes)
    
    glBufferSubData(GL_ARRAY_BUFFER, 0, 3*4*len(vertices), vertices)

    
    glBufferSubData(GL_ELEMENT_ARRAY_BUFFER, 0, 3*4*len(indices), indices)


    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))


    return vertices_array, indices_array, vertices, indices


def window_resize(window, width, height):
    glViewport(0, 0, width, height)

def main():
    # Initialize the library
    
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.set_window_pos(window, 400, 200)

    glfw.set_window_size_callback(window, window_resize)

    # Make the window's context current
    glfw.make_context_current(window)
    

    # vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
    #          0.5, -0.5, -1.0, 0.0, 1.0, 0.0,
    #          -0.5,  0.5, -1.0, 0.0, 0.0, 1.0,
    #          0.5, 0.5, 0.0, 1.0, 1.0, 1.0,
    #          0.0, 0.75, 0.0, 1.0, 1.0, 0]

    # indices = [0, 1, 2,
    #            1, 2, 3,
    #            2, 3, 4]

    a = 0.525731112119133606
    b = 0.850650808352039932
    a = 0.1
    # vertices = [-0.5, -0.5, 0.5, 1.0, 0.0, 0.0,
    #          0.5, -0.5, 0.5, 0.0, 1.0, 0.0,
    #          0.5,  0.5, 0.5, 0.0, 0.0, 1.0,
    #         -0.5,  0.5, 0.5, 1.0, 1.0, 1.0,

    #         -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
    #          0.5, -0.5, -0.5, 0.0, 1.0, 0.0,
    #          0.5,  0.5, -0.5, 0.0, 0.0, 1.0,
    #         -0.5,  0.5, -0.5, 1.0, 1.0, 1.0]

    # indices = [0, 1, 2, 2, 3, 0,
    #             4, 5, 6, 6, 7, 4,
    #             4, 5, 1, 1, 0, 4,
    #             6, 7, 3, 3, 2, 6,
    #             5, 6, 2, 2, 1, 5,
    #             7, 4, 0, 0, 3, 7]

    # vertices_array = [-a, 0.0, b,
    #     a, 0.0, b,
    #     -a, 0.0, -b,
    #     a, 0.0, -b,
    #     0.0, b, a,
    #     0.0, b, -a,
    #     0.0,-b, a,
    #     0.0, -b, -a,
    #     b, a, 0.0,
    #     -b, a, 0.0,
    #     b, -a, 0.0,
    #     -b, -a, 0.0
    # ]


    # indices_array = [0,1,4,
    #         0,4,9,
    #         9,4,5,
    #         4,8,5,
    #         4,1,8,
    #         8,1,10,
    #         8,10,3,
    #         5,8,3,
    #         5,3,2,
    #         2,3,7,
    #         7,3,10,
    #         7,10,6,
    #         7,6,11,
    #         11,6,0,
    #         0,6,1,
    #         6,10,1,
    #         9,11,0,
    #         9,2,11,
    #         9,5,2,
    #         7,11,2,
    #         0, 0, 0,
    #         0, 0, 0,
    #         0, 0, 0
    # ]
    
    vertices_array = [
        a, 0, 0,
        0, -a, 0,
        -a, 0, 0,
        0, a, 0,
        0, 0, a,
        0, 0, -a,
    ]

    indices_array = [
        0, 1, 4,
        1, 2, 4,
        2, 3, 4,
        3, 0, 4,
        0, 1, 5,
        1, 2, 5,
        2, 3, 5,
        3, 0, 5,
    ]

    indices = np.array(indices_array, dtype=np.uint32)
    tamano = 0

    vertices = np.array(vertices_array, dtype=np.float32)
    # print(vertices)
    # vertices_2 = np.array(vertices_2, dtype=np.float32)
    # colors = np.array(colors, dtype=np.float32)

    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    # print(VBO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER,  1000000000, None, GL_STATIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, 3*4*len(vertices), vertices)
    

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 1000000000, None, GL_STATIC_DRAW)
    glBufferSubData(GL_ELEMENT_ARRAY_BUFFER, 0, 3*4*len(indices), indices)

    # position = glGetAttribLocation(shader, "a_position")
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
    # glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
    

    # color = glGetAttribLocation(shader, "a_color")
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(12))


    glUseProgram(shader)
    glClearColor(0, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)

    rotation_loc = glGetUniformLocation(shader, "rotation")
    # glClearColor(0.1, 0.1, 0.1, 1)

    # Loop until the user closes the window
    flag = 4

    while not glfw.window_should_close(window):
        
        
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        valor = glfw.get_time()
        if(valor > flag):

            # if flag/flag == 1:
                vertices_array, indices_array, vertices, indices = get_new_figure(vertices_array, indices_array, vertices, indices, flag)
                flag += 4

        # print(flag)

        rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
        rot_x = 1
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
        # rot_y = 1

        glUniformMatrix4fv(rotation_loc, 1, GL_FALSE, rot_x * rot_y)
        
        # glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
        # glDrawArrays(GL_TRIANGLES, 0, len(indices))
        # print(glfw.get_time())
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)
        # Poll for and process events
        # glfw.poll_events()

        

    glfw.terminate()

if __name__ == "__main__":
    main()