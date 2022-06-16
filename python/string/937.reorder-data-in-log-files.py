#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        result = []
        let = {}
        for log in logs:
            log_list = log.split(' ')
            body = ' '.join(log_list[1:])
            head = ' '.join(log_list[:1])
            if str.isdigit(body.replace(' ', '')):
                result.append(log)
            else:
                let[body + head] = log
        return [let[key] for key in sorted(let)] + result

# @lc code=end

