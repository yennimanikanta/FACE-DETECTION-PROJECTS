import cv2
import mediapipe as mp

class FaceDetection:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.7)
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_faces(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.mp_face_detection.process(img_rgb)
        img_with_detections = img.copy()
        if results.detections:
            for detection in results.detections:
                self.mp_drawing.draw_detection(img_with_detections, detection)
        return img_with_detections

    def process_webcam(self):
        webcam = cv2.VideoCapture(0)
        while webcam.isOpened():
            success, img = webcam.read()
            if not success:
                break

            img_with_faces = self.detect_faces(img)

            cv2.imshow("MANIKANTA_FACE", img_with_faces)
            if cv2.waitKey(5) & 0xFF == ord("q"):
                break

        webcam.release()
        cv2.destroyAllWindows()

# If this script is run directly, it will execute face detection
if __name__ == "__main__":
    face_detector = FaceDete
ction()
    face_detector.process_webcam()

