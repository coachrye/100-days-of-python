from morse3 import Morse as m



def process_string(string_to_convert):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {string_to_convert}')  # Press ⌘F8 to toggle the breakpoint.

    # for letter in string_to_convert:
    # short mark, dot or dit (  ▄ ): 1
    # longer mark, dash or dah (  ▄▄▄ ): 111
    # intra-character gap (between the dits and dahs within a character): 0
    # short gap (between letters): 000
    # medium gap (between words): 0000000

    print(m(string_to_convert).stringToMorse())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_string(input("What do you want to say? "))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




# Get String Input
# Iterate String Input
# Output Morse