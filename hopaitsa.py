import tkinter as tk
from tkinter import messagebox
import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  

def generate_numbers():
    try:
        n = int(entry_n.get())
        a = int(entry_a.get())
        b = int(entry_b.get())

        if n <= 0 or a >= b:
            messagebox.showerror("Chyba", "dajte pozor na vstupy!")
            return

        global generated_numbers
        generated_numbers = [random.randint(a, b) for _ in range(n)]

        # Заполняем Listbox за один раз
        original_list.delete(0, tk.END)
        original_list.insert(tk.END, *generated_numbers)

    except ValueError:
        messagebox.showerror("Chyba", "Zadajte celé čísla!")


def convert_to_negative():
    if not generated_numbers:
        messagebox.showerror("Chyba", "Najprv vygenerujte čísla.")
        return

    global updated_numbers
    updated_numbers = [-abs(x) for x in generated_numbers]

    updated_list.delete(0, tk.END)
    for num in updated_numbers:
        updated_list.insert(tk.END, num)

def show_graph():
    if not generated_numbers or not updated_numbers:
        messagebox.showerror("Chyba", "Musíte najprv vygenerovať aj upraviť čísla.")
        return

    plt.figure("Graf pôvodných a upravených hodnôt")

    plt.plot(generated_numbers, label="Pôvodné")
    plt.plot(updated_numbers, label="Upravené (negatívne)")
    plt.title("Porovnanie hodnôt")
    plt.xlabel("Index")
    plt.ylabel("Hodnota")
    plt.grid(True)
    plt.legend()
    plt.show()

root = tk.Tk()
root.title("Generátor čísel Hopaitsa")

root.geometry("1000x600")

generated_numbers = []
updated_numbers = []


frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=50)   

tk.Label(frame_inputs, text="N:").grid(row=0, column=0, padx=10)
entry_n = tk.Entry(frame_inputs)
entry_n.grid(row=0, column=1, padx=10)

tk.Label(frame_inputs, text="A:").grid(row=1, column=0, padx=10)
entry_a = tk.Entry(frame_inputs)
entry_a.grid(row=1, column=1, padx=10)

tk.Label(frame_inputs, text="B:").grid(row=2, column=0, padx=10)
entry_b = tk.Entry(frame_inputs)
entry_b.grid(row=2, column=1, padx=10)


frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=50)   

btn_generate = tk.Button(frame_buttons, text="Vygenerovať", width=20, command=generate_numbers)
btn_generate.grid(row=0, column=0, padx=20)

btn_convert = tk.Button(frame_buttons, text="Zmeniť na záporné", width=20, command=convert_to_negative)
btn_convert.grid(row=0, column=1, padx=20)

btn_graph = tk.Button(frame_buttons, text="Zobraziť graf", width=20, command=show_graph)
btn_graph.grid(row=0, column=2, padx=20)


frame_lists = tk.Frame(root)
frame_lists.pack(pady=50)  

tk.Label(frame_lists, text="Pôvodné hodnoty", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=50)
tk.Label(frame_lists, text="Upravené hodnoty", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=50)

original_list = tk.Listbox(frame_lists, width=30, height=20)
original_list.grid(row=1, column=0, padx=50)

updated_list = tk.Listbox(frame_lists, width=30, height=20)
updated_list.grid(row=1, column=1, padx=50)

root.mainloop()
