import tkinter as tk
from pingPolish import WebsiteCheckerPolish

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x800")  # set window size
        self.window.title("Interface")  # set window title

        self.button = tk.Button(self.window, text="Click me!", command=self.on_click)
        self.button.pack(pady=20)  # add padding around button

    def on_click(self):
        checker = WebsiteCheckerPolish('https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites')
        checker.run()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Interface()
    app.run()
