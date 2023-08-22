'''  chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]'''

def compress(chars):
    count=0
    out=[]
    c_char=chars[0]
    #print(out)
    #print(len(chars))
    for x in range(len(chars)):
        if chars[x]==c_char:
            count=count+1
        else:
            out.append(c_char)
            out.append(str(count))
            c_char=chars[x]
            print(c_char)
            count=1
    out.append(c_char)
    out.append(str(count))        
    print(out)

chars=["a","a","b","b","c","c","c"]
compress(chars)