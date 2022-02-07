import numpy as np
import gc

minimum = 0
x_p = [] 
p_p = [] 

def wig_func(eta, x, p):
    global minimum, x_p, p_p

    c_1 = 67 * np.pi

    i_1 = x**2
    i_2 = x**4
    i_3 = p**2
    i_4 = p**4
    
    c_2 = np.exp(-2 * (i_1 + i_3))

    i_5 = eta**2
    i_6 = eta**3
    i_7 = np.sqrt(2)
    i_8 = 292 * eta
    i_9 = 96 * i_7 * eta
    i_10 = 144 * i_5
    i_11 = 192 * i_7 * i_5
    i_12 = 144 * i_6
    i_13 = 72 * i_5
    i_14 = 128 * i_7 * i_5
    i_15 = 32 * i_6
    i_16 = 96 * i_6

    w_1 = 67 - 146 * eta + 36 * i_5 - 24 * i_6
    w_2 = (i_8 + i_9 - i_10 - i_11 + i_12) * i_1
    w_3 = (i_8 - i_9 - i_10 + i_11 + i_12) * i_3
    w_4 = (i_13 + i_14 - i_12) * i_2
    w_5 = (i_13 - i_14 - i_12) * i_4
    w_6 = (i_10 - 2 * i_12) * i_1 * i_3
    w_7 = i_15 * (x**6 + p**6)
    w_8 = i_16 * (i_2 * i_3 + i_1 * i_4)

    # rslt is ndarray
    rslt = (2 * c_2 * (w_1 + w_2 + w_3 + w_4 + w_5 + w_6 + w_7 + w_8)) / c_1

    minimum = np.amin(rslt) 
    min_point_list = list(zip(*np.where(rslt.flatten() == minimum)))
    for i in min_point_list:
        x_p.append(x.flatten()[i[0]])
        p_p.append(p.flatten()[i[0]])

    return rslt

x = np.arange(-5.0, 5.0, 0.005)
p = np.arange(-5.0, 5.0, 0.005)
X, P = np.meshgrid(x, p)

eta = 1
while eta > 0 and eta < 1000:
    # print("eta : " + str(eta), file=sys.stderr)
    float_eta = eta / 1000
    Z = wig_func(float_eta, X, P)

    eta += 1

    print(("min : " +  str(minimum) + "(eta : " + str(float_eta) + ") with \nx : " + str(x_p) +  "\n p : " + str(p_p) + '\n'))

    x_p = []
    p_p = []
    minimum = 0

    del Z
    gc.collect