def fusionner_dicts(dict1,dict2):
    fusion = dict1.copy()
    for cle , val in dict2.items():
        if cle in fusion:
            fusion[cle] += val
        else :
            fusion[cle] = val
    return fusion
dict1 = {1: 20 , 2: 15 , 3 :10 }
dict2 = {4 : 17 , 2: 15 , 3 :20}

print(fusionner_dicts(dict1,dict2))