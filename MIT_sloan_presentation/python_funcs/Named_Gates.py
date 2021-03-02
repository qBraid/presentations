from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def Blackbox():  
    circ = QuantumCircuit(2, name='BlackBox') 
    circ.cx(0,1)   # a simple circuit implementing the function f such that f(0) = 1 and f(1) = 0.
    return circ.to_gate()



def One():
    circ = QuantumCircuit(1, name='One')
    circ.x(0)
    return circ.to_gate()


def Zero():
    circ = QuantumCircuit(1, name='Zero')
    circ.i(0)
    return circ.to_gate()



def BlackboxCircuit(firstValue,secondValue):
    circ = QuantumCircuit(2, 1)
    
    if firstValue == 0:
        circ.append(Zero(),[0])
    else:
        circ.append(One(),[0])
    
    if secondValue == 0:
        circ.append(Zero(),[1])
    else:
        circ.append(One(),[1])
    
    circ.append(Blackbox(),[0,1])
    circ.measure(0,0) #measure
    return circ
