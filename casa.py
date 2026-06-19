import OpenGL.GL.shaders as gls
from OpenGL.GL import *
import numpy as np
import ctypes
import glfw

vertices_telhado = [
    [-0.65, -0.05, 1.00, 0.00, 0.00],
    [-0.15, -0.05, 0.00, 1.00, 0.00],
    [-0.40,  0.22, 0.00, 0.00, 1.00]
]

verticesCasa = [
    [-0.6, -0.45, 0.85, 0.55, 0.35],
    [-0.2, -0.45, 0.85, 0.55, 0.35],
    [-0.2, -0.05, 0.85, 0.55, 0.35],
    [-0.6, -0.05, 0.85, 0.55, 0.35]
]

vertices_porta = [
    [-0.46, -0.45, 0.35, 0.2, 0.1],
    [-0.34, -0.45, 0.35, 0.2, 0.1],
    [-0.34, -0.20, 0.35, 0.2, 0.1],
    [-0.46, -0.20, 0.35, 0.2, 0.1]
]

vertices_chao = [
    [-1.00, -1.00, 0.25, 0.60, 0.25],
    [ 1.00, -1.00, 0.25, 0.60, 0.25],
    [ 1.00, -0.45, 0.25, 0.60, 0.25],
    [-1.00, -0.45, 0.25, 0.60, 0.25]
]

qtdVerticesChao = len(vertices_chao)  # Quantidade total de vértices do chão
vaoIdChao = 0  # Variável global que guardará o identificador do VAO do chão
qtdVerticesCasa = len(verticesCasa)  # Quantidade total de vértices da casa
vaoIdCasa = 0  # Variável global que guardará o identificador do VAO da casa
qtdVerticesTelhado = len(vertices_telhado)  # Quantidade total de vértices do telhado
vaoIdTelhado = 0  # Variável global que guardará o identificador do
qtdVerticesPorta = len(vertices_porta)  # Quantidade total de vértices da porta
vaoIdPorta = 0  # Variável global que guardará o identificador do
shaderId = 0  # Variável global que guardará o identificador do programa de shaders
colorLocation = 0  # Variável global que guardará a localização da variável uniforme "objectColor" no shader

def init_chao():
    global vertices_chao, vaoIdChao

    vertices_chao = np.array(vertices_chao, np.dtype(np.float32))  # Converte a lista de vértices para um array NumPy de float32

    # ===================== CRIAÇÃO DO VAO DO CHÃO =====================
    vaoIdChao = glGenVertexArrays(1)  # Gera um identificador para o VAO (Vertex Array Object) do chão
    glBindVertexArray(vaoIdChao)  # Ativa o VAO do chão. Tudo configurado agora ficará "guardado" nele

    # ===================== CRIAÇÃO DO VBO DO CHÃO =====================
    vboIdChao = glGenBuffers(1)  # Gera um identificador para o VBO (Vertex Buffer Object) do chão
    glBindBuffer(GL_ARRAY_BUFFER, vboIdChao)  # Torna o VBO do chão o buffer ativo do tipo ARRAY_BUFFER

    # Envia os dados dos vértices do chão para a memória da GPU
    glBufferData(GL_ARRAY_BUFFER,vertices_chao.nbytes,vertices_chao,GL_STATIC_DRAW)

    # Diz ao OpenGL como interpretar os dados dentro do VBO do chão
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)  # Habilita o atributo de posição (índice 0) para o chão

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(2 * 4))
    glEnableVertexAttribArray(1)  # Habilita o atributo de cor

    # Desativa o VBO e VAO após configurar
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

def init_casa():
    global verticesCasa, vaoIdCasa

    verticesCasa = np.array(verticesCasa, np.dtype(np.float32))  # Converte a lista de vértices da casa para um array NumPy de float32

    # ===================== CRIAÇÃO DO VAO DA CASA =====================
    vaoIdCasa = glGenVertexArrays(1)  # Gera um identificador para o VAO (Vertex Array Object) da casa
    glBindVertexArray(vaoIdCasa)  # Ativa o VAO da casa. Tudo configurado agora ficará "guardado" nele

    # ===================== CRIAÇÃO DO VBO DA CASA =====================
    vboIdCasa = glGenBuffers(1)  # Gera um identificador para o VBO (Vertex Buffer Object) da casa
    glBindBuffer(GL_ARRAY_BUFFER, vboIdCasa)  # Torna o VBO da casa o buffer ativo do tipo ARRAY_BUFFER

    # Envia os dados dos vértices da casa para a memória da GPU
    glBufferData(GL_ARRAY_BUFFER, verticesCasa.nbytes, verticesCasa, GL_STATIC_DRAW)

    # Diz ao OpenGL como interpretar os dados dentro do VBO da casa
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)  # Habilita o atributo de posição (índice 0) para a casa

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(2 * 4))
    glEnableVertexAttribArray(1)  # Habilita o atributo de cor (índice 1) para a casa

    # Desativa o VBO e VAO após configurar
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    
def init_telhado():
    global vertices_telhado, vaoIdTelhado

    vertices_telhado = np.array(vertices_telhado, np.dtype(np.float32))  # Converte a lista de vértices do telhado para um array NumPy de float32

    # ===================== CRIAÇÃO DO VAO DO TELHADO =====================
    vaoIdTelhado = glGenVertexArrays(1)  # Gera um identificador para o VAO (Vertex Array Object) do telhado
    glBindVertexArray(vaoIdTelhado)  # Ativa o VAO do telhado. Tudo configurado agora ficará "guardado" nele

    # ===================== CRIAÇÃO DO VBO DO TELHADO =====================
    vboIdTelhado = glGenBuffers(1)  # Gera um identificador para o VBO (Vertex Buffer Object) do telhado
    glBindBuffer(GL_ARRAY_BUFFER, vboIdTelhado)  # Torna o VBO do telhado o buffer ativo do tipo ARRAY_BUFFER

    # Envia os dados dos vértices do telhado para a memória da GPU
    glBufferData(GL_ARRAY_BUFFER, vertices_telhado.nbytes, vertices_telhado, GL_STATIC_DRAW)

    # Diz ao OpenGL como interpretar os dados dentro do VBO do telhado
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)  # Habilita o atributo de posição (índice 0) para o telhado

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(2 * 4))
    glEnableVertexAttribArray(1)  # Habilita o atributo de cor (

    # Desativa o VBO e VAO após configurar
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

def init_porta():
    global vertices_porta, vaoIdPorta

    vertices_porta = np.array(vertices_porta, np.dtype(np.float32))  # Converte a lista de vértices da porta para um array NumPy de float32

    # ===================== CRIAÇÃO DO VAO DA PORTA =====================
    vaoIdPorta = glGenVertexArrays(1)  # Gera um identificador para o VAO (Vertex Array Object) da porta
    glBindVertexArray(vaoIdPorta)  # Ativa o VAO da porta. Tudo configurado agora ficará "guardado" nele

    # ===================== CRIAÇÃO DO VBO DA PORTA =====================
    vboIdPorta = glGenBuffers(1)  # Gera um identificador para o VBO (Vertex Buffer Object) da porta
    glBindBuffer(GL_ARRAY_BUFFER, vboIdPorta)  # Torna o VBO da porta o buffer ativo do tipo ARRAY_BUFFER

    # Envia os dados dos vértices da porta para a memória da GPU
    glBufferData(GL_ARRAY_BUFFER, vertices_porta.nbytes, vertices_porta, GL_STATIC_DRAW)

    # Diz ao OpenGL como interpretar os dados dentro do VBO da porta
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)  # Habilita o atributo de posição (índice 0) para a porta

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 5 * 4, ctypes.c_void_p(2 * 4))
    glEnableVertexAttribArray(1)  # Habilita o atributo de cor 

    # Desativa o VBO e VAO após configurar
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    
def init_shaders():
    global shaderId, colorLocation

    vertexShaderCode = """
    #version 330 core
    layout (location = 0) in vec2 position;
    layout (location = 1) in vec3 color;
    
    out vec3 vertexColor; // Variável de saída para passar a cor do vértice para o fragment shader
    
    void main(){
        gl_Position = vec4(position, 0.0, 1.0);
        vertexColor = color; // Passa a cor do vértice para o fragment shader
    }
    """

    fragmentShaderCode = """
    #version 330 core
    in vec3 vertexColor; // Variável de entrada para receber a cor do vértice do vertex shader
    out vec4 FragColor;
    
    void main(){
        FragColor = vec4(vertexColor, 1.0);
    }
    """
    vertexShaderId = gls.compileShader(vertexShaderCode, GL_VERTEX_SHADER)  # Compila o shader de vértice
    fragmentShaderId = gls.compileShader(fragmentShaderCode, GL_FRAGMENT_SHADER)  # Compila o shader de fragmento
    shaderId = gls.compileProgram(vertexShaderId, fragmentShaderId)  # Link
    colorLocation = glGetUniformLocation(shaderId, "objectColor")  # Obtém a localização da variável uniforme "objectColor" no shader

def desenhar_porta():
    glBindVertexArray(vaoIdPorta) # Ativa o VAO da porta para desenhá-la
    glDrawArrays(GL_QUADS, 0, qtdVerticesPorta) # Desenha os vértices da porta como quadriláteros
    glBindVertexArray(0) # Desativa o VAO da porta após desenhá-la
    
def desenhar_casa():
    glBindVertexArray(vaoIdCasa) # Ativa o VAO da casa para desenhá-la
    glDrawArrays(GL_QUADS, 0, qtdVerticesCasa) # Desenha os vértices da casa como quadriláteros
    glBindVertexArray(0) # Desativa o VAO da casa após desenhá-la

def desenhar_telhado():
    glBindVertexArray(vaoIdTelhado) # Ativa o VAO do telhado para desenhá-lo
    glDrawArrays(GL_TRIANGLES, 0, qtdVerticesTelhado) # Desenha os vértices do telhado como triângulos
    glBindVertexArray(0) # Desativa o VAO do telhado após desenhá-lo
    
def desenhar_chao():
    glBindVertexArray(vaoIdChao) # Ativa o VAO do chão para desenhá-lo
    glDrawArrays(GL_QUADS, 0, qtdVerticesChao) # Desenha os vértices do chão como quadriláteros
    glBindVertexArray(0) # Desativa o VAO do chão após desenhá-lo
    
def display():
    glClearColor(0.68, 0.85, 0.90, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(shaderId) # Ativa o programa de shaders para renderizar os objetos
    desenhar_telhado()
    desenhar_casa()
    desenhar_porta()
    desenhar_chao()
    
def main():
    if not glfw.init():
        raise RuntimeError("Erro ao inicializar OpenGL")
    
    window = glfw.create_window(900, 700, 'Casinha', None, None)
    
    if not window:
        glfw.terminate()
        raise RuntimeError("Não foi possível criar a janela")
    
    glfw.make_context_current(window)
    init_shaders()
    init_telhado()
    init_casa()
    init_porta()
    init_chao()
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        display()
        glfw.swap_buffers(window)
        
    glfw.destroy_window(window)
    glfw.terminate()
    
main()