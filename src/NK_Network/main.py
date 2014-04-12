#import test
 
from Automata import NK_Automata
from Debug import log
 
import drawGraph
import BoolFunction
import AutomataProssesing
import ThroughAllAutomata
import GraphIsomorphism
import Automata
import os, sys
import SaveLoad
import math
 
 
#console main
def main():
    currentFolderPath = os.path.dirname(__file__)
    print ">>>", currentFolderPath==""
    N=3
    K=2
    sampleLength=100
    samplesAmount=1
     
    AutomataProssesing.doAutomata(N,K)
     
     
    """
    for i in range(1):
        print "automata:", i
        AutomataProsessing.doAutomata(N,K) 
    """
    #ThroughAllAutomata.throughAllFunctions(3,3)
     
    #ThroughAllAutomata.throughAllLinks(3,2)
    #print ThroughAllAutomata.throughAllCombinations(3,2)
     
    #print ThroughAllAutomata.throughAllAutomata(4,2)
     
     
    """
    filePath="/home/sashko/SelfEducation/Automata/NK_Automata_Refactored_2/SavedAutomata/N_03_K_03/000"
    nkAutomata1 = SaveLoad.loadVariableFromFile("automata.txt",filePath)
     
    filePath="/home/sashko/SelfEducation/Automata/NK_Automata_Refactored_2/SavedAutomata/N_03_K_03/001"
    nkAutomata2 = SaveLoad.loadVariableFromFile("automata.txt",filePath)
     
    nkAutomata1.functionsList=[BoolFunction.BoolFunction(3,"00001110"),
                                BoolFunction.BoolFunction(3,"01000001"),
                                BoolFunction.BoolFunction(3,"00100001")]
                                 
    nkAutomata1.spanAutomata()
    drawGraph.drawGraphByDictionary(nkAutomata1.stateSpan,"/home/sashko/SelfEducation/Automata/NK_Automata_Refactored_2")
     
                                 
    nkAutomata1.functionsList=[BoolFunction.BoolFunction(3,"01001110"),
                                BoolFunction.BoolFunction(3,"00000100"),
                                BoolFunction.BoolFunction(3,"00000011")]
     
     
     
    print nkAutomata1.functionsList
    print nkAutomata1.linksList
    print nkAutomata2.functionsList
    print nkAutomata2.linksList
     
    print nkAutomata1.stateList
    print nkAutomata2.stateList
     
    print GraphIsomorphism.hasBasinLevelBijections(nkAutomata1,nkAutomata2)
    """
     
    #print "attractorDict",nkAutomata.attractorDict
     
    #print "basinDict",GraphIsomorphism.analyseGraphBasins(nkAutomata)
     
    #print ThroughAllAutomata.throughAllPermutations(3)
     
     
     
    #ans= nkAutomata.countExpectedReturnTime()
    #print "Expected return time:", ans
     
    #Analyze.createAutomataStabilitySamples(N,K,currentFolderPath,sampleLength,samplesAmount)
     
    #Analyze.createAutomataReturnTimeSamples(N,K,currentFolderPath,sampleLength,samplesAmount)
     
     
    #createAutomataStabilitySamples(N,K,currentFolderPath,sampleLength,samplesAmount)
   
   
   
   
if __name__ == '__main__':
    main() 
   
   
   
    #nkAutomata.functionsList=[BoolFunction(4,"1010101010101010"),
    #BoolFunction(4,"0110000000000000"),BoolFunction(4,"0001100000000000"),BoolFunction(4,"0000010000000000")]
    #nkAutomata.linksList=[[3,2,1,0],[3,2,1,0],[3,2,1,0],[3,2,1,0]]
 
   
   