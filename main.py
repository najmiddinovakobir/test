from color import BLACK
from color import RED
from color import GREEN
from color import BROWN
from color import BLUE
from color import PURPLE
from color import CYAN
from color import LIGHT_GRAY
from color import DARK_GRAY
from color import LIGHT_RED

user = input("Enter text...")
print("Color Options:")
print("1.BLACK")
print("2.RED")
print("3.GREEN")
print("4.BROWN")
print("5.BLUE")
print("6.PURPLE")
print("7.CYAN")
print("8.LIGHT_GRAY")
print("9.DARK_GRAY")
print("10.LIGHT_RED")

number_color = int(input("Choose color (Enter the corresponding number:)"))
if number_color == 1:
    print(f"{BLACK} {user}")
elif number_color == 2:
    print(f"{RED} {user}")
elif number_color == 3:
    print(f"{GREEN} {user}")
elif number_color == 4:
    print(f"{BROWN} {user}")
elif number_color == 5:
    print(f"{BLUE} {user}")
elif number_color == 6:
    print(f"{PURPLE} {user}")
elif number_color == 7:
    print(f"{CYAN} {user}")
elif number_color == 8:
    print(f"{LIGHT_GRAY} {user}")
elif number_color == 9:
    print(f"{DARK_GRAY} {user}")
elif number_color == 10:
    print(f"{LIGHT_RED} {user}")
else:
    print(f"{user}")
