#product of Array except self
#[1,2,3,4]
# output=[24,12,8,6]

def out():
    l=[-1,1,0,-3,3]
    l2=[]
    p=1
    
    for x in l:
        for y in l:
            if y!=x:
                p *= y
        l2.append(p)
        p=1
    print(l2)

out()