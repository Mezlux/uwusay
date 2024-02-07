import translator
import sys

using_file = False

if len(sys.argv) == 1:
  input = input("Inpwut: ")
else:
  using_file = True
  in_file = open(sys.argv[1], "r", encoding="utf-8")
  input = in_file.read()

out_file = open("out.txt", "w", encoding="utf-8")
output = ""

# Read the file, then
# Ditch having to worry about case sentivity by making it
# lowercase, then translate and output
output = translator.translate(input.lower())
print(output)
print("----------------------------------")
print("Awtpwut cwan bwe fwound in out.txt")
out_file.write(output)

out_file.close()

if using_file:
  in_file.close()
