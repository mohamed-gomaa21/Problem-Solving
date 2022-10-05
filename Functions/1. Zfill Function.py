
def xfill(countstring,mystring):
    """"
        Finished Solve Date : 24/06/2022
        that function add zeros to any string like Zfill() function
    """
    if countstring <= len(mystring):    # there are no zeros here
        print(end="")
    else:
       countzero = countstring - len(mystring) -1 # zeros number

       while countzero >= 0 :
           countzero = countzero -1
           print("0",end="")    # print zeros without new lines
    return mystring

astring = "Mohamed"
print(xfill(28,astring))