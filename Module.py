defaultText = 'abcdefghijklmnopqrstuvwxyz'
defaultTextPlay = 'abcdefghiklmnopqrstuvwxyz'

class CaesarCipher:
    def __init__(self, key):
        self.key = key 
    def Encrypt(self, plainText):
        encryptedText = ''
        for i in plainText.lower():
            count = 0
            for j in defaultText:
                count += 1
                if(j==i):
                    encryptValue = ((count-1)+int(self.key))%26
                    encryptedText += defaultText[encryptValue]
        return encryptedText

    def Decrypt(self, cipherText):
        decryptedText = ''
        for i in cipherText.lower():
            count = 0
            for j in defaultText:
                count += 1
                if(j==i):
                    decryptValue = ((count-1)-int(self.key))%26
                    decryptedText += defaultText[decryptValue]
        return decryptedText

class MonoAlphabetic:
    def __init__(self, key):
        self.key = key 

    def Encrypt(self, plainText):
        cipherDict = {letter: self.key[i] for i, letter in enumerate(defaultText)}
        encryptedText = ''       
        plainText = plainText.lower().replace(" ","")
        for character in plainText:
            encryptedText += cipherDict[character]
        return encryptedText

    def Decrypt(self, cipherText):
        cipherDict = {letter: self.key[i] for i, letter in enumerate(defaultText)}
        decipherDict = {v: k for k, v in cipherDict.items()}
        decryptedText = ''
        cipherText = cipherText.lower().replace(" ","")
        for character in cipherText:
            decryptedText += decipherDict[character]
        return decryptedText    

class Playfair:
    def cleanText(self, text):
        text = text.lower().replace(" ","").replace("j","i")
        return text

    def createMatrix(self, key):
        key = self.cleanText(key)
        matrix = []
        
        for character in key:
            if character not in matrix:
                matrix.append(character)

        for character in defaultTextPlay:
            if character not in matrix:
                matrix.append(character)

        PlayfairMatrix = [matrix[i:i+5] for i in range(0, 25,5)]
        return PlayfairMatrix

    def checkCoordinates(self, matrix, char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j 

    def Encrypt(self, plainText, key):
        PlayfairMatrix = self.createMatrix(key)
        plainText = self.cleanText(plainText)
        i = 0 
        while i < len(plainText) - 1:
            if plainText[i] == plainText[i + 1]:
                plainText = plainText[:i + 1] + 'x' + plainText[i + 1:]
                i += 1
            i += 2
        if len(plainText) % 2 != 0:
            plainText += 'x'

        encryptedText = ""
        for i in range(0 , len(plainText), 2):
            char1, char2 = plainText[i], plainText[i+1]
            row1, col1 = self.checkCoordinates(PlayfairMatrix, char1)
            row2, col2 = self.checkCoordinates(PlayfairMatrix, char2)

            if row1 == row2:
                encryptedText += PlayfairMatrix[row1][(col1 + 1) % 5] + PlayfairMatrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encryptedText += PlayfairMatrix[(row1 + 1) % 5][col1] + PlayfairMatrix[(row2 + 1) % 5][col2]
            else:
                encryptedText += PlayfairMatrix[row1][col2] + PlayfairMatrix[row2][col1]
        return encryptedText

    def Decrypt(self, encryptText, key):
        playfairMatrix = self.createMatrix(key)
        encryptText = self.cleanText(encryptText)
        decryptedText = ""        
        for i in range(0, len(encryptText), 2):
            char1, char2 = encryptText[i], encryptText[i+1]
            row1, col1 = self.checkCoordinates(playfairMatrix, char1)
            row2, col2 = self.checkCoordinates(playfairMatrix, char2)

            if row1 == row2:
                decryptedText += playfairMatrix[row1][(col1 - 1) % 5] + playfairMatrix[row2][(col2 - 1) %5]
            elif col1 == col2:
                decryptedText += playfairMatrix[(row1 - 1) % 5][col1] + playfairMatrix[(row2 - 1) % 5][col2]
            else:
                decryptedText += playfairMatrix[row1][col2] + playfairMatrix[row2][col1]
        return decryptedText

class RailFence:
    def Encrypt(self, PlainText, key):
        rail = [["\n" for i in range(len(PlainText))] for j in range(key)]
        dir_down = False
        row, col = 0, 0
        for i in range(len(PlainText)):
            if (row==0) or (row==key-1):
                dir_down = not dir_down
            rail[row][col] = PlainText[i]
            col += 1 
            if dir_down:
                row += 1 
            else:
                row -= 1 
        result = []
        for i in range(key):
            for j in range(len(PlainText)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return("".join(result))

    def Decrypt(self, cipher, key):
        rail = [['\n' for i in range(len(cipher))] for j in range(key)]
        dir_down = None
        row, col = 0, 0 
        for i in range(len(cipher)):
            if row==0:
                dir_down = True 
            if row==key-1:
                dir_down = False
            rail[row][col] = '*'
            col += 1 
            if dir_down:
                row += 1 
            else:
                row -= 1 
        index = 0 
        for i in range(key):
            for j in range(len(cipher)):
                if((rail[i][j]=='*') and (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1 
        result = []
        row, col = 0,0 
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key-1:
                dir_down = False
            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1 
            if dir_down:
                row += 1 
            else: 
                row -= 1 
        return("".join(result))

class Vignere:
    def __init__(self, key):
        self.key = key.upper()

    def extendKey(self, message):
        keyExtension = ""
        keyIndex = 0 
        for char in message: 
            if char.isalpha():
                keyExtension += self.key[keyIndex]
                keyIndex = (keyIndex + 1) % len(self.key)
            else:
                keyExtension += char 
        return keyExtension

    def Encrypt(self, plainText):
        encryptedText = ""
        plainText = plainText.upper()
        extendedKey = self.extendKey(plainText)
        for i in range(len(plainText)):
            char = plainText[i]
            if char.isalpha():
                shift = ord(extendedKey[i]) - ord('A')
                encryptedChar = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
                encryptedText += encryptedChar
            else: 
                encryptedText += char 
        return encryptedText

    def Decrypt(self, cipherText):
        decryptedText = ""
        cipherText = cipherText.upper()
        extendedKey = self.extendKey(cipherText)
        for i in range(len(cipherText)):
            char = cipherText[i]
            if char.isalpha():
                shift = ord(extendedKey[i]) - ord('A')
                decryptedChar = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
                decryptedText += decryptedChar
            else:
                decryptedText += char 
        return decryptedText

class Columnar:
    def __init__(self, key):
        self.key = key

    def Encrypt(self, plainText):
        numRows = len(plainText) // len(self.key) + int(len(plainText) % len(self.key) > 0)
        matrix = [[' ' for _ in range(len(self.key))] for _ in range(numRows)]
        index = 0
        for row in range(numRows):
            for col in range(len(self.key)):
                if index < len(plainText):
                    matrix[row][col] = plainText[index]
                    index += 1 
        order = sorted(range(len(self.key)), key=lambda k: self.key[k])
        cipherText = ''
        for col in order:
            for row in range(numRows):
                cipherText += matrix[row][col]
        return cipherText

    def Decrypt(self, cipherText):
        numRows = len(cipherText) // len(self.key) + int(len(cipherText) % len(self.key) > 0)
        matrix = [[' ' for _ in range(len(self.key))] for _ in range(numRows)]
        order = sorted(range(len(self.key)), key=lambda k:self.key[k])
        index = 0
        for col in order:
            for row in range(numRows):
                if index < len(cipherText):
                    matrix[row][col] = cipherText[index]
                    index += 1 
        plainText = ''
        for row in range(numRows):
            for col in range(len(self.key)):
                plainText += matrix[row][col]
        return plainText

class Atbash:
    def __init__(self):
        self.key = 'zyxwvutsrqponmlkjihgfedcba'

    def Encrypt(self, plainText):
        cipherDict = {letter: self.key[i] for i, letter in enumerate(defaultText)}
        plainText = plainText.lower().replace(" ","")
        cipherText = ''
        for character in plainText:
            cipherText += cipherDict[character]
        return cipherText

    def Decrypt(self, cipherText):
        cipherDict = {letter: self.key[i] for i,letter in enumerate(defaultText)}
        decipherDict = {v:k for k,v in cipherDict.items()}
        cipherText = cipherText.lower().replace(" ","")
        plainText = ''
        for character in cipherText:
            plainText += decipherDict[character]
        return plainText
