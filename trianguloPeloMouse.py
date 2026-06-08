from OpenGL.GL import *
import glfw
triangulo = None

def atualizarViewport(window):
    largura, altura = glfw.get_framebuffer_size(window)
    glViewport(0, 0, largura, altura)

def criarTriangulo(x, y):
    largura = 0.25
    altura = 0.3
    
    return [(x, y), (x-largura, y-altura), (x+largura, y-altura)]

def desenharTriangulo():
    if triangulo is None:
        return
    
    glBegin(GL_TRIANGLES)
    
    glColor3f(1, 0, 0)
    glVertex2f(triangulo[0][0], triangulo[0][1])
    
    glColor3f(0, 1, 0)
    glVertex2f(triangulo[1][0], triangulo[1][1])
    
    glColor3f(0, 0, 1)
    glVertex2f(triangulo[2][0], triangulo[2][1])
    glEnd()

def cliqueMouse(window, button, action, mods):
    global triangulo
    if(button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS):
        x_mouse, y_mouse = glfw.get_cursor_pos(window)
        largura, altura = glfw.get_window_size(window)
        x, y = converterParaOpenGL(x_mouse, y_mouse, largura, altura)
        triangulo = (criarTriangulo(x, y))

def converterParaOpenGL(x_mouse, y_mouse, largura, altura):
    x = (x_mouse/largura) * 2 - 1
    y = 1 - (y_mouse/altura) * 2
    return x, y

def main():
    if not glfw.init():
        print("Não foi possível iniciar o glfw")
        return
    
    largura = 800
    altura = 600
    
    window = glfw.create_window(largura, altura, "Triângulo dinâmico", None, None)
    if not window:
        print("Erro ao criar a janela")
        return
    
    glfw.make_context_current(window)
    
    glfw.set_mouse_button_callback(window, cliqueMouse)
    
    while not glfw.window_should_close(window):
        atualizarViewport(window)
        glClear(GL_COLOR_BUFFER_BIT)
        
        desenharTriangulo()
        
        glfw.swap_buffers(window)
        glfw.poll_events()
        
    glfw.destroy_window(window)
    glfw.terminate()
    
if __name__ == "__main__":
    main()