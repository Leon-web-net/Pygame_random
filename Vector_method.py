import numpy
import numpy as np
import math , random, time
def d_collision(c1x,c1y,c2x,c2y,v1x,v1y,v2x,v2y):
    # Initial Velocity

    v1 = [v1x, v1y]
    v1 = np.array(v1)

    v2 = [v2x, v2y]
    v2 = np.array(v2)

    # centre
    c1 = [c1x, c1y]
    c1 = np.array(c1)

    c2 = [c2x, c2y]
    c2 = np.array(c2)

    # final

    top_v1 = np.dot(v1-v2, c1-c2)
    bottom_v1 = pow(np.linalg.norm(c1-c2),2)
    v_1 = v1 - ((top_v1)/(bottom_v1) * (c1-c2))
    print(f"player velocityt: {v_1}")
    v_1x = v_1[0]
    v_1y = v_1[1]

    top_v2 = np.dot(v2-v1, c2-c1)
    bottom_v2 = pow(np.linalg.norm(c2-c1),2)
    v_2 = v2 - ((top_v2)/(bottom_v2) * (c2-c1))
    print(f"Blue ball velocity: {v_2}")

    v_2x = v_2[0]
    v_2y = v_2[1]

    return v_1x, v_1y , v_2x, v_2y