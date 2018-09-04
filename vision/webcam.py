import cv2
import numpy as np
import ikpy
from ikpy import plot_utils
import matplotlib.pyplot as plt



my_chain = ikpy.chain.Chain.from_urdf_file("./poppy_ergo.URDF")
ax = plot_utils.init_3d_figure()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

aruco = cv2.aruco
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
aruco.drawMarker(aruco_dict, 2, 700)
print(aruco_dict)
# second parameter is id number
# last parameter is total image size

cameraMatrix = np.load("./calib_mtx.npy")
distCoeffs = np.load("./calib_dist.npy")
rvecs = np.load("./calib_rvecs.npy")
tvecs = np.load("./calib_tvecs.npy")
 
cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
 
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
 
    gray = aruco.drawDetectedMarkers(gray, corners)
 
    if len(corners) > 0:
        objectPoints = np.array([
            [-1,-1,1],
            [1,-1,1],
            [-1,1,1],
            [1,1,1]
        ])
        rvec,tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.05 , cameraMatrix, distCoeffs)
        target_vector = tvec[0][0]
        target_frame = np.eye(4)
        target_frame[:3, 3] = target_vector

        print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))
        ax.cla()
        my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)
        plt.xlim(-0.1, 0.1)
        plt.ylim(-0.1, 0.1)
        plt.pause(1.0/33)

