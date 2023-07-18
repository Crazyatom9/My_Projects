a=[10,5,9,8]
b=[8,4,3,-1]
c=[]
for i in range(len(a)):
    if a[i]!=b[i]:
        c.append(a[i]-b[i])    
msesu=0
mses=0   
maesu=0
maes=0
mapes=0
mape=0     
for j in range(len(c)):
    msesu+=c[j-1]**2
    maesu+=abs(c[j-1])
    mapes+=(c[j-1]/a[j-1])
mses=msesu/len(c)
maes=maesu/len(c)
mape=mapes/len(c)
print("MSE= ",mses,"MAE=",maes,"MAPE=",mape)

