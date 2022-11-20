from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk
from tkinter import ttk
import winsound
import pyperclip

def combine(word):
    try:
        key_dict = {'type': 'phrase',
                    'text': word+'组词',
                    'word_inc': word
                    }
                    
        url = 'https://guoxue.baike.so.com/query/index/'
        r = requests.get(url, params=key_dict)

        soup = bs(r.text, 'html.parser')
        div_content = soup.find("div", {'class': 'content'})
        all_title = div_content.find_all('a', {'data-logid': "ordinal_incgroup_phrases"})
        if all_title:
            combine_list = []
            for t in all_title:
                combine_list.append(t.string)
            return combine_list
        else:
            return -1
    except:
        return -1

def zuci_button(self=None):
    output_copy_successed.pack_forget()
    
    if len(input_entry.get()) > 1:
        if language:
            input_error.config(text='仅支持输入1个汉字！')
        else:
            input_error.config(text='僅支持輸入1個漢字！')
        input_error.pack()
        winsound.Beep(440, 500)
        return -1

    if len(input_entry.get()) == 0:
        if language:
            input_error.config(text='输入为空！')
        else:
            input_error.config(text='輸入為空')
        input_error.pack()
        winsound.Beep(440, 500)
        return -1

    output = combine(input_entry.get())

    if output == -1:
        if language:
            input_error.config(text='组词失败！')
        else:
            input_error.config(text='組詞失敗！')
        input_error.pack()
        winsound.Beep(440, 500)
        return -1

    input_error.pack_forget()
    output_text.configure(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(1.0, output)
    output_text.configure(state=tk.DISABLED)

    return 0

def output_clear_cmd():
    output_text.configure(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.configure(state=tk.DISABLED)
    output_copy_successed.pack_forget()

def output_copy_cmd():
    pyperclip.copy(output_text.get(1.0, tk.END))
    output_copy_successed.pack()

def to_tw():
    language = False
    root.title('組詞器')
    input_frame.config(text='輸入')
    title.config(text='組詞器')
    language_menu.config(title='語言')
    input_frame.config(text='輸入')
    input_button.config(text='組詞')
    output_frame.config(text='輸出')
    output_clear.config(text='清空')
    output_copy.config(text='複製')
    statement.config(text='詞語來源：https://guoxue.baike.so.com')

def to_cn():
    language = True
    root.title('组词器')
    input_frame.config(text='输入')
    title.config(text='组词器')
    language_menu.config(title='语言')
    input_frame.config(text='输入')
    input_button.config(text='组词')
    output_frame.config(text='输出')
    output_clear.config(text='清空')
    output_copy.config(text='复制')
    statement.config(text='词语来源：https://guoxue.baike.so.com')

root = tk.Tk()
root.geometry('300x250')
root.title('组词器')
root.resizable(False, False)

title = ttk.Label(root, text='组词器', font=('宋体', 20))
title.pack()

# Menu
language = True # true = cn; false = tw

main_menu = tk.Menu(root)

language_menu = tk.Menu(main_menu)
language_menu.add_radiobutton(label='简体中文', command=to_cn)
language_menu.add_radiobutton(label='繁體中文', command=to_tw)

main_menu.add_cascade(label='语言', menu=language_menu)

root.config(menu=main_menu)

# 输入部分
input_frame = ttk.LabelFrame(root, text='输入')

input_entry_frame = ttk.Frame(input_frame)

input_entry = ttk.Entry(input_entry_frame, width=20)
input_entry.bind('<Return>', zuci_button)
input_entry.pack(side=tk.LEFT)

input_button = ttk.Button(input_entry_frame, text='组词', command=zuci_button)
input_button.pack(side=tk.RIGHT)

input_entry_frame.pack()

input_error = tk.Label(input_frame)

input_frame.pack()

# 输出部分
output_frame = ttk.LabelFrame(root, text='输出')

output_text = tk.Text(output_frame, width=33, height=5)
output_text.configure(state=tk.DISABLED)
output_text.pack()

output_control_frame = ttk.Frame(output_frame)

output_clear = ttk.Button(output_control_frame, text='清空', command=output_clear_cmd)
output_clear.pack(side=tk.LEFT)

output_copy = ttk.Button(output_control_frame, text='复制', command=output_copy_cmd)
output_copy.pack(side=tk.LEFT)

output_copy_successed = ttk.Label(output_control_frame, text='复制成功！')

output_control_frame.pack()

output_frame.pack()

statement = ttk.Label(output_frame, text='词语来源：https://guoxue.baike.so.com')
statement.pack()

root.mainloop()