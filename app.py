import customtkinter as ctk
from tkinter import messagebox
import threading
import find_ip
import os
from PIL import Image


class GUI:

    def __init__(self, root):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')
        self.app = root
        self.app.title('IPeek')
        self.app.geometry('500x500+650+150')
        self.app.resizable(False, False)
        self.progress_bar = None  
        self.add_background()
        self.welcome()


    def start_process(self):
        self.progress_bar.place(relx=0.5, rely=0.5, anchor="center")  
        self.progress_bar.start()  

        process_thread = threading.Thread(target=self.process)
        process_thread.start()


    def process(self):
        ip_or_domin = self.entry.get().strip()
        ip = find_ip.Find_ip()
        
        if ip.is_private_ip(ip_or_domin):
            messagebox.showinfo("Private IP", "The entered IP is a private IP and does not have public information.")
            self.progress_bar.stop() 
            self.progress_bar.place_forget()  
            return
        
        ip.cheak(ip_or_domin)
        self.progress_bar.stop()  
        self.progress_bar.place_forget()  
        
        if ip.error:
            messagebox.showerror('Error', ip.error)
        else:
            self.show_info(ip)


    def show_info(self, ip):
        self.clear_window()
        self.add_background()
        result_label = ctk.CTkLabel(self.app, text='Result', font=('Arail', 20), text_color='yellow')
        result_label.place(relx=0.5, rely=0.1, anchor="center")

        result = ip.info
        result_text = ctk.CTkTextbox(self.app, wrap="word", height=300, width=400,
                                     font=("Arial", 18), state="normal", text_color='white')
        result_text.insert("1.0", result)
        result_text.configure(state="disabled")
        result_text.place(relx=0.5, rely=0.5, anchor="center")

        back_button = ctk.CTkButton(self.app, text='Back', font=('Arial', 16),
                                    hover_color='red', command=self.back)
        back_button.place(relx=0.5, rely=0.9, anchor="center")


    def clear_window(self):
        try:
            for widget in self.app.winfo_children():
                widget.place_forget()  
        except Exception as e:
            messagebox.showerror('Error', "Error while clearing window: {e}")


    def back(self):
        self.clear_window()
        self.add_background()
        self.welcome()


    def add_background(self):
        self.path_bg_image = os.path.join(os.path.dirname(__file__), 'find_ip_picture.png')
        self.image = ctk.CTkImage(light_image=Image.open(self.path_bg_image), size=(500, 500))
        self.label_image = ctk.CTkLabel(self.app, image=self.image, text='')
        self.label_image.place(relwidth=1, relheight=1)  


    def welcome(self):
        welcome_label = ctk.CTkLabel(self.app, text='Welcome to IPeek',
                                     font=('Arial', 18), text_color='white', bg_color='gray')
        welcome_label.place(relx=0.5, rely=0.1, anchor="center")

        self.entry = ctk.CTkEntry(self.app, placeholder_text='Enter IP or domain',
                                  placeholder_text_color='white', height=30, width=250)
        self.entry.place(relx=0.5, rely=0.2, anchor="center")

        submit_button = ctk.CTkButton(self.app, text='Submit', hover_color='green',
                                      font=('Arial', 20), width=130, height=30,
                                      command=self.start_process)  
        submit_button.place(relx=0.5, rely=0.35, anchor="center")

        self.progress_bar = ctk.CTkProgressBar(self.app, mode='indeterminate', indeterminate_speed=3,
                                               orientation='horizontal')
        self.progress_bar.set(0)

        self.app.bind('<Return>', lambda event: self.start_process())  


app = ctk.CTk()
gui = GUI(app)
app.mainloop()
