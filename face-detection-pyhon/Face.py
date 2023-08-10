import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
solution_face = mp.solutions.face_detection
face_detection = solution_face.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    verification, frame = webcam.read()
    if not verification:
        break
    face_List = face_detection.process(frame)
    if face_List.detections:  # Corrigir "detection" para "detections"
        for rosto in face_List.detections:  # Corrigir "detection" para "detections"
            desenho.draw_detection(frame, rosto)
    cv2.imshow('Face', frame)
    if cv2.waitKey(5) == ord('s'):
        cv2.imwrite('Face.jpg',str (frame))
        #mostra o caminho da imagem salva
        print('Imagem Salva' + 'Face.jpg')
        
        break

webcam.release()
cv2.destroyAllWindows()
