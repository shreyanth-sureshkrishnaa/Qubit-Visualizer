# gate_panel.py
import tkinter as tk
from tkinter import ttk

class GatePanel:
    def __init__(self, parentFrame, gateCallback):
        self.parentFrame = parentFrame
        self.gateCallback = gateCallback
        
        # Create main frame for all controls
        self.mainFrame = ttk.Frame(parentFrame)
        self.mainFrame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.CreateGateButtons()
        self.CreateControlButtons()
    
    def CreateGateButtons(self):
        """Create buttons for all quantum gates"""
        # Title for gate section
        gateLabel = ttk.Label(self.mainFrame, text="Quantum Gates", 
                            font=('Arial', 14, 'bold'))
        gateLabel.pack(pady=(0, 10))
        
        # Define gate information: (name, description, color)
        gateInfo = [
            ('X', 'Pauli-X (NOT)', '#FF4444'),
            ('Y', 'Pauli-Y', '#44FF44'), 
            ('Z', 'Pauli-Z', '#4444FF'),
            ('H', 'Hadamard', '#FF8800'),
            ('S', 'Phase Gate', '#8844FF'),
            ('T', 'T Gate', '#44FFFF'),
        ]
        
        # Create buttons in a grid
        for i, (gateName, description, color) in enumerate(gateInfo):
            self.CreateGateButton(gateName, description, color, i)

    def CreateGateButton(self, gateName, description, color, position):
        """Create a single gate button with styling"""
        # Create frame for this button
        buttonFrame = ttk.Frame(self.mainFrame)
        buttonFrame.pack(fill='x', pady=2)
        
        # Create the main gate button
        button = tk.Button(
            buttonFrame,
            text=gateName,
            font=('Arial', 12, 'bold'),
            bg=color,
            fg='white',
            width=3,
            height=2,
            command=lambda: self.OnGateClick(gateName)
        )
        button.pack(side='left', padx=(0, 10))
        
        # Create description label
        descLabel = ttk.Label(buttonFrame, text=description, 
                            font=('Arial', 10))
        descLabel.pack(side='left', anchor='w')

    def CreateControlButtons(self):
        """Create utility buttons like Reset"""
        # Add separator
        separator = ttk.Separator(self.mainFrame, orient='horizontal')
        separator.pack(fill='x', pady=20)
        
        # Control buttons title
        controlLabel = ttk.Label(self.mainFrame, text="Controls", 
                            font=('Arial', 14, 'bold'))
        controlLabel.pack(pady=(0, 10))
        
        # Reset button
        resetButton = tk.Button(
            self.mainFrame,
            text="Reset to |0⟩",
            font=('Arial', 12),
            bg='#666666',
            fg='white',
            width=12,
            height=2,
            command=self.OnResetClick
        )
        resetButton.pack(pady=5)

    def OnGateClick(self, gateName):
        """Handle gate button clicks"""
        print(f"Gate {gateName} clicked")  # Debug output
        
        # Call the callback function passed from main GUI
        if self.gateCallback:
            self.gateCallback(gateName)

    def OnResetClick(self):
        """Handle reset button click"""
        print("Reset clicked")  # Debug output
        
        # Call callback with special 'RESET' command
        if self.gateCallback:
            self.gateCallback('RESET')

    def GetWidget(self):
        """Return the main frame widget"""
        return self.mainFrame
    
    