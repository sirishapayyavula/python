def CountFreq(li):
  freq = {}
  for items in li:
    freq[items] = freq.get(items,0)+1
  print(freq)
li =['a', 'a', 1, 1, 1, 'b', 'b', 'b', 2, 2, 2]
CountFreq(li)
