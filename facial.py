import cv2

video = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier("recursos/haarcascade_frontalface_default.xml")

while True:
    conectado, frame = video.read()
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    deteccoes = classificador.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=9, minSize=(60,60))

    for(x, y, l, a) in deteccoes:
        cv2.rectangle(frame, (x,y), (x+l, y+a), (0,255,0), 2)

    cv2.imshow("WebCam Facial Recognition", frame)

    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()