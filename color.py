import colorama
from colorama import Back as bg, Fore as fg

colorama.init()
print(bg.RED)
print(colorama.ansi.clear_screen())
print(fg.YELLOW)
print("hello world")
print(fg.BLACK)
print("fdkf")