# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:31:18 2016

@author: Andi
"""
import random

class Neuron:
    def __init__(self):        
        self.__listofWeightIn=[]
        self.__listofWeightOut=[]
        
    def getlistofWeightIn(self):
        return self.__listofWeightIn

    def setlistofWeightIn(self,listofWeightIn):
        self.__listofWeightIn=listofWeightIn

    def getlistofWeightOut(self):
        return self.__listofWeightOut

    def setlistofWeightOut(self, listofWeightOut):
        self.__listofWeightOut=listofWeightOut
        
    listofWeightIn=property(getlistofWeightIn, setlistofWeightIn)
    listofWeightOut=property(getlistofWeightOut, setlistofWeightOut)

    def initNeuron(self):
        a=random.uniform(0.0, 100)
        return a