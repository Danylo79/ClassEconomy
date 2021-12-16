import main
import json
import os.path

def openJson(name, password, homeroom, studentId, isComittee):
  if (not name == "NULL"):
    file = "data/" + str(homeroom) + "/" + name + "-" + str(homeroom) + "-" + str(studentId) + ".json";

    if (not os.path.isfile(file)):
      makeJson(file, name, password, homeroom, studentId, isComittee);

    with open(file) as readfile:
      out = json.load(readfile)
      main.debug("Loading: " + out["name"]);
      main.debug("Full Json: " + json.dumps(out));
      main.debug(" ")
      return out
  else:
    main.debug("Skipping null user (" + str(homeroom) + "-" + str(studentId) + ")")
  main.debug(" ")


def makeJson(file, name, password, homeroom, studentId, isComittee):
  data = {
    "name": name,
    "password": password,
    "homeroom": homeroom,
    "studentId": studentId,
    "balance": 0,
    "isComittee": isComittee,
    "jobs": []
    }

  with open(file, "w+") as outfile:
    json.dump(data, outfile)