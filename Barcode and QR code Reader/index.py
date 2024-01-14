import cv2
from pyzbar.pyzbar import decode

def read_qr_code():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        decoded_objects = decode(frame)
        
        for obj in decoded_objects:
            points = obj.polygon
            if len(points) == 4:
                hull = cv2.convexHull(points)
                cv2.polylines(frame, [hull], True, (0, 255, 0), 2)

            qr_data = obj.data.decode("utf-8")
            print("QR Code Data:", qr_data)

        cv2.imshow("QR Code Reader", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    read_qr_code()
