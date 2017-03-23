def check(word):

  dic = {'+' : '+', '-':'-','Input':'input=', 'num':'int', '=':'='}

  if word in dic:

    x=dic[word]

    return(x)

  else:

    return False


print(check('='))