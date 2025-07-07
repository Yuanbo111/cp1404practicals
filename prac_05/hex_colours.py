"""
Lookup hexadecimal colour codes by name.
"""

HEX_COLOURS = {"Beaver":"#9f170",
               "Beige":"#f55dc",
               "Bistre":"#3d2b1f",
               "BlueViolet":"#8a2be2",
               "Brass":"#b5a642",
               "Brick Red":"#cb4154",
               "Bronze":"#cd7f32",
               "Brown":"#a52a2a",
               "Buff":"#f0dc82",
               "Burgundy":"#8000200"
}

colour_name = input("Enter colour name (blank to quit): ").strip()
while colour_name != "":
    colour_key = colour_name.title()
    try:
        hex_code = HEX_COLOURS[colour_key]
        print(f"{colour_name} is {hex_code}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name (blank to quit): ").strip()