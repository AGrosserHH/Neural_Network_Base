# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:52:11 2016

@author: Andi
"""

class Layer(object):
    def __init__(self,listOfNeurons, numberOfNeuronsInLayer):        
        self.__listOfNeurons=listOfNeurons
        self.__numberOfNeuronsInLayer=numberOfNeuronsInLayer
        
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