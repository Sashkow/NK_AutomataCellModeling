import Automata
import BoolFunction
import AutomataProssesing
### hasBasinLevelBijections testing begin
#returns two automatas with same basin sizes but different attractor sizes 
def basinAttractorsDoNotMatchTriggerAutomatas():
    N=3
    K=3
    
    functionsList1=[]
    functionsList1.append(BoolFunction.BoolFunction(K,"00001111"))
    functionsList1.append(BoolFunction.BoolFunction(K,"00000001"))
    functionsList1.append(BoolFunction.BoolFunction(K,"00000000"))
    
    linksList1=[[0,1,2],[0,1,2],[0,1,2]]
    
    
    automata1 = Automata.NK_Automata(N,K,functionsList1,linksList1)
    
    AutomataProssesing.doAutomata(N,K,automata1)
    
    functionsList2=[]
    functionsList2.append(BoolFunction.BoolFunction(K,"00001111"))
    functionsList2.append(BoolFunction.BoolFunction(K,"01000110"))
    functionsList2.append(BoolFunction.BoolFunction(K,"00001010"))
    
    linksList2=[[0,1,2],[0,1,2],[0,1,2]]
    
    automata2 = Automata.NK_Automata(N,K,functionsList2,linksList2)
    
    AutomataProssesing.doAutomata(N,K,automata2)
    
    return automata1,automata2

def basinAttractorOfCertainSizeIsAbsentTriggerAutomatas():
    N=3
    K=3
    
    functionsList1=[]
    functionsList1.append(BoolFunction.BoolFunction(K,"00001111"))
    functionsList1.append(BoolFunction.BoolFunction(K,"00000001"))
    functionsList1.append(BoolFunction.BoolFunction(K,"00000000"))
    
    linksList1=[[0,1,2],[0,1,2],[0,1,2]]
    
    
    automata1 = Automata.NK_Automata(N,K,functionsList1,linksList1)
    
    AutomataProssesing.doAutomata(N,K,automata1)
    
    functionsList2=[]
    functionsList2.append(BoolFunction.BoolFunction(K,"00001111"))
    functionsList2.append(BoolFunction.BoolFunction(K,"01000110"))
    functionsList2.append(BoolFunction.BoolFunction(K,"10001010"))
    
    linksList2=[[0,1,2],[0,1,2],[0,1,2]]
    
    automata2 = Automata.NK_Automata(N,K,functionsList2,linksList2)
    
    AutomataProssesing.doAutomata(N,K,automata2)
    
    return automata1,automata2

#automatas of equal amount of basins and attractor and basin sizes but different structure.
def bruteForceBeginningTriggerAutomatas():
    N=3
    K=3
    
    functionsList1=[]
    functionsList1.append(BoolFunction.BoolFunction(K,"00001111"))
    functionsList1.append(BoolFunction.BoolFunction(K,"00000001"))
    functionsList1.append(BoolFunction.BoolFunction(K,"00000000"))
    
    linksList1=[[0,1,2],[0,1,2],[0,1,2]]
    
    
    automata1 = Automata.NK_Automata(N,K,functionsList1,linksList1)
    
    AutomataProssesing.doAutomata(N,K,automata1)
    
    functionsList2=[]
    functionsList2.append(BoolFunction.BoolFunction(K,"00001111"))
    functionsList2.append(BoolFunction.BoolFunction(K,"01000110"))
    functionsList2.append(BoolFunction.BoolFunction(K,"00000010"))
    
    linksList2=[[0,1,2],[0,1,2],[0,1,2]]
    
    automata2 = Automata.NK_Automata(N,K,functionsList2,linksList2)
    
    AutomataProssesing.doAutomata(N,K,automata2)
    
    return automata1,automata2

def bruteForceBeginningTriggerAfterSimpleBijectionTriggerAutomatas():
    N=3
    K=3
    
    functionsList1=[]
    functionsList1.append(BoolFunction.BoolFunction(K,"00001110"))
    functionsList1.append(BoolFunction.BoolFunction(K,"01000000"))
    functionsList1.append(BoolFunction.BoolFunction(K,"00100000"))
    
    linksList1=[[0,1,2],[0,1,2],[0,1,2]]
     
    automata1 = Automata.NK_Automata(N,K,functionsList1,linksList1)
    
    AutomataProssesing.doAutomata(N,K,automata1)
    
    functionsList2=[]
    functionsList2.append(BoolFunction.BoolFunction(K,"01001111"))
    functionsList2.append(BoolFunction.BoolFunction(K,"00000100"))
    functionsList2.append(BoolFunction.BoolFunction(K,"00000010"))
    
    linksList2=[[0,1,2],[0,1,2],[0,1,2]]
    
    automata2 = Automata.NK_Automata(N,K,functionsList2,linksList2)
    
    AutomataProssesing.doAutomata(N,K,automata2)
    
    return automata1,automata2

### hasBasinLevelBijections testing end
def my_append(element,lst=[]):
    lst.append(element)
    return lst

def f(x):
    for y in xrange(2, x):
        if not x % y:
            return False
    return True
 
#could not create VBPCBP.mdb.91: Object variable or width block not set
def main():
    
    for i in range(2,7):
	print (i,end=' : ')
	for u in range(1,i):
	       if u%2:
		    print(u,end=' ')
	       if u%3==0:
		    print(u*5,end ' ')
		    continue
	print(' \n')
    
    //print (1,' ',2)
    
    
    
if __name__ == '__main__':
  main() 
  
   