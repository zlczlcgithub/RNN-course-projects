from numpy import *
class ass4:
    MAX = 2**31-1
    alpha = 1.0
    dic={}
    # X should be a row matrix 
    def cal_energy(self,weight, X):
        theta=weight[-1,0:-1]
        matrix_X = X.T*X

        W = weight[0:-1,0:-1]

        energy = sum(multiply(W,matrix_X))\
        +sum(multiply(theta,X))
        return energy

    def prob_rec(self,init):
        A = 1/185000000
        weight_mat = zeros((6,6))
        for weight in init:
            xs =  mat(weight)
            coeff =xs.T*xs
            weight_mat += coeff
         #change all the values on the diagonal to 0
        for i in range(shape(weight_mat)[0]):
            weight_mat[-1,i] *= 2
            weight_mat[-1,i] += weight_mat[i,i]
            weight_mat[i,i] = 0
        # initialize value of vector X
        X = mat([0,0,0,0,0])
        #keep updating 10000 times
        import random
        for num in range(10000):
            index = int(random.uniform(0,5))
            update_X = X.copy()
            update_X[0,index] = 1 if update_X[0,index] == 0 else 0
            diff_energy = -self.cal_energy(weight_mat,update_X)+self.cal_energy(weight_mat,X)
            # apply sigmoid function:
            prob = 1/(1+exp(self.alpha*diff_energy))
            rand_num = random.uniform(0,self.MAX)
            if (rand_num >= self.MAX*prob):
                    X = update_X
            x_list = X.tolist()[0]
            x_str = '{}{}{}{}{}'.format(x_list[0],x_list[1],x_list[2],x_list[3],x_list[4])
            tmp=self.dic.get(x_str,0)
            if tmp == 0:
                self.dic[x_str] = 1
            else:
                self.dic[x_str] += 1

        ideal = self.dic.copy()
        for i in self.dic:
            arr = list(i)
            for j in range(len(arr)):
                arr[j] = int(arr[j])
            ideal[i]= int(10000*A*exp(-self.alpha*self.cal_energy(weight_mat,mat(arr))))
            
        print("The final result of the function should be: ")
        print(self.dic)
        print(ideal)

if __name__ == "__main__":
        # set the coefficients of the equation set
        ass4().prob_rec([[1,-2,1,2,-1,-2],[-1,1,1,-1,-1,3],[2,1,-1,-2,-2,2], [1,2,-1,-1,-1,1],[-1,-1,1,1,1,-1]])


