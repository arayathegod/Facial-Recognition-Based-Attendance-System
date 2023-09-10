#pip install cmake
#pip install face_recognition
#pip install opencv-python
import face_recognition
import cv2
import csv
import numpy as np
from datetime import datetime


video_capture=cv2.VideoCapture(0) #capturing video using opencv

#Load known faces
appi_image=face_recognition.load_image_file('faces/appi.jpg')
sumit_image=face_recognition.load_image_file('faces/sumit.jpg')
otp_image=face_recognition.load_image_file('faces/otp.jpg')

#Encoding images- converting images to number so its easier to compare them
appi_encoding=face_recognition.face_encodings(appi_image)[0] #returns array of encodings of all faces in image (we need for first image)
sumit_encoding=face_recognition.face_encodings(sumit_image)[0]
otp_encoding=face_recognition.face_encodings(otp_image)[0]

known_face_encodings=[appi_encoding, sumit_encoding, otp_encoding]
known_face_names=["Appi","Sumit","Otp"]

#List of Students
students=known_face_names.copy()

face_locations=[]
face_encodings=[]

#Get the current date and time
now=datetime.now()
current_date=now.strftime("%D-%m-%y")

# Replace slashes with underscores in the formatted date
formatted_date = current_date.replace("/", "-")

#Creating csv writer

# Create the filename for the CSV
csv_filename = f"{formatted_date}.csv"

# Open the CSV file
f = open(csv_filename, "w+", newline="")
#f=open(f"{current_date}.csv", "w+",newline="")
lnwriter=csv.writer(f)

while True:
    _,frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    #Recognise faces
    face_locations=face_recognition.face_locations(rgb_small_frame)
    face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)

    for face_encoding in face_encodings:
        matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance=face_recognition.face_distance(known_face_encodings,face_encoding) #determines how similar current face is to known faces

        best_match_index=np.argmin(face_distance)

        if(matches[best_match_index]):
            name=known_face_names[best_match_index]

        #Add the text if a person is present
        if name in known_face_names:
            font=cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText=(10,100)
            fontScale=1.5
            fontColor=(255,0,0)
            thickness=3
            lineType=2
            cv2.putText(frame,name+" Present",bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)

            if name in students:
                students.remove(name) #No longer expect student as they are already present
                current_time=now.strftime("%H-%M-%S")
                lnwriter.writerow([name,current_time])

    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()






