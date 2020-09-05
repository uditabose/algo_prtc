#!/usr/local/bin/python3
import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original = [n for n in nums]
        self.shuffled = nums


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.shuffled = [n for n in self.original]
        return self.shuffled



    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.shuffled)
        return self.shuffled



def shuffle_an_array():
    """
    https://leetcode.com/problems/shuffle-an-array/

    Time :
    Space:
    Note :
    """
    nums = [1,2,3]
    obj = Solution(nums)
    param_1 = obj.reset()
    print(param_1)
    param_2 = obj.shuffle()
    print(param_2)
    param_1 = obj.reset()
    print(param_1)


def run():
    shuffle_an_array()


if __name__ == '__main__':
    run()
