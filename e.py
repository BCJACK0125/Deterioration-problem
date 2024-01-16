import numpy as np

def policy_iteration(n_dims):
    action = np.ones(n_dims)
    new_action = np.empty(n_dims)
    
    tot = 0
    while(True):
        tot += 1
        A = np.zeros((n_dims + 1, n_dims + 1))
        b = np.ones(n_dims + 1)
        A[-1][0] = 1
        b[-1] = 0
        for (i, a) in enumerate(action):
            fail_rate = 0.1 + i * 0.01
            if(a == 1):
                # v[i] + $phi = 1 * fail_rate + fail_rate * v[0] + (1 - fail_rate) * v[i + 1]
                A[i][i] = 1
                A[i][-1] = 1
                A[i][0] -= fail_rate
                if(fail_rate != 1):
                    A[i][i + 1] -= (1 - fail_rate)
                b[i] = 1 * fail_rate
            elif(a == 2):
                # v[i] + $phi = 0.6 + 1 * v[0]
                A[i][i] = 1
                A[i][-1] = 1
                A[i][0] -= 1
                b[i] = 0.6

        x = np.linalg.solve(A, b)

        for (i, a) in enumerate(action):
            fail_rate = 0.1 + i * 0.01
            new_action[i] = np.argmin([1 * fail_rate + fail_rate * x[0] + (1 - fail_rate) * x[i + 1], 0.6 + x[0]]) + 1     
        
        if(np.all(action == new_action)):
            break
        else:
            action = new_action

    print(x, action)
    return action

def value_iteration(n_dims):
    v_t = np.zeros(n_dims)
    v_T = np.zeros(n_dims)
    P1 = np.zeros((n_dims, n_dims))
    P2 = np.zeros((n_dims, n_dims))
    r1 = np.zeros(n_dims)
    r2 = np.zeros(n_dims)
    action = np.zeros(n_dims)
    ths = 1e-5
    tot = 0

    for i in range(n_dims):
        fail_rate = 0.1 + i * 0.01

        if(i != 90):
            P1[i][i + 1] = 1 - fail_rate 
        P1[i][0] = fail_rate
        P2[i][0] = 1

        r1[i] = 1 * fail_rate
        r2[i] = 0.6
    
    while(True):
        tot += 1
        v_T = np.minimum(r1 + np.matmul(P1, v_t), r2 + np.matmul(P2, v_t))
        action = np.logical_not(r1 + np.matmul(P1, v_t) < r2 + np.matmul(P2, v_t)) + 1

        if(np.abs(np.max(v_T - v_t) - np.min(v_T - v_t)) <= ths):
            break
        else:
            v_t = v_T

    print((v_T - v_t))
    print(action)
    return action


if __name__ == "__main__":
    n_dims = 91
    a1 = policy_iteration(n_dims)    
    a2 = value_iteration(n_dims)
    assert np.all(a1 == a2)
