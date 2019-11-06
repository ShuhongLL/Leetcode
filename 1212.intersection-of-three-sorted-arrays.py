class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def findIntersection(nums1: List[int], nums2: List[int]):
            result = []
            while nums1 and nums2:
                v1, v2 = nums1[0], nums2[0]
                if nums1[0] == nums2[0]:
                    result.append(nums1[0])
                    while nums1 and nums1[0] == v1: nums1.pop(0)
                    while nums2 and nums2[0] == v2: nums2.pop(0)
                elif nums1[0] < nums2[0]:
                    while nums1 and nums1[0] == v1: nums1.pop(0)
                else:
                     while nums2 and nums2[0] == v2: nums2.pop(0)
            return result
        first = findIntersection(arr1, arr2)
        return findIntersection(first, arr3)
