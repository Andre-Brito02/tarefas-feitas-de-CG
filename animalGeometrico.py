from OpenGL.GL import *
import glfw

# Variáveis globais para armazenar a posição do clique do mouse
g_pos_x = 0.0
g_pos_y = 0.0

# --- NOVA VARIÁVEL DE CONTROLE ---
# Começa como False para não desenhar nada na primeira execução
desenhar_animal = False 

# Tamanho fixo da janela para os cálculos de conversão
LARGURA = 800
ALTURA = 800

# Função de callback que será chamada toda vez que o mouse for clicado
def mouse_callback(window, button, action, mods):
    global g_pos_x, g_pos_y, desenhar_animal
    
    # Se o botão esquerdo do mouse for pressionado
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        # Ativa a permissão para desenhar (agora e para os próximos cliques)
        desenhar_animal = True
        
        # Pega os pixels (x, y) de onde o mouse está na janela
        x_mouse, y_mouse = glfw.get_cursor_pos(window)
        
        # Converte as coordenadas de pixels para o formato do OpenGL (-1.0 a 1.0)
        g_pos_x = (2.0 * x_mouse / LARGURA) - 1.0
        g_pos_y = 1.0 - (2.0 * y_mouse / ALTURA)

def init():
    glClearColor(1,1,1,1) # Define a cor de fundo da janela (branco)
    glPointSize(10)       # Define o tamanho dos pontos

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # --- VERIFICAÇÃO SE JÁ FOI CLICADO ---
    if not desenhar_animal:
        return # Sai da função mais cedo, deixando a tela em branco
    
    # Se passou pelo 'if' acima, significa que o usuário já clicou, então desenha:
    glLoadIdentity() 
    glTranslatef(g_pos_x, g_pos_y, 0.0) 
    
    glBegin(GL_LINE_LOOP)
    glColor3f(0,1,0)
    #Lado esquerdo
    glVertex2f(-0.3, -0.75)   # base esquerda
    glVertex2f(-0.44, -0.45)  # joelho esquerdo
    glVertex2f(-0.32, -0.30)  # perna esquerda
    glVertex2f(-0.38, -0.18)  # cintura esquerda
    glVertex2f(-0.20,  0.10)  # ombro esquerdo
    glVertex2f(-0.40,  0.30)  # bochecha esquerda
    glVertex2f(-0.32,  0.40)  # base orelha esquerda
    glVertex2f(-0.41,  0.65)  # ponta orelha esquerda
    glVertex2f(-0.14,  0.55)  # topo orelha esquerda

    #Lado direito
    glVertex2f( 0.14,  0.55)  # topo orelha direita  
    glVertex2f( 0.41,  0.65)  # ponta orelha direita
    glVertex2f( 0.32,  0.40)  # base orelha direita  
    glVertex2f( 0.40,  0.30)  # Bochecha direita  
    glVertex2f( 0.20,  0.10)  # ombro direito  
    glVertex2f( 0.38, -0.18)  # cintura direita  
    glVertex2f( 0.32, -0.30)  # perna direita  
    glVertex2f( 0.44, -0.45)  # joelho direito   
    glVertex2f( 0.3,  -0.75)  # base direita  
    glEnd()
    
    glBegin(GL_LINE_STRIP)
    glColor3f(1, 0, 0)
    glVertex2f( 0.3,  -0.75)  # base direita  
    glVertex2f( 0.57, -0.63)  # Base direita rabo
    glVertex2f( 0.75, -0.35)  # corpo rabo lado direito
    glVertex2f( 0.80, -0.10)  # ponta do rabo
    glVertex2f( 0.60, -0.20)  # corpo rabo lado esquerdo
    glVertex2f( 0.41, -0.42)  # Base esquerda rabo
    glEnd()
    
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    glVertex2f( 0.44, -0.45)  # joelho direito
    glVertex2f( 0.57, -0.63)# Base direita rabo
    
    glVertex2f( 0.75, -0.35)# corpo rabo lado direito
    glVertex2f( 0.60, -0.20)# corpo rabo lado esquerdo
    
    glVertex2f( 0.41, -0.42)#Base esquerda rabo
    glVertex2f( 0.75, -0.35)# corpo rabo lado direito
    
    glVertex2f(-0.32,  0.40)# Base orelha esquerda
    glVertex2f(-0.14,  0.55)#Topo orelha esquerda
    
    glVertex2f( 0.14,  0.55)  # topo orelha direita 
    glVertex2f( 0.32,  0.40)  # base orelha direita 
    
    glVertex2f( 0.0, 0.0) 
    glVertex2f( 0.20,  0.10)  # ombro direito 
    
    glVertex2f( 0.0, 0.0) 
    glVertex2f(-0.20,  0.10)  # ombro esquerdo 
    
    glVertex2f(0,0)
    glVertex2f(0.10, 0.16)
    
    glVertex2f(0,0)
    glVertex2f(-0.10, 0.16)
    
    glVertex2f( 0.10, 0.16)
    glVertex2f( 0.32,  0.40)  # base orelha direita 
    
    glVertex2f(-0.10, 0.16)
    glVertex2f(-0.32,  0.40)# Base orelha esquerda
    
    glVertex2f( 0.0, -0.75)# Base centro
    glVertex2f(-0.20,  0.10)  # ombro esquerdo 
    
    glVertex2f( 0.0, -0.75)# Base centro
    glVertex2f( 0.20,  0.10)  # ombro direito 
    
    glVertex2f( 0.11,-0.75) #BASE
    glVertex2f( 0.38, -0.18)  # cintura direita  
    
    glVertex2f(-0.11,-0.75)#BASE
    glVertex2f(-0.38, -0.18)  # cintura esquerda
    
    glVertex2f(0.08,-0.40)
    glVertex2f( 0.38, -0.18)  # cintura direita  
    
    glVertex2f(-0.08,-0.40)
    glVertex2f(-0.38, -0.18)  # cintura esquerda
    
    glVertex2f(-0.15,-0.35)
    glVertex2f(-0.11,-0.75)#BASE
    
    glVertex2f( 0.15,-0.35)
    glVertex2f(0.11,-0.75)#BASE
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glVertex2f(0.10, 0.16)
    glVertex2f(0.18, 0.24)
    glVertex2f(0.11, 0.24)
    
    glVertex2f(-0.10, 0.16)
    glVertex2f(-0.18, 0.24)
    glVertex2f(-0.11, 0.24)
    
    glVertex2f( 0.03,0.05)
    glVertex2f(-0.03,0.05)
    glVertex2f( 0.0 ,0.0 )
    glEnd()

def main():
    if not glfw.init():
        print("Não foi possível iniciar o glfw")
        return
    
    window = glfw.create_window(LARGURA, ALTURA, "Animal Geométrico Interativo", None, None)
    if not window:
        print("Erro ao criar a janela")
        return
    
    glfw.make_context_current(window)
    init()
    
    glfw.set_mouse_button_callback(window, mouse_callback)
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()
    
if __name__ == "__main__":
    main()