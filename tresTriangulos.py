import glfw
from OpenGL.GL import *

largura = 800
altura = 600

# Pontos do triângulo atual
pontos_temp = []

# Lista de triângulos completos
triangulos = []


def converter_para_OpenGL(x_mouse, y_mouse):
    x = (x_mouse / largura) * 2 - 1
    y = 1 - (y_mouse / altura) * 2
    return x, y


def atualizarViewport(window):
    largura_atual, altura_atual = glfw.get_framebuffer_size(window)
    glViewport(0, 0, largura_atual, altura_atual)


def mouse_button_callback(window, button, action, mods):

    global pontos_temp, triangulos

    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:

        x_mouse, y_mouse = glfw.get_cursor_pos(window)

        x, y = converter_para_OpenGL(x_mouse, y_mouse)

        # Adiciona ponto temporário
        pontos_temp.append((x, y))

        # Quando tiver 3 pontos, cria um triângulo
        if len(pontos_temp) == 3:

            # Guarda o triângulo completo
            triangulos.append(pontos_temp.copy())

            # Reinicia para começar novo triângulo
            pontos_temp.clear()


def key_callback(window, key, scancode, action, mods):

    global triangulos, pontos_temp

    if action == glfw.PRESS:

        # Limpar tela com tecla C
        if key == glfw.KEY_C:
            triangulos.clear()
            pontos_temp.clear()

        # Fechar janela com ESC
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)


def desenhar_triangulos():

    glColor3f(1, 0, 0)

    # Desenha todos os triângulos armazenados
    for triangulo in triangulos:

        glBegin(GL_TRIANGLES)

        for ponto in triangulo:
            glVertex2fv(ponto)

        glEnd()


def desenhar_pontos_temporarios():

    glPointSize(8)

    glColor3f(1, 1, 1)

    glBegin(GL_POINTS)

    for ponto in pontos_temp:
        glVertex2fv(ponto)

    glEnd()


def desenhar_linhas_temporarias():

    # Mostra linhas enquanto o triângulo está sendo criado

    if len(pontos_temp) >= 2:

        glColor3f(0, 1, 0)

        glBegin(GL_LINE_STRIP)

        for ponto in pontos_temp:
            glVertex2fv(ponto)

        glEnd()


def main():

    if not glfw.init():
        print("Erro ao inicializar o GLFW")
        return

    window = glfw.create_window(
        largura,
        altura,
        "Desenho de Triângulos",
        None,
        None
    )

    if not window:
        print("Erro ao criar a janela")
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glfw.set_mouse_button_callback(window, mouse_button_callback)

    glfw.set_key_callback(window, key_callback)

    glClearColor(0, 0, 0, 1)

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)

        atualizarViewport(window)

        # Desenha todos os triângulos já criados
        desenhar_triangulos()

        # Desenha os pontos temporários
        desenhar_pontos_temporarios()

        # Desenha linhas temporárias
        desenhar_linhas_temporarias()

        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()