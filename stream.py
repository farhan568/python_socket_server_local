# import cv2
# import base64
# import numpy as np
# import socket
# import json

# file_number = 1

# cap = cv2.VideoCapture("rtsp://admin:123456@streaming.deutics.live:65136/stream0")

# # #Defines Server Values
# listensocket = socket.socket()
# Port = 5000
# maxConnections = 999
# hostname = socket.gethostname()
# ## getting the IP address using socket.gethostbyname() method
# IP = socket.gethostbyname(hostname)
# listensocket.bind(('',Port))

# #Opens Server
# listensocket.listen(maxConnections)
# print("Server started at " + IP + " on port " + str(Port))

# #Accepts Incomming Connection
# (clientsocket, address) = listensocket.accept()
# print("New connection made!")



# # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # server_socket.bind(('127.0.0.1', 8888))
# # print("sds")
# # server_socket.listen(1)
# # client_socket, client_address = server_socket.accept()
# # print("Connected to", client_address)





# while True:
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, (720, 480))
#     # Convert the 3D NumPy array to a 1D array
#     _, img_encoded = cv2.imencode('.jpg', frame)
#     flat_array = img_encoded.flatten()
#     # Convert the values to uint8 and create a list
#     uint8_list = flat_array.astype(np.uint8).tolist()
#     json_data = json.dumps(uint8_list)
   
#     clientsocket.sendall(json_data.encode('utf-8'))
#     # client_socket.sendall(json_data.encode('utf-8'))
#     print(flat_array)



import cv2
import base64
import numpy as np
import socket
import pickle
import json
file_number = 1
cap = cv2.VideoCapture("rtsp://admin:123456@streaming.deutics.live:65136/stream0")
# Defines Server Values
listensocket = socket.socket()
Port = 5000
maxConnections = 999
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
listensocket.bind(('', Port))
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))
(clientsocket, address) = listensocket.accept()
print("New connection made!")

ret, frame = cap.read()
frame = cv2.resize(frame, (720, 480))
_, img_encoded = cv2.imencode('.jpg', frame)
flat_array = img_encoded.flatten()
uint8_list = flat_array.astype(np.uint8).tolist()
serialized_data = json.dumps(uint8_list)
# serialized_data = pickle.dumps(uint8_list)
print(serialized_data.encode())
print("---------------")
# print(serialized_data)

# Send the length of the data first
    # length_prefix = str(len(json_data)).ljust(10).encode('utf-8')  # Encode the length prefix
    # clientsocket.sendall(length_prefix)
    # Send the JSON-encoded data
clientsocket.send(serialized_data.encode())
print("Sent frame data")
file_name = "frame.txt"

with open(file_name, 'w') as file:
    file.write(str(uint8_list))
file.close()
    # # Send the length of the data first
    # length_prefix = str(len(json_data)).ljust(10)  # Use fixed-length 10 characters for length
    # clientsocket.sendall(length_prefix.encode('utf-8'))
    # # Send the JSON-encoded data
    # clientsocket.sendall(json_data.encode('utf-8'))
    # print("Sent frame data")
    # If needed, add a delay to control the frame rate
    # cv2.waitKey(50)  # 50 milliseconds delay

    