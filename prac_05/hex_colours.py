"""
CP1404/CP5632 Practical
Hex Colors
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
HEX_CODES = { "aliceblue": "#f0f8ff", "amber": "#ffbf00", "antiquewhite": "#faebd7", "darkgreen": "#006400",
             "emerald": "#50c878", "lavender": "#e6e6fa", "lightblue": "#add8e6", "navyblue": "#000080", "ocean green": "#48bf91"}

hex_name = input("Enter color name: ").lower().strip()
print(hex_name)
while hex_name != "":
    try:
        hex_code = HEX_CODES[hex_name]
        print(hex_name, "is", hex_code)
    except KeyError:
        print("Invalid color name")
    hex_name = input("Enter color name: ")


for code in HEX_CODES:
     print(code, "is", HEX_CODES[code])