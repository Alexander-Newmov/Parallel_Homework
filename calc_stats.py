from typing import List
import abc
import cv2
import numpy as np


class Calc_Stats(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __call__(self, file_path: List[str]):
        pass
    
    @abc.abstractmethod
    def aggregate_results(self, results):
        pass
    

class Calc_Mean(Calc_Stats):
    def __call__(self, file_path: List[str]):
        image = cv2.imread(file_path)
        mean = np.mean(image)
        
        return mean

    def aggregate_results(self, results):
        result = np.mean(results) / len(results)
        
        return result
