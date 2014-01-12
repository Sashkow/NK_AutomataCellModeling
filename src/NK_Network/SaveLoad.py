import sys
import os
import pickle
import shutil
import os.path

def saveVariableToFile(variable,fileName,filePath):
  aFile=open(filePath+'/'+fileName,'w')
  pickle.dump(variable,aFile)
  aFile.close()
  
def loadVariableFromFile(fileName,filePath):
  aFile=open(filePath+'/'+fileName,'r')
  variable = pickle.load(aFile)
  aFile.close()
  return variable
  
import sys
import os
import pickle
import shutil
from ProxyFunctions import*


def saveVariableToFile(variable,fileName,filePath):
  aFile=open(filePath+'/'+fileName,'w')
  pickle.dump(variable,aFile)
  aFile.close()
  
def loadVariableFromFile(fileName,filePath):
  aFile=open(filePath+'/'+fileName,'r')
  #print filePath+'/'+fileName
  variable = pickle.load(aFile)
  aFile.close()
  return variable
  
def generateAutomataTypeFolderName(N,K):
  maxNK=20
  return "N_"+addSucceedingZeroes(maxNK,N)+"_K_"+addSucceedingZeroes(maxNK,K)

def generateAutomataFolderName(automataTypeFoldersCollection):
  maxAutomataFoldersAmount=999
  currentAutomatFoldersAmount=len(automataTypeFoldersCollection)
  return addSucceedingZeroes(maxAutomataFoldersAmount,currentAutomatFoldersAmount)

def saveNKAutomata(currenaFolderPath,nkAutomata,picture=False):
  
  automataTypesFolderPath=currenaFolderPath+'/SavedAutomata'
  
  automataTypesFolderCollection =os.listdir(automataTypesFolderPath)
  
  automataTypeFolderName=generateAutomataTypeFolderName(nkAutomata.N,nkAutomata.K)
  
  automataTypeFolderPath=automataTypesFolderPath+'/'+automataTypeFolderName
  
  if not os.path.exists(automataTypeFolderPath):
    os.makedirs(automataTypeFolderPath)
  
  automataFoldersCollection=os.listdir(automataTypeFolderPath)
  
  #folders are numbered '000','001','002'...
  automataFolderName=generateAutomataFolderName(automataFoldersCollection)
  
  automataFolderPath=automataTypeFolderPath+'/'+automataFolderName
  
  os.makedirs(automataFolderPath)
  
  #print automataFolderPath
  
  saveVariableToFile(nkAutomata,'automata.txt',automataFolderPath)
  
  if picture:
    if os.path.exists(currenaFolderPath+'/'+'tempPic.png'): 
      shutil.copyfile(currenaFolderPath+'/'+'tempPic.png', automataFolderPath+'/'+automataTypeFolderName+'_'+automataFolderName+'.png')
    if os.path.exists(currenaFolderPath+'/'+'tempPic2.png'):
      shutil.copyfile(currenaFolderPath+'/'+'tempPic2.png', automataFolderPath+'/'+automataTypeFolderName+'_'+automataFolderName+"_CyclesOnly"+'.png')
    if os.path.exists(currenaFolderPath+'/'+'tempPic3.png'):
      shutil.copyfile(currenaFolderPath+'/'+'tempPic3.png', automataFolderPath+'/'+automataTypeFolderName+'_'+automataFolderName+"_FunLinks"+'.png')
      
      
def gatherData(automataList,automataFoldersFolderPath):
  automataFoldersList=os.listdir(automataFoldersFolderPath) #'000','001','002'
  i=0
  for automataFolderName in automataFoldersList:
    print "gathering:", i
    i+=1
    nkAutomata=loadVariableFromFile('automata.txt',automataFoldersFolderPath+'/'+automataFolderName)
    automataList.append(nkAutomata)
 
      
def testFoldersCreation(currenaFolderPath):
  automata=[]
  enters=[]
  initialState=[]
  N=5
  K=5
  I=3
  for n in range(N):
    for k in range(K):
      for i in range(I):
	saveNKAutomata(automata,enters,initialState,currenaFolderPath,n,k)
	




