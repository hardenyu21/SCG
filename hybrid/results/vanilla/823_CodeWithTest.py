import time
import numpy as np

def task_func(samples=10, delay=0.1):
    delay_times = []

    for _ in range(samples):
        start_time = time.time()
        time.sleep(delay)
        end_time = time.time()
        
        actual_delay = end_time - start_time
        delay_times.append(actual_delay)

    mean_delay = np.mean(delay_times)
    std_dev_delay = np.std(delay_times)

    return (mean_delay, std_dev_delay)

# Example usage:
# mean, std_dev = task_func(samples=10, delay=0.1)
# print(f"Mean delay: {mean}, Standard deviation: {std_dev}")
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        start = time.time()
        mean, std = task_func(samples=100, delay=0.001)
        end = time.time()
        self.assertAlmostEqual(100 * 0.001, end-start, delta=3)
        self.assertAlmostEqual(mean, 0.001, places=0)
        self.assertTrue(0 <= std <= 0.01)
        
    def test_case_2(self):
        start = time.time()
        mean, std = task_func(samples=3, delay=0.1)
        end = time.time()
        self.assertAlmostEqual(3 * 0.1, end-start, places=1)
        self.assertAlmostEqual(mean, 0.1, delta=0.2)
        self.assertTrue(0 <= std <= 0.01)
    def test_case_3(self):
        start = time.time()
        mean, std = task_func(samples=2, delay=0.2)
        end = time.time()
        self.assertAlmostEqual(2 * 0.2, end-start, places=1)
        self.assertTrue(0.19 <= mean <= 0.21)
        self.assertTrue(0 <= std <= 0.02)
    def test_case_4(self):
        start = time.time()
        mean, std = task_func(samples=100, delay=0.05)
        end = time.time()
        self.assertTrue(3 <= end-start <= 7)
        self.assertTrue(0.03 <= mean <= 0.07)
        self.assertTrue(0 <= std <= 0.05)
    def test_case_5(self):
        start = time.time()
        mean, std = task_func(samples=1, delay=1)
        end = time.time()
        self.assertAlmostEqual(1, end-start, places=0)
        self.assertTrue(0.9 <= mean <= 1.1)
        self.assertTrue(0 <= std <= 0.1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)