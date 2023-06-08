# --------------------------------------
# CSCI 127, Lab 7                      |
# Date                    |
# Your Name                            |
# --------------------------------------
class Ascii:

    def __init__(self, init_char, init_bin):
        self.character = init_char
        self.binary = init_bin

    def getCharacter(self):
        return self.character

    def getBinary(self):
        return self.binary

    def __str__(self):
        return self.character + ":" + self.binary


# The missing functions go here.
def create_ascii_list(file_name):
    alist = []
    ascii_file = open(file_name, "r")

    for line in ascii_file:
        line_list = line.split(",")

        if line_list[1] == "space\n":
            alist.append( Ascii("space", line_list[0]) )
        elif line_list[1] == "comma\n":
            alist.append( Ascii("comma", line_list[0]) )
        else:
            alist.append( Ascii(line_list[1][0], line_list[0]) )

    ascii_file.close()
    
    return alist

def is_in_list(char, ascii_list):
    for item in ascii_list:
        if item.getCharacter() == char or item.getCharacter in ['comma', 'space']:
            return True
    return False

def translate(sentence, ascii_list, file_name):
    output_file = open(file_name, "w")
    for char in sentence:
        if char == ",":
            ## search for the Ascii object in the list that is a comma
            for item in ascii_list:
                if item.getCharacter() == 'comma':
                    output_file.write(char + " " + item.getBinary() + "\n")
        elif char == " ":
            for item in ascii_list:
                if item.getCharacter() == 'space':
                    output_file.write(char + " " + item.getBinary() + "\n")
        elif not is_in_list(char, ascii_list):
            output_file.write(char + " " + "UNKNOWN\n")
        else:
            for item in ascii_list:
                if item.getCharacter() == char:
                    output_file.write(char + " " + item.getBinary() + "\n")
            
    output_file.close()
    
# --------------------------------------

def main():
    alist = create_ascii_list("ascii-codes.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, alist, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, alist, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, alist, "output-3.txt")

# --------------------------------------
main()
