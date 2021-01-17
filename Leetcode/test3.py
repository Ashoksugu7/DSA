from collections import Counter



def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):
    # Write your code here
    text_word = sorted(text1.split(" "))
    print(dict(Counter(text_word)))
    print( key1, val1, list1)
    
    counter1 =  Counter(dictionary1)
    counter2 = Counter(deduct)

    counter1.subtract(counter2)
    print(dict(counter1))

    dict3={}
    i=0
    for x,y in (zip(key1,val1)):
        if i !=1:        
            dict3[x]=y
        i+=1
        
    dict3[key1[1]]=val1[1]
    print(dict3)

    dict4={}
    odd=[]
    even=[]
    for z in list1:
        if z%2==0:
            even.append(z)
        else:
            odd.append(z)
    if len(odd) > 0:
        dict4['odd']=odd

    if len(even) >0:
        dict4['even']=even
    print(dict4)


collectionfunc("how many times does each word show up in this sentence word times each each word", {'1': 3, '2': 4, '12': 2, '14': 6}, ['a', 'b', 'c'] ,[1, 2, 3], {'1': 0, '14': 2}, [1, 3, 5, 7, 9, 10])