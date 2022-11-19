from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk
from tkinter import ttk
import winsound

def combine(word):
    try:
        key_dict = {'type': 'phrase',
                    'text': word+'组词',
                    'word_inc': word
                    }
                    
        url = 'https://guoxue.baike.so.com/query/index/'
        r = requests.get(url, params=key_dict)

        soup = bs(r.text, 'html.parser')
        # 查找上图绿色标注标签
        div_content = soup.find("div", {'class': 'content'})
        # 查找上图橙色标注标签中的a标签
        all_title = div_content.find_all('a', {'data-logid': "ordinal_incgroup_phrases"})
        # 加入判断 判断all_title是否为空
        if all_title:
            # 如果all_title不为空
            combine_list = []
            for t in all_title:
                combine_list.append(t.string)
            return combine_list
        else:
            return -1
    except:
        return -1

def zuci_button(self=None):
    if (len(input_entry.get()) > 1):
        input_error.config(text='仅支持输入1个汉字！')
        input_error.pack()
        winsound.Beep(440, 500)
        return -1

    if (len(input_entry.get()) == 0):
        input_error.config(text='输入为空！')
        input_error.pack()
        winsound.Beep(440, 500)
        return -1

    output = combine(input_entry.get())

    if (output == -1):
        input_error.config(text='组词失败！')
        input_error.pack()
        winsound.Beep(440, 500)
        return -1

    input_error.pack_forget()
    output_text.configure(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(1.0, output)
    output_text.configure(state=tk.DISABLED)

    return 0

def output_clear_command():
    output_text.configure(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.configure(state=tk.DISABLED)

root = tk.Tk()
root.geometry('300x250')
root.title('组词器')
root.resizable(False, False)

ttk.Label(root, text='组词器', font=('宋体', 20)).pack()

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

output_clear = ttk.Button(output_frame, text='清空', command=output_clear_command)
output_clear.pack()

output_frame.pack()

ttk.Label(output_frame, text='词语来源：https://guoxue.baike.so.com').pack()

root.mainloop()