import glfw
from OpenGL.GL import *

largura = 800
altura = 600
pontos = []
cor = [1.0, 1.0, 1.0]

def converter_para_OpenGL(x_mouse, y_mouse):
    x = (x_mouse/largura) * 2 - 1
    y = 1 - (y_mouse/altura) * 2
    return x, y

def atualizarViewport(window):
    largura, altura = glfw.get_framebuffer_size(window)
    glViewport(0, 0, largura, altura)

def mouse_button_callback(window, button, action, mods):    
    if(button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS):
        x_mouse, y_mouse = glfw.get_cursor_pos(window)
        x, y = converter_para_OpenGL(x_mouse, y_mouse)
        if len(pontos) < 3:
            pontos.append((x,y))

def key_callback(window, key, scancode, action, mods):
    global cor
    if(action == glfw.PRESS or action == glfw.REPEAT):
        if(key == glfw.KEY_R):
            cor = [1.0, 0.0, 0.0]

        elif(key == glfw.KEY_G):
            cor = [0.0, 1.0, 0.0]

        elif(key == glfw.KEY_B):
            cor = [0.0, 0.0, 1.0]

        elif(key == glfw.KEY_Y):
            cor = [1.0, 1.0, 0.0]

        elif(key == glfw.KEY_M):
            cor = [1.0, 0.0, 1.0]

        elif(key == glfw.KEY_W):
            cor = [1.0, 1.0, 1.0]
            
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

def desenhar_triangulo():
    if len(pontos) == 3:

        glColor3fv(cor)  # define a cor UMA vez
        glBegin(GL_TRIANGLES)
        for v in pontos:
            glVertex2fv(v)
        glEnd()
        
def desenhar_pontos():
    glPointSize(8)
    glColor3f(1,1,1)
    glBegin(GL_POINTS)
    for p in pontos:
        glVertex2fv(p)
    glEnd()

def main():
    if not glfw.init():
        print("Erro ao incializar o GLFW")
        return
    
    window = glfw.create_window(largura, altura, "Triângulo com Eventos de Mouse e Teclado", None, None)
    
    if not window:
        print("Erro ao criar a janela")
        return
    
    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_key_callback(window, key_callback)
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        atualizarViewport(window)
        
        desenhar_triangulo()
        desenhar_pontos()
        
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()
    
if __name__ == "__main__":
    main()