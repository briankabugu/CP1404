"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        state_name = CODE_TO_NAME[state_code]
        print(state_code, "is", state_name)
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")


for code in CODE_TO_NAME:
     print(code, "is", CODE_TO_NAME[code])