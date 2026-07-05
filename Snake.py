import customtkinter as ctk
import random
snake=ctk.CTk()
snake.title("python (snake)")
snake.geometry("500x600")
snake.wm_minsize(500, 600)
snake.wm_maxsize(500, 600)
snake.resizable(False, False)
class fsclass:
    def __init__(self):
        self.serpiente=[[3, 4, "R"]]
    # U,arriba. D,abajo. R,derecha. L,izquierda.
    def mover(self):
        for i in range(len(self.serpiente) - 1, 0, -1):
            self.serpiente[i][0] = self.serpiente[i-1][0]
            self.serpiente[i][1] = self.serpiente[i-1][1]
            self.serpiente[i][2] = self.serpiente[i-1][2]
        cabeza = self.serpiente[0]
        if cabeza[2] == "R":
            cabeza[0] += 1
        elif cabeza[2] == "L":
            cabeza[0] -= 1
        elif cabeza[2] == "U":
            cabeza[1] -= 1
        elif cabeza[2] == "D":
            cabeza[1] += 1
    def cambiar_direccion(self,D):
        if not((self.serpiente[0][2]=="R" and D=="L") or (self.serpiente[0][2]=="L" and D=="R") or (self.serpiente[0][2]=="D" and D=="U") or (self.serpiente[0][2]=="U" and D=="D")):
            self.serpiente[0][2]=D
    def añadir_cola(self):
        self.serpiente.append([self.serpiente[-1][0],self.serpiente[-1][1],self.serpiente[-1][2]])
        if self.serpiente[-1][2]=="R":#x,y
            self.serpiente[-1][0]-=1
        elif self.serpiente[-1][2]=="L":
            self.serpiente[-1][0]+=1
        elif self.serpiente[-1][2]=="U":
            self.serpiente[-1][1]+=1
        elif self.serpiente[-1][2]=="D":
            self.serpiente[-1][1]-=1
    def check_vida(self):
        lista_check=[]
        for a in self.serpiente:
            lista_check.append([a[0],a[1]])
        for a in self.serpiente:
            if lista_check.count([a[0],a[1]])>1:
                return False
        if not(0<=self.serpiente[0][0]<=9 and 0<=self.serpiente[0][1]<=9) :
            return False
        return True
    def check_manzana(self,apple):
        if [self.serpiente[0][0], self.serpiente[0][1]] == [apple[0][0], apple[0][1]]:
            self.añadir_cola()
            apple.pop(0)
            return True
        else:
            return False
try:
    fisicas.serpiente
except NameError:
    fisicas=fsclass()
try:
    apple==1
except NameError:
    apple=[]
try:
    points
except NameError:
    points=0
try:
    zz
except NameError:
    zz=False
try:
    speed
except NameError:
    speed=500
try:
    pausa
except NameError:
    pausa=False
try:
    snake_color
except NameError:
    snake_color="#B7FF00"
def cambiar_velocidad():
    global speed
    global snake_color
    if speed==500:
        speed=250
        snake_color="#FFF132"
        hud_pb.configure(text="X2")
    elif speed==250:
        speed=125
        snake_color="#FF9900"
        hud_pb.configure(text="X4")
    elif speed==125:
        speed=500
        snake_color="#B7FF00"
        hud_pb.configure(text="X1")
def pausar():
    global pausa
    if pausa==False:
        pausa=True
    else:
        pausa=False
hud_v=ctk.CTkButton(snake, text=f"cambiar velocidad",font=("Arial", 14, "bold"),width=150, height=30, command=lambda: cambiar_velocidad())
hud_v.place(relx=0.25, rely=0.89)
cuadricula=ctk.CTkCanvas(snake, width=500, height=500, bg="#514141", highlightthickness=0)
cuadricula.pack(fill="x", expand="False")
hud_p=ctk.CTkLabel(snake, text=f"Puntos:{points}",font=("Arial", 14, "bold"),width=100, height=30)
hud_p.place(relx=0, rely=0.89)
hud_pb=ctk.CTkLabel(snake, text="X1",font=("Arial", 14, "bold"),width=100, height=30)
hud_pb.place(relx=0.8, rely=0.89)
hud_v=ctk.CTkButton(snake, text=f"▐▐",font=("Arial", 14, "bold"),width=30, height=30, command=lambda: pausar())
hud_v.place(relx=0.915, rely=0)
def estado_inicial():
    global fisicas
    global apple
    global points
    global zz
    zz=False
    points=0
    hud_p.configure(text=f"Puntos:{points}")
    fisicas.serpiente=[[3, 4, "R"]]
    apple=[]
def cambiar_direccion_p(D):
    global fisicas
    global pausa
    if not pausa:
        fisicas.cambiar_direccion(D)
snake.bind("<Up>", lambda event: cambiar_direccion_p("U"))
snake.bind("<Down>", lambda event: cambiar_direccion_p("D"))
snake.bind("<Right>", lambda event: cambiar_direccion_p("R"))
snake.bind("<Left>", lambda event: cambiar_direccion_p("L"))
snake.bind("<space>", lambda event: cambiar_velocidad())
snake.bind("<r>", lambda event: estado_inicial())
snake.bind("<Escape>", lambda event: pausar())
def tiempo():
    global points
    global zz#cuando la serpiente esta en una posicion no valida, este booleano se encarga de devolver la serpiente en la posicion anterior UNA SOLA VEZ.
    global speed
    global pausa
    global snake_color
    if not pausa:
        if fisicas.check_vida():
            fisicas.mover()
            if fisicas.check_vida():
                if not pausa:
                    cuadricula.delete("all")
                    if apple==[]:
                        lista_exclusiva=[]
                        lista_pos_valida=[]
                        for a in range(0,9):
                            for b in range(0,9):
                                lista_pos_valida.append([a,b])
                        for a in fisicas.serpiente:
                            lista_exclusiva.append([a[0],a[1]])
                        for a in lista_exclusiva:
                            b=0
                            while b<len(lista_pos_valida):
                                if a==lista_pos_valida[b]:
                                    lista_pos_valida.pop(b)
                                else:
                                    b+=1
                        apple.append(lista_pos_valida[random.randint(0,len(lista_pos_valida)-1)])
                    cuadricula.create_rectangle(apple[0][0]*50,apple[0][1]*50,apple[0][0]*50+50,apple[0][1]*50+50,fill="#FF0000",outline="#FF0000")
                    if fisicas.check_manzana(apple):
                        if speed==500:
                            points+=1
                            hud_p.configure(text=f"Puntos:{points}")
                        elif speed==250:
                            points+=2
                            hud_p.configure(text=f"Puntos:{points}")
                        elif speed==125:
                            points+=5
                            hud_p.configure(text=f"Puntos:{points}")
                    for a in range(len(fisicas.serpiente)):
                        if a==0:
                            cuadricula.create_rectangle(fisicas.serpiente[a][0]*50,fisicas.serpiente[a][1]*50,fisicas.serpiente[a][0]*50+50,fisicas.serpiente[a][1]*50+50,fill="#000000",outline="#000000")
                        else:
                            cuadricula.create_rectangle(fisicas.serpiente[a][0]*50,fisicas.serpiente[a][1]*50,fisicas.serpiente[a][0]*50+50,fisicas.serpiente[a][1]*50+50,fill=snake_color ,outline=snake_color)
                    snake.after(speed, tiempo)
                else:
                    cuadricula.create_text(250, 250, text=f"Pause\nPuntos:{points}\nPresiona 'Esc' para continuar", fill="#ffffff",font=("Arial", 24, "bold"), justify="center")
                    snake.after(500, tiempo)
            else:
                cuadricula.delete("all")
                if not(zz):
                    fisicas.añadir_cola()
                    zz=True
                for a in fisicas.serpiente:
                    cuadricula.create_rectangle(a[0]*50,a[1]*50,a[0]*50+50,a[1]*50+50,fill="#730000",outline="#730000")  
                cuadricula.create_text(250, 250, text=f"GAME OVER\nPuntos={points}\nPresiona 'R' para reiniciar", fill="#ff3333",font=("Arial", 24, "bold"), justify="center")
                snake.after(500, tiempo)
        else:
            cuadricula.delete("all")
            if not(zz):
                fisicas.añadir_cola()
                zz=True
            for a in fisicas.serpiente:
                cuadricula.create_rectangle(a[0]*50,a[1]*50,a[0]*50+50,a[1]*50+50,fill="#730000",outline="#730000")  
            cuadricula.create_text(250, 250, text=f"GAME OVER\nPuntos:{points}\nPresiona 'R' para reiniciar", fill="#ff3333",font=("Arial", 24, "bold"), justify="center")
            snake.after(500, tiempo)
    else:
        cuadricula.create_text(250, 250, text=f"Pause\nPuntos:{points}\nPresiona 'Esc' para continuar", fill="#ffffff",font=("Arial", 24, "bold"), justify="center")
        snake.after(500, tiempo)
snake.after(speed, tiempo)
snake.mainloop()