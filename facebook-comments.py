# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

import requests
# root.iconbitmap('tends.ico')
root = Tk()

root.title("Facebook get comments Coded by:Ismael Al-safadi")

buButton = ttk.Button(root, text="GO")
buButton.grid(row=9, column=3)
ttk.Label(root, text="Access Token:").grid(row=1, column=0, pady=10, padx=10)
Name = ttk.Entry(root, width=50)
Name.grid(row=1, column=1, columnspan=2, pady=10)
#
ttk.Label(root, text="User ID:").grid(row=2, column=0, pady=10, padx=10)
idu = ttk.Entry(root, width=50)
idu.grid(row=2, column=1, columnspan=2, pady=10)
#
ttk.Label(root, text="Post ID:").grid(row=3, column=0, pady=10, padx=10)
idp = ttk.Entry(root, width=50)
idp.grid(row=3, column=1, columnspan=2, pady=10)
global post_id
global access_token
global user_id


def onc():
    access_token=Name.get()
    user_id=idu.get()
    post_id=idp.get()


    graph_api_version = 'v2.9'
    url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, user_id, post_id)

    comments = []

    r = requests.get(url, params={'access_token': access_token})
    while True:
        data = r.json()
        if 'error' in data:
            raise Exception(data['error']['message'])
        for comment in data['data']:
            text = comment['message'].replace('\n', ' ')
            comments.append(text)

        print('got {} comments'.format(len(data['data'])))
        if 'paging' in data and 'next' in data['paging']:
            r = requests.get(data['paging']['next'])
        else:
            break
    with open('comments.txt', 'w') as f:
        for comment in comments:
            comment=comment.encode('utf-8')
            f.write(comment + '\n')
        f.close()
    messagebox.showinfo(title="Done", message="Done ^__^ Check 'comments.txt' ")        
try:
    buButton.config(command=lambda: onc())
except:
    messagebox.showerror(title='Ops', message="please select your choices ! ")        
root.mainloop()
