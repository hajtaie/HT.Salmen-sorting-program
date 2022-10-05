from tkinter import *
root = Tk()
"""prompt = '      Press any key      '
label1 = Label(root, text=prompt, width=len(prompt), bg='yellow')
label1.pack()
def key(event):
    if event.char == event.keysym:
        msg = 'Normal Key %r' % event.char
    elif len(event.char) == 1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym
    label1.config(text=msg)
root.bind_all('<Control-Key-C>', key)
root.bind_all('<Control-Key-1>', key)
root.bind_all('<Control-Key-2>', key)
root.bind_all('<Control-Key-/>', key)"""
button=Button(bg="#0062ec",width=1,height=2).pack()
button.pack_forget()
root.mainloop()