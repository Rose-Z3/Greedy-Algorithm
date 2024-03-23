def density(value,weight):
    return float(value/weight)

def knapsack_greedy(c,value,weight,n):
    D = []
    item = []
    packet =[0]*n
    total_weight=0
    max_profit =0
    for i in range(n):
        D.append(density(value[i],weight[i]))
        
    order=[] #order list contains list index of object in decreasing order of profit value per weight
    for i in range(n):
        order.append(D.index(max(D)))
        D[D.index(max(D))]=0
    i=0
        #Putting items of higher profit value per weight in sack
        
    print("\nItem\tWeight\tProfit Value\packet")
    while total_weight!=c:
        if (total_weight+weight[order[i]])<=c:
            max_profit+=value[order[i]]
            total_weight+=weight[order[i]]
            print("%d\t%d\t%d\t\t1"%(order[i]+1,weight[order[i]],value[order[i]]))
        else:
            packet = round((c-total_weight)/weight[order[i]])
            value = value[order[i]]*packet
            max_profit+= value
            total_weight+=(c-total_weight)
            if value !=0:
                print("%d\t%d\t%0.2f\t\t%0.2f"%(order[i]+1,weight[order[i]],value,packet))
        i+=1
               
    return max_profit ,total_weight


C = int(input("Enter the capacity of the knapsack: ")) #the capacity of the knapsack
N = int(input("Enter the number of available items: "))
W = []#the weights of the available items
V = []#the values of the available items
for i in range(N):
    w = int(input("Enter the weight of item "+str(i+1)+": "))
    v = int(input("Enter the value of item "+str(i+1)+": "))
    W.append(w)
    V.append(v)
    
max_profit,total_weight=knapsack_greedy(C, V, W,N)
print("\nMaximum profit= %0.2f"%max_profit)




