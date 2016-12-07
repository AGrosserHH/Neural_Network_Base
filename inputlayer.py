# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:58:14 2016

@author: Andi
"""
from neuron import Neuron

class InputLayer():
    
    def __init__(self):        
        self.__listOfNeurons=[]
        self.__numberOfNeuronsInLayer=0
            
    def initLayer(self):
        listOfWeightInTemp=[]        
        
        for x in range(self.getnumberOfNeuronsInLayer()):
            a=Neuron()
            listOfWeightInTemp.append(a.initNeuron())            
            a.setlistofWeightIn(listOfWeightInTemp)                        
            self.__listOfNeurons.append(a)
            listOfWeightInTemp=[]
            
        
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