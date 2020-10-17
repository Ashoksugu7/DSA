"""
Throne Inheritance
User Accepted:2048
User Tried:2640
Total Accepted:2093
Total Submissions:4249
Difficulty:Medium
A kingdom consists of a king, his children, his grandchildren, and so on. Every once in a while, someone in the family dies or a child is born.

The kingdom has a well-defined order of inheritance that consists of the king as the first member. Let's define the recursive function Successor(x, curOrder), which given a person x and the inheritance order so far, returns who should be the next person after x in the order of inheritance.

Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder
For example, assume we have a kingdom that consists of the king, his children Alice and Bob (Alice is older than Bob), and finally Alice's son Jack.

In the beginning, curOrder will be ["king"].
Calling Successor(king, curOrder) will return Alice, so we append to curOrder to get ["king", "Alice"].
Calling Successor(Alice, curOrder) will return Jack, so we append to curOrder to get ["king", "Alice", "Jack"].
Calling Successor(Jack, curOrder) will return Bob, so we append to curOrder to get ["king", "Alice", "Jack", "Bob"].
Calling Successor(Bob, curOrder) will return null. Thus the order of inheritance will be ["king", "Alice", "Jack", "Bob"].
Using the above function, we can always obtain a unique order of inheritance.

Implement the ThroneInheritance class:

ThroneInheritance(string kingName) Initializes an object of the ThroneInheritance class. The name of the king is given as part of the constructor.
void birth(string parentName, string childName) Indicates that parentName gave birth to childName.
void death(string name) Indicates the death of name. The death of the person doesn't affect the Successor function nor the current inheritance order. You can treat it as just marking the person as dead.
string[] getInheritanceOrder() Returns a list representing the current order of inheritance excluding dead people.
 

Example 1:

Input
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
Output
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

Explanation
ThroneInheritance t= new ThroneInheritance("king"); // order: king
t.birth("king", "andy"); // order: king > andy
t.birth("king", "bob"); // order: king > andy > bob
t.birth("king", "catherine"); // order: king > andy > bob > catherine
t.birth("andy", "matthew"); // order: king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "alex", "asha", "catherine"]
 

Constraints:

1 <= kingName.length, parentName.length, childName.length, name.length <= 15
kingName, parentName, childName, and name consist of lowercase English letters only.
All arguments childName and kingName are distinct.
All name arguments of death will be passed to either the constructor or as childName to birth first.
For each call to birth(parentName, childName), it is guaranteed that parentName is alive.
At most 105 calls will be made to birth and death.
At most 10 calls will be made to getInheritanceOrder.
"""

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.gen_line={}
        self.gen_line[kingName]=[]
        
       

    def birth(self, parentName: str, childName: str) -> None:
        self.gen_line[parentName].append(childName)
        self.gen_line[childName]=[]
        
        

    def death(self, name: str) -> None:
        their_child = self.gen_line[name]

        their_parent=None

        for parent, child_list in self.gen_line.items():
            if name in child_list:
                their_parent = parent
                break

        if their_parent is not None:
            index = (self.gen_line[their_parent]).index(name)
            self.gen_line[their_parent].remove(name)
                    
            while len(their_child) > 0:
                self.gen_line[their_parent].insert(index, their_child.pop())
        else:
            first_gen=self.gen_line[ list(self.gen_line.keys())[0]]
            if len(first_gen) > 1:
                self.gen_line[first_gen[0]].extend(first_gen[1:])


            del self.gen_line[list(self.gen_line.keys())[0]]


        

    def getInheritanceOrder(self) :
        print(self.gen_line)
        res=[]
        qu=[]
        qu.append(list(self.gen_line.keys())[0])
        while len(qu) > 0:
            cur=qu.pop()
            qu.extend( self.gen_line[cur][::-1] )
            res.append(cur)

            
        return res
            



        
obj = ThroneInheritance("king")    
obj.birth("king", "clyde")
obj.birth("clyde","shannon")
obj.birth("shannon","scott")
obj.birth("king","keith")
obj.birth("clyde","joseph")
obj.death("clyde")

# obj.birth("king","clyde")
# obj.death("king")
# obj.birth("clyde","shannon")
# obj.birth("shannon","scott")
# obj.death("clyde")

print(obj.getInheritanceOrder())
