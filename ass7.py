from numpy import *
import math
class ass7:
    RAND_MAX = 2**31-1
    alpha = 0.2
    # X should be a row matrix 
    def cal_energy(self, weight, theta, X):
        matrix_X = mat(X)
        matrix_X = matrix_X.T*matrix_X
        for i in range(3):
            matrix_X[i,i] = 0
        energy = sum(multiply(weight,matrix_X))\
        +sum(multiply(theta,X))
        return energy

    def gen_weight(self):
        state = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
        value = [0.25,0,0,0.25,0,0.25,0,0.25]
        weights = array([0,0,0])
        q = [0] * 3
        for z in range(8):
            q[0]+= state[z][0] * state[z][1]*value[z]
            q[1]+= state[z][0] * state[z][2]*value[z]
            q[2]+= state[z][1] * state[z][2]*value[z]
        theta = [1,1,1]
        while True:
            gradient = array([0]*3)
            for m in range(3):
                p = [0] * 3
                X = [0,0,0]
                for num in range(1000):
                    for i in range(3):
                        weight_copy = weights.copy()
                        cancel = 2-i
                        weight_copy[cancel] = 0
                        S = sum(multiply(X,weight_copy))+sum(multiply(X,theta))
                        P = 1/(1+exp(-self.alpha*S*1))
                        rand_num = random.uniform(0,self.RAND_MAX)
                        if(rand_num>self.RAND_MAX*P):
                            X[i] = 0
                        else:
                            X[i] = 1

                    if(X[0]*X[1] == 1): p[0] += 1/1000
                    if(X[0]*X[2] == 1): p[1] += 1/1000
                    if(X[1]*X[2] == 1): p[2] += 1/1000
                    gradient[m] = 100 * self.alpha * (p[m] - q[m])
            weights = weights - gradient
            G = 0
            for i in range(3):
                 G += q[i] * abs(math.log((q[i])/(p[i])))
            print(G)
            if(G < 0.05):
                break
        print("The final weights are : ",weights)


if __name__ == "__main__":
        ass7().gen_weight()

