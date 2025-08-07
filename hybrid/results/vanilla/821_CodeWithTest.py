import time
import threading

def task_func(delay_time: float = 1.0, num_threads: int = 5):
    def thread_task(thread_id, results):
        time.sleep(delay_time)
        results[thread_id] = f'Delay in thread {thread_id} completed'

    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        thread = threading.Thread(target=thread_task, args=(i, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

# Example usage:
# print(task_func(1, 10))
import unittest
from faker import Faker
class TestCases(unittest.TestCase):
    def test_case_1(self):
        start = time.time()
        result = task_func()
        end = time.time()
        exec_time = end - start
        self.assertAlmostEqual(exec_time, 5, places=0)
        self.assertEqual(len(result), 5)
    def test_case_2(self):
        start = time.time()
        result = task_func(0.2, 1)
        end = time.time()
        exec_time = end - start
        self.assertAlmostEqual(exec_time, 0.2, places=1)
        self.assertEqual(len(result), 1)
    def test_case_3(self):
        delay = 0.1
        threads = 10
        start = time.time()
        result = task_func(delay, threads)
        end = time.time()
        exec_time = end - start
        self.assertAlmostEqual(exec_time, delay*threads, places=0)
        self.assertEqual(len(result), 10)
    def test_case_4(self):
        result = task_func(num_threads=0)
        self.assertEqual(len(result), 0)
    def test_case_5(self):
        'test for exact return string'
        fake = Faker()
        num_threads = fake.random_int(min=1, max=20)
        result = task_func(num_threads=num_threads)
        self.assertEqual(len(result), num_threads)
        for i in range(num_threads):
            self.assertIn(f'Delay in thread {i} completed', result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)