from typing import List
from joblib import Parallel, delayed

from calc_stats import Calc_Stats


def do_parallel(file_pathes: List[str], calc_stats: Calc_Stats, threads_num: int):
    stats = Parallel(n_jobs=threads_num)(
        delayed(calc_stats)(file_path) for file_path in file_pathes)
    
    return calc_stats.aggregate_results(stats)


def do_sequential(file_pathes: List[str], calc_stats: Calc_Stats):
    stats = [None] * len(file_pathes)
    for i, file_path in enumerate(file_pathes):
        stats[i] = calc_stats(file_path)
        
    return calc_stats.aggregate_results(stats)
