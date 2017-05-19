#!/usr/bin/env python3
import tkinter

# mandelbrot set settings
HEIGHT = 500
WIDTH = 500
ITERS = 20
MIN_REAL = -2.3
MAX_REAL = 1.0
MIN_IMAGINARY = -1.5
MAX_IMAGINARY = MIN_IMAGINARY + (MAX_REAL - MIN_REAL) * HEIGHT / WIDTH
FACTOR_REAL = (MAX_REAL - MIN_REAL) / (WIDTH - 1)
FACTOR_IMAGINARY = (MAX_IMAGINARY - MIN_IMAGINARY) / (HEIGHT - 1)

# initialize window
root = tkinter.Tk()
root.title("Mandelbrot set")
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
img = tkinter.PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((0, 0), image=img, state="normal", anchor=tkinter.NW)

for y in range(HEIGHT):
    imaginary = MAX_IMAGINARY - y * FACTOR_IMAGINARY
    for x in range(WIDTH):
        real = MIN_REAL + x * FACTOR_REAL
        real2 = real
        imaginary2 = imaginary

        inside = True

        for z in range(0, ITERS):
            real3 = real2 * real2
            imaginary3 = imaginary2 * imaginary2

            if real3 + imaginary3 > 4:
                inside = False
                red = str(hex((z * (14 if (z < int((ITERS * (7/10)))) else 14)) % 256)[2:4].zfill(2))
                green = str(hex((z * (14 if (z < int((ITERS * (7/10)))) else 1)) % 256)[2:4].zfill(2))
                blue = str(hex((z * (1 if (z < int((ITERS * (7/10)))) else 1)) % 256)[2:4].zfill(2))
                img.put("#" + red + green + blue, (x, y))
                break

            imaginary2 = 2 * real2 * imaginary2 + imaginary
            real2 = real3 - imaginary3 + real

        if inside:
            img.put("#000000", (x, y))

canvas.pack()

root.mainloop()
