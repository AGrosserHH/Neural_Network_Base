# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:02:04 2016

@author: Andi
"""
from inputlayer import InputLayer
from outputlayer import OutputLayer
from hiddenlayer import HiddenLayer

class NeuralNet():
    
    def initNet(self):
        inputLayer=InputLayer()
        inputLayer.setnumberOfNeuronsInLayer(2)
        numberOfHiddenLayers=3
        listOfHiddenLayer=[]
        
        for x in range(numberOfHiddenLayers):    
            hiddenLayer=HiddenLayer() 
            hiddenLayer.setnumberOfNeuronsInLayer(2)          
            listOfHiddenLayer.append(hiddenLayer)
            
        outputLayer=OutputLayer()
        outputLayer.setnumberOfNeuronsInLayer(1)
        
        inputLayer.initLayer()
        print(inputLayer.getnumberOfNeuronsInLayer())
        
        hiddenLayer.initLayer(listOfHiddenLayer, inputLayer, outputLayer)
        
        outputLayer.initLayer() 
        
        print(outputLayer.getnumberOfNeuronsInLayer())
        print(inputLayer.getlistOfNeurons()[0].getlistofWeightIn())
        
        print(listOfHiddenLayer[0].getlistOfNeurons()[0].getlistofWeightIn())
        print(listOfHiddenLayer[0].getlistOfNeurons()[0].getlistofWeightOut())
        
        print(listOfHiddenLayer[1].getlistOfNeurons()[0].getlistofWeightIn())
        print(listOfHiddenLayer[1].getlistOfNeurons()[0].getlistofWeightOut())
        
        print(outputLayer.getlistOfNeurons()[0].getlistofWeightIn())

test=NeuralNet()
test.initNet()
