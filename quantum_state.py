import numpy as np
from qiskit.quantum_info import Statevector, Operator

class QubitState:
    def __init__(self):
        # the |0> State
        self.state = Statevector([1,0])

    def GetBlochVector(self):
        # Here, we map the quantum state of the qubit to the bloch sphere
        alpha = self.state.data[0] #Amplitude of the zero state
        beta = self.state.data[1] #Amplitude of the one state

        x = 2 * np.real(alpha * np.conj(beta)) #np.imag extracts sine components while np.real extracts cosine components. 
        y = 2 * np.imag(alpha * np.conj(beta))

        # We multiply by two here because the range of the initial expression is [-0.5,0.5]
        # As the bloch sphere is a unit sphere where each point represents a quantum state, the multiplication is required. 


        z = np.abs(alpha)**2 - np.abs(beta)**2

        return [x,y,z]
    
    def applyGate(self, gateName):
        gates = {
        
        # The .from_label() command generates the gate's matrix from its corresponing label. 

        'X': Operator.from_label('X'),  # Pauli-X (bit flip)
        'Y': Operator.from_label('Y'),  # Pauli-Y 
        'Z': Operator.from_label('Z'),  # Pauli-Z (phase flip)
        'H': Operator.from_label('H'),  # Hadamard
        'S': Operator.from_label('S'),  # Phase gate
        'T': Operator.from_label('T'),  # T gate
        'I': Operator.from_label('I'),  # Identity (do nothing)

        }

        if gateName in gates:
            self.state = self.state.evolve(gates[gateName])
            #The evolve() method handles all of the matrix math. It applies the matrix transformation to the qubit under the hood.
            return self.GetBlochVector()
        else:
            raise ValueError("Gate ",gateName," Not recognized.")
        

    def Reset(self):
        self.state = Statevector([1,0])
        return self.GetBlochVector()
    
    
