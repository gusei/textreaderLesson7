import tkinter as tk
from tkinter.filedialog import askopenfilename
def open_file():
    """Отрываем файл для редактирования"""
    filepath=askopenfilename(filetypes=[("Текстовые файлы",".txt"),("Все файлы","*.*")])

    if not filepath:
        return
    txt_edit.delete("1.0",tk.END)
    with open(filepath,'r') as input_file:
        text=input_file.read()
        txt_edit.insert(tk.END,text)
    win.title(f"Простой текстовой редактор-{filepath}")

def save_file():
    """Сохраняем текущий файл как новый файл"""
    filepath=askopenfilename(
        defaultextension='txt',filetypes=[("Текстовые файлы","*txt"),("Все файлы","*.*")],
    )
    if not filepath:
        return
    with open(filepath,'w')as output_file:
        text=txt_edit.get("1.0",tk.END)
        output_file.write(text)
    win.title(f"Простой текстовой редактор-{filepath}")


win = tk.Tk()
win.title("Простой текстовой редактор")
# Строки 3 и 4 создают новое окно с заголовком

win.rowconfigure(0, minsize=800, weight=1)
win.columnconfigure(1, minsize=800, weight=1)
# Строки 6 и 7 устанавливают конфигурацию строк и столбцов

txt_edit = tk.Text(win)
fr_buttons = tk.Frame(win,relief=tk.RAISED,bd=2)
btn_open = tk.Button(fr_buttons, text='Открыть',command=open_file)
btn_save = tk.Button(fr_buttons, text='Сохранить как....',command=save_file)

# Строки 9 и 12 создают четыре виджета — текстовый бокс,
# рамку, кнопка для открытия и кнопка для сохранения файла.


btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)

fr_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

win.mainloop()
