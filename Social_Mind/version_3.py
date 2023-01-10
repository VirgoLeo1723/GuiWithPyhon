import json, requests
import numpy as np
import threading
import time
import os
import pyglet
from playsound import playsound
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk, Image
from stories_read import story_infor
from testing import process_content
from mutagen.mp3 import MP3
from custom_rect import *

# Constant Val
COLOR_1="#FFEBC9"
COLOR_2="#753422"
COLOR_3="#D79771"
COLOR_4="#FFDF91"
COLOR_5="#B05B3B"
COLOR_6="#FFFEB7"
COLOR_7="#FEF7DC"
url_login='http://127.0.0.1:9999/login'
url_create='http://127.0.0.1:9999/create'
url_forget='http://127.0.0.1:9999/forget'
url_story='http://127.0.0.1:9999/story'
url_request_mail='http://127.0.0.1:9999/mail'
url_feedback='http://127.0.0.1:9999/feedback'
music_list=["music/relax.mp3","music/matnai.mp3","music/tellurmom.mp3","music/only.mp3"]
#audio_list=["audio/nhapten.wav","audio/nhapmaykhau.wav","audio/failed.wav"]
pyglet.font.add_file('Font/Mali-LightItalic.ttf')
pyglet.font.add_file('Font/FlorPersonalUseRegular-DOyBx.ttf')
pyglet.font.add_file('Font/BalonkuRegular-la1w.otf')
pyglet.font.add_file('Font/QuirkyLovePersonalUseRegular-RpwrM.ttf')

# Class user
class user_info:
    def __init__(self,user_name,password, email):
        self.user_name = user_name
        self.password = password
        self.email = email
        

# Class menu button
class menu_button:
    button_list=[]
    def __init__(self, frame, text, pos):
        self.button=Button(frame, text=text)
        self.button.config(bg=COLOR_3, relief=RIDGE, state=DISABLED)
        self.button.place(relheight=0.06, relwidth=0.6, rely=pos, relx=0.2)
        self.button_list.append(self.button)
    @classmethod
    def enable_button(cls):
        for button in cls.button_list:
            button.config(state=NORMAL)
    @classmethod
    def disable_button(cls):
        for button in cls.button_list:
            button.config(state=DISABLED)
    def button_config(self,frame):
        self.button.config(command=frame.frame_place)     
# Class inf frame
class root_frame:
    frame_list=[]
    def __init__(self, name, color):
        self.name=name
        self.color=color
        self.frame_setup()
    def frame_setup(self):
        self.frame=Frame(inf_frame)
        self.canvas=Canvas(self.frame)
        root_frame.frame_list.append(self.frame)
        self.name_label=Label(self.frame, text=self.name)
        self.display_frame=Frame(self.frame)
    def frame_config(self):
        self.canvas.config(bg=COLOR_1)
        self.display_frame.config(bg=COLOR_4)
        self.frame.config(bg=self.color)
        self.name_label.config(font=("Time","15","bold"),
                    fg="#FFEBC9",
                    bg="#753422")
        #self.display_frame.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.2)
        self.frame.place(relheight=1, relwidth=1)
        self.name_label.place(relwidth=0.21, relx=0.05, rely=0.06)
    def frame_place(self): 
        pass
    @staticmethod
    def clear():
        for frame in root_frame.frame_list:
            frame.grid_forget()
# Class login frame
class login_frame:
    def __init__(self):
        self.frame=Frame(inf_frame)
        self.frame.config(bg=COLOR_2)
        self.frame.place(relheight=0.5, relwidth=0.5, relx=0.25, rely=0.25)
        self.frame_edit()
    def frame_edit(self):
        self.user_label=Label(self.frame, text="Tên")
        self.pass_label=Label(self.frame, text="Mật Khẩu")
        self.email_label=Label(self.frame, text="Email")
        self.user_entry=Entry(self.frame)
        self.pass_entry=Entry(self.frame)
        self.email_entry=Entry(self.frame)
        self.login_button=Button(self.frame, text="ĐĂNG NHẬP", command=lambda:login_frame.check(self.user_entry.get(), self.pass_entry.get()))
        self.forget_button=Button(self.frame, text="Quên mật khẩu", command=lambda:login_frame.forget())
        self.new_button=Button(self.frame, text="Tạo tài khoản mới", command=lambda:login_frame.new())

        self.user_label.config(bg=COLOR_1)
        self.pass_label.config(bg=COLOR_1)
        self.email_label.config(state=DISABLED, bg=COLOR_1)
        self.email_entry.config(state="disabled")
        self.login_button.config(bg=COLOR_3)
        self.forget_button.config(bg=COLOR_2, fg=COLOR_1, relief=FLAT)
        self.new_button.config(bg=COLOR_6)

        self.user_label.place(relwidth=0.2, relx=0.1, rely=0.12)
        self.pass_label.place(relwidth=0.2, relx=0.1, rely=0.27)
        self.user_entry.place(relwidth=0.5, relx=0.4, rely=0.12)
        self.pass_entry.place(relwidth=0.5, relx=0.4, rely=0.27)
        self.email_label.place(relwidth=0.2, relx=0.1, rely=0.42)
        self.email_entry.place(relwidth=0.5, relx=0.4, rely=0.42)
        self.login_button.place(relwidth=0.8, relx=0.1, rely=0.6)
        self.forget_button.place(relwidth=0.4, relx=0.3, rely=0.71)
        self.new_button.place(relwidth=0.6, relx=0.2, rely=0.85)
    @staticmethod
    def check(name, password):
        global user_current
        if len(name)==0: messagebox.showerror("ERROR","Bạn chưa nhập tên")
        elif len(password)==0: messagebox.showerror("ERROR","Bạn chưa nhập mât khẩu")
        else:
            login_request = requests.get(url_login,f"user={name}&pass={password}")
            if login_request.text=="Login success":
                intro.frame_place()
                user_current=user_info(name,password,requests.get(url_request_mail,f"user={name}").text)
                
            else: 
                messagebox.showinfo("Information","Đăng nhập thất bại") 

    @staticmethod
    def forget():
        login.email_entry.config(state="normal")
        login.email_label.config(state="normal")
        user = login.user_entry.get()
        email = login.email_entry.get()
        if login.email_entry.get()!="": 
            forget = requests.get(url_forget,f"user={user}&mail={email}")
            messagebox.showinfo("INFORMATION","Chúng mình sẽ gửi thông tin qua email")
        else: messagebox.showerror("ERROR","Bạn chưa nhập Email")
    @staticmethod
    def new():
        global current_user
        login.email_entry.config(state="normal")
        login.email_label.config(state="normal")
        user = login.user_entry.get()
        passd = login.pass_entry.get()
        email = login.email_entry.get()
        if email!="":
            create = requests.get(url_create,f"user={user}&pass={passd}&mail={email}")
            if create.text == "Exist": messagebox.showerror("ERROR","Tên đã tồn tại")
            else:
                current_user=user_info(user, passd, email)
                messagebox.showinfo("INFORMATION","Bạn đã tạo tài khoản thành công")
                intro_frame.frame_place()
        else: messagebox.showerror("ERROR","Bạn chưa nhập Email")
#class intro_frame
class intro_frame(root_frame):
    def __init__(self, name, color):
        super().__init__(name, color)
    def intro_setup(self):
        greet=Label(self.frame, text="GIẢI PHÁP HỖ TRỢ CHỮA TRỊ HỘI CHÚNG RỐI LOẠN LO ÂU")
        thank=Label(self.frame, text="Ở học sinh THPT thông qua nên tản ứng dụng")
        name=Label(self.frame, text= "AXIETY \n HEALING ")
        guide1=Text(self.frame)
        start=Button(self.frame, text="bấm vào đây để bắt đầu")
        img_1=ImageTk.PhotoImage(Image.open("Image/calm.png"))
        img_2=ImageTk.PhotoImage(Image.open("Image/relief.png"))
        self.infor_img_1=Label(self.frame, image=img_1)
        self.infor_img_2=Label(self.frame, image=img_2)     
        
        rect=round_rectangle(self.canvas, 35,160, 275,310, fill=COLOR_5)
        guide1.insert(END,"TẠI ĐÂY BẠN CÓ THỂ: \n\
* Kiểm tra và đánh giá mức độ rối loạn lo âu.\n\
* Trải nghiệm giải pháp hỗ trợ chữa trị lo âu\n\
* Chia sẻ bí mật cùng tụi mình. ")
        self.infor_img_1.image=img_1
        self.infor_img_2.image=img_2

        menu_author_button.config(state="normal")
        name.config(font=("Balonku","30"),bd=0, 
                    bg=COLOR_5,
                    fg=COLOR_7,
                    pady=10)
        greet.config(font=("Time", "11", "bold italic"),bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        thank.config(font=("Time", "9", "italic"),bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        guide1.config(font=("Mali Light","10"),state=DISABLED)
        guide1.config(bd=0,
                    bg="#FEF7DC",
                    fg="#753422",
                    pady=10, padx=10)
        start.config(font=("Mali Light","10"),
                    fg=COLOR_5,
                    bg=COLOR_7,
                    relief="flat",
                    command=lambda: home.frame_place())
        self.infor_img_1.config(bg=COLOR_1)
        self.infor_img_2.config(bg=COLOR_1)
        

        self.canvas.place(relheight=1, relwidth=1)
        name.place(relx=0.07, rely=0.36)
        greet.place(relwidth=0.9, relx=0.05, rely=0.16)
        thank.place(relwidth=0.9, relx=0.05, rely=0.23)
        guide1.place(relwidth=0.5, relheight=0.3, rely=0.32, relx=0.45)
        self.infor_img_1.place(relx=0.15, rely=0.66, relwidth=0.2, relheight=0.2)
        self.infor_img_2.place(relx=0.65, rely=0.66, relwidth=0.2, relheight=0.2)
        start.place(relwidth=0.3, relx=0.35, rely=0.7)
    def frame_place(self):
        self.clear()
        self.frame_setup()
        self.frame_config()
        self.intro_setup()  
# Class Home frame
class home_frame(root_frame):
    def __init__(self, name, color):
        super().__init__(name, color)
    def read_lt(self):
        f=open("Server/Loitua.txt","rb")
        return f.read().decode("utf-8")
    def home_setup(self):
        menu_button.enable_button()
        greet=Label(self.frame, text="Xin chào, tụi mình là Yên Khương và Tiến Long")
        thank=Label(self.frame, text="Rất cảm ơn bạn đã đến với dự án của chúng mình")
        guide1=Text(self.frame)
        guide2=Text(self.frame)
        infor=process_content(self.read_lt(),82)
        scrollbar = Scrollbar(self.frame)
        guide1.insert(END,infor.process_content())
        guide2.insert(END,"Hướng dẫn sử dụng: \n\
        1. Câu chuyện: Những câu chuyện chữa lành. \n\
        2. Kiểm tra: Kiểm tra mức độ lo âu của bạn. \n\
        3. Chia sẻ: Chia sẻ những câu chuyện của bạn với chúng mình.")
        guide1.config(font=("Mali Light","10"),state=DISABLED)
        guide2.config(font=("Mali Light","10"),state=DISABLED)

        greet.place(relwidth=0.9, relx=0.05, rely=0.16)
        thank.place(relwidth=0.9, relx=0.05, rely=0.23)
        scrollbar.place(relheight=0.33, relwidth=0.02, rely=0.58, relx=0.93)
        guide2.place(relwidth=0.9, relheight=0.26, rely=0.31, relx=0.05)
        guide1.place(relwidth=0.9, relheight=0.33, rely=0.58, relx=0.05)

        greet.config(font=("Time", "11", "bold italic"),bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        thank.config(font=("Time", "9", "italic"),bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        guide1.config(bd=0,
                    bg="#FEF7DC",
                    fg="#753422",
                    pady=10, padx=10)
        guide2.config(bd=0,
                    bg="#FEF7DC",
                    fg="#753422",
                    pady=10, padx=10)
        guide1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=guide1.yview)
    def frame_place(self):
        self.clear()
        self.frame_setup()
        self.frame_config()
        self.home_setup()     
# Class Anxiety Frame
class story:
    def __init__(self, frame, infor, topic, x,y):
        self.infor=infor
        self.topic=topic
        self.frame=frame
        self.x=x
        self.y=y    
        self.display_sample()    
    def display_sample(self):
        self.group=Frame(self.frame)
        topic_label=Label(self.group, text=self.topic)
        infor_label=Text(self.group)
        infor_label.insert(END,self.infor[0:80])
        infor_label.config(state="disabled")
        self.more=Button(self.group, text="thêm", command=lambda:self.display_all())
        
        self.group.config(bg=COLOR_7)
        topic_label.config(bg=COLOR_5,fg=COLOR_7)
        infor_label.config(bg=COLOR_4,fg=COLOR_5, relief="flat")
        self.more.config(bg=COLOR_5, fg=COLOR_7, relief="flat")

        self.group.place(relwidth=1,relheight=0.24,rely=self.y)
        topic_label.place(relx=0.01, rely=0)
        infor_label.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.6)
        self.more.place(relx=0.84,rely=0.65, relwidth=0.15)
    def display_all(self):
        #place_forget()
        anxiety.next_button.config(state="disabled")
        anxiety.prev_button.config(state="disabled")
        temp=self.infor.index('\n')
        anxiety.sub_frame_2.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.16)
        anxiety.sub_frame_2.config(bg=COLOR_7)
        
        close_button=Button(anxiety.sub_frame_2, text="ĐÓNG", command=lambda: self.close_sub_frame())
        cmt_button=Button(anxiety.sub_frame_2, text="Comment", command=lambda: self.open_cmt_window())
        content=Text(anxiety.sub_frame_2)
        
        infor_content = process_content(self.infor[temp:len(self.infor)],68)
        content.insert(END,infor_content.process_content())
        scrollbar = Scrollbar(anxiety.sub_frame_2)
        idea = Label(anxiety.sub_frame_2, text=self.infor[0:temp-1])
        
        
        close_button.config(bg="#FF7E67", fg="#ECF4F3", relief="flat")
        cmt_button.config(bg="#006A71", fg="#ECF4F3" ,relief="flat")
        content.config(bg=COLOR_7, fg=COLOR_2, relief="flat", state="disabled",
                    font=("Mali Light"," 11"), spacing2=10, spacing3=10)
        content.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=content.yview)
        idea.config(font=("Mali Light","9", "italic"),bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        
        close_button.place(relwidth=0.1, relheight=0.08, relx=0.9, rely=0)
        #cmt_button.place(relwidth=0.1, relheight=0.08, relx=0.79, rely=0)
        content.place(relwidth=0.9, relheight=0.75, rely=0.18, relx=0.05)
        scrollbar.place(relheight=0.75, relwidth=0.02, rely=0.18, relx=0.97)
        idea.place(relwidth=0.5, relheight=0.1, relx=0.05, rely=0.05)
    def close_sub_frame(self):
        #print("close")
        anxiety.next_button.config(state="disabled")
        anxiety.prev_button.config(state="disabled")
        anxiety.sub_frame_2.place_forget()
        anxiety.sub_frame.place(relwidth=0.5, relheight=0.7, relx=0.45, rely=0.16)
    def open_cmt_window(self):
        pass
class anxiety_frame(root_frame):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.checking=0
        
    def anxiety_setup(self):
        self.read=IntVar()
        self.next_button=Button(self.frame, text="SAU")
        self.prev_button=Button(self.frame, text="TRƯỚC")
        self.page_label=Label(self.frame, text="")
        
        style = ttk.Style()
        if self.checking==0:
            self.checking=1
            style.theme_create('Cloud', settings={
                ".": {
                    "configure": {
                        "background": '#FFDF91', # All colors except for active tab-button
                        "foreground": "#753422",
                        "selectbackground":COLOR_3,
                        "borderwidth":0.5
                    }
                },
                "TNotebook": {
                    "configure": {
                        "background":'#FFEBC9', # color behind the notebook
                        "tabmargins":[5,5,5,0],
                        "borderwidth":0
                    }
                },
                "TNotebook.Tab": {
                    "configure": {
                        "background": '#D79771', # Color of non selected tab-button
                        "padding": [20, 1],
                        "foreground":"#753422",
                        "font": "Helvetica 8",
                        "borderwidth":0
                        
                    },
                    "map": {
                        "background": [("selected", '#753422')], # Color of active tab
                        #"expand": [("selected", [1, 1, 1, 0])] # text margins
                        "foreground":[("selected","#D79771")]
                    }
                },
                "TConbobox":{
                    "configure":{
                        'selectbackground': 'blue',
                        'fieldbackground': 'red',
                    },
                }
            })
        style.theme_use('Cloud')

        #setup
        self.topic=["Học Tập",
                    "Gia Đình",
                    "Mối Quan Hệ Xã Hội",
                    "Bản Thân Học Sinh",
                    ]
        self.topic_list=ttk.Combobox(self.frame, value=self.topic)
        self.topic_img=["Image/study.jpg","Image/family.jpg","Image/social.jpg","Image/you.jpg"]
        self.button_find=Button(self.frame, text="TÌM KIẾM", command=lambda:self.anxiety_infor())
        self.intro_1=Label(self.frame, text="NHỮNG CÂU CHUYỆN NGẮN NHẸ NHÀNG")
        self.intro_2=Label(self.frame, text="Hi vọng có thể giúp các bạn phần nào đó")
        self.guide=Label(self.frame, text="\n\
    1. Hãy chọn chủ đề và nhấn TÌM KIẾM để tìm chủ đề mình muốn nhé.\n\
    2. Nhấn TRƯỚC, SAU để xem thêm nhiều câu chuyện.\n\
    3. Nhấn thêm để đọc kĩ hơn về câu chuyện bạn muốn.\n")
        self.next_button=Button(self.frame, text="SAU")
        self.prev_button=Button(self.frame, text="TRƯỚC")
        self.page_label=Label(self.frame, text="")
        self.anxiety_read_button=Radiobutton(self.frame, variable=self.read, value=1)
        self.anxiety_read_label=Label(self.frame, text="Bạn đã đọc kỹ hướng dẫn trên")
        self.anxiety_confirm_button=Button(self.frame, text="Tiếp tục", command=lambda: self.anxiety_setup_2())
        #setup position
        
        self.intro_1.place(relwidth=0.9, relx=0.05, rely=0.16)
        self.intro_2.place(relwidth=0.9, relx=0.05, rely=0.23)
        self.guide.place(relwidth=0.9, relx=0.05, rely=0.31, relheight=0.30)
        self.canvas.place(relwidth=1, relheight=1)
       
        self.anxiety_read_button.place(relx=0.6, rely=0.78)
        self.anxiety_read_label.place(relheight=0.05, relwidth=0.31,relx=0.64, rely=0.78)
        self.anxiety_confirm_button.place(relwidth=0.15, relheight=0.05, relx=0.8,rely=0.88)
        #setup element
        self.topic_list.set("Học Tập")
        self.topic_list.config(font=("Time","9","italic"))
        self.button_find.config(width=10, bg=COLOR_5, fg=COLOR_7, state="disabled")
        self.intro_1.config(font=("Time", "11", "bold italic"),bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        self.intro_2.config(font="Time 9 italic",bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        self.guide.config(bd=0, font=("Mali Light","10"),
                    bg="#FEF7DC",
                    fg="#753422",
                    pady=10, padx=10,
                    anchor="w",justify="left")
        self.next_button.config(bg=COLOR_5, fg=COLOR_7)
        self.prev_button.config(bg=COLOR_5, fg=COLOR_7)
        self.page_label.config(bg=COLOR_7, fg=COLOR_5)
        self.next_button.config(state="disabled")
        self.prev_button.config(state="disabled")
        self.page_label.config(text="page 0/0")
        self.anxiety_read_button.config(bg=COLOR_4, fg=COLOR_5, relief="flat", padx=5)
        self.anxiety_read_label.config(bg=COLOR_4, fg=COLOR_5)
        self.anxiety_confirm_button.config(bg=COLOR_5, fg=COLOR_7, relief="flat")
    def anxiety_setup_2(self):
        self.intro_1.place(relwidth=0, relheight=0)
        self.intro_2.place(relwidth=0, relheight=0)
        self.guide.place(relwidth=0.9, relx=0.05, rely=0.31, relheight=0.30)
        self.button_find.config(state="normal")
        self.topic_list.place(relwidth=0.35, relx=0.38, rely=0.08)
        self.button_find.place(relx=0.75, rely=0.08) 
        self.next_button.place(rely=0.92, relx=0.6, relwidth=0.1)
        self.prev_button.place(rely=0.92, relx=0.3, relwidth=0.1)
        self.page_label.place(rely=0.92, relx=0.45, relwidth=0.1)
        self.anxiety_read_button.place(relx=0.6, rely=0.78)
        self.anxiety_read_label.place(relheight=0, relwidth=0)
        self.anxiety_confirm_button.place(relwidth=0, relheight=0)
        self.anxiety_infor()
    def anxiety_infor(self):
        self.prev_button.config(state="normal")
        self.next_button.config(state="normal")
        self.next_button.bind("<Button-1>",self.rightkey)
        self.prev_button.bind("<Button-1>",self.leftkey)
        self.intro_1.place(relwidth=0, relheight=0)
        # show image
        temp=self.topic_list.get()
        num=self.topic.index(str(temp))
        #print(num," - ",temp)
        img=ImageTk.PhotoImage(Image.open(self.topic_img[num]))
        self.infor_img=Label(self.frame, image=img)
        self.infor_img.image=img       
        self.infor_img.place(relx=0.05, rely=0.16, relwidth=0.9, relheight=0.7)
        # recognise arrow key
        self.stories=[]
        self.read_story()
        self.num_page = int(np.ceil(len(self.stories[self.topic_list.get()])/4))
        self.page_label.config(text=f"page 0/{int(np.ceil(len(self.stories[self.topic_list.get()])/4))}")
        self.frame.focus_set()
    def read_story(self):
        # read story
        self.stories = story_infor.stories
        self.pos=0
        self.page=1
    def leftkey(self,event):
        try:
            anxiety.sub_frame_2.place_forget()
        except AttributeError:
            pass
        self.next_button.config(state="normal")
        if self.pos-4>=0: 
            #print(self.pos)
            self.page-=1
            self.pos-=4
            self.display_story()
            
        else: self.prev_button.config(state="disabled")
        #print(-1)
    def rightkey(self,event):
        try:
            anxiety.sub_frame_2.place_forget()
        except AttributeError:
            pass
        self.prev_button.config(state="normal")
        if self.pos<=len(self.stories) and self.page<=self.num_page: 
            self.display_story()
            if self.pos+4<=len(self.stories) : 
                self.pos+=4
                self.page+=1
            else: self.next_button.config(state="disabled")
        #print(1)
    def display_story(self):
        label_y=0.01
        self.sub_frame=Frame(self.frame)
        self.sub_frame_2=Frame(self.frame)
        self.sub_frame.config(bg=COLOR_7)
        self.sub_frame_2.config(bg=COLOR_7)
        self.sub_frame.place(relwidth=0.5, relheight=0.7, relx=0.45, rely=0.16)
        self.page_label.config(text=f"page {self.page}/{int(np.ceil(len(self.stories[self.topic_list.get()])/4))}")
        for i in range(self.pos, self.pos+4):
            if i < len(self.stories[self.topic_list.get()]):
                temp=story(self.sub_frame, self.stories[self.topic_list.get()][i],  self.topic_list.get(),0.1,label_y)
                label_y+=0.25
            else: break
    def frame_place(self):
        self.clear()
        self.frame_setup()
        self.frame_config()
        self.anxiety_setup()
#class Testing Frame
class rate:
    def __init__(self, frame):
        self.choices=[]
        self.r=StringVar()
        self.r.set(0)
        for index in range(0,4):
            self.button=Radiobutton(frame, text='',variable=self.r,value=index)
            self.choices.append(self.button)
    def point(self):
        return self.r.get()
class testing_frame(root_frame):
    def __init__(self, name, color):
        super().__init__(name, color)
        
    def testing_setup(self):
        self.read=IntVar()
        self.read.set("0")
        testing_intro_1=Label(self.frame, text="THANG ĐÁNH GIÁ MỨC ĐỘ LO ÂU")
        testing_intro_2=Label(self.frame, text="Thang điểm DASS 21 (Depression - Anxiety - Stress Scale)")
        testing_guide_1=Text(self.frame)
        testing_guide_2=Text(self.frame)
        self.testing_read_button=Radiobutton(self.frame, variable=self.read, value=1)
        testing_read_label=Label(self.frame, text="Bạn đã đọc kỹ hướng dẫn trên")
        self.testing_confirm_button=Button(self.frame, text="Tiếp tục", command=lambda: self.testing_start(self.read.get()))

        testing_guide_1.insert(END,"CÁC BẠN TRẢ LỜI CÂU HỎI VÀ TÍNH ĐIỂM DỰA TRÊN TIÊU CHÍ NÀY NHÉ\n\
    0 - Không Đúng với bạn chút nào.\n\
    1 - Đúng với bạn một phần, hoặc thỉnh thoảng mới đúng.\n\
    2 - Đúng với bạn phần nhiều, hoặc phần lớn thời gian là đúng.\n\
    3 - Hoàn toàn đúng với bạn, hoặc hầu hết thời gian là đúng.\n")
        testing_guide_2.insert(END, "CÁCH TÍNH ĐIỂM\n\
    Cộng tất cả điểm thanh phần rồi nhân với hệ số 2\n")
        
        testing_intro_1.config(font=("Time", "11", "bold italic"),bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        testing_intro_2.config(font="Time 9 italic",bd=0, 
                    bg="#FFDF91",
                    fg="#1B1A17",
                    pady=10)
        testing_guide_1.config(bd=0, font=("Mali Light","8"),
                    bg="#FEF7DC",
                    fg="#753422",
                    pady=10, padx=10)
        testing_guide_2.config(bd=0, font=("Mali Light","8"),
                    bg="#FEF7DC",
                    fg="#753422",
                    pady=10, padx=10)
        self.testing_read_button.config(bg=COLOR_4, fg=COLOR_5, relief="flat", padx=5)
        testing_read_label.config(bg=COLOR_4, fg=COLOR_5)
        self.testing_confirm_button.config(bg=COLOR_5, fg=COLOR_7, relief="flat")

        testing_intro_1.place(relwidth=0.9, relx=0.05, rely=0.16)
        testing_intro_2.place(relwidth=0.9, relx=0.05, rely=0.23)
        testing_guide_1.place(relwidth=0.9, relx=0.05, rely=0.31, relheight=0.30)
        testing_guide_2.place(relwidth=0.9, relx=0.05, rely=0.62, relheight=0.15)
        self.testing_read_button.place(relx=0.6, rely=0.78)
        testing_read_label.place(relheight=0.05, relwidth=0.31,relx=0.64, rely=0.78)
        self.testing_confirm_button.place(relwidth=0.15, relheight=0.05, relx=0.8,rely=0.88)
    def testing_setup_2(self):
        label_x=0.71
        for index in range(0,4):
            rate_label=Label(self.frame, text=str(index))
            rate_label.config(bg=COLOR_7, fg=COLOR_2, font=("Helvectica", "7" ,"bold"))
            rate_label.place(relx=label_x, rely=0.135)
            label_x+=0.05
        ques_list=[ "Tôi bị khô miệng\n",
                    "Tôi bị rối loạn nhịp thở \n (thở gấp, khó thở dù chẳng làm việc gì nặng)",
                    "Tôi bị ra mồ hồi\n",
                    "Tôi lo lắng về những tình huống có thể làm tôi hoảng sợ,\n hoặc biến tôi thành trò cười",
                    "Tôi thấy mình gần như hoảng loạn\n",
                    "Tôi nghe thấy rõ tiếng nhịp tim dù chẳng làm việc gì cả \n(ví dụ: tiếng nhịp tim tăng, tiếng tim loạn nhịp)",
                    "Tôi hay sợ vô cớ\n"]
        self.ans_list=[]
        label_y=0.2
        for index,ques in enumerate(ques_list):
            label=Label(self.frame, text=f"{ques}" )
            self.ans_list.append(rate(self.frame))
            label.config(anchor="w",justify="left",bg=COLOR_7, fg=COLOR_5, font=("Helvectica", "8", "italic"))
            label.place(relwidth=0.5, relx=0.1, rely=label_y)
            label_x=0.7
            for choice in self.ans_list[index].choices:
                choice.place(relx=label_x, rely=label_y)
                choice.config(bg=COLOR_7)
                label_x+=0.05     
            label_y+=0.1
        self.canvas.create_rectangle(40,68, 610,444, fill=COLOR_7, width=0)
        self.canvas.create_line(420,70,420,440,fill=COLOR_5)
        self.canvas.create_line(50,90,600,90, fill=COLOR_5)
        self.canvas.create_line(50,144,600,144, fill=COLOR_5)
        self.canvas.create_line(50,194,600,194, fill=COLOR_5)
        self.canvas.create_line(50,244,600,244, fill=COLOR_5)
        self.canvas.create_line(50,294,600,294, fill=COLOR_5)
        self.canvas.create_line(50,344,600,344, fill=COLOR_5)
        self.canvas.create_line(50,394,600,394, fill=COLOR_5)
        self.result_button=Button(self.frame,text="KẾT QUẢ", command=lambda:self.testing_setup_3())
        self.result_button.config(bg=COLOR_4, fg=COLOR_2, relief="flat")
        self.result_button.place(relwidth=0.3, relx=0.65, rely=0.9)
    def testing_setup_3(self):
        self.clear()
        self.frame_setup()
        self.frame_config()
        img_list=["Image/Good.jpg","Image/ok.jpg","Image/quite-ok.jpg","Image/not_okay.jpg","Image/doctor.jpg"]
        point_frame=Frame(self.frame)
        img_frame=Frame(self.frame)
        point=Label(point_frame, text="")
        ann=Label(point_frame, text="")
        sum=0
        for ans in self.ans_list:
            sum+=int(ans.point())
        sum*=2
        if sum>=0 and sum<=7: 
            ann.config(text="Bình Thường")
            img=ImageTk.PhotoImage(Image.open(img_list[0]))
        if sum>=8 and sum<=9: 
            ann.config(text="Nhẹ")
            img=ImageTk.PhotoImage(Image.open(img_list[1]))
        if sum>=10 and sum<=14: 
            ann.config(text="Vừa")
            img=ImageTk.PhotoImage(Image.open(img_list[2]))
        if sum>=15 and sum<=19: 
            ann.config(text="Nặng")
            img=ImageTk.PhotoImage(Image.open(img_list[3]))
        if sum>19: 
            ann.config(text="Rất Nặng")
            img=ImageTk.PhotoImage(Image.open(img_list[4]))
        
        infor_img=Label(img_frame, image=img, bg=COLOR_7)
        infor_img.image=img       
        img_canvas=Canvas(img_frame)
        img_canvas.config(bg=COLOR_7)
        point_frame.config(bg=COLOR_4)
        point.config(text=str(sum), font=("Mali Light", "90" ,"bold"), bg=COLOR_4)
        ann.config(font=("Mali Light", "15" ,"italic"), bg=COLOR_4)

        img_frame.place( relheight=0.75,relwidth=0.5, rely=0.15, relx=0.45)
        point_frame.place(relheight=0.75, relwidth=0.4, rely=0.15, relx=0.05)
        point.place(relx=0.2,rely=0.1, relwidth=0.6)
        ann.place(relx=0.2,rely=0.7, relwidth=0.6)
        infor_img.place(relwidth=1, relheight=1)
    def testing_start(self,temp):
        if int(temp)==1:
            self.clear()
            self.frame_setup()
            self.frame_config()
            self.canvas.place(relheight=1, relwidth=1)
            
            self.testing_setup_2()
        else: messagebox.showerror("ERROR","Bạn chưa đọc kỹ")
    def frame_place(self):
        self.clear()
        self.frame_setup()
        self.frame_config()
        self.testing_setup() 
#class Sharing Frame
class sharing_frame(root_frame):
    def __init__(self, name, color):
        super().__init__(name, color)
    def frame_place(self):
        self.clear()
        self.frame_setup()
        self.frame_config()
        self.sharing_setup()
    def sharing_setup_0(self):
        pass
    def sharing_setup(self):
        self.val=["Học tập","Gia đình","Mối quan hệ xã hội","Bản thân học sinh"]
        admin_frame=Frame(self.frame)
        mess_frame=Frame(self.frame)
        sharing_intro=Label(self.frame, text="Đây sẽ là bí mật của tụi mình")
        self.sharing_topic_list=ttk.Combobox(self.frame, values=self.val)
        sharing_topic_intro=Label(self.frame, text="Chủ đề của câu chuyện")
        sharing_finish=Button(self.frame, text="Chia Sẻ")
        sharing_admin=Label(admin_frame, text="USERS")
        self.sharing_admin1=Button(admin_frame, text="ADMIN 1")
        self.sharing_admin2=Button(admin_frame, text="ADMIN 2")
        self.sharing_show_mess=Text(mess_frame)
        self.sharing_input_mess=Text(mess_frame)
        self.feedback_input_mess=Text(mess_frame)
        self.feedback_send_button=Button(self.frame, text="Gửi Hồi Đáp")
        self.sharing_show_mess.insert(END,f"Chọn Admin 1 hoặc 2 để có thể nói chuyện với chúng mình.\n")
        
        admin_frame.config(bg=COLOR_3)
        mess_frame.config(bg=COLOR_4)
        sharing_intro.config(bg=COLOR_1,fg=COLOR_5)
        sharing_topic_intro.config(bg=COLOR_1, fg=COLOR_5)
        sharing_finish.config(bg=COLOR_5, fg=COLOR_7, relief="flat", command=lambda:self.sharing_setup_2())
        sharing_admin.config(bg=COLOR_5, fg=COLOR_7)
        self.sharing_admin1.config(bg=COLOR_5, fg=COLOR_7, relief=GROOVE, command=lambda:self.admin_setup(1))
        self.sharing_admin2.config(bg=COLOR_5, fg=COLOR_7, relief=GROOVE, command=lambda:self.admin_setup(2))
        self.sharing_show_mess.config(bg="white", relief="flat", state="disabled")
        self.sharing_input_mess.config(bg="white", relief="flat")
        self.sharing_input_mess.bind("<Return>",self.show_message)
        self.feedback_input_mess.config(bg="white", relief="flat")
        self.feedback_input_mess.bind("<Return>", self.collect_feedback)
        self.feedback_send_button.config(bg=COLOR_5, fg=COLOR_7, relief="flat", command=lambda:self.sharing_setup_3())

        admin_frame.place(relwidth=0.1, relheight=0.7, rely=0.15, relx=0.05)
        mess_frame.place(relwidth=0.8, relheight=0.7, rely=0.15, relx=0.15)
        sharing_topic_intro.place(relwidth=0.3, relx=0.33, rely=0.08)
        self.sharing_topic_list.place(relwidth=0.3, relx= 0.65, rely=0.08)
        sharing_finish.place(relx=0.8, rely=0.88, relwidth=0.15)
        sharing_admin.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        self.sharing_admin1.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)
        self.sharing_admin2.place(relx=0, rely=0.6, relwidth=1, relheight=0.1)
        self.sharing_show_mess.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.44)
        self.sharing_input_mess.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.4)
        
    def admin_setup(self,num):
        self.story=''
        self.feedback=''
        if num==1: self.sharing_admin2.config(state="disabled")
        else: self.sharing_admin1.config(state="disabled")
        self.sharing_show_mess.config(state="normal")
        self.sharing_show_mess.insert(END,f"ADMIN: Hi!! Bạn có thể chia sẻ bất cứ chuyện gì, đó sẽ là bí mật của tụi mình\n")
        self.sharing_show_mess.config(state="disabled")
    def sharing_setup_2(self):
        global user_current
        if not(self.sharing_topic_list.get() in self.val): messagebox.showerror("ERROR","Bạn chưa chọn chủ đề")
        else :
            respone=messagebox.askokcancel("Chia sẻ câu chuyện",f"Chủ đề: {self.sharing_topic_list.get()}")
            datas= {user_current.email:self.story,}
            files=[ ('datas', ('datas', json.dumps(datas), 'application/json')),]
            r = requests.post(url_story, files=files)
            #print(r.text)
            if respone==1:
                self.sharing_show_mess.config(state="normal")
                self.sharing_show_mess.delete(1.0,END)
                self.sharing_show_mess.insert(END,f"ADMIN: Hì hì, Bạn hãy nói vài lời cũng như góp ý về dự án của tụi mình\n")
                self.sharing_show_mess.config(state="disabled")
                self.feedback_input_mess.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.4)
                self.feedback_send_button.place(relx=0.8, rely=0.88, relwidth=0.15)
    def collect_feedback(self,event):
        self.feedback += self.feedback_input_mess.get(1.0, END)
    def sharing_setup_3(self):
        global current_user
        menu_button.enable_button()
        respone=messagebox.askokcancel("Information","Send Feedback")
        if respone:
            datas= {current_user.email:self.feedback,}
            files=[ ('datas', ('datas', json.dumps(datas), 'application/json')),]
            r = requests.post(url_feedback, files=files)
            #print(r.text)
        self.sharing_input_mess.delete(1.0,END)
    def show_message(self,event):
        temp=''
        temp1=self.sharing_input_mess.get(1.0,END)
        if temp1[0]=="\n": temp=temp1[1:len(temp1)]
        else: temp=temp1
        self.sharing_show_mess.config(state="normal")
        self.sharing_show_mess.insert(END,f"YOU: {temp}")
        self.sharing_input_mess.delete(1.0,END)
        self.sharing_input_mess.insert(1.0,"")
        self.sharing_show_mess.config(state="disabled")
        self.story+=temp
# SETUP MAIN WINDOW
def on_closing():
    if messagebox.askokcancel("Quit","Do you want to quit?"):
        mixer.music.stop()
        root.destroy()
root=Tk()
root.title("Anxiety Healing")
root.geometry("800x500")
root_canvas=Canvas(root)
root_canvas.place(relheight=1, relwidth=1)
root.resizable(0,0)
root.protocol("WM_DELETE_WINDOW", on_closing)


def play_music():
    mixer.init()
    for song in music_list:
        song_mut = MP3(song)
        song_length = song_mut.info.length
        mixer.music.load(song)
        mixer.music.play(loops=0)
        mixer.music.set_volume(0.2)
        time.sleep(np.ceil(song_length))
        
def start_threading_music():
    thread1 = threading.Thread(target=play_music)
    thread1.start()
start_threading_music()
os.startfile("server.exe")
global current_user
current_user=user_info("","","")
# setup menu frame
menu_frame=Frame(root)
menu_name=Label(menu_frame, text="ANXIETY HEALING")
menu_home_button=menu_button(menu_frame,"TRANG CHỦ",0.27)
menu_anxiety_button=menu_button(menu_frame,"CÂU CHUYỆN",0.42)
menu_testing_button=menu_button(menu_frame,"KIỂM TRA",0.57)
menu_feedback_button=menu_button(menu_frame,"CHIA SẺ",0.72)
menu_author_button=Button(menu_frame, text="@yenKhuong - 2021")
menu_frame.config(bg=COLOR_2)
menu_name.config(font=("Time", 12, "bold italic"),
                bg=COLOR_2,fg=COLOR_1)
menu_author_button.config(fg=COLOR_5,bg=COLOR_2)
menu_frame.place(relheight=1, relwidth=0.2)
menu_name.place(relheight=0.1, relwidth=1, rely=0.06)
menu_author_button.place(relheight=0.1, relwidth=0.8, relx=0.1, rely=0.9)

# setup inf frame 
inf_frame=Frame(root)
inf_frame_canvas=Canvas(inf_frame)
inf_frame.config(bg=COLOR_7)
inf_frame_canvas.config(bg=COLOR_7)
inf_frame.place(relheight=1,relwidth=0.8, relx=0.2)
inf_frame_canvas.place(relheight=1, relwidth=1)

# setup login frame
login=login_frame()

# setup main frame
home=home_frame("TRANG CHỦ", COLOR_1) 
anxiety=anxiety_frame("CÂU CHUYỆN", COLOR_1)
testing=testing_frame("KIỂM TRA", COLOR_1)
feedback=sharing_frame("CHIA SẺ", COLOR_1)
intro=intro_frame("CHÀO MỪNG",COLOR_1)

menu_home_button.button_config(home)
menu_anxiety_button.button_config(anxiety)
menu_testing_button.button_config(testing)
menu_feedback_button.button_config(feedback)
menu_author_button.config(command=lambda: intro.frame_place(), relief="flat", state="disabled")
root.mainloop()
