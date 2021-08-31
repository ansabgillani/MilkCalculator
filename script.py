import numpy as np
import scipy
import scipy.linalg as lg
import scipy.optimize as op


def run(fat, protein, sugar):
    response = dict()
    t = np.array([fat, protein, sugar, 1])

    dat = np.array([3.6, 1.7, 0.3, 5.4, 2.55, 0.45,
                    3.4, 3.8, 3.6, 5.1, 5.7, 5.4,
                    4.7, 4.6, 4.9, 7.05, 6.9, 7.35,
                    1, 1, 1, 1, 1, 1, ])
    dat = dat.reshape(4, 6)

    sol, resid, rank, s = lg.lstsq(dat, t)
    N = lg.null_space(dat)
    N1, N2 = N[:, 0], N[:, 1]

    c1 = np.arange(-3, 3, 0.01)
    c2 = np.arange(-3, 3, 0.01)
    c1, c2 = np.meshgrid(c1, c2)

    Z = np.zeros(c1.shape)
    for i in range(len(c1)):
        for j in range(len(c2)):
            Z[i][j] = np.min(sol + c1[0][i] * N1 + c2[j][0] * N2)

    # print('max(Z)',np.max(Z))

    if np.max(Z) > -0.01:
        response['header_message'] = 'You can make that'
        response['follow_up_message'] = 'Here is the recipe'
    else:
        response['header_message'] = 'You cannot make that'
        response['follow_up_message'] = 'Here is the closest thing you can get with your ingredients'

    bobby = op.nnls(dat, t)
    bob = bobby[0]
    bob = bob / np.sum(bob)

    res = np.dot(dat, bob)

    response['whole'] = round(100 * bob[0])
    response['semi'] = round(100 * bob[1])
    response['skimmed'] = round(100 * bob[2])
    response['fd_whole'] = round(100 * bob[3])
    response['fd_semi'] = round(100 * bob[4])
    response['fd_skimmed'] = round(100 * bob[5])

    response['fat'] = round(res[0], 1)
    response['protein'] = round(res[1], 1)
    response['sugar'] = round(res[2], 1)

    return response