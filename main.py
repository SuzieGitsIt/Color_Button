import tkinter as tk
import tkinter.ttk as ttk   

GUI = tk.Tk();
GUI.title("Button Press Counter")
GUI.geometry("200x100")                                     # Set the geometry of Tkinter frame
s = ttk.Style(); 
s.theme_use('clam');                                     # alt, default, clam and classic
s.configure('T.Button',borderwidth='20')
s.configure('T.Button',highlightthickness='20')             
s.configure('W.Button',highlightcolor='pink')
color = 'pink'
s.map('T.TButton',background=[('active', 'pressed', 'grey'),('!active',color), ('active','!pressed',color)]) # active, not active, not pressed
s.map('T.TButton',relief    =[('pressed','sunken'),('!pressed','raised')]) # pressed, not pressed

class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.bttn = tk.Button(self)
        self.bttn['text'] = "Total Clicks: 0"
        self.bttn['command'] = self.update_count
        self.bttn.grid()
       
    def update_count(self):
        state = bttn_clicks= ["state"] 
        self.bttn_clicks += 1
        if self.bttn_clicks== 5 or self.bttn_clicks== 10 or self.bttn_clicks== 15:
            self.bttn['bg']= "PINK"
        else:
            self.bttn['bg']= "GREY"
        self.bttn['text'] = "Total Clicks: " + str(self.bttn_clicks)
        print(self.bttn_clicks)

app = Application(GUI)

GUI.mainloop() 
