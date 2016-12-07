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

class OutputLayer():
    
    def __init__(self):        
        self.__listOfNeurons=[]
        self.__numberOfNeuronsInLayer=0
            
    def initLayer(self):
        listOfWeightOutTemp=[]        
        
        for x in range(self.getnumberOfNeuronsInLayer()):
            a=Neuron()
            listOfWeightOutTemp.append(a.initNeuron())            
            a.setlistofWeightIn(listOfWeightOutTemp)                        
            self.__listOfNeurons.append(a)
            listOfWeightOutTemp=[]       
        
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
    
    