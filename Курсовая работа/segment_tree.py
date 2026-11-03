"""Простое дерево отрезков: сумма, минимум, максимум, точечное изменение."""


class SegmentTree:
    """Индексы в методах начинаются с нуля."""

    def __init__(self, values):
        if not values:
            raise ValueError("Массив не должен быть пустым")
        self.data = list(values)
        self.n = len(self.data)
        self.sums = [0] * (4 * self.n)
        self.minimums = [0] * (4 * self.n)
        self.maximums = [0] * (4 * self.n)
        self.intervals = {}
        self._build(1, 0, self.n - 1)

    def _build(self, node, left, right):
        self.intervals[node] = (left, right)
        if left == right:
            value = self.data[left]
            self.sums[node] = value
            self.minimums[node] = value
            self.maximums[node] = value
            return
        middle = (left + right) // 2
        self._build(node * 2, left, middle)
        self._build(node * 2 + 1, middle + 1, right)
        self._recalculate(node)

    def _recalculate(self, node):
        a, b = node * 2, node * 2 + 1
        self.sums[node] = self.sums[a] + self.sums[b]
        self.minimums[node] = min(self.minimums[a], self.minimums[b])
        self.maximums[node] = max(self.maximums[a], self.maximums[b])

    def query(self, left, right, operation="sum"):
        """Вернуть сумму/min/max на включительном отрезке [left, right]."""
        result, _, _ = self.query_with_steps(left, right, operation)
        return result

    def query_with_steps(self, left, right, operation="sum"):
        """Для рисунка дополнительно возвращает посещенные и выбранные узлы."""
        if not 0 <= left <= right < self.n:
            raise IndexError("Неверные границы отрезка")
        if operation not in ("sum", "min", "max"):
            raise ValueError("Операция должна быть sum, min или max")

        tree = {"sum": self.sums, "min": self.minimums,
                "max": self.maximums}[operation]
        visited, selected = set(), set()

        def search(node, lo, hi):
            visited.add(node)
            if left <= lo and hi <= right:
                selected.add(node)
                return tree[node]

            mid = (lo + hi) // 2
            if right <= mid:
                return search(node * 2, lo, mid)
            if left > mid:
                return search(node * 2 + 1, mid + 1, hi)

            a = search(node * 2, lo, mid)
            b = search(node * 2 + 1, mid + 1, hi)
            if operation == "sum":
                return a + b
            if operation == "min":
                return min(a, b)
            return max(a, b)

        return search(1, 0, self.n - 1), visited, selected

    def update(self, index, new_value):
        """Изменить один элемент и вернуть узлы, пересчитанные при изменении."""
        if not 0 <= index < self.n:
            raise IndexError("Неверный индекс элемента")
        self.data[index] = new_value
        changed = set()

        def change(node, lo, hi):
            changed.add(node)
            if lo == hi:
                self.sums[node] = new_value
                self.minimums[node] = new_value
                self.maximums[node] = new_value
                return
            mid = (lo + hi) // 2
            if index <= mid:
                change(node * 2, lo, mid)
            else:
                change(node * 2 + 1, mid + 1, hi)
            self._recalculate(node)

        change(1, 0, self.n - 1)
        return changed
