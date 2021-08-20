def toStack(num: int, fullStack=1):
    print (f"num: {(num)}, fullStack: {fullStack} and filled in: {(num-1)//fullStack+1} sta")
    return (num-1)//fullStack+1

x=toStack(0)
x=toStack(1)
x=toStack(15)
x=toStack(16)
x=toStack(31)
x=toStack(32)
x=toStack(128)
x=toStack(129)
