import time


def measure_time(times_to_measure, function, **kwargs):
    results = [0.] * times_to_measure
    for i in range(times_to_measure):
        start = time.time()
        function(**kwargs)
        end = time.time()
        
        results[i] = end - start
        
    return results
