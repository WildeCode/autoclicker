import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

pad_frm = ttk.Frame(padding=20)
instruct_frm = ttk.Frame(master=pad_frm,
                         relief=tk.FLAT)
assign_frm = ttk.Frame(master=pad_frm,
                       relief=tk.GROOVE)
instruct_lbl = ttk.Label(master=instruct_frm,
                     text="Click the button to assign a turbo key")
assign_btn = ttk.Button(master=assign_frm,
                        width=10,
                        text="Click Me")

pad_frm.pack()
instruct_frm.pack()
assign_frm.pack()
instruct_lbl.pack()
assign_btn.pack()

window.mainloop()