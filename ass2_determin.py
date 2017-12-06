from numpy import *
class ass2_determin:
    def determin_rec(init):
        weight_mat = -mat(ones((6,6)))
        weight_mat[0,:] = 0.5 
        # initialize value of vector X
        X = mat(init).astype(float)
        #keep updating until no value changes
        order = list(range(1,shape(X)[1]))
        for j in range(4):
            change = True
            import random
            # disorganize the the order of the updating 
            random.shuffle(order)
            while change == True:
                change = False
                for i in order:
                    origin = X[0,i]
                    X[0,i] = X*weight_mat[:,i]-X[0,i]*weight_mat[i,i]
                    if(X[0,i] < 0):
                        X[0,i] = 0.0
                    else:
                        X[0,i] = 1.0
                    if(origin != X[0,i]):
                        change = True
                if change == False:
                    break          
            print("The final result of output value with the updating order: ",order," should be: ")
            print(X[0,1:6])
            # restore X to the initial value
            X = mat(init).astype(float)
        print('\n')

    if __name__ == "__main__":
        # set the array of X, the first value should be
        # the input unchangeable value
        determin_rec([1,0,0,0,0,0])
        determin_rec([1,1,1,1,1,1])
        determin_rec([1,0.5,0.5,0.5,0.5,0.5])
        determin_rec([1,0.5,1,0.5,1,0.5])

