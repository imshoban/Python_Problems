#Finding number of matching pairs 
def sockMerchant(n, ar):
    matching_Pairs=0
    new_set=set(ar)
    for values in new_set:
        matching_Pairs=matching_Pairs+ar.count(values)//2
    return matching_Pairs
#input:n=9,ar=[10 20 20 10 10 30 50 10 20]
#output:3
