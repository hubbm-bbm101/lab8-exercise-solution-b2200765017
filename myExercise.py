import sys
dict,file,inpt = [{},sys.argv[1],sys.argv[2]]
with open(file) as f:
    for line in f:
        liste = line.rstrip("\n").split(":")
        dict[liste[0]] = liste[1].split(",")
    try:
        for x in inpt.split(","):print("Name: {}, University: {} ".format(x, ",".join(dict[x])),end="")
    except:print("No record of ‘{}’ was found!".format(x), end="")