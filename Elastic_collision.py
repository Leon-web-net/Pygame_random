import math
import numpy as np
def d_collision(c1x,c1y,c2x,c2y,v1x,v1y,v2x,v2y):

    x_axis = [1, 0]

    v1 = [v1x, v1y]
    modulus_v1 = pow(v1[0]*v1[0]+v1[1]*v1[1], 0.5)
    v2 = [v2x, v2y]
    modulus_v2 = pow(v2[0]*v2[0]+v2[1]*v2[1], 0.5)
    Initial_KE_2 = modulus_v1*modulus_v1 + modulus_v2*modulus_v2


    c1 = [c1x, c1y]
    c2 = [c2x, c2y]
    d = [c1[0]-c2[0], c1[1]-c2[1]]
    modulus_d = pow(d[0]*d[0]+d[1]*d[1], 0.5)

    # Angle between velocity1 and Line of center:
    angle_cos1 = np.dot(v1, d)/(modulus_d*modulus_v1)
    angle_rad1 = np.arccos(angle_cos1)
    angle_deg1 = np.degrees(np.arccos(angle_cos1))


    # normal and tangents
    n = d
    t = [n[1], -n[0]]


    # decompose v1
    v1tangent = modulus_v1*np.sin(angle_rad1)
    v1normal = modulus_v1*angle_cos1


    # tangent to x,y
    # t_x_cos_angle = t[0]/(modulus_d)
    # t_y_sin_angle = np.cross(x_axis,t)/(modulus_d)
    # v1t_x = v1tangent*t_y_sin_angle
    # v1t_y = v1tangent*t_x_cos_angle

    # Angle between velocity2 and Line of center:
    angle_cos2 = np.dot(v2, d)/(modulus_d*modulus_v2)
    angle_rad2 = np.arccos(angle_cos2)
    angle_deg2 = np.degrees(np.arccos(angle_cos2))


    # decompose v2
    v2tangent = modulus_v2*np.sin(angle_rad2)
    v2normal = modulus_v2*angle_cos2
    # v2t_x = v2tangent*t_y_sin_angle
    # v2t_y = v2tangent*t_x_cos_angle

    print(v1normal, v2normal)


    # 1D collision v1 v2 simultaneous equations
    a = np.array([[1, -1], [1, 1]])
    b = np.array([-v1normal+v2normal, v1normal+v2normal])
    x = np.linalg.solve(a, b)
    v1A = x[0]
    v2A = x[1]


    # back to final velocity

    v1_F = pow(v1A*v1A + v1tangent*v1tangent, 0.5)
    v2_F = pow(v2A*v2A + v2tangent*v2tangent, 0.5)
    final_KE_2 = v1_F*v1_F + v2_F*v2_F     # check if KE is conserved

    print(Initial_KE_2, final_KE_2)

    vector_v1_f = np.array([v1normal*n[0]+v1tangent*t[0], (v1normal*n[1]+v1tangent*t[0])])
    vector_v2_f = np.array([v2normal*n[0]+v2tangent*t[0], (v2normal*-n[1]+v2tangent*-t[0])])

    vector1_total = pow((vector_v1_f[0]*vector_v1_f[0] + vector_v1_f[1]*vector_v1_f[1]),0.5)
    vector2_total = pow((vector_v2_f[0]*vector_v2_f[0] + vector_v2_f[1]*vector_v2_f[1]),0.5)

    v1x_f = vector_v1_f[0]/(vector1_total) * v1_F
    v1y_f = vector_v1_f[1]/(vector1_total) * v1_F

    v2x_f = vector_v2_f[0]/(vector2_total) * v2_F
    v2y_f = vector_v2_f[1]/(vector2_total) * v2_F
    print(v1x_f,v1y_f,v2x_f,v2y_f)
    return v1x_f,v1y_f,v2x_f,v2y_f

    # final velocity

