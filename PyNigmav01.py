"""
______      _   _ _                                _____  __
| ___ \    | \ | (_)                              |  _  |/  | 
| |_/ /   _|  \| |_  __ _ _ __ ___   __ _   __   _| |/' |`| | 
|  __/ | | | . ` | |/ _` | '_ ` _ \ / _` |  \ \ / /  /| | | | 
| |  | |_| | |\  | | (_| | | | | | | (_| |   \ V /\ |_/ /_| |_
\_|   \__, \_| \_/_|\__, |_| |_| |_|\__,_|    \_/  \___(_)___/
       __/ |         __/ | 
      |___/         |___/        Welcome to Python Enigma v0.1
"""
"""Enigma Class defines how the whole machine comes together and its paramaters"""
class Enigma:
    def __init__(self, 
                 ref, 
                 rotor1, 
                 rotor2, 
                 rotor3, 
                 plug_board="", 
                ): 
        self.reflector = ref
        self.rotor1 = rotor1 
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plug_board = plug_board
        
    def step_rotors(self):
        step_rotor2 = self.rotor1.psn in self.rotor1.notches # Checks is the notch(s) on rotor 1 are in postion rotate rotor 2
        step_rotor3 = self.rotor2.psn in self.rotor2.notches and step_rotor2  # Checks is the notch(s) on rotor 2 are in postion rotate rotor 3
        if step_rotor2: # Step the rotor 2 (middle) rotor if needed
            self.rotor2.psn = chr(((ord(self.rotor2.psn)-64)%26)+65) # +-65 is the same as ord(char) +- ord("A") # -64 =  +1 -65
        if step_rotor3: # Step the rotor3 (leftmost) rotor if needed
            self.rotor3.psn = chr(((ord(self.rotor3.psn)-64)%26)+65)
        self.rotor1.psn = chr(((ord(self.rotor1.psn)-64)%26)+65) #Steps rotor 1 (rightmost) every keypress
        #print(f'rotor3: {self.rotor3.psn}, rotor2: {self.rotor2.psn}, rotor1: {self.rotor1.psn}')      
              
    def encipher(self, in_text):
        out_text = "" 
        char_count = 0
        out_text = ""
        clean_text = clean_input(in_text)
        for i in clean_text:
            test_enigma.step_rotors() # calls step rotor functing on each key press
            t = self.rotor1.forward(i)
            t = self.rotor2.forward(t)
            t = self.rotor3.forward(t)
            t = self.reflector.reflect(t)
            t = self.rotor3.backward(t)
            t = self.rotor2.backward(t)
            t = self.rotor1.backward(t)
            out_text += t # append output charecter to temportary string
            char_count += 1
            if char_count % 5 == 0: # breaks thge output up into groups of 5 charecters
                out_text += " "
                char_count = 0
        return out_text #return output string 

"""Reflector Class defines the setup abd behavior of the reflector"""    
class Reflector:
    def __init__(self, wiring, name):
        self.wiring = wiring
        self.name = name
        self.position = 0
        self.state = 'A'

    def reflect(self, char):
        index = ord(char) - ord("A")  # true index
        letter = self.wiring[index]  # rotor letter generated
        output_char = chr(ord("A") + (ord(letter) - ord("A") + 26) % 26 # actual output
        )
        return output_char

"""Rotor Class defines the setup abd behavior of the rotors"""   
class Rotor:
    def __init__(self, wiring, notches, name, psn="A", ring="A"):
        self.wiring = wiring
        self.notches = notches
        self.name = name
        self.psn = psn
        self.ring = ring
      
    def forward(self, char):
        # Encrypts a character by passing it through the rotor from right to left.
        input_pos = ord(char) - ord('A')  # Change character to Unicode, subtract 65
        rotor_pos = (ord(self.psn) - ord('A')) + (ord(self.ring) - ord('A')) # Apply a position & ring setting on input side
        mapped_pos = (input_pos + rotor_pos) % 26  # Apply a position & ring setting on for output side
        output_char = self.wiring[mapped_pos]  # Get the output character from the wiring
        output_pos = (ord(output_char) - ord('A') - rotor_pos) % 26 # Adjust the output character's position based on the rotor's position
        output_char = chr(output_pos + ord('A')) # turns mapping back to a character
        return output_char

    def backward(self, char):
        # Encrypts a character by passing it through the rotor from left to right.
        rotor_pos = (ord(self.psn) - ord('A')) + (ord(self.ring) - ord('A')) # Apply a position & ring setting rot the reaverse input side
        adjusted_char = chr((ord(char) - ord('A') + rotor_pos) % 26 + ord('A'))  # Adjust the input character's position based on the rotor's position
        input_pos = self.wiring.index(adjusted_char) # finds the charecter position in the wiring index
        output_pos = (input_pos - rotor_pos) % 26  # Subtract the rotor & ring position to modify the character mapping for output
        output_char = chr(output_pos + ord('A'))        
        return output_char

"""
Defintions for the rotors and reflectors
"""

Rotor_I = Rotor(
    wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    notches="Q",
    name="Rotor I",
)
Rotor_II = Rotor(
    wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE",
    notches="E",
    name="Rotor II",
)
Rotor_III = Rotor(
    wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO",
    notches="V",
    name="Rotor III",
)
Rotor_IV = Rotor(
    wiring="ESOVPZJAYQUIRHXLNFTGKDCMWB",
    notches="J",
    name="Rotor IV",
)
Rotor_V = Rotor(
    wiring="VZBRGITYUPSDNHLXAWMJQOFECK",
    notches="Z",
    name="Rotor V",
)
Rotor_VI = Rotor(
    wiring="JPGVOUMFYQBENHZRDKASXLICTW",
    notches="ZM",
    name="Rotor VI",
)
Rotor_VII = Rotor(
    wiring="NZJHGRCXMYSWBOUFAIVLPEKQDT",
    notches="ZM",
    name="Rotor VII",
)
Rotor_VIII = Rotor(
    wiring="FKQHTLXOCBJSPDZRAMEWNIUYGV",
    notches="ZM",
    name="Rotor VIII",
)
Reflector_A = Reflector(wiring="EJMZALYXVBWFCRQUONTSPIKHGD", name="Reflector A")
Reflector_B = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT", name="Reflector B")
Reflector_C = Reflector(wiring="FVPJIAOYEDRZXWGCTKUQSBNMHL", name="Reflector C")

"""
Menus
"""
def menu_main():
    global user_quit
    while True:
        print("\nMAIN MENU:")
        print("Please select an option\n1. Show current settings\n2. Change settings\n3. Encrypt/Decrypt\n4. Quit")
        main_in = input(">>> ")
        try: 
            main_in = int(main_in)
        except:
            print(f"\tAn error occurred:\n\tPlease use a number 1-4 to make your selection.")
            break
        if main_in == 1:
            print("\nThe currnet machine settings are:\n")
            show_settings()
        elif main_in == 2:
            print("\nThe currnet machine settings are:\n")
            show_settings()
            change_settings()
        elif main_in == 3:
            print ("\nPlease enter the message to encrypt or decrypt?")
            raw_in_text = input(">>>")
            try:
                out_text = test_enigma.encipher(raw_in_text)
            except Exception as e:
                print(f"An error occurred: {e}")
            print(f"\nYour message: {out_text}")
            break
        elif main_in == 4:
            try:
                print("\n\n...Exiting pyNigma...\n Thanks for checking out the program!\n")
                user_quit = True
                break
            except Exception: 
                pass
        else:
            print("\nPlease select a number from 1-4.")

def menu_ops():
    while True: 
        print ("\nPlease enter the message to encrypt or decrypt?")
        raw_in_text = input(">>> ")
        try:
            out_text = test_enigma.encipher(raw_in_text)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break
        print(f'Your message: {out_text}')
        break

def show_settings():    
    print(f"\t\t Left Roter | Middle Roter | Right Roter")
    print(f"\t\t    {test_enigma.rotor3.name} | {test_enigma.rotor2.name} | {test_enigma.rotor1.name}")
    print(f"Position Setting: \t{test_enigma.rotor3.psn}\t{test_enigma.rotor2.psn}\t{test_enigma.rotor1.psn}") 
    print(f"Ring Setting: \t\t{test_enigma.rotor3.ring}\t{test_enigma.rotor2.ring}\t{test_enigma.rotor1.ring}")
    print("Plugboard Settings: This Feature is not yet implimented")

def change_settings():
    
    #change_settings = input("Please make a selection >>>")
    #print("\nSorry, this feature is not yet implimented")
    while True:
        print("\nSETTINGS:\nWhat settigns would you like to change?\n1. Rotors & Settings\n2. Plugboard\n3. Show Current Settings\n4. Return to Main Menu")
        cng_set = input(">>> ")
        num_out = validate_int_in(cng_set)
        if num_out == 1:
            print(f"\nYou selected {num_out}") 
            change_rotor_settings()
        #elif num_out == 2:
        #    print(f"\nYou selected {num_out}") 
        #    change_rotor_settings()
        #elif num_out == 3:
        #    print(f"\nYou selected {num_out}")
        #    change_ring_settings()
        elif num_out == 2:
            print(f"\nYou selected {num_out}") 
            change_plubboard_settigns()
        elif num_out == 3:
            show_settings()
        elif num_out == 4:
            break
        else:
            print("Sorry, I didnt understand that. Please select a number 1-6 for your selection.")
            pass

def change_rotor_settings():
    print(f"\nThe current Right Rotor is: {test_enigma.rotor1.name}")
    print("\nPlease select a replacement:")
    r1_replace = select_rotor()
    print(f"\nThe current Middle Rotor is: {test_enigma.rotor2.name}")
    print("\nPlease select a replacement:")
    r2_replace = select_rotor()
    print(f"\nThe current Left Rotor is: {test_enigma.rotor3.name}")
    print("\nPlease select a replacement:")
    r3_replace = select_rotor()
    test_enigma.rotor3 = r3_replace
    test_enigma.rotor2 = r2_replace
    test_enigma.rotor1 = r1_replace
    print(f"\nYou Selected:\n1. Left Rotor: {test_enigma.rotor3.name}\n2. Middle Rotor: {test_enigma.rotor2.name}\n3. Right Rotor: {test_enigma.rotor1.name}")
    rotor_set = input("\nUPDATE POSITION SETTINGS:\nPlease specifiy the position settings with three alpha charecter, i.e. AAA, or press enter to keep defaults:\n>>> ")
    rotor_set = clean_input(rotor_set)
    print(f"Rotor_set is: {rotor_set}")
    if len(rotor_set) > 2:
        test_enigma.rotor3.psn = rotor_set[0]
        test_enigma.rotor2.psn = rotor_set[1]
        test_enigma.rotor1.psn = rotor_set[2]
        print(f"\nPosition Setting:\n1. Left Rotor: {test_enigma.rotor3.psn}\n2. Middle Rotor: {test_enigma.rotor2.psn}\n3. Right Rotor: {test_enigma.rotor1.psn}")
    else:
        pass
    ring_set = input("\nUPDATE RING SETTINGS:\nPlease specifiy the ring settings with three alpha charecter, i.e. AAA, or press enter to keep defaults:\n>>> ")
    ring_set = clean_input(ring_set)
    print(f"Ring_set is: {ring_set}")
    if len(ring_set) > 2:
        test_enigma.rotor3.ring = ring_set[0]
        test_enigma.rotor2.ring = ring_set[1]
        test_enigma.rotor1.ring = ring_set[2]
        print(f"\nRing Setting:\n1. Left Rotor: {test_enigma.rotor3.ring}\n2. Middle Rotor: {test_enigma.rotor2.ring}\n3. Right Rotor: {test_enigma.rotor1.ring}")
    else:
        pass
    show_settings()


def select_rotor():
    print("Avalible Rotors for Enigma M3:")
    print("1. Rotor I\n2. Rotor II\n3. Rotor III\n4. Rotor IV\n5. Rotor V")
    selr_in = input(">>> ")
    selr_out = validate_int_in(selr_in)
    if selr_out == 1:
        return Rotor_I
    elif selr_out == 2:
        return Rotor_II
    elif selr_out == 3:
        return Rotor_III
    elif selr_out == 4:
        return Rotor_IV
    elif selr_out == 5:
        return Rotor_V
    else:
        print("\nPlease select only numbers 1-5")
        select_rotor()

def change_position_setting():
    print("Select a rotor to place in its position:")

"""
def change_rotor_order():
    print("\nSelect a rotor to modify:")
    print(f"1. Left Roter: {test_enigma.rotor3.name}\n2. Middle Roter: {test_enigma.rotor2.name}\n3. Right Roter: {test_enigma.rotor1.name}\n4. Cancel")
    cro_in = input(">>> ")
    num_out2 = validate_int_in(cro_in)
    if num_out2 == 1: 
        new_rotor = "rotor3"
    elif num_out2 == 2: 
        new_rotor = "rotor2"
    elif num_out2 == 3: 
        new_rotor = "rotor1"
    elif num_out2 == 4:
        pass 
    else:
        print("\nPlease select only numbers 1-3")
        change_rotor_order()
    print("Select a rotor to place in its position:")
    selr_out = select_rotor()
    try:
        setattr(test_enigma, new_rotor, selr_out) # Throws an error if you select the same rotor that is already in that place. #add try.
    except Exception: 
        print("Unexpected Error!!!")
        pass 

def change_ring_setting():
    print("Select a rotor to place in its position:")
"""

def change_plubboard_settigns():
    print("Plugboard Settings: This Feature is not yet implimented")

def validate_int_in(user_in):
    try: 
        num_out = int(user_in)
        return (num_out)
    except:
        print(f"\tAn error occurred:\n\tPlease use a number 1-4 to make your selection.")

def clean_input(raw_in_text):
        # Sanatizes input for later functions. 
        clean_text = "" 
        in_text_upper = raw_in_text.upper() # makes all lowercase leters uppercase
        for c in in_text_upper:
            if c.isalpha(): # remove non alpha charecters from input text
                clean_text += c
        return clean_text
"""
Main Program Loop
"""
#Print Start up logo/info
print("\n\n______      _   _ _                                _____  __")
print("| ___ \    | \ | (_)                              |  _  |/  | ")
print("| |_/ /   _|  \| |_  __ _ _ __ ___   __ _   __   _| |/' |`| | ")
print("|  __/ | | | . ` | |/ _` | '_ ` _ \ / _` |  \ \ / /  /| | | | ")
print("| |  | |_| | |\  | | (_| | | | | | | (_| |   \ V /\ |_/ /_| |_")
print("\_|   \__, \_| \_/_|\__, |_| |_| |_|\__,_|    \_/  \___(_)___/")
print("       __/ |         __/ | ")
print("      |___/         |___/        Welcome to Python Enigma v0.1\n\n")

#default_psn="AAA", 
default_plug_board="", 
#default_ring="AAA"
test_enigma = Enigma(
    ref=Reflector_B, 
    rotor1=Rotor_I, 
    rotor2=Rotor_II, 
    rotor3=Rotor_III, 
    plug_board="", 
)
#test_enigma.rotor1.psn = default_psn[0]
#test_enigma.rotor2.psn = default_psn[1]
#test_enigma.rotor3.psn = default_psn[2]
#test_enigma.rotor1.ring = default_ring[0]
#test_enigma.rotor2.ring = default_ring[1]
#test_enigma.rotor3.ring = default_ring[2]

user_quit = False
while user_quit == False:
    menu_main() 