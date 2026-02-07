def timeConversion(s):
    o=""
    h= int(s[0]+s[1])
    if s[-2]=='P':
        if h!=12:
             hr= 12+int(h)
             o=str(hr)+":"+s[3:8]
        else:
            o=s[0:8]
    else:
         if h==12:
            hr="00"
            o=hr+":"+s[3:8]
         else:
            o=s[0:8]
    return o
