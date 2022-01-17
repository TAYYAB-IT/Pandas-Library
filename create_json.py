import json as js
data={
    'Student':{
      'Tayyab':1,
      'Qasim':2,
      'Ali':  3,
    },
    'Grade':{
      'Tayyab':89,
      'Qasim':76,
      'Ali': 43,
    }
}
x=open("file.json",'w')
data=js.dumps(data) #convert to json
print(data)
x.write(data)
x.close()