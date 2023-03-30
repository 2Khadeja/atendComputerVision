
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseU'
    'RL':"https://faceatendence-default-rtdb.firebaseio.com/"
})
ref = db.reference('students')
data = {
    "963852":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "345621":
        {
            "name": "Mohammed al-shably",
            "major": "IA",
            "starting_year": 2021,
            "total_attendance": 5,
            "standing": "E",
            "year": 3,
            "last_attendance_time": "2022-2-11 00:54:34"
        },
    "852741":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}
for key, value in data.items():
    ref.child(key).set(value)