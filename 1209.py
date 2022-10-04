def percents(string):
    big_str = 0
    stroka = string.split(" ")
    for podstroka in stroka:
        upp = 0  
        low = 0 
        for element in podstroka:
            if element.isupper(): 
                upp +=1
            if element.islower():
                low +=1
        if upp > low :
            big_str +=1 
    otvet = (big_str*100)/ len(stroka)
    return otvet
print(percents('NDp Lka nuR vtE'), '%')
