import tkinter as tk
from tkinter import ttk
from all_polish import AllChecker

class AllCheckerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create label and textbox for user input
        self.input_label = ttk.Label(self, text='Enter URL:')
        self.input_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.input_box = ttk.Entry(self, width=50)
        self.input_box.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Create button to trigger AllChecker run
        self.check_button = ttk.Button(self, text='Check', command=self.run_all_checker)
        self.check_button.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Create labels to display AllChecker output
        self.online_label = ttk.Label(self, text='Online URLs: ')
        self.online_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.offline_label = ttk.Label(self, text='Offline URLs: ')
        self.offline_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')

    def run_all_checker(self):
        # Get user input from textbox
        source_url = self.input_box.get()
        # Create AllChecker object and run
        checker = AllChecker(source_url)
        checker.run()
        # Update online and offline labels with AllChecker output
        self.online_label.config(text=f'Online URLs: {", ".join(checker.onlineURLs)}')
        self.offline_label.config(text=f'Offline URLs: {", ".join(checker.offlineURLs)}')

if __name__ == '__main__':
    root = tk.Tk()
    app = AllCheckerGUI(root)
    app.pack()
    root.mainloop()
