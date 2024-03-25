from PIL import Image

obrazek = Image.open("tiger.PNG")
sirka, vyska = obrazek.size


def filtr1():
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
                obrazek.putpixel((x, y), (107, 142, 35))  # Bílá barva pro světlé pixely
            else:
                obrazek.putpixel((x, y), (85, 107, 47))  # Černá barva pro tmavé pixely
            y += 1
        x += 1
    obrazek.show()


def filtr2():
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
                obrazek.putpixel((x, y), (255, 215, 235))  # Bílá barva pro světlé pixely
            else:
                obrazek.putpixel((x, y), (87, 51, 51))  # Černá barva pro tmavé pixely
            y += 1
        x += 1
    obrazek.show()


def filtr3():
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
                obrazek.putpixel((x, y), (255, 230, 179))  # Bílá barva pro světlé pixely
            else:
                obrazek.putpixel((x, y), (70, 130, 180))  # Černá barva pro tmavé pixely
            y += 1
        x += 1
    obrazek.show()


print("Vítejte v mém filtrovém studiu.\nNabízíme 3 druhy různých filtrů.")
moznost = input("Na jaký se chcete podívat (1,2,3): ")

while True:
    if moznost == "1":
        print("Zde vidíte možnost tanku s kamufláží.")
        filtr1()
        break

    elif moznost == "2":
        print("Zde vidíte mírumilovný tank.")
        filtr2()
        break
    
    elif moznost == "3":
        print("Zde vidíte plážový tank.")
        filtr3()
        break

    else:
        print("Tuto možnost tu nemáne.")
        moznost = input("Na jaký se chcete podívat (1,2,3): ")