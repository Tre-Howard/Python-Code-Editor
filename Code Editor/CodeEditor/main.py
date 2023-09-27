import tkinter as tk
from tkinter import filedialog

class CodeEditor:
    def __init__(self, root):

        # ------------ Initialization ------------
        self.root = root
        self.root.title("Code Editor")
        self.root.geometry("800x500")  # geometry allows you to pick window size

        # ------------ Textbox ------------
        self.textbox = tk.Text(root, wrap="word")
        self.textbox.pack(expand=True, fill="both")

        # ------------ Buttons ------------
        self.import_file_button = tk.Button(root, text="Open File", command=self.import_file)
        self.import_file_button.pack(side="left", padx=10, pady=10)

        self.save_as_text_button = tk.Button(root, text="Save as Text", command=self.save_as_text)
        self.save_as_text_button.pack(side="right", padx=10, pady=10)

        self.save_as_python_button = tk.Button(root, text="Save as Python", command=self.save_as_python)
        self.save_as_python_button.pack(side="right", padx=10, pady=10)  # side = attach to a side of the window / pad x&y means padding

        # ------------ Menu Bar ------------
        self.menubar = tk.Menu(root)  # create a menu bar

        # sub menus and add them to main menu bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)

        # file sub menu options
        self.filemenu.add_command(label="Open", command=self.import_file)  # add a function/button in the sub menu bar named filemenu named Open
        self.filemenu.add_command(label="Save", command=self.menu_save)  # add a function/button in the sub menu bar named filemenu named save
        self.filemenu.add_separator()  # puts a line between function/buttons in the file menu for UX
        self.filemenu.add_command(label="Quit", command=quit)  # add a function/button in the sub menu bar named filemenu named save

        # edit sub menu options
        self.editmenu.add_command(label="Copy", command=self.copy_text)
        self.editmenu.add_command(label="Cut", command=self.cut_text)
        self.editmenu.add_command(label="Paste", command=self.paste_text)

        # add sub menus to the main menu bar and name them
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.editmenu, label="Edit")

        self.root.config(menu=self.menubar)  # add parent menu bar to program, which houses the submenu filemenu, which houses close

    # ------------ Functions/Methods ------------

    def copy_text(self):  # copies the text in the textbox and adds it to the clipboard
        content = self.textbox.get("1.0", tk.END)
        root.clipboard_clear()
        root.clipboard_append(content)

    def cut_text(self):  # copies the text in the textbox and adds to clipboard, deletes info in textbox
        content = self.textbox.get("1.0", tk.END)
        root.clipboard_clear()
        root.clipboard_append(content)
        self.textbox.delete("1.0", tk.END)

    def paste_text(self):  # past the users clipboard into the textbox at the end
        content = root.clipboard_get()
        self.textbox.insert(tk.END, content)

    def save_as_text(self):  # takes the textbox information, add it to var code, then saves as a text file
        code = self.textbox.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:  # "w" means write
                f.write(code)

    def save_as_python(self):  # takes the textbox information, add it to var code, then saves as a python file
        code = self.textbox.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                filetypes=[("Python files", "*.py")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(code)

    def menu_save(self):  # takes the textbox information, add it to var code, then saves as a text or python file
        code = self.textbox.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(
            filetypes=[("Python files", "*.py"), ("Text files", "*.txt")]
        )

        if file_path:
            with open(file_path, "w") as f:
                f.write(code)

    def import_file(self):  # asks for a file (python/text) and then imports it into the textbox
        file_path = filedialog.askopenfilename(
            filetypes=[("Python files", "*.py"), ("Text files", "*.txt")]
        )

        # checks if a file was selected
        if file_path:
            with open(file_path, 'r') as file:  # 'r' means read
                file_contents = file.read()
                self.textbox.delete("1.0", tk.END)  # clears existing code in textbox
                self.textbox.insert("1.0", file_contents)
        else:  # else do nothing
            print("No file selected.")


# ------------ Main/Run Program ------------
if __name__ == "__main__":
    root = tk.Tk()  # make Tk() into a variable named root
    editor = CodeEditor(root)  # take root and create an instance of the CodeEditor class using the root or Tk() as the parent/reference
    root.mainloop()  # run until forced to stop/x button/etc
