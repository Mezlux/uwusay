import translator
import sys

in_file = open(sys.argv[1], "r", encoding="utf-8")

out_file = open("out.txt","w", encoding="utf-8")

# Read the file, then
# Ditch having to worry about case sentivity by making it
# lowercase, then translate and output
out_file.write(translator.translate(in_file.read().lower()))

out_file.close()
in_file.close()