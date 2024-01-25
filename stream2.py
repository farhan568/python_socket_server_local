import socket
import cv2
import numpy as np
# Assuming you have a function to capture frames from a video source
def capture_frame():
    # Implement your frame capture logic here
    # Example using OpenCV to capture frames from a camera
    cap = cv2.VideoCapture("rtsp://admin:123456@streaming.deutics.live:61932/stream0?")
    ret, frame = cap.read()
    cap.release()
    return frame
def send_frame(client_socket, frame):
    # Convert the frame to an 8-bit array
    frame_bytes = frame.tobytes()
    # Send the frame size first
    frame_size = len(frame_bytes)
    print(frame_size)
    print(frame_bytes)
    client_socket.sendall(frame_size.to_bytes(4, 'big'))
    # Send the frame data
    client_socket.sendall(frame_bytes)
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Port = 5000
    maxConnections = 999
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    print("Server started at " + IP + " on port " + str(Port))
    server_socket.bind(('0.0.0.0', Port))
    server_socket.listen(1)
    
    print("Waiting for a connection...")
    client_socket, address = server_socket.accept()
    print("Connected to", address)
    try:
        while True:
            frame = capture_frame()
            send_frame(client_socket, frame)
    except KeyboardInterrupt:
        print("Server interrupted")
    client_socket.close()
    server_socket.close()
if __name__ == "__main__":
    main()