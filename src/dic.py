def check(word):

  dic = {'+' : '+', '-':'-', 'Input':'input=', 'num':'int()', '=':'=',  'Begin':'',  'End':'',  'Print':'print' , 'if':'if',
  'AND':'and','OR':'or','NOT':'not','true':'True','false':'False','elseif':'elif','else:':'','endif':'' }

  if word in dic:
    x=dic[word]
    return(x)
  elif word=='End' and (dic[word]==''):
    return 0
  else:
    return word



