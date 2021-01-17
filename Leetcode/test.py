def performIterator(tuplevalues):
    # Write your code here
    res=[]
    odd_element=[]
    all_element=[]
    list_val=list(tuplevalues)

    for i in range(len(list_val)):
        if i==0:
            res.append(list_val[i][:4])

        if i==1:
            res.append( tuple( [list_val[1][0]]*len(list_val[1])) )
            

        if i==2:
            t=list_val[i]
            t_res=[]
            for k in range(1, len(t)+1):
                t_res.append(sum(t[:k]) )
            res.append( tuple(t_res) )
        # print(i)
        # print(list_val[i])
        for ele in list_val[i]:
            if ele%2 != 0:
                odd_element.append(ele)
            all_element.append(ele)

    res.append(tuple(all_element))
    res.append(tuple(odd_element))

    return tuple(res)

    one_tup = list_val[0]
    print( one_tup, )

    t=list_val[2]
    t_res=[]
    for i in range(1, len(t)+1):
        t_res.append(sum(t[:i]) )

    print( one_tup, tuple([list_val[1][0]]*len(list_val[1])), tuple(t_res))

    main_list=[]
    main_list.append((3,4))
    print(main_list)
        

x=((1, 10, 5, 2), (8, 48, 14, 63), (59, 47, 49, 22), (19, 60, 1, 40))
print(performIterator(x))