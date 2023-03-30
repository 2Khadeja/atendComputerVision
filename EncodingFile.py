import cv2
import os
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceatendence-default-rtdb.firebaseio.com/",
    'storageBucket': "faceatendence.appspot.com"
})

# loaded students  images into a list
folderPath = 'images'
print(folderPath)
PathList = os.listdir(folderPath)
imgList = []
studentId = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentId.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    # print(path)
    # os.path.splitext(path[0])
print(studentId)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print(' Encoding Started ')
encodListKnown = findEncodings(imgList)
encodListKnownWithIds = [encodListKnown, studentId]
print('Encoding Complete')
# Generated File.
file = open("encodeFile.p", 'wb')
pickle.dump(encodListKnownWithIds, file)
file.close()
print('file save')




