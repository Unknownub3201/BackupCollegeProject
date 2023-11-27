import importlib
import subprocess
import sys 

# Updating Pip if there's an update available
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
        print(f"checking for {moduleName}")
        print(f"Requirements for {moduleName} already satisfied.")
    except ImportError:
        print(f"{moduleName} is not installed. Installating {moduleName}")
        subprocess.run(["pip", "install", moduleName])
        print(f"{moduleName} has been installed successfully.")

# Checking for Pip update and calling updatePip
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "q", "--disable-pip-version-check"])
    print("Pip is up-to-date.")
except subprocess.CalledProcessError:
    print("An update is available for pip, Updating")
    updatePip()

# Checking all required Modules and installing each
requiredMod = ["packaging", "numpy", "customtkinter"]
for module in requiredMod:
    checkInstall(module)

# Importing modules for various cipher methods and GUI
import Module
import tkinter

# Creating GUI Window 
window = tkinter.Tk()
window.title("EnKruptos")
window.geometry("324x415")
window.resizable(False, False)

# Differentiating among the user's choice of cipher method
def select_caesar():
    global selected_method
    print("Selected Caesar Cipher")
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be the number of character shift.")
    selected_method = "Caesar"

def select_Mono():
    global selected_method
    print("Selected MonoAlphabetic Cipher")
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must contain 26 unique characters.")
    selected_method = "MonoAlphabetic"

def select_Atbash():
    global selected_method
    print("Selected Atbash Cipher")
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "No Need to Enter the Key")
    selected_method = "Atbash"

def select_playfair():
    global selected_method
    print("Selected PlayFair Cipher")
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be a word.")
    selected_method = "PlayFair"

def select_vigenere():
    global selected_method
    print("Selected Vigenere Cipher")
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be a word.")
    selected_method = "Vigenere"

def select_railfence():
    global selected_method
    print("Selected RailFence Cipher")
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be the number of diagonal shift")
    selected_method = "RailFence"

def select_columnar():
    global selected_method
    print("Selected Columnar Cipher")
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be the order of the arrangements")
    selected_method = "Columnar"

# Using the user's selection to call upon appropriate encryption functions 
def callEncryptMethod():
    if selected_method == "Caesar":
        InitialText = "Key must be shift Number"
        outputText.insert("1.0", InitialText)
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
        print(f"key:{key}")
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
        plainText = inputText.get("1.0", "end-1c")
        test = Module.Columnar(keyArray)
        encryptedText = test.Encrypt(plainText)
        print(f"Key:{key}")
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
        cipherText = inputText.get("1.0","end-1c")
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
        print(keyArray)
        cipherText = inputText.get("1.0", "end-1c")
        test = Module.Columnar(keyArray)
        decryptedText = test.Decrypt(cipherText)
        print(f"Key:{key}")
        print(f"Columnar Decryption: {decryptedText}")
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

# Label for Textbox 
cipherLabel = tkinter.Label(window, text="Cipher Method")
cipherLabel.place(x=120, y=2)

#User Cipher Method selection 
# Caesar Cipher Button 
caesar = tkinter.Button(window, text="Caesar",command=select_caesar, width=12)
caesar.place(x=15, y=25)

# MonoAlphabetic Cipher Button
mono = tkinter.Button(window, text="MonoAlphabetic", command=select_Mono, width=12)
mono.place(x=170, y=25)

# PlayFair Cipher Button
playfair = tkinter.Button(window, text="PlayFair", command=select_playfair, width=12)
playfair.place(x=15, y=60)

# AtBash Cipher Button 
atbash = tkinter.Button(window, text="Atbash", command=select_Atbash, width=12)
atbash.place(x=100, y=135)

# Vigenere Cipher Button
vigenere = tkinter.Button(window, text="Vigenere", command=select_vigenere, width=12)
vigenere.place(x=170, y=60)

# RailFence Cipher Button
railfence = tkinter.Button(window, text="RailFence", command=select_railfence, width=12)
railfence.place(x=15, y=95)

# Columnar Cipher Button
columnar = tkinter.Button(window, text="Columnar", command=select_columnar, width=12)
columnar.place(x=170, y=95)

# Input Label and TextBox to take Plain Text from the user 
inputLabel = tkinter.Label(window, text="Plain Text: ")
inputLabel.place(x=120, y=170)
inputText = tkinter.Text(window,height=2.5, width=40)
inputText.place(x=0, y=190)

# Key Label and Entry to take the Cipher Key from the user 
keyLabel = tkinter.Label(window, text="Key: ")
keyLabel.place(x=130, y=250)
keyEntry = tkinter.Entry(window, width=40)
keyEntry.place(x=0, y=270)

# Creating Encryption Button 
encryptButton = tkinter.Button(window, text="Encrypt", command=callEncryptMethod, width=12)
encryptButton.place(x=20, y=295)
# Creating Decryption Button 
decryptButton = tkinter.Button(window, text="Decrypt", command=callDecryptMethod, width=12)
decryptButton.place(x=165, y=295)

# Output Label and TextBox to display the Cipher Text 
outputLabel = tkinter.Label(window, text="Cipher Text: ")
outputLabel.place(x=120, y=335) 
outputText = tkinter.Text(window, height=2.5, width=40)
outputText.place(x=0, y=355)

window.mainloop()
