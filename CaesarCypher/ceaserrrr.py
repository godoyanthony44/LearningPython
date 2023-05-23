def ceaserCypher(code,messag,shift):
    shifted_word = []
    if code == "encode":
        for n in messag:
            shifted_word.append( chr(ord(n) + shift))
    elif code == "decode":
        for n in messag:
            shifted_word.append( chr(ord(n) - shift))
    return ''.join(shifted_word)