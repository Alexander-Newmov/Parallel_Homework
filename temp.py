import os
import argparse
import numpy as np

from parallel import do_parallel, do_sequential
from calc_stats import Calc_Mean
from measure_time import measure_time


THREADS_NUMS_FOR_TEST = [2, 3, 4, 6, 8]


parser = argparse.ArgumentParser()
parser.add_argument('--data_folder', type=str,
                    help='Path to folder with images.')
parser.add_argument('--times_to_test', type=int, default=5,
                    help='How many times check one threads number.')


def main():
    args = parser.parse_args()
    data_folder = args.data_folder
    times_to_test = args.times_to_test
    
    file_pathes = os.listdir(data_folder)
    file_pathes = [os.path.join(data_folder, file_path)
                   for file_path in file_pathes]
    
    calc_stats = Calc_Mean()
    
    
    times = []
    current_times = measure_time(times_to_test, do_sequential,
                                 file_pathes=file_pathes,
                                 calc_stats=calc_stats)
    times.append(np.mean(current_times))
    
    
    for threads_num in THREADS_NUMS_FOR_TEST:
        current_times = measure_time(times_to_test, do_parallel,
                                     file_pathes=file_pathes,
                                     calc_stats=calc_stats,
                                     threads_num=threads_num)
        times.append(np.mean(current_times))
    
    
    print(f'Sequential: {times[0]}\n')
    for i, threads_num in enumerate(THREADS_NUMS_FOR_TEST):
        print(f'Parallel with {threads_num} threads: {times[i + 1]}')
        print(f'Acceleration {times[0] / times[i + 1]}\n')

    
if __name__ == '__main__':
    main()