import Module
import tkinter 
window = tkinter.Tk()
window.title("Encrypto")
window.geometry("324x415")

# def createMatrix(text, key):
    # matrixSize = int(key)
    # numbers = [int(num) for num in text.split()]
    # numbers = [ord(char) - ord('A') for char in text]
    # paddingSize = (matrixSize - len(numbers) % matrixSize) % matrixSize
    # numbers += [0] * paddingSize
    # matrix = [numbers[i:i+matrixSize] for i in range(0, len(numbers), matrixSize)]
    # return matrix

# Differentiating among the user's choice of cipher method
def select_caesar():
    global selected_method
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be the number of character shift")
    selected_method = "Caesar"

def select_Mono():
    global selected_method
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must contain 26 unique characters ")
    selected_method = "MonoAlphabetic"

def select_playfair():
    global selected_method
    selected_method = "PlayFair"

def select_hill():
    global selected_method 
    selected_method = "Hill"

def select_vigenere():
    global selected_method
    selected_method = "Vigenere"

def select_railfence():
    global selected_method
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be the number of diagonal shift")
    selected_method = "RailFence"

def select_columnar():
    global selected_method
    keyEntry.delete(0, tkinter.END)
    keyEntry.insert(0, "Key must be the order of the arrangements")
    selected_method = "Columnar"

# Using the user's selection to call upon appropriate encryption functions 
def callEncryptMethod():
    if selected_method == "Caesar":
        InitialText = "Key must be shift Number"
        outputText.insert("1.0", InitialText)
        pt = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.CaesarCipher(key)
        encryptedText = test.Encrypt(pt)
        print(encryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    if selected_method == "MonoAlphabetic":
        pt = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.MonoAlphabetic(key)
        encryptedText = test.Encrypt(pt)
        print(encryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "PlayFair":
        test = Module.Playfair()
        pt = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        encryptedText = test.Encrypt(pt, key)
        print(encryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "Hill":
        pass
        # key = keyEntry.get()
        # size = MatrixSizeEntry.get()
        # finalKey = createMatrix(key, size)
        # print(finalKey)
        # test = Module.Hill(finalKey)
        # plainText = inputText.get("1.0", "end-1c")
        # encryptedText = test.Encrypt(plainText)
        # outputText.delete("1.0","end")
        # outputText.insert("1.0", encryptedText)

    elif selected_method == "Vigenere":        
        key = keyEntry.get()
        test = Module.Vignere(key)
        plainText = inputText.get("1.0", "end-1c")
        encryptedText = test.Encrypt(plainText)
        print(encryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)


    elif selected_method == "RailFence":
        test = Module.RailFence()
        plainText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        encryptedText = test.Encrypt(plainText, int(key))
        print(encryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

    elif selected_method == "Columnar":
        key = keyEntry.get()
        keyArray = [int(char) for char in key]
        print(keyArray)
        plainText = inputText.get("1.0", "end-1c")
        test = Module.Columnar(keyArray)
        encryptedText = test.Encrypt(plainText)
        print(encryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", encryptedText)

# Using user's selection to call upon appropriate decryption function
def callDecryptMethod():
    if selected_method == "Caesar":
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.CaesarCipher(key)
        decryptedText = test.Decrypt(cipherText)
        print(decryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "MonoAlphabetic":
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        test = Module.MonoAlphabetic(key)
        decryptedText = test.Decrypt(cipherText)
        print(decryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "PlayFair":
        test = Module.Playfair()
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        decryptedText = test.Decrypt(cipherText, key)
        print(decryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)
        
    elif selected_method == "Hill":
        pass

    elif selected_method == "Vigenere":
        key = keyEntry.get()
        test = Module.Vignere(key)
        cipherText = inputText.get("1.0", "end-1c")
        decryptedText = test.Decrypt(cipherText)
        print(decryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "RailFence":
        test = Module.RailFence()
        cipherText = inputText.get("1.0", "end-1c")
        key = keyEntry.get()
        decryptedText = test.Decrypt(cipherText, int(key))
        print(decryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

    elif selected_method == "Columnar":
        key = keyEntry.get()
        keyArray = [int(char) for char in key]
        print(keyArray)
        cipherText = inputText.get("1.0", "end-1c")
        test = Module.Columnar(keyArray)
        decryptedText = test.Decrypt(cipherText)
        print(decryptedText)
        outputText.delete("1.0", "end")
        outputText.insert("1.0", decryptedText)

# Creating buttons for cipher method selection 
cipherLabel = tkinter.Label(window, text="Cipher Method")
cipherLabel.place(x=120, y=2)

caesar = tkinter.Button(window, text="Caesar",command=select_caesar, width=12)
caesar.place(x=15, y=25)

mono = tkinter.Button(window, text="MonoAlphabetic", command=select_Mono, width=12)
mono.place(x=170, y=25)

playfair = tkinter.Button(window, text="PlayFair", command=select_playfair, width=12)
playfair.place(x=15, y=60)

hill = tkinter.Button(window,text="Hill Cipher", command=select_hill, width=12)
# hill.pack()

vigenere = tkinter.Button(window, text="Vigenere", command=select_vigenere, width=12)
vigenere.place(x=170, y=60)

railfence = tkinter.Button(window, text="RailFence", command=select_railfence, width=12)
railfence.place(x=15, y=95)

columnar = tkinter.Button(window, text="Columnar", command=select_columnar, width=12)
columnar.place(x=170, y=95)

# Creating a text box to take the PlainText
InputLabel = tkinter.Label(window, text="Plain Text: ")
InputLabel.place(x=120, y=135)
inputText = tkinter.Text(window,height=2.5, width=40)
inputText.place(x=0, y=155)

# Creating textbox to take the Key 
keyLabel = tkinter.Label(window, text="Key: ")
keyLabel.place(x=130, y=220)
keyEntry = tkinter.Entry(window, width=40)
keyEntry.place(x=0, y=240)

# In case of Hill cipher, the size of key matrix 
# MatrixSizeLabel = tkinter.Label(window, text="Matrix Size")
# MatrixSizeLabel.pack()
# MatrixSizeEntry = tkinter.Entry(window)
# MatrixSizeEntry.pack()

# Creating encryption and decryption buttons 
encryptButton = tkinter.Button(window, text="Encrypt", command=callEncryptMethod, width=12)
encryptButton.place(x=20, y=280)
decryptButton = tkinter.Button(window, text="Decrypt", command=callDecryptMethod, width=12)
decryptButton.place(x=165, y=280)

# Textbox for Results 
outputLabel = tkinter.Label(window, text="Cipher Text: ")
outputLabel.place(x=120, y=325) 
outputText = tkinter.Text(window, height=2.5, width=40)
outputText.place(x=0, y=345)

# def motion(event):
    # x, y = event.x, event.y
    # print('{}, {}'.format(x,y))
# window.bind('<Motion>', motion)

window.mainloop()
