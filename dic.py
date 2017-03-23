def check(word):

  dic = {'+' : '+',
  '-':'-',
  'Input':'input=',
  'num':'int',
  '=':'=',
  'Begin':'',
  'End':'',
  'Print':'print'
  }

  if word in dic:

    x=dic[word]

    return(x)

  else:

    return False



    
  ##if end tell luke's program to close the file and run the converted script!



print(check('='))