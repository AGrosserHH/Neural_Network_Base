
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:16:07 2016

@author: Andi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:58:14 2016

@author: Andi
"""
from neuron import Neuron

class HiddenLayer():
    def __init__(self):        
        self.__listOfNeurons=[]        
        self.__numberOfNeuronsInLayer=0
            
    def initLayer(self, listOfHiddenLayer, inputLayer, outputLayer):
        listOfWeightIn=[]        
        listOfWeightOut=[]        
        
        
        numberOfHiddenLayers=len(listOfHiddenLayer)
        
        for i in range(numberOfHiddenLayers):
            for j in range(self.getnumberOfNeuronsInLayer()):
                neuron=Neuron()
                
                limitIn=0;
                limitOut=0;
                
                if (i==0):
                    limitIn=inputLayer.getnumberOfNeuronsInLayer()
                    print(limitIn)
                    if (numberOfHiddenLayers>1):                        
                        limitOut=listOfHiddenLayer[i+1].getnumberOfNeuronsInLayer()
                    else:
                        
                        limitOut=listOfHiddenLayer[i].getnumberOfNeuronsInLayer()
                elif (i==numberOfHiddenLayers-1):
                    limitOut=listOfHiddenLayer[i-1].getnumberOfNeuronsInLayer()
                    limitOut=outputLayer.getnumberOfNeuronsInLayer()
                else:
                    limitIn=listOfHiddenLayer[i-1].getnumberOfNeuronsInLayer()
                    limitOut=listOfHiddenLayer[i+1].getnumberOfNeuronsInLayer()                    
                       
                for k in range(limitIn):                    
                    listOfWeightIn.append(neuron.initNeuron())  
                
                for k in range(limitOut):                    
                    listOfWeightOut.append(neuron.initNeuron())
                
                neuron.setlistofWeightIn(listOfWeightIn)
                neuron.setlistofWeightOut(listOfWeightOut)
                
                self.__listOfNeurons.append(neuron)
                listOfWeightIn=[]        
                listOfWeightOut=[]        
                
            listOfHiddenLayer[i].setlistOfNeurons(self.__listOfNeurons)                        
            self.__listOfNeurons=[]          
        return listOfHiddenLayer  
        
    def getlistOfNeurons(self):
        return self.__listOfNeurons

    def setlistOfNeurons(self,listOfNeurons):
        self.__listOfNeurons=listOfNeurons

    def getnumberOfNeuronsInLayer(self):
        return self.__numberOfNeuronsInLayer

    def setnumberOfNeuronsInLayer(self, numberOfNeuronsInLayer):
        self.__numberOfNeuronsInLayer=numberOfNeuronsInLayer
        
    listOfNeurons=property(getlistOfNeurons, setlistOfNeurons)
    numberOfNeuronsInLayer=property(getnumberOfNeuronsInLayer, setnumberOfNeuronsInLayer)




