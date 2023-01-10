from tkinter import *
from random import *
from PIL import Image, ImageTk
COLOR_1 = "#FF5C58"
COLOR_2 = "#FE8F8F"
COLOR_3 = "#FCD2D1"
COLOR_4 = "#FFEDD3"

image_list = {"Paper":"Images/paper.png",
            "Rock":"Images/rock.png",
            "Scissor":"Images/scissor.png"}

class button:
    def __init__ (self, frame, name, result):
        self.result=result
        self.name=name
        self.object = Button(frame, text=name)
        self.object.config(bg=COLOR_1, fg=COLOR_4, command=self.show_result)
    
    def place_element(self,w=0.1,h=0.1,x=0.1,y=0.2):
        self.object.place(relwidth=w, relheight=h, relx=x, rely=y)

    def disable(self):
        self.object.config(state="disabled")

    def enable(self):
        self.object.config(state="normal")
    
    def show_result(self):
        self.result.config(text=self.name)
        player_1.result=self.name
        computer.result=computer.random_result()
        image1=Image.open(image_list[player_1.result])
        image2=Image.open(image_list[computer.result])
        photo1 = ImageTk.PhotoImage(image1.resize((32, 32), Image.ANTIALIAS))
        photo2 = ImageTk.PhotoImage(image2.resize((32, 32), Image.ANTIALIAS))
        player_1.result_image.config(image=photo1)
        computer.result_image.config(image=photo2)
        player_1.result_image.image=photo1
        computer.result_image.image=photo2
        result_compare(player_1.result, computer.result)
        

class frame:
    def __init__(self, frame, w=0.4,h=0.4,x=0,y=0):
        self.object = Frame(frame)
        self.object.config(bg=COLOR_4, highlightbackground=COLOR_2, highlightcolor=COLOR_2 ,highlightthickness=1)
        self.pos ={
            "w":w,
            "h":h,
            "x":x,
            "y":y
        }      
        
    def place_elements(self):
        self.object.place(relwidth=self.pos["w"], relheight=self.pos["h"], relx=self.pos["x"], rely=self.pos["y"])


class PSR:
    def __init__ (self,x,y,name):
        self.name=name
        self.result=""
        self.frame = frame(root,x=x, y=y)
        self.frame.place_elements()
        
        self.player_label = Label(self.frame.object)
        self.result_label = Label(self.frame.object, text="")
        self.result_image = Label(self.frame.object)
        self.r_button = button(self.frame.object, "Rock", self.result_label)
        self.p_button = button(self.frame.object, "Paper", self.result_label)
        self.s_button = button(self.frame.object, "Scissor", self.result_label)

    def edit_elements(self):
        self.player_label.config(font="Time 11 bold", bg=COLOR_3, fg=COLOR_1)
        self.result_label.config(font="Time 11 bold", bg=COLOR_4, fg=COLOR_1)
        self.result_image.config(font="Time 11 bold", bg=COLOR_4, fg=COLOR_1)
    def place_elements(self):
        self.player_label.place(relwidth=0.9, relx=0.05, rely=0.1)
        self.r_button.place_element(w=0.25, h=0.2, x=0.05, y=0.3)
        self.s_button.place_element(w=0.25, h=0.2, x=0.35, y=0.3)
        self.p_button.place_element(w=0.25, h=0.2, x=0.65, y=0.3)
        self.result_label.place(relwidth=0.9, relx=0.05, rely=0.8)
        self.result_image.place(relwidth=0.9, relheight=0.2, relx=0.05, rely=0.55)

class PSR_player(PSR):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)    

    def edit_elements(self):
        self.player_label.config(text=self.name)
        return super().edit_elements()
    
    def place_elements(self):
        return super().place_elements()

class PSR_computer(PSR):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
    
    def edit_elements(self):
        self.player_label.config(text=self.name)
        self.r_button.disable()
        self.p_button.disable()
        self.s_button.disable()
        return super().edit_elements()
    
    def place_elements(self):
        return super().place_elements()
    
    def random_result(self):
        self.r_button.disable()
        self.p_button.disable()
        self.s_button.disable()
        choose = randint(0,2)
        text={  0:("Rock",self.r_button),
                1:("Paper",self.p_button),
                2:("Scissor", self.s_button)}
        self.result_label.config(text=text[choose][0])
        text[choose][1].enable()
        return text[choose][0]

def result_compare(player, computer_r):
    if player == computer_r:
        text="Draw"
    elif player == "Scissor":
        if computer_r == "Paper":
            text="You win"
        else:
            text="You lose"
    elif player == "Paper":
        if computer_r == "Rock":
            text="You win"
        else:
            text="You lose"
    elif player == "Rock":
        if computer_r == "Scissor":
            text="You win"
        else:
            text="You lose"
    result_label.config(text=text)
root= Tk()
root.title("Rock Paper Scissor")
root.geometry("600x400")
root.config(bg=COLOR_4)
root.resizable(0,0)

name_label = Label(root, text="ROCK - PAPER - SCISSOR")
intro_label = Label(root, text="Beat your computer")
result_label = Label (root, text="")

name_label.config(bg=COLOR_2, fg=COLOR_4, font="Time 13 bold")
intro_label.config(bg=COLOR_4, fg=COLOR_2, font="Time 11 bold italic")
result_label.config(bg=COLOR_4, fg=COLOR_2, font="Time 11 bold italic")

name_label.place(relwidth=0.6, relx=0.2, rely=0.03)
intro_label.place(relwidth=0.6, relx=0.2, rely=0.1)
result_label.place(relwidth=0.6, relx=0.2, rely=0.65)

player_1 = PSR_player(0.09,0.2, "PLAYER 1")
player_1.edit_elements()
player_1.place_elements()

computer = PSR_computer(0.51, 0.2, "COMPUTER")
computer.edit_elements()
computer.place_elements()


root.mainloop()


