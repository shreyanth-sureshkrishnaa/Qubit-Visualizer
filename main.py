# main.py
import tkinter as tk
from tkinter import ttk
from quantum_state import QubitState
from bloch_sphere import BlochSphere
from gatepanel import GatePanel

class QuantumVisualizer:
    def __init__(self):
        # Initialize the quantum state
        self.quantumState = QubitState()
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Quantum Circuit Visualizer")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        self.CreateLayout()
        self.InitializeVisualization()

    def CreateLayout(self):
        """Create the main GUI layout"""
        # Create main container with two panels
        mainContainer = ttk.Frame(self.root)
        mainContainer.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Left panel for controls
        leftPanel = ttk.Frame(mainContainer)
        leftPanel.pack(side='left', fill='y', padx=(0, 10))
        
        # Right panel for Bloch sphere
        rightPanel = ttk.Frame(mainContainer)
        rightPanel.pack(side='right', fill='both', expand=True)
        
        # Create the gate panel
        self.gatePanel = GatePanel(leftPanel, self.OnGateAction)
        
        # Create the Bloch sphere visualization
        self.blochSphere = BlochSphere(rightPanel)

    def OnGateAction(self, action):
        """Handle gate button clicks and control actions"""
        try:
            if action == 'RESET':
                # Reset to |0⟩ state
                newVector = self.quantumState.Reset()
                print(f"Reset to |0⟩ state: {newVector}")
                
            else:
                # Apply quantum gate
                newVector = self.quantumState.applyGate(action)
                print(f"Applied {action} gate. New state: {newVector}")
            
            # Update the Bloch sphere with animation
            self.blochSphere.UpdateStateVector(newVector)
            
        except Exception as e:
            print(f"Error applying {action}: {e}")

    def InitializeVisualization(self):
        """Set up the initial display"""
        # Get initial state (|0⟩)
        initialVector = self.quantumState.GetBlochVector()
        
        # Update Bloch sphere without animation
        self.blochSphere.currentStateVector = initialVector
        self.blochSphere.DrawStateVector()
        
        print(f"Initial state |0⟩: {initialVector}")

    def Run(self):
        """Start the application"""
        print("Starting Quantum Circuit Visualizer...")
        print("Initial quantum state: |0⟩")
        print("Click gates to see quantum state evolution!")
        
        # Start the GUI event loop
        self.root.mainloop()

# Main execution
if __name__ == "__main__":
    app = QuantumVisualizer()
    app.Run()