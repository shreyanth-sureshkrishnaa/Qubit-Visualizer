from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class BlochSphere:
    def __init__(self, parentFrame):
        # Create a Matplotlib figure (not using plt.figure!)
        self.figure = Figure(figsize=(6, 6))
        self.ax = self.figure.add_subplot(111, projection='3d')

        # Embed into Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, parentFrame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        # Draw the static sphere
        self.CreateSphere()

        # Initial state vector |0⟩
        self.currentStateVector = [0, 0, 1]
        self.stateArrow = None
        self.DrawStateVector()

    def CreateSphere(self):
        """Draw the surface of the Bloch sphere and axis markers"""
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)

        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones_like(u), np.cos(v))

        self.ax.plot_surface(x, y, z, alpha=0.1, color='lightblue')

        # Axes
        axis_len = 1.2
        self.ax.plot([0, axis_len], [0, 0], [0, 0], 'r-', linewidth=2)
        self.ax.plot([0, -axis_len], [0, 0], [0, 0], 'r-', linewidth=2)

        self.ax.plot([0, 0], [0, axis_len], [0, 0], 'g-', linewidth=2)
        self.ax.plot([0, 0], [0, -axis_len], [0, 0], 'g-', linewidth=2)

        self.ax.plot([0, 0], [0, 0], [0, axis_len], 'b-', linewidth=2)
        self.ax.plot([0, 0], [0, 0], [0, -axis_len], 'b-', linewidth=2)

        # Labels
        self.ax.text(0, 0, 1.3, '|0⟩', fontsize=12, ha='center')
        self.ax.text(0, 0, -1.3, '|1⟩', fontsize=12, ha='center')
        self.ax.text(1.3, 0, 0, '|+⟩', fontsize=12, ha='center')
        self.ax.text(-1.3, 0, 0, '|−⟩', fontsize=12, ha='center')

        # Axis limits and scaling
        self.ax.set_xlim([-1.5, 1.5])
        self.ax.set_ylim([-1.5, 1.5])
        self.ax.set_zlim([-1.5, 1.5])
        self.ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

    def DrawStateVector(self):
        """Draw or redraw the state vector arrow"""
        if self.stateArrow:
            self.stateArrow.remove()

        self.stateArrow = self.ax.quiver(
            0, 0, 0,
            self.currentStateVector[0],
            self.currentStateVector[1],
            self.currentStateVector[2],
            color='red',
            arrow_length_ratio=0.1,
            linewidth=3
        )
        self.canvas.draw()

    def UpdateStateVector(self, newVector, animationSteps=20):
        """Smoothly animate the state vector transition"""
        self.oldVector = self.currentStateVector.copy()
        self.newVector = newVector
        self.step = 0
        self.animationSteps = animationSteps
        self._animate_step()

    def _animate_step(self):
        """Internal method for handling smooth animation"""
        if self.step > self.animationSteps:
            self.currentStateVector = self.newVector
            self.DrawStateVector()
            return

        t = self.step / self.animationSteps
        interpolatedVector = [
            self.oldVector[0] + t * (self.newVector[0] - self.oldVector[0]),
            self.oldVector[1] + t * (self.newVector[1] - self.oldVector[1]),
            self.oldVector[2] + t * (self.newVector[2] - self.oldVector[2])
        ]

        self.currentStateVector = interpolatedVector
        self.DrawStateVector()

        self.step += 1
        self.canvas.get_tk_widget().after(20, self._animate_step)

    def GetWidget(self):
        return self.canvas.get_tk_widget()
