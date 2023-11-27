import importlib
import subprocess
import sys 

def updatePip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    except subprocess.CalledProcessError as e:
        print(f"Error updating Pip: {e}")
        sys.exit(1)

# Checking if the system has the required modules 
def checkInstall(moduleName):
    try:
        importlib.import_module(moduleName)
    except ImportError:
        print(f"{moduleName} is not installed. Installing...")
        subprocess.run(["pip", "install", moduleName])
        print(f"{moduleName} has been installed successfully!")

requiredMod = ["packaging", "numpy", "customtkinter"]
for module in requiredMod:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "q", "--disable-pip-version-check"])
        print("Pip is up-to-date.")
    except subprocess.CalledProcessError:
        print("An Update is available for pip. Updating...")
        updatePip()
    checkInstall(module)

# Importing modules for various cipher methods and GUI
import Module
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

# Creating GUI Window 
window = customtkinter.CTk()
window.title("EnKruptos")
window.geometry("324x390")
window.resizable(False, False)

# Differentiating among the user's choice of cipher method
def select_caesar():
    global selected_method
    print("Selected Caesar Cipher.")
    keyEntry.delete(0, customtkinter.END)
    keyEntry.insert(0, "Key must be the number of character shift")
    selected_method = "Caesar"

def select_Mono():
    global selected_method
    print("Selected MonoAlphabetic Cipher.")
    keyEntry.delete(0, customtkinter.END)
    keyEntry.insert(0, "Key must contain 26 unique characters ")
    selected_method = "MonoAlphabetic"

def select_Atbash():
    global selected_method
    print("Selected Atbash Cipher.")
    keyEntry.delete(0, customtkinter.END)
    keyEntry.insert(0, "No need to enter the Key.")
    selected_method = "Atbash"

def select_playfair():
    global selected_method
    print("Selected PlayFair Cipher.")
    keyEntry.delete(0, customtkinter.END)
    keyEntry.insert(0, "Key must be a word.")
    selected_method = "PlayFair"

def select_vigenere():
    global selected_method
    print("Selected Vigenere Cipher.")
    keyEntry.delete(0, customtkinter.END)
    keyEntry.insert(0, "Key must be a word.")
    selected_method = "Vigenere"

def select_railfence():
    global selected_method
    print("Selected RailFence Cipher.")
    keyEntry.delete(0, customtkinter.END)
    keyEntry.insert(0, "Key must be the number of diagonal shift")
    selected_method = "RailFence"

def select_columnar():
    global selected_method
    print("Selected Columnar Cipher.")
    keyEntry.delete(0, customtkinter.END)
    keyEntry.insert(0, "Key must be the order of the arrangements")
    selected_method = "Columnar"

# Using the user's selection to call upon appropriate encryption functions 
def callEncryptMethod():
    if selected_method == "Caesar":
        plainText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.CaesarCipher(key)
        encryptedText = test.Encrypt(plainText)
        print(f"Key:{key}")
        print(f"Caesar Encryption: {encryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    if selected_method == "MonoAlphabetic":
        plainText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.MonoAlphabetic(key)
        encryptedText = test.Encrypt(plainText)
        print(f"Key:{key}")
        print(f"MonoAlphabetic Encryption: {encryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "Atbash":
        plainText = inputText.get("1.0", "end-1c")
        test = Module.Atbash()
        encryptedText = test.Encrypt(plainText)
        print(f"Atbash Encryption: {encryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "PlayFair":
        test = Module.Playfair()
        plainText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        encryptedText = test.Encrypt(plainText, key)
        print(f"Key:{key}")
        print(f"PlayFair Encryption: {encryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "Vigenere":        
        key = keyEntry.get()
        test = Module.Vignere(key)
        plainText = inputText.get("1.0", "end-1c")
        encryptedText = test.Encrypt(plainText)
        print(f"Key:{key}")
        print(f"Vigenere Encryption: {encryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "RailFence":
        test = Module.RailFence()
        plainText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        encryptedText = test.Encrypt(plainText, int(key))
        print(f"Key:{key}")
        print(f"RailFence Encryption: {encryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "Columnar":
        key = keyEntry.get()
        keyArray = [int(char) for char in key]
        print(keyArray)
        plainText = inputText.get("1.0", "end-1c")
        test = Module.Columnar(keyArray)
        encryptedText = test.Encrypt(plainText)
        print(f"Key:{keyArray}")
        print(f"Columnar Encryption: {encryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

# Using user's selection to call upon appropriate decryption function
def callDecryptMethod():
    if selected_method == "Caesar":
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.CaesarCipher(key)
        decryptedText = test.Decrypt(cipherText)
        print(f"Key:{key}")
        print(f"Caesar Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "MonoAlphabetic":
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.MonoAlphabetic(key)
        decryptedText = test.Decrypt(cipherText)
        print(f"Key:{key}")
        print(f"MonoAlphabetic Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "Atbash":
        cipherText = inputText.get("1.0", "end-1c")
        test = Module.Atbash()
        decryptedText = test.Decrypt(cipherText)
        print(f"Atbash Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "PlayFair":
        test = Module.Playfair()
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        decryptedText = test.Decrypt(cipherText, key)
        print(f"Key:{key}")
        print(f"PlayFair Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)
        
    elif selected_method == "Vigenere":
        key = keyEntry.get()
        test = Module.Vignere(key)
        cipherText = inputText.get("1.0", "end-1c")
        decryptedText = test.Decrypt(cipherText)
        print(f"Key:{key}")
        print(f"Vigenere Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "RailFence":
        test = Module.RailFence()
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        decryptedText = test.Decrypt(cipherText, int(key))
        print(f"Key:{key}")
        print(f"RailFence Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "Columnar":
        key = keyEntry.get()
        keyArray = [int(char) for char in key]
        cipherText = inputText.get("1.0", "end-1c")
        test = Module.Columnar(keyArray)
        decryptedText = test.Decrypt(cipherText)
        print(f"Key:{keyArray}")
        print(f"Columnar Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

# Label for Textbox 
cipherLabel = customtkinter.CTkLabel(window, text="Cipher Method")
cipherLabel.place(x=120, y=2)

# User Cipher Method Selection 
# Caesar Cipher Button 
caesar = customtkinter.CTkButton(window, text="Caesar", width=120, hover_color="red", corner_radius=25, text_color="black", command=select_caesar)
caesar.place(x=25,y=25)

# MonoAlphabetic Cipher Button
monoAlpha = customtkinter.CTkButton(window, text="MonoAlphabetic", width=120, hover_color="red", corner_radius=25, text_color="black", command=select_Mono)
monoAlpha.place(x=180, y=25)

# AtBash Cipher Button
atBash = customtkinter.CTkButton(window, text="Atbash", width=120, hover_color="red", corner_radius=25, text_color="black", command=select_Atbash)
atBash.place(x=100, y=135)

# PlayFair Cipher Button
playFair = customtkinter.CTkButton(window, text="PlayFair",  width=120, hover_color="red", corner_radius=25, text_color="black", command=select_playfair)
playFair.place(x=25,y=60)

# Vigenere Cipher Button
vigenere = customtkinter.CTkButton(window, text="Vigenere", width=120, hover_color="red", corner_radius=25, text_color="black", command=select_vigenere)
vigenere.place(x=180,y=60)

# RailFence Cipher Button
railFence = customtkinter.CTkButton(window, text="RailFence", width=120, hover_color="red",corner_radius=25, text_color="black", command=select_railfence)
railFence.place(x=25,y=95)

# Columnar Cipher Button
columnar = customtkinter.CTkButton(window, text="Columnar", width=120, hover_color="red", corner_radius=25, text_color="black", command=select_columnar)
columnar.place(x=180, y=95)

# Input label and TextBox to take Plain Text from the User 
inputLabel = customtkinter.CTkLabel(window, text="Plain Text: ")
inputLabel.place(x=130, y=170)
inputText = customtkinter.CTkTextbox(window, height=12, width=320)
inputText.place(x=0, y=190)

# Key label and Entry to take the Input from the user 
keyLabel = customtkinter.CTkLabel(window, text="Key:")
keyLabel.place(x=140, y=230)
keyEntry = customtkinter.CTkEntry(window, height=12, width=320, placeholder_text="Key goes here")
keyEntry.place(x=0, y=250)

# Creating Encryption Button 
encryptButton = customtkinter.CTkButton(window, text="Encrypt", width=140, hover_color="red", corner_radius=25, text_color="black", command=callEncryptMethod)
encryptButton.place(x=10, y=295)
# Creating Decryption Button 
decryptButton = customtkinter.CTkButton(window, text="Decrypt", width=140, hover_color="red", corner_radius=25, text_color="black", command=callDecryptMethod)
decryptButton.place(x=160, y=295)

# Output Label and the TextBox to display the Cipher Text 
outputLabel = customtkinter.CTkLabel(window, text="Cipher Text:")
outputLabel.place(x=130, y=335)
outputText = customtkinter.CTkTextbox(window, height=12, width=320)
outputText.place(x=0,y=355)

window.mainloop()
