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