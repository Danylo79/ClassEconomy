import json
import os.path;

level = input('Are you viewing (v) or editing (e)? ')
Class = input('Which class do you want to view? ')

while Class != '7-03' and Class != '7-07' and Class != '7-10' and Class != '7-11' and Class != '7-12' and Class != '703' and Class != '707' and Class != '710' and Class != '711' and Class != '712':
  Class = input('Not a valid class, please try again: ')

if level == 'e':
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
elif level == 'v':
  if Class == '7-03' or Class == '703':
    import viewthree
  elif Class == '7-07' or Class == '707':
    import viewseven
  elif Class == '7-10' or Class == '710':
    import viewten
  elif Class == '7-11' or Class == '711':
    import vieweleven
  elif Class == '7-12' or Class == '712':
    import viewtwelve

def openJson(folder, name, homeroom, studentId):
  file = os.path.join(folder, name + "-" + str(homeroom) + "-" + str(studentId) + ".json");

  if (not os.path.isfile(file)):
    makeJson(file, folder, name, homeroom, studentId);

  with open(file) as readfile:
    out = json.load(readfile)
    print("Loading: " + out["name"]);
    print("Full Json: " + json.dumps(out));
    return out


def makeJson(file, name, homeroom, studentId, isComittee):
  data = {
    "name": name,
    "homeroom": homeroom,
    "studentId": studentId,
    "balance": 0,
    "jobs": [],
    "isComittee": isComittee
    }

  jstr = json.dumps(data);

  with open(file, "w+") as outfile:
    json.dump(jstr, outfile)