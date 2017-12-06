from numpy import *
class ass3_determin:
    # X should be a row matrix 
    def cal_energy(self,weight, X):
        theta=weight[-1,0:-1]
        matrix_X = X.T*X

        W = weight[0:-1,0:-1]

        energy = sum(multiply(W,matrix_X))\
        +sum(multiply(theta,X))
        return energy

    def determin_rec(self,init):
        weight_mat = zeros((6,6))
        for weight in init:
            xs =  mat(weight)
            coeff =xs.T*xs
            weight_mat += coeff
        # initialize value of vector X
         #change all the values on the diagonal to 0
        for i in range(shape(weight_mat)[0]):
            weight_mat[-1,i] *= 2
            weight_mat[-1,i] += weight_mat[i,i]
            weight_mat[i,i] = 0
        print(weight_mat)
        X = mat([0,0,0,0,0])
        #keep updating until energy reaches minimum
        change = True
        import random
        # disorganize the the order of the updating
        order = list(range(0,shape(X)[1]))
        random.shuffle(order)
        while change == True:
            change = False
            for i in order:
                update_X = X.copy()
                update_X[0,i] = 1 if update_X[0,i] == 0 else 0
                diff_energy = self.cal_energy(weight_mat,update_X)-self.cal_energy(weight_mat,X)
                if (diff_energy <= 0):
                    X = update_X
                    change = True
            if (change == False):
                break
        print(self.cal_energy(weight_mat,mat([1,0,0,1,1]))) #-19
        print(self.cal_energy(weight_mat,mat([0,0,0,1,0]))) #-15
        print(self.cal_energy(weight_mat,mat([0,0,1,1,1]))) #-15

        print("The final result of the function should be: ")
        print(X[:])

if __name__ == "__main__":
        # set the array of X, the first value should be
        # the input unchangeable value
        ass3_determin().determin_rec([[1,-2,1,2,-1,-2],[-1,1,1,-1,-1,3],[2,1,-1,-2,-2,2], [1,2,-1,-1,-1,1],[-1,-1,1,1,1,-1]])


