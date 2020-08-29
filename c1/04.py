str = "Hi He Lied Because Boron Could Not Oxidize Fluorine New Nations Might Also Sign Peace Security Clause. Arthur King Can"
sary = str.split()
oneelem = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element = {}

for i in range(len(sary)):
    if len(oneelem) > 0 and oneelem[0] - 1 == i:
        element[sary[i][0:1]] = i + 1
        oneelem.pop(0)
    else:
        element[sary[i][0:2]] = i + 1

print(element)
