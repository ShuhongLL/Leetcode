class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = []
        letters = {}
        for log in logs:
            log_list = log.split(' ')
            body = ' '.join(log_list[1:])
            head = ' '.join(log_list[:1])
            if str.isdigit(body.replace(' ', '')):
                nums.append(log)
            else:
                # note: body may be the same
                # hence add head into key
                letters[(body, head)] = log
        return [letters[key] for key in sorted(letters)] + nums
