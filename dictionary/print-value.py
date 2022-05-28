# sample dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#get values
x = thisdict["model"]
print ("The value of the key=model is:",x)

y = thisdict.get("model")

print ("The value of the key=model is:",y)

k = thisdict.keys()
print(k)

item = thisdict.items()
print(item)