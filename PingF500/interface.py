import tkinter as tk
from pingPolish import WebsiteCheckerPolish

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x800")
        self.window.title("Interface")
        
        self.result_label = tk.Label(self.window, text='')
        self.result_label.pack(pady=20)

        self.button = tk.Button(self.window, text="Search Websites", command=self.on_click)
        self.button.pack(pady=20)

    def on_click(self):
        checker = WebsiteCheckerPolish('https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites')
        checker.run()
        result_text = '\n'.join(checker.used_urls) if checker.used_urls else "NO URLS IN USE!"
        self.result_label.config(text=result_text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Interface()
    app.run()
