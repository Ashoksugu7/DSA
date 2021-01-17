from collections import Counter

class Test():
    def __init__(self):
        pass

    def result(self, s, t):
        s_count=Counter(s).items()
        t_count=Counter(t).items()
        print(s_count, t_count)

        # for key in s_count:
        #     if abs( t_count[0] )

        for s_key in s_count:
            #print(key[0])
            for t_key in t_count:
                if s_key[0] == t_key[0]:
                    #print(s_key[0], s_key[1], t_key[1])
                    if abs(s_key[1] - t_key[1]) > 3:
                        return "No"
        

        return "Yes"

        


obj = Test()
s=[10, 10, 10, 10, 10, -20, -20, 30]
t=[10, -20, -20, -20, -20, 10, -20, -20]
print(obj.result(s,t))