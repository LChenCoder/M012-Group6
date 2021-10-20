tableLetters = {" ": "100000", "a": "100001", "d": "100010", "e": "100011", "h": "100100", "i": "100101", "I": "100110", "n": "100111", "o": "101000", "r": "101001", "s": "101010", "t": "101011", "an": "101100",
                "as": "101101", "will": "101110", "in": "101111", "is": "110000", "it": "110001", "of": "110010", "or": "110011", "so": "110100", "to": "110101", "the": "110110", "and": "110111", "ar": "111000", 
                "er": "111001", "not": "111010", "ed": "111011", "at": "111100", "re": "111101", "have": "111110", "en": "111111", "b": "0000000", "c": "0000001", "f": "0000010", "g": "0000011", "j": "0000100", 
                "k": "0000101", "l": "0000110", "m": "0000111", "p": "0001000", "q": "0001001", "u": "0001010", "v": "0001011", "w": "0001100", "x": "0001101", "y": "0001110", "z": "0001111", "A": "0010000", "B": "0010001", 
                "C": "0010010", "D": "0010011", "E": "0010100", "F": "0010101", "G": "0010110", "H": "0010111", "J": "0011000", "K": "0011001", "L": "0011010", "M": "0011011", "N": "0011100",  "O": "0011101", "P": "0011110", 
                "Q": "0011111", "R": "0100000", "S": "0100001", "T": "0100010", "U": "0100011", "V": "0100100", "W": "0100101", "X": "0100110", "Y": "0100111", "Z": "0101000", "ea": "0101001", "be": "0101010",  "that": "0101011", 
                "ing": "0101100", "this": "0101101", "tion": "0101110", "ou": "0101111", "st": "0110000", "with": "0110001",  "one": "0110010", "te": "0110011", "all": "0110100", "il": "0110101", "every": "0110110", "co": "0110111", 
                "for": "0111000", "’": "0111001", "\'": "0111001", "“": "0111010", "”": "0111010", "\"": "0111010", ".": "0111011", ",": "0111100","-": "0111101", "!": "0111110", "\n": "0111111"}

#Thought: replace string word by word first before iterating through everything
#Thought2: You might not even need to replace one by one, you can replace certain areas first, since '0' and '1' arent in the dictionary

#Trial 2
#Martin Luther King Jr. "I have a dream speech": 37063 bits

def encode():
    table = {}
    for k in sorted(tableLetters, key=len, reverse=True):
        table[k] = tableLetters[k]

    my_file = open("textToEncode.txt", "r", encoding = "utf-8")
    content = my_file.read()
    my_file.close()

    x = ' '.join([table.get(i, i) for i in content.split()])
    for i, initial in table.items():
        x = x.replace(i, initial)

    f = open("encodedText.txt", "w", encoding = "utf-8")
    f.write(str(len(x)) + "." + x)
    f.close()
encode()

#Food For Thought: What if inside the encode function, it incorporates a pattern recognition sequence/function that 
# finds the most often occuring patterns of string in a file and adds them to the dictionary with its respective binary counterpart


# Don't necessarily need to sort the table for decode

def decode():
    table = {v: k for k, v in tableLetters.items()}

    my_file = open("textToDecode.txt", "r", encoding = "utf-8")
    content = my_file.read()
    my_file.close()

    i = 0
    while i < len(content):
        if content[i] == '1':
            content = content[:(i+6)] + '2' + content[(i+6):]
            i+=7
        if content[i] == '0':
            content = content[:(i+7)] + '2' + content[(i+7):]
            i+=8
        else:
            continue

    x = ''.join([table.get(j, j) for j in content.split('2')])
    
    f = open("decodedText.txt", "w", encoding = "utf-8")
    f.write(x)
    f.close()
decode()