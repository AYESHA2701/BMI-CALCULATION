import tkinter as tk

def calculate_bmi():
    try :
        weight =float(weight_entry.get())
        height =float(height_entry.get())
        height_m =height/100
        bmi =weight/(height_m**2)
        result_label.config(text="BMI:"+str(round(bmi,4)))
    except:
        result_label.config(text="Invalid input")
# MAIN WINDOW
root= tk.Tk ()
root.title("BMI Calculator")
root.geometry("300x250")
# WEIGHT
tk.Label(root, text="Weight(kg)").pack()
weight_entry=tk.Entry(root)
weight_entry.pack()
# HEIGHT
tk.Label(root,text="height(cm)").pack()
height_entry=tk.Entry(root)
height_entry.pack()
# BUTTON
tk.Button(root, text ="calculate",command=calculate_bmi).pack(pady=10)
result_label=tk.Label(root,text="")
result_label.pack()

root.mainloop()