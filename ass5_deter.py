from numpy import *
class ass5_deter:
    MAX = 2**31-1
    alpha = 0.5
    dic={}

    def cal_energy(self,weight,theta, X):
        energy = 0
        for x in range(16):
            for y in range(16):
                i = int(x/4)
                j = int(y/4)
                n = x%4
                m = y%4  
                energy += -weight[x,y]*X[i,j]*X[n,m]
        energy += sum(multiply(theta,X))
        return energy

    def single_energy(self,X):
        energy = 0
        for i in range(shape(X)[1]):
            row = X[i,:]
            energy += (sum(row)-1)**2
        for i in range(shape(X)[0]):
            col = X[:,i]
            energy += (sum(col)-1)**2
        return energy

    def deter(self):
        
        A = 1/90
        weight_mat = mat(zeros((16,16)))
        theta = mat(zeros((4,4)))
        # weight
        for x in range(16):
            for y in range(16):
                i = int(x/4)
                j = int(y/4)
                n = x%4
                m = y%4
                alpha1 = mat(zeros((4,4)))
                alpha2 = mat(zeros((4,4)))
                beta = mat(zeros((4,4)))
                alpha1[i,j] = 1
                alpha2[n,m] = 1
                beta[i,j] = 1;beta[n,m] = 1
                if(i==n and j==m):
                    weight_mat[x,y] = 0
                else:
                    weight_mat[x,y] = self.single_energy(alpha1)+self.single_energy(alpha2)-self.single_energy(beta)-8
        # theta
        for x in range(4):
            for y in range(4):
                zero_mat = mat(zeros((4,4)))
                nonzero_mat = mat(zeros((4,4)))
                nonzero_mat[x,y] = 1
                theta[x,y] = self.single_energy(nonzero_mat)-self.single_energy(zero_mat)
        X =mat(zeros((4,4)))
        X[0,0] = 1
        X[1,1] = 1
        X[1,2] = 1
        X[2,2] = 1
        X[3,3] = 1
        
        import random
        change = True
        # disorganize the the order of the updating
        order = list(range(0,16))
        random.shuffle(order)
        while change == True:
            change = False
            for index in order:
                update_X = X.copy()
                update_X[int(index/4),index%4] = 1 if update_X[int(index/4),index%4] == 0 else 0
                diff_energy = self.cal_energy(weight_mat,theta,update_X)-self.cal_energy(weight_mat,theta,X)
                if (diff_energy <= 0):
                    X = update_X
                    change = True
                if(change == False):
                    break
                
        print("The final result of the function should be: ")
        print(X[:])
        
if __name__ == "__main__":
        ass5_deter().deter()
        

