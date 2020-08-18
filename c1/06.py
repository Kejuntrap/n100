
def makebigram(s):
  returnset = set()
  for i in range(len(s) - 1):
    returnset.add(s[i:i + 2])
  return returnset
    

str1 = "paraparaparadise"
str2 = "paragraph"

s1map = makebigram(str1)
s2map = makebigram(str2)

union = s1map | s2map
intersection = s1map & s2map
diff = s1map - s2map
print(union)
print(intersection)
print(diff)
print('se' in (s1map | s2map))