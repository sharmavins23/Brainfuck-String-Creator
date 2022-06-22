from src import brainfuck


# ===== Space complexity reduction =============================================


# Given a number, create the corresponding tick increment strings
def createTickStrings(num):
    upTick, downTick = "", ""

    # Get the decimal amount of loops and append these values
    numDecimal = num // 10
    upTick += ("+" * numDecimal)
    downTick += ("+" * numDecimal)

    # Append the loop itself (10 increments)
    upTick += "[>++++++++++<-]>"
    downTick += "[>----------<-]>"

    # Append the excess
    numExcess = num % 10
    upTick += ("+" * numExcess)
    downTick += ("-" * numExcess)

    return upTick, downTick


# ===== Conversion functions ===================================================


# Given a character, return the corresponding Brainfuck instructions
def convertCharToBF(char):
    bfString = ""  # Empty string for instructions

    # First, get the ASCII decimal value of the character
    charDecimalASCII = ord(char)

    # Get tick strings
    upTick, downTick = createTickStrings(charDecimalASCII)

    # Create the instruction
    bfString += upTick + ".<" + downTick

    # Create a newline, for readability
    bfString += "\n"

    return bfString


# Given a string, return the corresponding Brainfuck instructions
def convertStringToBF(string):
    bfString = ""  # Empty string for instructions

    # For each character in the string, convert it to BF
    for char in string:
        bfString += convertCharToBF(char)

    return bfString


# A better print command:
#  Convert a string to BF
#  Have the BF interpreter handle it
def printBF(string):
    bfString = convertStringToBF(string)
    brainfuck.evaluate(bfString)


# ===== Driver code ============================================================

def main():
    stringToConvert = input("Enter a string to convert: ")

    bfString = convertStringToBF(stringToConvert)

    print("The corresponding BF instructions are:")
    print(bfString)

    print("This sourcecode evaluated in Brainfuck is:")
    printBF(stringToConvert)


if __name__ == "__main__":
    main()
