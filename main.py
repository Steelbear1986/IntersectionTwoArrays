class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums2)  # Подсчитываем количество каждого элемента в nums2
        answer = []
        for num in nums1:
           if counter[num] > 0:  # Если элемент есть в nums2
               answer.append(num)
               counter[num] -= 1  # Уменьшаем счетчик

        return answer