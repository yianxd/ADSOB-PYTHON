for k in range(1,500+1):
    for c in range(1,500+1):
        x=k**2+c**2
        for i in range(1,500+1):
            h=i**2
            if x ==h:
                print("CA=",k,"co=",c,"h=",h,i,)