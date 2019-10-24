#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import itertools
class Solution:
    """
    The most frequent appear element determin the output
    (except len(tasks) exceed the max number of occurence)
    Hence A__A__A+ is the general pattern for the answer
    Where A is the most frequent occurring element
    The return value would be: (A__A__...) + (A+ possible other tasks which appear same times)
    (A__) has interval of n+1, times (max_times_of_occuring - 1), will be (A__A__...) 
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if n == 0:
            return len(tasks)
        # have to sort list in order to use itertools.groupby
        tasks.sort()
        tasks_dict = { key: len(list(group)) for key, group in itertools.groupby(tasks) }
        max_len = max(tasks_dict.values())
        replica = 0
        for value in tasks_dict.values():
            if value == max_len:
                replica += 1
        return max(len(tasks), (max_len-1) * (n+1) + replica)

# @lc code=end

