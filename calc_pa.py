import numpy as np

def cmp_pa(a, eta):
    pa_1 = 1 - eta
    pa_2 = (64 * eta + 9 * eta * pa_1**2) - a * (9 * eta**2 * pa_1 + 3 * eta**3)
    pa = pa_2 / 67

    pam_1 = np.sqrt(9 + 8 * a)
    pam_2 = np.sqrt(3 + 4 * a * (3 + 2 * a) + pam_1)
    pam_3 = np.exp(2 / (1 - pam_1))
    pam_4 = 3 + 4 * a + pam_1
    pam = (pam_2 * pam_3 * pam_4) / (8 * np.sqrt(2) * (1 + a)) - a

    # print(str(a) + ', ' + str(pa) + ', ' + str(pam))
    if pa > pam :
       print("eta : " + str(eta) + " / a : " + str(a))
    
eta = 1
a = -999
while eta < 1000:
    float_eta = eta / 1000
    while a < 25000:
        cmp_pa(a/1000, float_eta)
        a += 1

    a = -999
    eta += 1