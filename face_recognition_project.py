import cv2
import face_recognition

# Get the images of known faces
names = []
images = []

# Load images and encodings
name1 = face_recognition.load_image_file(r"C:\Users\dhara\OneDrive\Desktop\face_detection\dharani.jpg")
name2 = face_recognition.load_image_file(r"C:\Users\dhara\OneDrive\Desktop\face_detection\elon.jpg")
name3 = face_recognition.load_image_file(r"C:\Users\dhara\OneDrive\Desktop\face_detection\indira.jpg")

name1_encoding = face_recognition.face_encodings(name1)[0]
name2_encoding = face_recognition.face_encodings(name2)[0]
name3_encoding = face_recognition.face_encodings(name3)[0]

names.append(name1_encoding)
names.append(name2_encoding)
names.append(name3_encoding)

images.append("Dharani")
images.append("Elon Musk")
images.append("Indira Gandhi")

# Open video capture
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    # Find face locations and encodings
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Iterate through faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare face encodings
        matches = face_recognition.compare_faces(names, face_encoding)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = images[first_match_index]

        # Draw rectangle and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Check for quit command
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
