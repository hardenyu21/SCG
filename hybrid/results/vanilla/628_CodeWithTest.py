import math
from random import uniform
import matplotlib.pyplot as plt

def task_func():
    # Generate random frequency, amplitude, and phase shift
    frequency = uniform(0.5, 5.0)  # Random frequency between 0.5 and 5.0
    amplitude = uniform(0.5, 2.0)  # Random amplitude between 0.5 and 2.0
    phase_shift = uniform(0, 2 * math.pi)  # Random phase shift between 0 and 2π

    # Generate time values
    time = [t for t in range(100)]

    # Generate sine wave values
    sine_wave = [amplitude * math.sin(2 * math.pi * frequency * t + phase_shift) for t in time]

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(time, sine_wave)

    # Set the title and labels
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

    # Show the plot
    plt.show()

    return ax

# Call the function to generate and display the plot
task_func()
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_2(self):
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_3(self):
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_4(self):
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')
        
    def test_case_5(self):
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')
        self.assertEqual(ax.get_xlabel(), 'Time')
        self.assertEqual(ax.get_ylabel(), 'Amplitude')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)