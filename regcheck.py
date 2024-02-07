import re
import symbols

class RegCheck:
    def __init__(self, pattern, replace_with) -> None:
        # The "RegCheck" will store a pattern to search and then
        # an index corresponding with an item in SYMBOL_ENTRIES
        self.pat = pattern
        self.rpl = replace_with
        pass
    def apply(self, string):
        # Apply the RegCheck to a string by replacing matches with
        # a symbol
        return re.sub(self.pat, chr(symbols.SYMBOL_START+self.rpl), string)