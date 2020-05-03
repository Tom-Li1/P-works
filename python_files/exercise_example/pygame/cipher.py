SYMBOLS = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789~!@#$%^&*()_+[]{}\|;':",./<>?"""
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    print("Do you wish to encrypt or decrypt or brute-force a message?")
    while True:
        mode = input(">>>").lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'b', 'brute']:
            return mode
        else:
            print("Please enter 'encrypt' or 'e' or 'decrypt' or 'd' or 'brute' or 'b'.")

def getMessage():
    print('Enter your message:')
    while True:
        msg = input('>>>')
        if msg:
            return msg
        else:
            print('Please type something here!')

def getKey():
    key = 0
    print("Enter the key number (1 - %s)" % (MAX_KEY_SIZE))
    while True:
        key = int(input(">>>"))
        if key <= MAX_KEY_SIZE and key >= 1:
            return key
        else:
            print('Make sure the key is lower than %s and greater than 1.' % (MAX_KEY_SIZE))

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key

    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]

    return translated

while True:
    mode = getMode()
    message = getMessage()

    if mode[0] != 'b':
        key = getKey()
    print('Your translated text is:')

    if mode[0] != 'b':
        print('=' * len(message))
        print(getTranslatedMessage(mode, message, key))
        print('=' * len(message))
    else:
        print('===' + '=' * len(message))
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key, getTranslatedMessage("decrypt", message, key))
        print('===' + '=' * len(message))
