"""
# 정렬 알고리즘
목록의 요소를 특정 순서대로 넣는 알고리즘으로 대게 숫자식 순서 (Numerical Order)와 사전식 순서 (Lexicorgraphical Order)로 정렬한다.

안정 정렬 vs 불안정 정렬 (Stable vs Unstable)
안정 정렬
ex) 시간순으로 정렬했던 요소를 지역순으로 재정렬해도 시간순서가 유지된 채 정렬됨

불안정 정렬
ex) 시간순으로 정렬했던 요소를 지역순으로 재정렬하는 경우 시간순서가 유지되지 않음
"""

"""
버블 정렬 (Bubble Sort)
  * 배열 전체를 탐색하여, 인접한 두 요소 간 순서가 잘못된 것의 위치를 바꾼다.
  * 시간 복잡도는 항상 O(n^2)
"""
def bubble_sort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A) - 1):
            if A[j] > A[i + 1]:
                A[j], A[i] = A[i], A[j]

"""
병합 정렬 (Merge Sort)
  * 각 요소들을 더 이상 쪼갤 수 없을 만큼 분할한 후, 대소를 비교하며 병합하며 정렬한다.
  * 분할 정복 (Division and Conquer)의 진수를 보여주는 알고리즘이다.
  * 최선 최악 모두 O(n log n)
  * 대부분의 경우 Quick sort보다 느리지만, 일정한 실행 속도를 가지고 있음
  * 안정 정렬 (Stable sort)라는 점에서 여전히 많이 사용되고 있음
  * 각 요소들을 dd
"""

"""
퀵 정렬 (Quick Sort)
  * pivot을 기준으로 좌우를 나누는 특성 때문에 파티션 교환 정렬이라고도 불린다.
  * 분할 정복 알고리즘 중 하나이며, 피벗보다 작은 경우 왼쪽, 큰 경우 오른쪽에 위치시키며 정렬한다.
  * 매우 빠르며 효율적인 정렬알고리즘 이지만, 최악의 경우 O(n^2)가 된다.
  * 입력 값에 따라서 성능이 좌우될 수 있는 알고리즘이다.
"""

def quick_sort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort(A, lo, pivot - 1)
        quick_sort(A, pivot + 1, hi)


