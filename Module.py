defaultText = 'abcdefghijklmnopqrstuvwxyz'
defaultTextPlay = 'abcdefghiklmnopqrstuvwxyz'
class CaesarCipher:
    def Encrypt(self, plainText, key, encryptedText=''):
        plainText = plainText.lower()
        #defaultText = 'abcdefghijklmnopqrstuvwxyz'
        encryptedText = ''
        for i in plainText:
            count = 0
            for j in defaultText:
                count += 1
                if(j==i):
                    encryptValue = ((count-1)+key)%26
                    encryptedText += defaultText[encryptValue]
        return encryptedText

    def Decrypt(self, cipherText, key, decryptedText=''):
        cipherText = cipherText.lower()
        #defaultText = 'abcdefghijklmnopqrstuvwxyz'
        decryptedText = ''
        for i in cipherText:
            count = 0
            for j in defaultText:
                count += 1
                if(j==i):
                    decryptValue = ((count-1)-key)%26
                    decryptedText += defaultText[decryptValue]
        return decryptedText

class MonoAlphabetic:
    def createCipher(self):
        key = 'zyxwvutsrqponmlkjihgfedcba'
        #alphabet = 'abcdefghijklmnopqrstuvwxyz'
        cipherDict = {letter: key[i] for i, letter in enumerate(defaultText)}
        return cipherDict

    def Encrypt(self, plainText, cipherDict):
        cipherText = ''       
        plainText = plainText.replace(" ","")
        plainText = plainText.lower()
        for character in plainText:
            cipherText += cipherDict[character]
        return cipherText

    def Decrypt(self, cipherText, cipherDict):
        decipherDict = {v: k for k, v in cipherDict.items()}
        plainText = ''
        cipherText = cipherText.replace(" ","")
        cipherText = cipherText.lower()
        for character in cipherText:
            plainText += decipherDict[character]
        return plainText    

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
        PlayfairMatrix = self.createMatrix(key)
        encryptText = self.cleanText(encryptText)
        decryptedText = ""
        
        for i in range(0, len(encryptText), 2):
            char1, char2 = encryptText[i], encryptText[i+1]
            row1, col1 = self.checkCoordinates(PlayfairMatrix, char1)
            row2, col2 = self.checkCoordinates(PlayfairMatrix, char2)

            if row1 == row2:
                decryptedText += PlayfairMatrix[row1][(col1 - 1) % 5] + PlayfairMatrix[row2][(col2 - 1) %5]
            elif col1 == col2:
                decryptedText += PlayfairMatrix[(row1 - 1) % 5][col1] + PlayfairMatrix[(row2 - 1) % 5][col2]
            else:
                decryptedText += PlayfairMatrix[row1][col2] + PlayfairMatrix[row2][col1]
        return decryptedText
