from regcheck import RegCheck
from symbols import remove_symbols

checks = [
    RegCheck(r'(?<=[a-z])ti(?=[a,e,i,o,u])', 1),
    RegCheck(r'ere', 11),
    RegCheck(r"(?<=\w)er", 10),
    RegCheck(r'or', 12),
    RegCheck(r'ou', 3),
    RegCheck(r"(?<=[a-z])oo", 9),
    RegCheck(r'o(?=[a-z])', 0),
    RegCheck(r'r(?![^a-z])', 2),
    RegCheck(r"l(?!e[^a-z])(?![^a-z])", 2),
    RegCheck(r"(?<=[^aeiouw])(?<=[a-z])a", 4),
    RegCheck(r"(?<=[^aeiouw])(?<=[a-z])e(?=[a-z])", 5),
    RegCheck(r"(?<=[^aeiouw])(?<=[a-z])i", 6),
    RegCheck(r"(?<=[^aeiouw])(?<=[a-z])o", 7),
    RegCheck(r"(?<=[^aeiouw])(?<=[a-z])u", 8),
]


def translate(string):
  for c in checks:
    string = c.apply(string)
  string = remove_symbols(string)
  return string
  pass
