# SYMBOL_START is the Unicode index where "placeholder symbols" start.
# SYMBOL_START can be set arbitrarily but should be really high
# SYMBOL_ENTRIES is a list of substitutions to use
SYMBOL_START = 880
SYMBOL_TEXT = ["aw","sh","w","ow","wa","we","wi","wo","wu"]

def remove_symbols(string):
    new_string = ""
    for l in string:
        if ord(l)<SYMBOL_START:
            new_string += l
        else:
            new_string += SYMBOL_TEXT[ord(l)-SYMBOL_START]
    return new_string