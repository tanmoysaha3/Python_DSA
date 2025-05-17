def towerOfHanoi(N, source, destination, midWay):
    total = 0
    def rec(N, source, destination, midWay):
        nonlocal total
        if(N==1):
            print("move disk "+ str(N) +" from rod "+ str(source) + " to rod " + str(destination))
            total+=1
            return
        rec(N-1, source, midWay, destination)
        print("move disk " + str(N) + " from rod " + str(source) + " to rod " + str(destination))
        total+=1
        rec(N - 1, midWay, destination, source)
    rec(N, source, destination, midWay)
    return total
print(towerOfHanoi(3,1,3,2))