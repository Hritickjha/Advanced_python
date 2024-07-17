import tkinter as tk
from tkinter import filedialog

class NotePad(tk.Tk):
    def_init: any
    self=tk   
    self.title("Notepad")
        
    self.text = tk.Text(self,wrap="word")
    self.text.pack(side='top',fill='both',expand=True)
        
    self.menu = tk.Menu(self)
    self.config(menu=self.menu)
        
    #Create a file menu
    file_menu = tk.Menu(self.menu)
    self.menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="New",command=self.new_file)
    file_menu.add_command(label="Open",command=self.open_file)
    file_menu.add_command(label="save",command=self.save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit",command=self.quit)
        
    #create an edit menu
    edit_menu = tk.Menu(self.menu)
    self.menu.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="cut",command=self.cut)
    edit_menu.add_command(label="copy",command=self.copy)
    edit_menu.add_command(label="paste",command=self.paste)
        
    def new_file(Self):
        Self.text.delete("1.0","end")
        Self.title("Notepad")
    def open_file(Self):
            file = filedialog.askopenfile(parent=Self,mode="rb",title="Open a file")
            if file:
                contents = file.read()
                Self.text.delet("1.0","end")
                Self.text.insert("1.0",contents)
                file.close()
                Self.title(file.name+"-Notepad")
        
    def cut(Self):
            Self.text.event_generate("<<cut>>")
    def copy(Self):
            Self.text.event_generate("<<copy>>")
    def paste(Self):
            Self.text.event_generate("<<paste>>")
if __name__ == "_main":
    NotePad = NotePad()
    NotePad.mainloop()
            
                        
    