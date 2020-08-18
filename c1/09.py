import random


def rnd():
  return random.random()

def shuffle(s):  #シャッフル関数
  nakami = ""
  if len(s) > 4:
    sdash = slice(s[1:len(s) - 1])
    for i in range(len(sdash)):
      index = int(rnd() * len(sdash))
      nakami += sdash[index]
      sdash.pop(index)
    nakami = s[0] + nakami + s[len(s) - 1]
  else:
    nakami = s

  return nakami

def slice(s):   #スライス関数
  ret = []
  for i in range(len(s)):
    ret.append(s[i])
  return ret

def Typoglycemia(s):
  sl = s.split()
  ret = ""
  for i in range(len(sl)):
    ret += shuffle(sl[i]) + " "
  return ret

source = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(source))
