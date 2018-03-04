def readdata(filepath,x,label,sex=1):
    fr = open(filepath)
    arrayOfLine = fr.readlines()
    for line in arrayOfLine:
        dataOfLine = line.strip().split()
        x.append([float(dataOfLine[0]),float(dataOfLine[1]),float(dataOfLine[2])])
        label.append(sex)

def readdata1(filepath,height,weight,feetsize,label,sex=1):
    fr = open(filepath)
    arrayOfLine = fr.readlines()
    for line in arrayOfLine:
        dataOfLine = line.strip().split()
        height.append(dataOfLine[0])
        weight.append(dataOfLine[1])
        feetsize.append(dataOfLine[2])
        label.append(sex)
