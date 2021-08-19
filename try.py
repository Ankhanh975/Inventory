name = "Gold_Apawfsegdrhftpl"
n = "13"

if len(name) >= 7 and len(name) <= 18:
    fName = "{:^9}".format(name[0:len(name)//2])
    sName = "{:^9}".format(name[len(name)//2: ])
elif len(name) < 7:
    fName = "{:^9}".format(name)
    sName = "{:^9}".format("")
else:
    name = name[0:18]
    fName = "{:^9}".format(name[0:len(name)//2])
    sName = "{:^9}".format(name[len(name)//2: ])

out=f'''\
 ___________ 
|           |
| {fName  } |
| {sName  } |
|           |
|________{n}_|'''

print(out)