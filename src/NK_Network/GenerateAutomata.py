import myRandom
from ProxyFunctions import*
import BoolFunction
    

def generateNKAutomata(N,K,functionsList,linksList):
  generateFunctionsList(N,K,functionsList)
  generateLinksList(N,K,linksList)
  #generateState(initialState,N)

def generateFunctionsList(N,K,functionsList):
  for i in range(N):
    #print "generating function", i
    bf=BoolFunction.BoolFunction(K)
    bf.generateRandom()
    
    functionsList.append(bf)
    
def generateLinksList(N,K,linksList):
  for n in range(N):
    currentFunctionLinks=[]
    while len(currentFunctionLinks)<K:
      randValue=myRandom.randrange(0,N)
      if not (randValue in currentFunctionLinks):
	currentFunctionLinks.append(randValue)
    linksList.append(currentFunctionLinks)
    
    


