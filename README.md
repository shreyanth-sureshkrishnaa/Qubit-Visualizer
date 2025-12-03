# Qubit-Visualizer

An interactive Bloch sphere visualization tool I made for a seminar on Post-Quantum Cryptography. Used for exploring single-qubit quantum states. Apply quantum gates and watch your qubit evolve in real-time.


## Installation

```bash
# Install dependencies
pip install qiskit numpy matplotlib

# Run the application
python main.py
```

## How to Use

1. **Launch the app** - Opens a window with the Bloch sphere on the right, control panel on the left
2. **Click gate buttons** - X, Y, Z, H, S, T buttons apply quantum gates to your qubit
3. **Watch the animation** - Red arrow shows your quantum state moving on the sphere
4. **Reset** - Click "Reset to |0⟩" to return to the initial state

## Project Structure

- `main.py` - Main application
- `quantum_state.py` - Quantum state management (Qiskit)
- `bloch_sphere.py` - 3D visualization (Matplotlib)
- `gatepanel.py` - Control panel UI

## Requirements

- Python 3.8+
- qiskit
- numpy
- matplotlib
- tkinter (included with Python)

## License
MIT

