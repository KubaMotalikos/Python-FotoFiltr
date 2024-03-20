from PIL import Image

obrazek = Image.open("tiger.PNG")
sirka, vyska = obrazek.size

x = 0
while x < sirka:
    y = 0
    while y < vyska:
        pixel = obrazek.getpixel((x, y))
        if len(pixel) == 4:  # Pokud je v pixlu alfa kanál
            r, g, b, a = pixel
        else:
            r, g, b = pixel
        prumer = int((r + g + b) / 3)
        if prumer > 150:
            obrazek.putpixel((x, y), (222, 68, 13))  # Bílá barva pro světlé pixely
        else:
            obrazek.putpixel((x, y), (25, 10, 64))  # Černá barva pro tmavé pixely
        y += 1
    x += 1

obrazek.show()




