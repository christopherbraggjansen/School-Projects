# -------------------------------------------------------------------------------
# Your Name: Chris Jansen
# Python Version:2.7
# Purpose: This program demonstrates the fundamentals of a class by implementing a Caesar Cipher.
#           The class imports a file, encrypts the file, and exports the cipher to a new file
#           You need to implement the decrypt function.
#           You can reuse the import and export functions when decrypting!
#
# Acknowledgements: Original code by Scott Heggen and Jan Pearce
# -------------------------------------------------------------------------------
import sys


class CaesarCipher:
    def __init__(self, input_file="io_input.txt", key=0, crypt_type="encrypt"):
        """
        A constructor for the CaesarCipher class
        """
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            # The alphabet, which will be used to do our shifts
        self.input_file = input_file                            # The file to be encrypted or decrypted
        self.key = key                                          # The amount each message/cipher will be shifted
        self.message = ""                                       # A placeholder for the message
        self.cipher = ""                                        # A placeholder for the cipher
        self.crypt_type = crypt_type                            # Either "encrypt" or "decrypt"
        self.import_file()                                      # Calls the import_file() method below


    def import_file(self):
        """
        Imports a file stored in the variable self.input_file
        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")
        if self.crypt_type == "encrypt":
            self.message = f.read()                  # Set self.message to the file contents
        elif self.crypt_type == "decrypt":
            self.cipher = f.read()                   # Set self.cipher to the file contents
        f.close()


    def export_file(self, text_to_export, filename):
        """
        Exports a file called filename
        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")
        f.write(text_to_export)
        f.close()
        print("File exported to " + filename)


    def encrypt(self):
        """
        Converts an original message into a ciphered message with each letter shifted to the right by the key
        :return: a string representing the ciphertext
        """
        output = ""
        for i in self.message:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                # Uses modulus to return the correct index for each letter after the shift
                # (for cases where the index is outside the range of self.alphabet,
                #  it wraps back to the beginning of the alphabet)
                output += self.alphabet[(old_letter+self.key) % 26]
            else:
                output += i                                                 # Adds non-alphabet characters directly
        return output


    def decrypt(self):
        """
        Converts a ciphertext into an original message by shifting each letter to the left by the key
        :return: a string representing the original message
        """
        output = ""
        reverse_key = self.key * -1 # Makes the key go right instead of left
        for i in self.cipher:
            if i.upper() in self.alphabet:
                old_letter = self.alphabet.find(i.upper())
                output += self.alphabet[(old_letter+reverse_key) %26]

            else:
                output += i
        return output

    def testit(self, did_pass):
        """  Prints the result of a test.  """
        linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)


    def CaesarCipher_test_suite(self):
        """
        A test suite for testing the encrypt and decrypt methods of the class

        NOTES:
        Typically, a test suite for a Class would be written into a second class entirely.
        However, to keep the complexity low, we chose to incorporate the test suite into the class itself.
        This allows you to directly test the encrypt() and decrypt() methods.
        In the future, we will explore how to properly write a test suite using a separate class.
        """

        # tests encrypting a normal string
        self.key = 3
        self.message = "A test string"
        self.testit(self.encrypt() == "D WHVW VWULQJ")

        # tests encrypting a string with punctuation
        self.key = 13
        self.message = "It's a so-so kind of day!"
        self.testit(self.encrypt() == "VG'F N FB-FB XVAQ BS QNL!")

        # tests decrypting a normal string
        self.key = 3
        self.cipher = "D WHVW VWULQJ"
        self.crypt_type = "decrypt"
        self.testit(self.decrypt() == "A TEST STRING")

        # tests decrypting a string with punctuation
        self.key = 6
        self.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"
        self.testit(self.decrypt() == "IT'S A SO-SO KIND OF DAY!")


def main():
    # A sample encryption
    cipher0 = CaesarCipher("message_input.txt", 2, "encrypt")   # Constructs a new CaesarCipher object called cipher0
    cipher_text0 = cipher0.encrypt()                            # Encrypts the file specified in the constructor
    cipher0.export_file(cipher_text0, "cipher_sample.txt")      # Writes the output to a file


    # Caesar has some letters to send and receive.
    # Letter 1 goes to P. Lentulus Spinther, who has agreed with Caesar to use a key of 3
    cipher1 = CaesarCipher ("letter_to_friend_1.txt", 3, "encrypt")
    cipher_text1 = cipher1.encrypt()
    cipher1.export_file(cipher_text1, "cipher_to_friend_1.txt")

    # Letter 2 goes to Marcus Tullius Cicero, who has agreed to use a key of 14
    cipher2 = CaesarCipher("letter_to_friend_2.txt", 14, "encrypt")
    cipher_text2 = cipher2.encrypt()
    cipher2.export_file(cipher_text2, "cipher_to_friend_2.txt")

    # Letter 3 is coming from Cicero for Caesar to decrypt. Again, they agreed to use key 14
    cipher3 = CaesarCipher("letter_from_friend_3.txt", 14, "decrypt")   # constructs a new CaesarCipher object called cipher3
    letter_text3 = cipher3.decrypt()
    cipher3.export_file(letter_text3, "message_from_friend_3.txt")
    # Uncomment to run the test suite
#    testing = CaesarCipher()
#    testing.CaesarCipher_test_suite()

main()
