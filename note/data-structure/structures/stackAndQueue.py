"""
スタックの実装

Code 9.1 - 配列を用いたスタックの実装
例外処理:
- スタックが空のとき (top == 0) に pop しようとする場合
- スタックが満杯のとき (top == MAX) に push しようとする場合
"""


class Stack:
    """
    スタックの実装

    Attributes:
        MAX: スタック配列の最大サイズ
        st: スタックを表す配列
        top: スタックの先頭を表す添字
    """

    def __init__(self, max_size: int = 100000) -> None:
        """
        スタックを初期化する

        Args:
            max_size: スタックの最大サイズ (デフォルト: 100000)
        """
        self.MAX = max_size
        self.st: list[int] = [0] * self.MAX
        self.top = 0

    def init(self) -> None:
        """
        スタックを初期化する
        スタックの添字を初期位置に戻す
        """
        self.top = 0

    def is_empty(self) -> bool:
        """
        スタックが空かどうかを判定する

        Returns:
            スタックサイズが 0 かどうか
        """
        return self.top == 0

    def is_full(self) -> bool:
        """
        スタックが満杯かどうかを判定する

        Returns:
            スタックサイズが MAX かどうか
        """
        return self.top == self.MAX

    def push(self, value: int) -> None:
        """
        スタックに値を追加する

        Args:
            value: 追加する値

        Raises:
            OverflowError: スタックが満杯の場合
        """
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push to a full stack")

        self.st[self.top] = value
        self.top += 1

    def pop(self) -> int:
        """
        スタックから値を取り出す

        Returns:
            スタックの先頭の値

        Raises:
            IndexError: スタックが空の場合
        """
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")

        self.top -= 1
        return self.st[self.top]

    def peek(self) -> int:
        """
        スタックの先頭の値を見る（取り出さない）

        Returns:
            スタックの先頭の値

        Raises:
            IndexError: スタックが空の場合
        """
        if self.is_empty():
            raise IndexError("Stack is empty: cannot peek")

        return self.st[self.top - 1]

    def size(self) -> int:
        """
        スタックのサイズを取得する

        Returns:
            現在のスタックのサイズ
        """
        return self.top

    def __repr__(self) -> str:
        """スタックの文字列表現"""
        elements = [str(self.st[i]) for i in range(self.top)]
        return f"Stack({' <- '.join(elements)}) [top={self.top}]"


def main() -> None:
    """使用例"""
    # スタックを作成
    stack = Stack(max_size=10)

    print("=== スタックの操作例 ===")

    # Push操作
    print("\n1. Push操作:")
    for i in [10, 20, 30, 40, 50]:
        stack.push(i)
        print(f"  push({i}) -> {stack}")

    # サイズ確認
    print(f"\nスタックサイズ: {stack.size()}")

    # Peek操作
    print(f"先頭の値 (peek): {stack.peek()}")

    # Pop操作
    print("\n2. Pop操作:")
    for _ in range(3):
        value = stack.pop()
        print(f"  pop() = {value} -> {stack}")

    # 空チェック
    print(f"\nスタックは空? {stack.is_empty()}")

    # 残りを全てpop
    print("\n3. 残りを全てpop:")
    while not stack.is_empty():
        value = stack.pop()
        print(f"  pop() = {value} -> {stack}")

    print(f"\nスタックは空? {stack.is_empty()}")

    # 例外処理の例
    print("\n4. 例外処理の例:")
    try:
        stack.pop()  # 空のスタックからpop
    except IndexError as e:
        print(f"  エラー: {e}")

    # 満杯チェック
    print("\n5. 満杯チェック:")
    small_stack = Stack(max_size=3)
    for i in [1, 2, 3]:
        small_stack.push(i)
        print(f"  push({i}) -> {small_stack}")

    print(f"スタックは満杯? {small_stack.is_full()}")

    try:
        small_stack.push(4)  # 満杯のスタックにpush
    except OverflowError as e:
        print(f"  エラー: {e}")


class Queue:
    """
    キューの実装

    Code 9.2 - 配列を用いたキューの実装
    キューが満杯のとき (head == (tail + 1) % MAX) に enqueue しようとする場合や
    キューが空のとき (head == tail) に dequeue しようとする場合について例外処理を行う

    Attributes:
        MAX: キュー配列の最大サイズ
        qu: キューを表す配列
        head: キューの先頭を表す添字 (リングバッファの読み取り位置)
        tail: キューの末尾を表す添字 (リングバッファの書き込み位置)
    """

    def __init__(self, max_size: int = 100000) -> None:
        """
        キューを初期化する

        Args:
            max_size: キューの最大サイズ (デフォルト: 100000)
        """
        self.MAX = max_size
        self.qu: list[int] = [0] * self.MAX
        self.head = 0
        self.tail = 0

    def init(self) -> None:
        """
        キューを初期化する
        head と tail を 0 に設定
        """
        self.head = 0
        self.tail = 0

    def is_empty(self) -> bool:
        """
        キューが空かどうかを判定する

        Returns:
            head == tail かどうか
        """
        return self.head == self.tail

    def is_full(self) -> bool:
        """
        キューが満杯かどうかを判定する

        Returns:
            (tail + 1) % MAX == head かどうか
            (self.tail + 1) = 次に追加する場合の位置 を最大値で割った値がheadと同じになる場合もう満杯
            リングバッファとして実装されているため満杯の場合tailが先頭に戻ってくるため 
        """
        return (self.tail + 1) % self.MAX == self.head

    def enqueue(self, value: int) -> None:
        """
        キューに要素を追加する (enqueue操作)

        Args:
            value: 追加する値

        Raises:
            OverflowError: キューが満杯の場合
        """
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue to a full queue")

        self.qu[self.tail] = value
        self.tail += 1
        if self.tail == self.MAX:
            self.tail = 0

    def dequeue(self) -> int:
        """
        キューから要素を取り出す (dequeue操作)

        Returns:
            キューの先頭の値

        Raises:
            IndexError: キューが空の場合
        """
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")

        value = self.qu[self.head]
        self.head += 1
        # リングバッファで実装しているのでheadは配列の最後まで到達したら先頭に戻ってくる必要がある
        if self.head == self.MAX:
            self.head = 0
        return value

    def peek(self) -> int:
        """
        キューの先頭の値を見る（取り出さない）

        Returns:
            キューの先頭の値

        Raises:
            IndexError: キューが空の場合
        """
        if self.is_empty():
            raise IndexError("Queue is empty: cannot peek")

        return self.qu[self.head]

    def size(self) -> int:
        """
        キューのサイズを取得する

        Returns:
            現在のキューのサイズ
        """
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.MAX - self.head + self.tail

    def __repr__(self) -> str:
        """キューの文字列表現"""
        elements = []
        i = self.head
        while i != self.tail:
            elements.append(str(self.qu[i]))
            i = (i + 1) % self.MAX
        return f"Queue({' <- '.join(elements)}) [head={self.head}, tail={self.tail}]"


def test_queue() -> None:
    """キューの使用例"""
    # キューを作成
    queue = Queue(max_size=10)

    print("\n=== キューの操作例 ===")

    # Enqueue操作
    print("\n1. Enqueue操作:")
    for i in [10, 20, 30, 40, 50]:
        queue.enqueue(i)
        print(f"  enqueue({i}) -> {queue}")

    # サイズ確認
    print(f"\nキューサイズ: {queue.size()}")

    # Peek操作
    print(f"先頭の値 (peek): {queue.peek()}")

    # Dequeue操作
    print("\n2. Dequeue操作:")
    for _ in range(3):
        value = queue.dequeue()
        print(f"  dequeue() = {value} -> {queue}")

    # 空チェック
    print(f"\nキューは空? {queue.is_empty()}")

    # 追加のenqueue (リングバッファの動作確認)
    print("\n3. 追加のenqueue (リングバッファ):")
    for i in [60, 70]:
        queue.enqueue(i)
        print(f"  enqueue({i}) -> {queue}")

    # 残りを全てdequeue
    print("\n4. 残りを全てdequeue:")
    while not queue.is_empty():
        value = queue.dequeue()
        print(f"  dequeue() = {value} -> {queue}")

    print(f"\nキューは空? {queue.is_empty()}")

    # 例外処理の例
    print("\n5. 例外処理の例:")
    try:
        queue.dequeue()  # 空のキューからdequeue
    except IndexError as e:
        print(f"  エラー: {e}")

    # 満杯チェック
    print("\n6. 満杯チェック:")
    small_queue = Queue(max_size=4)
    # MAX=4の場合、実際に格納できるのは3要素 (1つは番兵)
    for i in [1, 2, 3]:
        small_queue.enqueue(i)
        print(f"  enqueue({i}) -> {small_queue}")

    print(f"キューは満杯? {small_queue.is_full()}")

    try:
        small_queue.enqueue(4)  # 満杯のキューにenqueue
    except OverflowError as e:
        print(f"  エラー: {e}")


if __name__ == "__main__":
    main()
    test_queue()
