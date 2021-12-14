Class = input('Which class do you want to view? ')

while Class != '7-03' and Class != '7-07' and Class != '7-10' and Class != '7-11' and Class != '7-12' and Class != '703' and Class != '707' and Class != '710' and Class != '711' and Class != '712':
  Class = input('Not a valid class, please try again: ')

if Class == '7-03' or Class == '703':
  passWord = input('What is the password? ')
  if passWord == 'OpenUp':
    print('Access Granted!')
    import seventhree
  else:
    print('Wrong! Access Denied')
elif Class == '7-07' or Class == '707':
  passWord = input('What is the password? ')
  if passWord == 'OpenUp':
    print('Access Granted!')
    import sevenseven
  else:
    print('Wrong! Access Denied')
elif Class == '7-10' or Class == '710':
  passWord = input('What is the password? ')
  if passWord == 'OpenUp':
    print('Access Granted!')
    import seventen
  else:
    print('Wrong! Access Denied')
elif Class == '7-11' or Class == '711':
  passWord = input('What is the password? ')
  if passWord == 'OpenUp':
    print('Access Granted!')
    import seveneleven
  else:
    print('Wrong! Access Denied')
elif Class == '7-12' or Class == '712':
  passWord = input('What is the password? ')
  if passWord == 'OpenUp':
    print('Access Granted!')
    import seventwelve
  else:
    print('Wrong! Access Denied')