from numpy import *

def feature_change(data):
    mydata = mat(data)
    mymean = mydata.mean(0)
    feature_max = (mydata-mymean).max(0)
    result = (mydata - mymean)/feature_max
    return  result,mymean,feature_max