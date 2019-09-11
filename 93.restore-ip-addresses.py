#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # no answer
        if not s or len(s) < 4:
            return []
        self.result = []
        self.string = s
        self.recursiveDfs([self.string[0]], 1, 1)
        return self.result
        
    def recursiveDfs(self, partition, index, lenOfPartition):
        if index == len(self.string) and lenOfPartition == 4:
            self.result.append('.'.join(partition))

        elif index < len(self.string) and lenOfPartition <= 4:
            prev, curr = partition[-1], self.string[index]

            # start a new partition
            if lenOfPartition < 4:
                self.recursiveDfs(partition + [curr], index + 1, lenOfPartition + 1)
            # if the previous value is less than 255
            # then append to the previous value
            if int(partition[-1] + curr) <= 255 and prev != '0':
                partition[-1] += curr
                self.recursiveDfs(partition, index + 1, lenOfPartition)

