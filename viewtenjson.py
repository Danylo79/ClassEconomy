import jsonutil;

Money1 = jsonutil.openJson("Saly", "1234", 710, 1, False)
Money2 = jsonutil.openJson("Shaun", "1234", 710, 2, False)
Money3 = jsonutil.openJson("Kayden", "1234", 710, 3, False)
Money4 = jsonutil.openJson("Lucas", "1234", 710, 4, False)
Money5 = jsonutil.openJson("Sadie", "1234", 710, 5, False)
Money6 = jsonutil.openJson("Aiden", "1234", 710, 6, False)
Money7 = jsonutil.openJson("NULL", "1234", 710, 7, False)
Money8 = jsonutil.openJson("Tatiana", "1234", 710, 8, False)
Money9 = jsonutil.openJson("NULL", "1234", 710, 9, False)
Money10 = jsonutil.openJson("Tyson", "1234", 710, 10, False)
Money11 = jsonutil.openJson("Bryce", "1234", 710, 11, False)
Money12 = jsonutil.openJson("David", "1234", 710, 12, False)
Money13 = jsonutil.openJson("Ana", "1234", 710, 13, False)
Money14 = jsonutil.openJson("Danylo", "1234", 710, 14, True)
Money15 = jsonutil.openJson("Acacia", "1234", 710, 15, True)
Money16 = jsonutil.openJson("Finlay", "1234", 710, 16, False)
Money17 = jsonutil.openJson("Ben", "1234", 710, 17, False)
Money18 = jsonutil.openJson("Abraham", "1234", 710, 18, False)
Money19 = jsonutil.openJson("NULL", "1234", 710, 19, False)
Money20 = jsonutil.openJson("Makaylah", "1234", 710, 20, False)
Money21 = jsonutil.openJson("Emilia", "1234", 710, 21, False)
Money22 = jsonutil.openJson("Olivia", "1234", 710, 22, False)
Money23 = jsonutil.openJson("Lucas", "1234", 710, 23, False)
Money24 = jsonutil.openJson("Ishleen", "1234", 710, 24, False)
Money25 = jsonutil.openJson("Becky", "1234", 710, 25, True)
Money26 = jsonutil.openJson("Samuel", "1234", 710, 26, False)
Money27 = jsonutil.openJson("NULL", "1234", 710, 27, False)
Money28 = jsonutil.openJson("NULL", "1234", 710, 28, False)
Money29 = jsonutil.openJson("NULL", "1234", 710, 29, False)
Money30 = jsonutil.openJson("NULL", "1234", 710, 30, False)

def choice(account):
  passWord = input('What is the password? ')
  if passWord == account["password"]:
    print('Access Granted!')
    print("Name: " + account["name"]);
    print("Balance: " + account["balance"]);
  else:
    print('Wrong! Access Denied!')

while True:
        Choice2 = input("Which student ID number do you want to view? ")
        while Choice2 != '1' and Choice2 != '2' and Choice2 != '3' and Choice2 != '4' and Choice2 != '5' and Choice2 != '6' and Choice2 != '7' and\
        Choice2 != '8' and Choice2 != '9' and Choice2 != '10' and Choice2 != '11' and Choice2 != '12' and Choice2 != '13' and Choice2 != '14' and\
        Choice2 != '15' and Choice2 != '16' and Choice2 != '17' and Choice2 != '18' and Choice2 != '19' and Choice2 != '20' and Choice2 != '21' and\
        Choice2 != '22' and Choice2 != '23' and Choice2 != '24' and Choice2 != '25' and Choice2 != '26' and Choice2 != '27' and\
        Choice2 != '28' and Choice2 != '29' and Choice2 != '30':
            Choice2 = input("Not a valid ID, please try again: ")
        if Choice2 == '1':
          choice(Money1);
        elif Choice2 == '2':
          choice(Money2);
        elif Choice2 == '3':
          choice(Money3);
        elif Choice2 == '4':
          choice(Money4);
        elif Choice2 == '5':
          choice(Money5);
        elif Choice2 == '6':
          choice(Money6);
        elif Choice2 == '7':
          choice(Money7);
        elif Choice2 == '8':
          choice(Money8);
        elif Choice2 == '9':
          choice(Money9);
        elif Choice2 == '10':
          choice(Money10);
        elif Choice2 == '11':
          choice(Money11);
        elif Choice2 == '12':
          choice(Money12);
        elif Choice2 == '13':
         choice(Money13);
        elif Choice2 == '14':
          choice(Money4);
        elif Choice2 == '15':
          choice(Money15);
        elif Choice2 == '16':
          choice(Money16);
        elif Choice2 == '17':
          choice(Money17);
        elif Choice2 == '18':
          choice(Money18);
        elif Choice2 == '19':
          choice(Money19);
        elif Choice2 == '20':
          choice(Money20);
        elif Choice2 == '21':
          choice(Money21);
        elif Choice2 == '22':
          choice(Money22);
        elif Choice2 == '23':
          choice(Money23);
        elif Choice2 == '24':
          choice(Money24);
        elif Choice2 == '25':
          choice(Money25);
        elif Choice2 == '26':
          choice(Money26);
        elif Choice2 == '27':
          choice(Money27);
        elif Choice2 == '28':
          choice(Money28);
        elif Choice2 == '29':
          choice(Money29);
        elif Choice2 == '30':
          choice(Money30);