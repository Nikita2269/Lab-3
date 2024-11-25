import tkinter as tk
import random
import pygame

def generate_key():
    hex_input = input_entry.get().strip().upper()
    if len(hex_input) != 5 or not all(c in '0123456789ABCDEF' for c in hex_input):
        key_entry.delete(0, tk.END)
        key_entry.insert(0, "Неверный HEX (5 знаков)")
        return
    dec_number = int(hex_input, 16)
    dec_str = str(dec_number).zfill(5)
    first_three = dec_str[:3]
    last_two = dec_str[-2:]
    key = f"{first_three[0]}{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))}-" \
          f"{first_three[1]}{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))}-" \
          f"{first_three[2]}{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))} " \
          f"{last_two}"
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

def close_app():
    window.destroy()

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("8bit_music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

play_music()

window = tk.Tk()
window.title("Keygen")
window.geometry("576x360")

bg_img = tk.PhotoImage(file="game_screen.png")

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="lightblue", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

input_label = tk.Label(frame, text="Введите HEX (5 знаков):", font=("Verdana", 12), bg="lightblue")
input_label.grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(frame, width=20, font=("Verdana", 12))
input_entry.grid(row=0, column=1, padx=10, pady=5)

key_label = tk.Label(frame, text="Сгенерированный ключ:", font=("Verdana", 12), bg="lightblue")
key_label.grid(row=1, column=0, padx=10, pady=5)
key_entry = tk.Entry(frame, width=25, font=("Verdana", 12))
key_entry.grid(row=1, column=1, padx=10, pady=5)

generate_button = tk.Button(frame, text="Сгенерировать ключ", font=("Verdana", 10), command=generate_key)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

exit_button = tk.Button(window, text="Выйти", font=("Verdana", 10), command=close_app)
exit_button.place(relx=0.85, rely=0.9, anchor="center")

window.mainloop()
