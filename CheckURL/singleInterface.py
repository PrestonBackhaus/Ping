import tkinter as tk
from single import SingleChecker

EXAMPLE = 'https://www.żywienie.com'

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x800")
        self.window.title("Interface")
        
        self.intro_label = tk.Label(self.window, text='Must use "http(s)://www.abc.com"')
        self.intro_label.pack(pady=20)
        
        self.input_box = tk.Entry(self.window)
        self.input_box.pack(pady=20)
        
        self.button = tk.Button(self.window, text='Check', command=self.on_button_click)
        self.button.pack()
        
        self.result_label = tk.Label(self.window, text='', wraplength=700)
        self.result_label.pack(pady=20)

    def on_button_click(self):
        input_text = self.input_box.get()
        checker = SingleChecker(input_text)
        result = checker.run()
        print(result)
        self.input_box.delete(0, tk.END)
        self.result_label.configure(text=result)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Interface()
    app.run()
