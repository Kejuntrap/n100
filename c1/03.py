str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace(',', '')
str = str.replace('.', '')
sary = str.split()
toujo = [0] * len(sary)

for i in range(len(sary)):
    toujo[i] = len(sary[i])

print(toujo)
