s = input("Digite a frase: ")
t = ""

i = 0
while i < len(s):
    t = t + s[i] + " "
    i = i + 1
print(t)

x = ""
for c in s:
    x = x + c + " "
print(x)
