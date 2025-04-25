def round(num,rep):
    sq_num = (sum(int(i)*int(i) for i in str(num)))
    print(sq_num)
    
    if sq_num in rep:
        return 2
    elif sq_num==1:
        return 3
    rep.append(sq_num)
    print(rep)
    round(sq_num,rep)

num = 123
rep=[]
if round(num,rep) == 2:
    print("FALSE")
else:
    print("TRUE")