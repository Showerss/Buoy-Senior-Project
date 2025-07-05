import tkinter as tk

class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.resizable(True, True)
        self.canvas = tk.Canvas(self, width=500, height=500, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.canvas.config(width=self.width*wscale, height=self.height*hscale)

if __name__ == '__main__':
    app = MainScreen()
    app.mainloop()
