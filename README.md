##Description:##
For conjunctive normal form(CNF) where each clause is a disjunction (a Boolean or operation) of two variables defines whether it is satisfied or not  
Complexity O(n^3)

##Using:##
SAT2.py 'file_name'
(default: "SAT2.py simple.txt")

test-SAT2.py for ordinary unittest

###Description input file:###
-each clause should be written on separate line  
-whitespace should separate terms  
-the negatiation should be marked by '!' before term  
-term could consist of [0-9a-zA-Z]*  
  
e.g.  
(A || B) && (B || !C)  
"input":  
A B  
B !C  