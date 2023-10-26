
### Posing estimation on photos

#import statement
from requirefunction import getText,get_angle,calculate_distanace,occlusionHandling
from ultralytics import YOLO
import cv2

#Loading The Model
model = YOLO('../yolov8n-pose.pt')

# Get the image path
img_path = ''


## Just read the image in array form
frame = cv2.imread(img_path)


width = frame.shape[1]

# Just get the keypoints from the image
results = model(source=frame)
keypoints = results[0].keypoints.xy[0].tolist()
print(type(keypoints))
print(keypoints)
left_keypoints = []
right_keypoints = []
left_shoulder_prev = [(0,0)]
left_elbow_prev = [(0,0)]
left_wrist_prev = [(0,0)]
right_shoulder_prev = [(0,0)]
right_elbow_prev = [(0,0)]
right_wrist_prev = [(0,0)]
i = 0


for keypoint in keypoints:

    cx = int(keypoint[0])
    cy = int(keypoint[1])
    ### Left side
    if (i == 5 or i == 7 or i == 9):  # blue for left
        cv2.circle(frame, (cx, cy), 6, (255, 0, 0), -1)
        left_keypoints.append((cx, cy))


    ### Right side
    elif (i == 6 or i == 8 or i == 10):  # green for right
        cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)
        right_keypoints.append((cx, cy))

    else:  # red for remaning
        cv2.circle(frame, (cx, cy), 6, (0, 0, 255), -1)

    i += 1

### Inner Operation

if (len(left_keypoints) != 0 and len(right_keypoints) != 0):

    left_shoulder = left_keypoints[0]
    left_shoulder = occlusionHandling(left_shoulder, left_shoulder_prev)


    left_elbow = left_keypoints[1]
    left_elbow = occlusionHandling(left_elbow, left_elbow_prev)


    left_wrist = left_keypoints[2]
    left_wrist = occlusionHandling(left_wrist, left_wrist_prev)


    right_shoulder = right_keypoints[0]
    right_shoulder = occlusionHandling(right_shoulder, right_shoulder_prev)


    right_elbow = right_keypoints[1]
    right_elbow = occlusionHandling(right_elbow, right_elbow_prev)


    right_wrist = right_keypoints[2]
    right_wrist = occlusionHandling(right_wrist, right_wrist_prev)


    left_se = int(calculate_distanace(left_shoulder, left_elbow))
    left_ew = int(calculate_distanace(left_elbow, left_wrist))
    left_sw = int(calculate_distanace(left_shoulder, left_wrist))


    ## Calculating the individual right side difference
    right_se = int(calculate_distanace(right_shoulder, right_elbow))
    right_ew = int(calculate_distanace(right_elbow, right_wrist))
    right_sw = int(calculate_distanace(right_shoulder, right_wrist))






    # Getting Left angle

    left_degree_e = get_angle(left_sw, left_se, left_ew)
    print(f'left_angle is {left_degree_e}')

    # Getting Right angle

    right_degree_e = get_angle(right_sw, right_se, right_ew)
    print(f'right_angle is {right_degree_e}')

    # Displaying message bar
    top_position = (int(width * 0.3), 0)
    down_position = (int(width * 1), 40)
    cv2.rectangle(frame, top_position, down_position, (255, 255, 255), -1)

    # Displaying the Left angle
    cv2.putText(frame, getText(left_degree_e,'left'), (int(width * 0.31), 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 0), 1)

    # Displaying the Right angle
    cv2.putText(frame, getText(right_degree_e,'right'), (int(width * 0.31), 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 1)

    ### Left Line
    cv2.line(frame, (int(left_shoulder[0]), int(left_shoulder[1])), (int(left_elbow[0]), int(left_elbow[1])),
                 (255, 0, 0), 3)
    cv2.line(frame, (int(left_elbow[0]), int(left_elbow[1])), (int(left_wrist[0]), int(left_wrist[1])), (255, 0, 0),
                 3)

    ### Right Line
    cv2.line(frame, (int(right_shoulder[0]), int(right_shoulder[1])), (int(right_elbow[0]), int(right_elbow[1])),
                 (0, 255, 0), 3)
    cv2.line(frame, (int(right_elbow[0]), int(right_elbow[1])), (int(right_wrist[0]), int(right_wrist[1])),(0, 255, 0), 3)

cv2.imshow("frame",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


