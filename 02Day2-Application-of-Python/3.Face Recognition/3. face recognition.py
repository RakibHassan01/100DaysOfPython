import cv2

# Load the Cascade File (Haar Cascade for face detection)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the Input Image
image = cv2.imread('1.png')
# image = cv2.imread('1.jpeg')

# Resize the Image
img = cv2.resize(image, None, fx=0.3, fy=0.3)

# Convert the image into grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the Output Image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
