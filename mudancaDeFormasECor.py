import glfw
from OpenGL.GL import *
import random as rd

modo_atual = "TRIANGULO"

# Cor atualmente selecionada
cor = [1.0, 1.0, 1.0]

# Histórico de formas desenhadas
historico_formas = []

# Valor de deslocamento do movimento
PASSO = 0.05

def atualizarViewport(window):
    largura, altura = glfw.get_framebuffer_size(window)
    glViewport(0, 0, largura, altura)

def criarPonto(x, y):
    return [(x, y)]


def criarTriangulo(x, y):

    largura = rd.uniform(-1, 1)
    altura = rd.uniform(-1, 1)

    return [
        (x, y),
        (x - largura, y - altura),
        (x + largura, y - altura)
    ]


def criarLinha(x, y):

    largura = rd.uniform(-1, 1)
    altura = rd.uniform(-1, 1)

    return [
        (x, y),
        (x + largura, y + altura),
    ]


def criarQuadrado(x, y):

    largura = rd.uniform(-1, 1)
    altura = rd.uniform(-1, 1)

    return [
        (x, y),
        (x + largura, y),
        (x + largura, y + altura),
        (x, y + altura)
    ]

def desenharTodasAsFormas():

    global historico_formas

    for forma in historico_formas:

        vertices = forma["vertices"]
        tipo = forma["tipo"]
        cor_forma = forma["cor"]

        glColor3fv(cor_forma)

        if tipo == "PONTO":
            glPointSize(10.0)
            glBegin(GL_POINTS)

        elif tipo == "LINHA":
            glBegin(GL_LINES)

        elif tipo == "TRIANGULO":
            glBegin(GL_TRIANGLES)

        elif tipo == "QUADRADO":
            glBegin(GL_QUADS)

        for v in vertices:
            glVertex2fv(v)

        glEnd()

def moverUltimaForma(dx, dy):

    global historico_formas

    # Se não houver formas, não faz nada
    if len(historico_formas) == 0:
        return

    ultima_forma = historico_formas[-1]

    novos_vertices = []

    for x, y in ultima_forma["vertices"]:
        novos_vertices.append((x + dx, y + dy))

    ultima_forma["vertices"] = novos_vertices

def alterarCorUltimaForma():

    global historico_formas, cor

    if len(historico_formas) == 0:
        return

    historico_formas[-1]["cor"] = list(cor)

def key_callback(window, key, scancode, action, mods):

    global modo_atual, cor, historico_formas

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_T:
            modo_atual = "TRIANGULO"

        elif key == glfw.KEY_Q:
            modo_atual = "QUADRADO"

        elif key == glfw.KEY_L:
            modo_atual = "LINHA"

        elif key == glfw.KEY_P:
            modo_atual = "PONTO"

        elif key == glfw.KEY_C:
            historico_formas.clear()

        elif key == glfw.KEY_R:
            cor = [1.0, 0.0, 0.0]

        elif key == glfw.KEY_G:
            cor = [0.0, 1.0, 0.0]

        elif key == glfw.KEY_B:
            cor = [0.0, 0.0, 1.0]

        elif key == glfw.KEY_Y:
            cor = [1.0, 1.0, 0.0]

        elif key == glfw.KEY_M:
            cor = [1.0, 0.0, 1.0]

        elif key == glfw.KEY_W:
            cor = [1.0, 1.0, 1.0]

        elif key == glfw.KEY_ENTER:

            alterarCorUltimaForma()


        elif key == glfw.KEY_LEFT:
            moverUltimaForma(-PASSO, 0)

        elif key == glfw.KEY_RIGHT:
            moverUltimaForma(PASSO, 0)

        elif key == glfw.KEY_UP:
            moverUltimaForma(0, PASSO)

        elif key == glfw.KEY_DOWN:
            moverUltimaForma(0, -PASSO)

        elif key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)


def cliqueMouse(window, button, action, mods):

    global modo_atual, cor, historico_formas

    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:

        x_mouse, y_mouse = glfw.get_cursor_pos(window)

        largura, altura = glfw.get_window_size(window)

        x, y = converterParaOpenGL(
            x_mouse,
            y_mouse,
            largura,
            altura
        )

        vertices = None

        if modo_atual == "TRIANGULO":
            vertices = criarTriangulo(x, y)

        elif modo_atual == "QUADRADO":
            vertices = criarQuadrado(x, y)

        elif modo_atual == "LINHA":
            vertices = criarLinha(x, y)

        elif modo_atual == "PONTO":
            vertices = criarPonto(x, y)

        if vertices is not None:

            nova_forma = {
                "tipo": modo_atual,
                "vertices": vertices,
                "cor": list(cor)
            }

            historico_formas.append(nova_forma)

    # Botão direito limpa a tela
    elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:

        historico_formas.clear()


def converterParaOpenGL(x_mouse, y_mouse, largura, altura):

    x = (x_mouse / largura) * 2 - 1

    y = 1 - (y_mouse / altura) * 2

    return x, y

def main():

    if not glfw.init():
        print("Erro ao iniciar GLFW")
        return

    largura = 800
    altura = 600

    window = glfw.create_window(
        largura,
        altura,
        "Editor de Formas",
        None,
        None
    )

    if not window:
        print("Erro ao criar janela")
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glfw.set_mouse_button_callback(window, cliqueMouse)

    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):

        atualizarViewport(window)

        glClear(GL_COLOR_BUFFER_BIT)

        desenharTodasAsFormas()

        glfw.swap_buffers(window)

        glfw.poll_events()

    glfw.destroy_window(window)

    glfw.terminate()


if __name__ == "__main__":
    main()