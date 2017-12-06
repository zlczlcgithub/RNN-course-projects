from numpy import *
class ass6:
    MAX = 2**31-1
    alpha = 2
    dic={}

    def cal_energy(self,weight,theta, X):
        energy = 0
        for x in range(16):
            for y in range(16):
                i = int(x/4)
                j = x%4
                n = int(y/4)
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

    def prob_rec(self):
        
        A = 1/90
        distance = mat([[0,2,6,5],
                        [2,0,4,4],
                        [6,4,0,2],
                        [5,4,2,0]])
        weight_mat = mat(zeros((16,16)))
        theta = mat(zeros((4,4)))
        # weight
        for x in range(16):
            for y in range(16):
                i = int(x/4)
                j = x%4
                n = int(y/4)
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
                    if(m + 1 == (j + 1) % 4 + 1):
                        weight_mat[x,y] = -0.06*distance[i,n] + self.single_energy(alpha1)+self.single_energy(alpha2)-self.single_energy(beta)-8
                    else:
                        weight_mat[x,y] = self.single_energy(alpha1)+self.single_energy(alpha2)-self.single_energy(beta)-8

        # theta
        for x in range(4):
            for y in range(4):
                zero_mat = mat(zeros((4,4)))
                nonzero_mat = mat(zeros((4,4)))
                nonzero_mat[x,y] = 1
                theta[x,y] = self.single_energy(nonzero_mat)-self.single_energy(zero_mat)
        X =mat(identity(4))
        
        import random
        for num in range(10000):
            index = int(random.uniform(0,16))
            update_X = X.copy()
            if update_X[int(index/4),index%4] == 1:
                update_X[int(index/4),index%4] = 0
                trans = int(random.uniform(1,4))
                new_pos = (trans+index%4) % 4
                exchange_index = 0
                for exchange_index in range(4):
                    if(update_X[exchange_index,new_pos] ==1 ):
                        break
                update_X[exchange_index,new_pos] = 0
                update_X[exchange_index,index%4] = 1
                update_X[int(index/4),new_pos] = 1
            diff_energy = -self.cal_energy(weight_mat,theta,update_X)+self.cal_energy(weight_mat,theta,X)
            # apply sigmoid function:
            prob = 1/(1+exp(self.alpha*diff_energy))
            rand_num = random.uniform(0,self.MAX)
            if (rand_num >= self.MAX*prob):
                    X = update_X
            x_str = '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(X[0,0],X[0,1],X[0,2],X[0,3],\
                X[1,0],X[1,1],X[1,2],X[1,3],\
                X[2,0],X[2,1],X[2,2],X[2,3],\
                X[3,0],X[3,1],X[3,2],X[3,3])
            tmp=self.dic.get(x_str,0)
            if tmp == 0:
                self.dic[x_str] = 1
            else:
                self.dic[x_str] += 1
        
        import operator
        sorted_x=sorted(self.dic.items(),key=operator.itemgetter(1),reverse = True)
        print("The most 10 frequent state of the results: ")
        # output most frequent states
        for i in sorted_x:
            print(i)
        
if __name__ == "__main__":
        ass6().prob_rec()

