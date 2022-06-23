import pymongo
conn = pymongo.MongoClient('mongodb://admin:password@mongodb')

dblist = conn.list_database_names()
mydb = False
mycol = False
if "chatbot" in dblist:
  print("The database exists.")
  mydb = conn["chatbot"]
  mycol = mydb["users"]
else:
  mydb = conn["chatbot"]
  mycol = mydb["users"]
  mydict = { "username": "nouman", "password": "nouman" }
  mycol.insert_one(mydict)


def validate_user(user, password):
  print("validate_user")
  myquery = { "username": user, "password" : password }
  mydoc = mycol.count_documents(myquery)
  if (mydoc):
    return True
  else:
    return False


#print(validate_user("nouman", "nouman2"))
