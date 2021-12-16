import json

Money1 = open("Accounts2/Money1.txt").read()
Money2 = open("Accounts2/Money2.txt").read()
Money3 = open("Accounts2/Money3.txt").read()
Money4 = open("Accounts2/Money4.txt").read()
Money5 = open("Accounts2/Money5.txt").read()
Money6 = open("Accounts2/Money6.txt").read()
Money7 = open("Accounts2/Money7.txt").read()
Money8 = open("Accounts2/Money8.txt").read()
Money9 = open("Accounts2/Money9.txt").read()
Money10 = open("Accounts2/Money10.txt").read()
Money11 = open("Accounts2/Money11.txt").read()
Money12 = open("Accounts2/Money12.txt").read()
Money13 = open("Accounts2/Money13.txt").read()
Money14 = open("Accounts2/Money14.txt").read()
Money15 = open("Accounts2/Money15.txt").read()
Money16 = open("Accounts2/Money16.txt").read()
Money17 = open("Accounts2/Money17.txt").read()
Money18 = open("Accounts2/Money18.txt").read()
Money19 = open("Accounts2/Money19.txt").read()
Money20 = open("Accounts2/Money20.txt").read()
Money21 = open("Accounts2/Money21.txt").read()
Money22 = open("Accounts2/Money22.txt").read()
Money23 = open("Accounts2/Money23.txt").read()
Money24 = open("Accounts2/Money24.txt").read()
Money25 = open("Accounts2/Money25.txt").read()
Money26 = open("Accounts2/Money26.txt").read()
Money27 = open("Accounts2/Money27.txt").read()
Money28 = open("Accounts2/Money28.txt").read()
Money29 = open("Accounts2/Money29.txt").read()
Money30 = open("Accounts2/Money30.txt").read()

while True:
        Choice2 = input("Which student ID number do you want to view? ")
        while Choice2 != '1' and Choice2 != '2' and Choice2 != '3' and Choice2 != '4' and Choice2 != '5' and Choice2 != '6' and Choice2 != '7' and\
        Choice2 != '8' and Choice2 != '9' and Choice2 != '10' and Choice2 != '11' and Choice2 != '12' and Choice2 != '13' and Choice2 != '14' and\
        Choice2 != '15' and Choice2 != '16' and Choice2 != '17' and Choice2 != '18' and Choice2 != '19' and Choice2 != '20' and Choice2 != '21' and\
        Choice2 != '22' and Choice2 != '23' and Choice2 != '24' and Choice2 != '25' and Choice2 != '26' and Choice2 != '27' and\
        Choice2 != '28' and Choice2 != '29' and Choice2 != '30':
            Choice2 = input("Not a valid ID, please try again: ")
        if Choice2 == '1':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money1.txt', 'w')
            file.write(str(Money1))
            file.close()
            print(open("Accounts2/Money1.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '2':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money2.txt', 'w')
            file.write(str(Money2))
            file.close()
            print(open("Accounts2/Money2.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '3':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money3.txt', 'w')
            file.write(str(Money3))
            file.close()
            print(open("Accounts2/Money3.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '4':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money4.txt', 'w')
            file.write(str(Money4))
            file.close()
            print(open("Accounts2/Money4.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '5':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money5.txt', 'w')
            file.write(str(Money5))
            file.close()
            print(open("Accounts2/Money5.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '6':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money6.txt', 'w')
            file.write(str(Money6))
            file.close()
            print(open("Accounts2/Money6.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '7':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money7.txt', 'w')
            file.write(str(Money7))
            file.close()
            print(open("Accounts2/Money7.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '8':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money8.txt', 'w')
            file.write(str(Money8))
            file.close()
            print(open("Accounts2/Money8.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '9':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money9.txt', 'w')
            file.write(str(Money9))
            file.close()
            print(open("Accounts2/Money9.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '10':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money10.txt', 'w')
            file.write(str(Money10))
            file.close()
            print(open("Accounts2/Money10.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '11':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money11.txt', 'w')
            file.write(str(Money11))
            file.close()
            print(open("Accounts2/Money11.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '12':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money12.txt', 'w')
            file.write(str(Money12))
            file.close()
            print(open("Accounts2/Money12.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '13':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money13.txt', 'w')
            file.write(str(Money13))
            file.close()
            print(open("Accounts2/Money13.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '14':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money14.txt', 'w')
            file.write(str(Money14))
            file.close()
            print(open("Accounts2/Money14.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '15':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money15.txt', 'w')
            file.write(str(Money15))
            file.close()
            print(open("Accounts2/Money15.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '16':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money16.txt', 'w')
            file.write(str(Money16))
            file.close()
            print(open("Accounts2/Money16.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '17':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money17.txt', 'w')
            file.write(str(Money17))
            file.close()
            print(open("Accounts2/Money17.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '18':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money18.txt', 'w')
            file.write(str(Money18))
            file.close()
            print(open("Accounts2/Money18.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '19':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money19.txt', 'w')
            file.write(str(Money19))
            file.close()
            print(open("Accounts2/Money19.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '20':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money20.txt', 'w')
            file.write(str(Money20))
            file.close()
            print(open("Accounts2/Money20.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '21':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money21.txt', 'w')
            file.write(str(Money21))
            file.close()
            print(open("Accounts2/Money21.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '22':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money22.txt', 'w')
            file.write(str(Money22))
            file.close()
            print(open("Accounts2/Money22.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '23':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money23.txt', 'w')
            file.write(str(Money23))
            file.close()
            print(open("Accounts2/Money23.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '24':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money24.txt', 'w')
            file.write(str(Money24))
            file.close()
            print(open("Accounts2/Money24.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '25':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money25.txt', 'w')
            file.write(str(Money25))
            file.close()
            print(open("Accounts2/Money25.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '26':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money26.txt', 'w')
            file.write(str(Money26))
            file.close()
            print(open("Accounts2/Money26.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '27':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money27.txt', 'w')
            file.write(str(Money27))
            file.close()
            print(open("Accounts2/Money27.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '28':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money28.txt', 'w')
            file.write(str(Money28))
            file.close()
            print(open("Accounts2/Money28.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '29':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money29.txt', 'w')
            file.write(str(Money29))
            file.close()
            print(open("Accounts2/Money29.txt").read())
          else:
            print('Wrong! Access Denied!')
        elif Choice2 == '30':
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
          passWord = input('What is the password? ')
          if passWord == 'OpenUp':
            print('Access Granted!')
            file = open('Accounts2/Money30.txt', 'w')
            file.write(str(Money30))
            file.close()
            print(open("Accounts2/Money30.txt").read())
          else:
            print('Wrong! Access Denied!')