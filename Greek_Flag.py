import tkinter as tk

window = tk.Tk()
window.title("Greek Flag")

stripeHeight = 50
height = 9 * stripeHeight
width = height * 3 // 2
window.geometry(f"{width}x{height}")

canvas = tk.Canvas(window, highlightthickness = 0, background = "white")

for i in range(5):
    canvas.create_rectangle(0, 2 * i * stripeHeight,
        width, (2 * i + 1) * stripeHeight, width = 0, fill = "blue")

canvas.create_rectangle(0, 0, 5 * stripeHeight, 5 * stripeHeight,
   width = 0, fill = "white")
canvas.create_rectangle(0, 0, 1/7 * width, 2 * stripeHeight,
    width = 0, fill = "blue")
canvas.create_rectangle(140, 3 * stripeHeight, 5 * stripeHeight, 5 * stripeHeight,
    width = 0, fill = "blue")
canvas.create_rectangle(0, 3 * stripeHeight, 1/7 * width, 5 * stripeHeight,
    width = 0, fill = "blue")
canvas.create_rectangle(140, 0, 5 * stripeHeight, 2 * stripeHeight,
    width = 0, fill = "blue")

canvas.pack(expand = tk.YES, fill = "both")
window.mainloop()
