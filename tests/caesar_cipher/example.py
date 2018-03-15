def encrypt(message):
    """Encrypt the given message
    
    Arguments:
        message {str} -- Message to encrypt
    
    Returns:
        str -- The encrypted string
    """

    if message:
        enc_message = list(map(encrypt_letter, message))
        enc_message = "".join(enc_message)
        return enc_message
    else:
        return ""

def encrypt_letter(letter):
    """Encrypt a single letter
    
    Arguments:
        letter {char} -- The character to encrypt
    
    Returns:
        char -- The encrypted character
    """

    inc_ord_char = ord(letter) + 3
    if letter.isupper():
       if inc_ord_char > 90:
           inc_ord_char = inc_ord_char % 90 + 64 
    else:
        if inc_ord_char > 122:
            inc_ord_char = inc_ord_char % 122 + 96
    return chr(inc_ord_char)
    