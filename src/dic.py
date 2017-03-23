def check(word):

  dic = {'+' : '+', '-':'-', 'Input':'input=', 'num':'int', '=':'=',  'Begin':'',  'End':'',  'Print':'print' }

  if word in dic:
    x=dic[word]
    return(x)
  elif (word=='End'and (dic[word]=='')):
    return 0
  else:
    return word



