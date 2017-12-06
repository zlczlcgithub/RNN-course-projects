from numpy import *
class ass7_prob:
    def prob_rec(init):
        #x0 should be 1 which is not listed here
        X = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
        value = [0.25,0,0,0.25,0,0.25,0,0.25]
        weight_mat = mat(ones((4,4)))
        for i in range(4):
            weight_mat[i,i] = 0
        RAND_MAX = 2**32-1
        q = mat(zeros((3,3)))
        for i in range(3):
            for j in range(3):
                for z in [0,3,5,7]:
                    q[i,j]+= X[z][i] * X[z][j]*0.25
        print(q)
        count = 0
        while True:
            gradient = mat(zeros((3,3)))
            p_avg = mat(zeros((3,3)))
            p = [0] * 9
            for m in range(3):
                for n in range(3):
                    #update for 10000 times
                    for time in range(10000):
                        #randomly choose a neuron to update with uniform distribution on all neurons
                        index = int(random.uniform(1,6))
                        S = X*weight_mat[:,index]-X[0,index]*weight_mat[index,index]
                        P = 1/(1+exp(-S*1))
                        rand_num = random.uniform(0,RAND_MAX)
                        if(rand_num>RAND_MAX*P):
                            X[0,index] = 0
                        else:
                            X[0,index] = 1
                        if(linalg.norm(X[0,1:]-array([1,0,0,0,0]))<2):
                            count+=1
                            print("The number of times that distance smaller than 2 in 10000 times is: "+str(count))

    if __name__ == "__main__":
        # set the array of X, the first value should be 1
        # the input unchangeable value
        prob_rec([1,1.3,1.2,0.7,1.2,1.0])
        prob_rec([1,2,3,0,1,4])
