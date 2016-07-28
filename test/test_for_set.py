noneedlist = set(["1509", "1702", "1703", "2509", "1337", "1339", "1334", "1337"])
hh = set(["1509", "1337"])
print noneedlist - hh
for temp in noneedlist:
    if "1337" == temp:
        print "test"
        noneedlist.remove(temp)
        
print noneedlist