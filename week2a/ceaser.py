def caesar_cipher(msg, shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    msg=msg.lower()
    code=[]
    for char in msg:
        char=str(char)
        if char.isdigit():            
            code.append(str((int(char)+shift)%10))
        elif char in alphabet:
            code.append(alphabet[(alphabet.find(char)+shift)%26])
        else:
            code.append(char)
    return ''.join(code)
