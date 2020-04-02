class Vector:

    def __init__(self, arr=None):
        self._size = len(arr)
        self._capacity = len(arr)
        self._elem = []
        for ele in arr:
            self._elem.append(ele)

    def size(self):
        return self._size

    def get(self, r):
        return self._elem[r]

    def put(self, r, e):
        self._elem[r] = e

    def insert(self, r, e):
        if self._size == self._capacity:
            self._elem.extend([0] * self._size)
            self._capacity *= 2
        i = self._size
        while i > r:
            self._elem[i] = self._elem[i - 1]
            i -= 1
        self._elem[r] = e
        self._size += 1

    def removeRange(self, lo, hi) -> int:
        if lo == hi:
            return 0
        while hi < self._size:
            self._elem[lo] = self._elem[hi]
            lo += 1
            hi += 1
        self._size = lo
        # TODO 删除元素
        return hi - lo

    def remove(self, r) -> int:
        return self.removeRange(r, r + 1)

    def find(self, e, lo, hi) -> int:
        hi -= 1
        while lo <= hi and e != self._elem[hi]:
            hi -= 1
        return hi

    def deduplicate(self) -> int:
        old_size = self._size
        for i in range(1, self._size):
            if self.find(self._elem[i], 0, i) < 0:
                i += 1
            else:
                self.remove(i)
        return old_size - self._size

    def traverse(self, func):
        for i in range(self._size):
            func(self._elem[i])

    def disordered(self) -> int:
        n = 0
        for i in range(self._size):
            n += 1 if self._elem[i - 1] > self._elem[i] else 0
            i += 1
        return n

    def uniquify(self) -> int:
        i = 1
        for j in range(1, self.size()):
            if self._elem[j] != self._elem[i]:
                self._elem[i] = self._elem[j]
                i += 1
        deleted_num = self._size - i
        self._size = i
        return deleted_num

    def bin_search(self, e, lo, hi) -> int:
        while lo < hi:
            mid = (lo + hi) >> 1
            if e < self._elem[mid]:
                hi = mid
            elif self._elem[mid] < e:
                lo = mid + 1
            else:
                return mid
        return -1

    def bin_search2(self, e, lo, hi) -> int:
        while hi - lo > 1:
            mid = (lo + hi) >> 1
            if e < self._elem[mid]:
                hi = mid
            else:
                lo = mid
        return lo if e == self._elem[lo] else -1

    def bin_search3(self, e, lo, hi) -> int:
        while lo < hi:
            mid = (lo + hi) >> 1
            if e < self._elem[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1

    def fib_search(self, e, lo, hi) -> int:
        mid = (lo + hi) >> 1
        while lo < hi:
            if e < self._elem[mid]:
                return self.fib_search(e, lo, mid)
            elif self._elem[mid] < e:
                return self.fib_search(e, mid + 1, hi)
            else:
                return mid
        return -1

    def interpolation_search(self, e, lo, hi) -> int:
        while lo < hi:
            mid = lo + int((hi - lo) * (e - self._elem[lo]) / (self._elem[hi] - self._elem[lo]))
            if e < self._elem[mid]:
                hi = mid - 1
            elif self._elem[mid] < e:
                lo = mid + 1
            else:
                return mid
        return -1

    def bubble_sort(self, lo, hi):
        while lo < hi:
            for j in range(lo + 1, hi):
                if self._elem[j - 1] > self._elem[j]:
                    self._elem[j - 1], self._elem[j] = self._elem[j], self._elem[j - 1]
            hi -= 1

    def bubble_sort_opt1(self, lo, hi):
        while lo < hi:
            is_sorted = True
            for j in range(lo + 1, hi):
                if self._elem[j - 1] > self._elem[j]:
                    self._elem[j - 1], self._elem[j] = self._elem[j], self._elem[j - 1]
                    is_sorted = False
            if is_sorted:
                break
            hi -= 1

    def bubble_sort_opt2(self, lo, hi):
        while lo < hi:
            sorted_idx = lo
            for j in range(lo + 1, hi):
                if self._elem[j - 1] > self._elem[j]:
                    self._elem[j - 1], self._elem[j] = self._elem[j], self._elem[j - 1]
                    sorted_idx = max(sorted_idx, j)
            if sorted_idx == -1:
                break
            hi = sorted_idx

    def merge_sort(self, lo, hi):

        if hi - lo < 2:
            return
        mi = (lo + hi) >> 1
        self.merge_sort(lo, mi)
        self.merge_sort(mi, hi)
        self._merge(lo, mi, hi)

    def _merge(self, low, mid, high):
        b = self._elem[low:mid]
        c = self._elem[mid:high]
        i = j = k = 0
        while i < high - low:
            if j < mid - low and (k >= high - mid or b[j] <= c[k]):
                self._elem[low + i] = b[j]
                j += 1
                i += 1
            if k < high - mid and (j >= mid - low or c[k] < b[j]):
                self._elem[low + i] = c[k]
                k += 1
                i += 1
                if k == high - mid:
                    self._elem[i:high] = b[j:]

    def _merge_opt(self, low, mid, high):
        b = self._elem[low:mid]
        c = self._elem[mid:high]
        i = j = k = 0
        while j < mid - low:
            if k < high - mid and c[k] < b[j]:
                self._elem[low + i] = c[k]
                k += 1
                i += 1
            if k >= high - mid or b[j] <= c[k]:
                self._elem[low + i] = b[j]
                j += 1
                i += 1


v = Vector([2, 4, 6, 7, 1, 3, 5, 6, 7])
v._merge(0, 4, 9)
print(v)
