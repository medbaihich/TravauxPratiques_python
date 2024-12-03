def compte_occurences(liste):
    occurence = {}
    for i in liste:
        if i in occurence:
            occurence[i] +=1
        else : 
            occurence[i] = 1
    return occurence
list = ["med","akm","brhm","med","med","akm"]
print(compte_occurences(list)) 