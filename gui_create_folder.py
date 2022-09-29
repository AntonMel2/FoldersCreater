from tkinter import*
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter.ttk import Combobox
from create_folders import FolderCr

class Window:
    def __init__(self, width, height, title="Folder Creator", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        self.name = Entry(self.root, width=25, font=("Verdana", 10), justify=CENTER)
        n = StringVar()
        self.parts = Combobox(self.root, state="readonly",
                              textvariable=n, justify=CENTER, font=("Times New Roman", 12))
        self.parts['values'] = ('6', '7', '8', '9', '10', '11', '12', '13', '14')

    def run(self):
        self.draw_widgets()
        self.parts.current(4)
        self.root.geometry("600x300+600+200")
        self.root.mainloop()

    def draw_widgets(self):
        self.name.grid(row=0, column=1, padx=20)
        self.parts.grid(row=1, column=1, padx=20)
        self.draw_menu()
        Label(self.root, text="Название проекта: ",
              font=("Times New Roman", 14)).grid(row=0, column=0, padx=50, pady=30)
        Label(self.root, text="Количество подпапок: ",
              font=("Times New Roman", 14)).grid(row=1, column=0, pady=30)
        Button(self.root, text="Создать папку", width=20, command=self.conf_create,
               font=("Times New Roman", 12)).grid(row=2, column=0, columnspan=2, pady=20)

    def draw_menu(self):
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Выйти", command=self.exit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.root.configure(menu=menu_bar)

    def conf_create(self):
        choice = mb.askyesno("Создание папки", "Вы точно хотите создать папку?")
        if choice:
            film_name = self.name.get()
            value = int(self.parts.get())
            if self.name.get() and self.parts.get():
                if self.valid_value(self.name.get()):
                    directory = fd.askdirectory(title="Выберите каталог для создания папки", mustexist=True)
                    if directory and FolderCr(film_name, directory).create_folder(value):
                        mb.showinfo("Отлично", f'Поздравляю. Папка с именем "{self.name.get()}" создана успешно.')
                    elif not directory:
                        mb.showinfo("Информация", "Вы отменили создание папки")
                    else:
                        mb.showerror("Ошибка", f'Используйте другое имя. \n Папка с именем "{self.name.get()}" уже существует!')
            else:
                mb.showerror("Ошибка", "Заполните все поля!")

    def valid_value(self, value):
        flag = True
        invalid = '\/:*?"<>|'
        for i in value:
            if i in invalid:
                mb.showerror("Ошибка", 'Некорректное название, использование символов \ / : * ? " < > | запрещено')
                flag = False
                break
        if flag == True:
            return True
        else:
            return False

    def exit(self):
        choice = mb.askyesno("Выход", "Вы действительно хотите выйти?")
        if choice:
            self.root.destroy()

if __name__ == "__main__":
        window = Window(1200, 1600)
        window.run()

