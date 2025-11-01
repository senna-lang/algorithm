class Heap:
    """最大ヒープの実装"""

    def __init__(self):
        self.heap = []

    def push(self, x):
        """ヒープに値 x を挿入する"""
        self.heap.append(x)
        i = len(self.heap) - 1

        while i > 0:
            # 親頂点とindexを取得する
            p = (i - 1) // 2
            # 親頂点の値と挿入値の比較
            if self.heap[p] >= x:
                # ヒープの関係性であれば挿入完了
                break
            # 親頂点の値を子頂点の位置に持ってくる（穴あけ法なのでこの時まだxの代入はしない）
            self.heap[i] = self.heap[p]
            i = p
        # 最後にヒープ構造の構築が保障されてからxを穴に代入
        self.heap[i] = x

    def top(self):
        """最大値を知る"""
        if not self.heap:
            return -1
        return self.heap[0]

    def pop(self):
        """最大値を削除する"""
        if not self.heap:
            return

        # 最後尾の値を取得（ルートに持ってくる候補）
        x = self.heap[-1]
        # 最後尾を削除
        self.heap.pop()

        # ヒープが空になった場合は終了
        if not self.heap:
            return

        # 穴を根から降ろしていく
        i = 0
        # 左の子が存在する限りループ
        while i * 2 + 1 < len(self.heap):
            # 左の子の位置
            child1 = i * 2 + 1
            # 右の子の位置
            child2 = i * 2 + 2

            # 子頂点同士を比較して大きい方を child1 とする
            if child2 < len(self.heap) and self.heap[child2] > self.heap[child1]:
                child1 = child2

            # 逆転がなければ終了（xの方が大きいまたは等しい）
            if self.heap[child1] <= x:
                break

            # 自分の値を子頂点の値にする（子を上に上げる）
            self.heap[i] = self.heap[child1]
            # 自分は下に行く
            i = child1

        # x は最終的にこの位置にもってくる
        self.heap[i] = x

    def is_empty(self):
        return len(self.heap) == 0


class MinHeap:
    """最小ヒープの実装"""

    def __init__(self):
        self.heap = []

    def push(self, x):
        """ヒープに値 x を挿入する"""
        self.heap.append(x)
        i = len(self.heap) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] <= x:
                break
            self.heap[i] = self.heap[p]
            i = p

        self.heap[i] = x

    def top(self):
        """最小値を知る"""
        if not self.heap:
            return -1
        return self.heap[0]

    def pop(self):
        """最小値を削除する"""
        if not self.heap:
            return

        x = self.heap[-1]
        self.heap.pop()

        if not self.heap:
            return

        i = 0
        while i * 2 + 1 < len(self.heap):
            child1 = i * 2 + 1
            child2 = i * 2 + 2

            if child2 < len(self.heap) and self.heap[child2] < self.heap[child1]:
                child1 = child2

            if self.heap[child1] >= x:
                break

            self.heap[i] = self.heap[child1]
            i = child1

        self.heap[i] = x

    def is_empty(self):
        return len(self.heap) == 0


def main():
    """使用例"""
    print("=== 最大ヒープの例 ===")
    h = Heap()

    h.push(5)
    h.push(3)
    h.push(7)
    h.push(1)

    print(f"h.top() = {h.top()}")  # 7
    h.pop()
    print(f"h.top() = {h.top()}")  # 5

    h.push(11)
    print(f"h.top() = {h.top()}")  # 11

    print()
    print("=== 最小ヒープの例 ===")
    min_h = MinHeap()

    min_h.push(5)
    min_h.push(3)
    min_h.push(7)
    min_h.push(1)

    print(f"min_h.top() = {min_h.top()}")  # 1
    min_h.pop()
    print(f"min_h.top() = {min_h.top()}")  # 3


if __name__ == "__main__":
    main()
