"""
AtCoder Grand Contest 009 A - Multiple Array の解答例

問題: 配列Aの各要素を操作してB[i]の倍数にするための最小操作回数を求める
各操作では任意の要素A[i]を1増やすことができる
ただし、i番目の要素を操作すると、それ以前の要素(0からi-1まで)も同時に1増える
"""


def solve(N: int, A: list[int], B: list[int]) -> int:
    """
    最小操作回数を計算する

    Args:
        N: 配列の要素数
        A: 操作対象の配列
        B: 目標となる倍数の配列

    Returns:
        最小操作回数
    """
    total_sum = 0

    # 後ろから処理していく（後ろの+1の操作をするとそれより前の配列も+1される問題の制約があるため）
    for i in range(N - 1, -1, -1):
        # 前回までの操作回数を足す
        A[i] += total_sum

        # A[i]をB[i]で割った余り
        amari = A[i] % B[i]

        # 余りがあれば、B[i]の倍数にするために必要な操作回数を計算
        D = 0
        if amari != 0:
            # 余り分の+1を行うことで倍数になる
            D = B[i] - amari

        total_sum += D

    return total_sum


def main() -> None:
    """メイン処理"""
    # 入力
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 答え
    result = solve(N, A, B)
    print(result)


if __name__ == "__main__":
    main()
