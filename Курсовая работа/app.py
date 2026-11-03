"""Графическая демонстрация дерева отрезков. Запуск: python app.py"""

import tkinter as tk
from tkinter import ttk, messagebox

from segment_tree import SegmentTree


class SegmentTreeApp:
    COLORS = {"normal": "#f0f3f8", "visited": "#ffecaa",
              "selected": "#a9e6c4", "changed": "#add1ff"}

    def __init__(self, root):
        self.root = root
        root.title("Курсовая работа - Дерево отрезков")
        root.geometry("980x795")
        root.minsize(760, 650)
        root.configure(bg="#f7f9fc")

        self.tree = SegmentTree([5, 2, 8, 6, 1, 4, 7, 3])
        self.active = set()
        self.selected = set()
        self.changed = set()
        self.current_operation = "sum"

        ttk.Style().theme_use("clam")
        main = ttk.Frame(root, padding=15)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="ДЕРЕВО ОТРЕЗКОВ",
                  font=("DejaVu Sans", 18, "bold")).pack(anchor="w")
        ttk.Label(main, text="Простой пример: сумма, минимум, максимум и изменение элемента",
                  font=("DejaVu Sans", 10)).pack(anchor="w", pady=(2, 14))

        row = ttk.Frame(main)
        row.pack(fill="x", pady=(0, 10))
        ttk.Label(row, text="Массив:").pack(side="left", padx=(0, 8))
        self.array_entry = ttk.Entry(row)
        self.array_entry.pack(side="left", fill="x", expand=True)
        self.array_entry.insert(0, "5 2 8 6 1 4 7 3")
        ttk.Button(row, text="Построить дерево", command=self.on_build).pack(side="left", padx=(10, 0))

        panels = ttk.Frame(main)
        panels.pack(fill="x", pady=(0, 8))
        request = ttk.LabelFrame(panels, text="Запрос на отрезке (нумерация с 1)", padding=9)
        request.pack(side="left", fill="x", expand=True, padx=(0, 7))
        ttk.Label(request, text="От").pack(side="left")
        self.left_entry = ttk.Entry(request, width=4)
        self.left_entry.insert(0, "2")
        self.left_entry.pack(side="left", padx=(3, 7))
        ttk.Label(request, text="До").pack(side="left")
        self.right_entry = ttk.Entry(request, width=4)
        self.right_entry.insert(0, "6")
        self.right_entry.pack(side="left", padx=(3, 7))
        self.operation = ttk.Combobox(request, values=["Сумма", "Минимум", "Максимум"],
                                     width=10, state="readonly")
        self.operation.set("Сумма")
        self.operation.pack(side="left", padx=(0, 7))
        ttk.Button(request, text="Найти", command=self.on_query).pack(side="left")

        update = ttk.LabelFrame(panels, text="Изменить элемент", padding=9)
        update.pack(side="left", fill="x")
        ttk.Label(update, text="№").pack(side="left")
        self.index_entry = ttk.Entry(update, width=4)
        self.index_entry.insert(0, "4")
        self.index_entry.pack(side="left", padx=(3, 6))
        ttk.Label(update, text="Значение").pack(side="left")
        self.value_entry = ttk.Entry(update, width=5)
        self.value_entry.insert(0, "10")
        self.value_entry.pack(side="left", padx=(3, 7))
        ttk.Button(update, text="Изменить", command=self.on_update).pack(side="left")

        self.result_var = tk.StringVar(value="Нажмите «Найти», чтобы выполнить запрос")
        ttk.Label(main, textvariable=self.result_var,
                  font=("DejaVu Sans", 12, "bold")).pack(anchor="w", pady=(5, 3))
        self.array_var = tk.StringVar(value="Массив: [5, 2, 8, 6, 1, 4, 7, 3]")
        ttk.Label(main, textvariable=self.array_var,
                  font=("DejaVu Sans", 10)).pack(anchor="w", pady=(0, 8))

        self.canvas = tk.Canvas(main, height=410, bg="white", highlightthickness=1,
                                highlightbackground="#dce3ee")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda event: self.draw())

        legend = ttk.Frame(main)
        legend.pack(anchor="w", pady=(10, 3))
        for color, label in [("#a9e6c4", "Узлы, вошедшие в ответ"),
                             ("#ffecaa", "Просмотренные узлы"),
                             ("#add1ff", "Узлы после изменения")]:
            swatch = tk.Label(legend, bg=color, width=2, relief="solid", bd=1)
            swatch.pack(side="left", padx=(0, 5))
            ttk.Label(legend, text=label).pack(side="left", padx=(0, 16))
        ttk.Label(main, text="В кружке: отрезок [лево, право] и значение выбранной операции."
                            " Визуализация рассчитана на массив до 16 чисел.",
                  font=("DejaVu Sans", 9)).pack(anchor="w")
        self.draw()

    def on_build(self):
        try:
            values = [int(x) for x in self.array_entry.get().replace(",", " ").split()]
            if not values:
                raise ValueError("Введите хотя бы одно число")
            self.tree = SegmentTree(values)
            self.active.clear()
            self.selected.clear()
            self.changed.clear()
            self.current_operation = "sum"
            self.operation.set("Сумма")
            self.array_var.set(f"Массив: {self.tree.data}")
            self.result_var.set(f"Дерево построено. Элементов: {len(values)}")
            self.draw()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целые числа через пробел, например: 5 2 8 6")

    def on_query(self):
        try:
            left, right = int(self.left_entry.get()), int(self.right_entry.get())
            mapping = {"Сумма": ("sum", "Сумма"), "Минимум": ("min", "Минимум"),
                       "Максимум": ("max", "Максимум")}
            operation, title = mapping[self.operation.get()]
            result, self.active, self.selected = self.tree.query_with_steps(
                left - 1, right - 1, operation)
            self.current_operation = operation
            self.changed = set()
            self.result_var.set(f"{title} на отрезке [{left}, {right}] = {result}")
            self.draw()
        except (ValueError, IndexError, KeyError):
            messagebox.showerror("Ошибка", f"Введите границы от 1 до {self.tree.n}, левая не больше правой")

    def on_update(self):
        try:
            index = int(self.index_entry.get())
            value = int(self.value_entry.get())
            self.changed = self.tree.update(index - 1, value)
            self.active.clear()
            self.selected.clear()
            self.array_var.set(f"Массив: {self.tree.data}")
            self.result_var.set(f"Элемент №{index} изменён на {value}. Синим показан путь обновления")
            self.draw()
        except (ValueError, IndexError):
            messagebox.showerror("Ошибка", f"Укажите номер от 1 до {self.tree.n} и целое значение")

    def draw(self):
        canvas = self.canvas
        canvas.delete("all")
        if self.tree.n > 16:
            canvas.create_text(canvas.winfo_width() / 2, 130,
                               text="Для массива более 16 элементов дерево не рисуется.\n"
                                    "Запросы и изменения продолжают работать.",
                               font=("DejaVu Sans", 13), justify="center")
            return
        width = max(canvas.winfo_width(), 700)
        height = max(canvas.winfo_height(), 310)
        n = self.tree.n
        leaves = [width / 2] if n == 1 else [56 + (width - 112) * i / (n - 1) for i in range(n)]
        depths = self.tree.n.bit_length() + 1
        gap_y = min(100, (height - 110) / max(1, depths - 2))
        positions = {}

        def position(node, lo, hi, depth):
            x = (leaves[lo] + leaves[hi]) / 2
            y = 55 + depth * gap_y
            positions[node] = (x, y, lo, hi)
            if lo == hi:
                return
            mid = (lo + hi) // 2
            position(node * 2, lo, mid, depth + 1)
            position(node * 2 + 1, mid + 1, hi, depth + 1)
            for child in (node * 2, node * 2 + 1):
                cx, cy, _, _ = positions[child]
                canvas.create_line(x, y + 21, cx, cy - 21, fill="#a9b7c9", width=2)

        position(1, 0, n - 1, 0)
        values = {"sum": self.tree.sums, "min": self.tree.minimums,
                  "max": self.tree.maximums}[self.current_operation]
        radius = 24 if n >= 12 else 29
        for node, (x, y, lo, hi) in positions.items():
            state = "normal"
            if node in self.active:
                state = "visited"
            if node in self.selected:
                state = "selected"
            if node in self.changed:
                state = "changed"
            canvas.create_oval(x-radius, y-radius, x+radius, y+radius,
                               fill=self.COLORS[state], outline="#61768d", width=1.3)
            canvas.create_text(x, y-10, text=f"{lo+1}–{hi+1}",
                               font=("DejaVu Sans", 8))
            canvas.create_text(x, y+9, text=str(values[node]),
                               font=("DejaVu Sans", 11, "bold"))


if __name__ == "__main__":
    window = tk.Tk()
    SegmentTreeApp(window)
    window.mainloop()
