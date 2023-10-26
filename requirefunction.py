# Function to use
import math


def get_angle(opp_distance, adj_distance1, adj_distance2):
    numerator = ((adj_distance1) ** 2) + ((adj_distance2) ** 2) - ((opp_distance) ** 2)
    denominator = 2 * (adj_distance1) * (adj_distance2)
    if (denominator != 0 ):
        cos_e = numerator / denominator
        if (-1<=cos_e<= 1):
            radian_e = math.acos(cos_e)
            degree_e = (180 / math.pi) * radian_e
            return degree_e
        else:
            print(f'cos_e value is {cos_e}')
            return None
    else:
        print(f'side value si {adj_distance1,adj_distance2}')
        return None





def calculate_distanace(point1, point2):
    x1, y1 = int(point1[0]), int(point1[1])
    x2, y2 = int(point2[0]), int(point2[1])

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def getText(checkvar,side):

    if checkvar is None:
        return f'{side} angle is {(checkvar)} deg'
    else:
        return f'{side} angle is {int(checkvar)} deg'




def occlusionHandling(keypoint,keypoint_list):
    if (keypoint == (0,0)):
        return keypoint_list[0]
    else:
        keypoint_list[0] = keypoint
        return keypoint