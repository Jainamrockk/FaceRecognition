import requests
import pyrebase
import urllib
from retinaface import RetinaFace
from deepface import DeepFace
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/verify/")
def verify_image(url1):
    firebaseConfig = {
      "apiKey": "AIzaSyClnRJAnrJgAgkYjuYnlvu-CJ6Cxyklebo",
      "authDomain": "socioverse-2025.firebaseapp.com",
      "projectId": "socioverse-2025",
      "storageBucket": "socioverse-2025.appspot.com",
      "messagingSenderId": "689574504641",
      "appId": "1:689574504641:web:a22f6a2fa343e4221acc40",
      "databaseURL": "https://console.firebase.google.com/project/socioverse-2025/storage/socioverse-2025.appspot.com/files",
      "serviceAccount":"Firebase_Service_Account_Keys.json"
    };
    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()
    path = "Faces/"
    files = storage.bucket.list_blobs(prefix=path)
    flag = False
    # url1 = "https://api.time.com/wp-content/uploads/2023/04/shah-rukh-khan-time100-2023-1.jpg"
    for file in files:
      if file.name.endswith(".jpg"):
        # print(file.name)
        url = storage.child(f"{file.name}").get_url(None)
        # print(url)
        with requests.get(url) as response:
          result = DeepFace.verify(f"{url1}",url, model_name="Facenet", distance_metric='cosine')
          if result['verified']:
            flag = True
            start_index = file.name.rfind('/')
            end_index = file.name.rfind('$')
            if start_index != -1 and end_index != -1:
              name = file.name[start_index + 1:end_index]
              return {"username": name}
              break

    if flag == False:
      print("Not Verified")
      return {"username": "Not Found"}



