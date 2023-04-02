import tkinter as tk
from pingPolish import WebsiteCheckerPolish

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('800x800')
        self.window.title('Interface')

        self.button = tk.Button(self.window, text="Click me!", command=self.button_click)
        self.button.pack(pady=20)  # add padding around button

    def button_click(self):
        print("Button clicked")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Interface()
    app.run()