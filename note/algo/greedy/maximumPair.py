"""
最大ペア数問題

N個の整数a0, a1, ..., aN-1とN個の整数b0, b1, ..., bN-1が与えられる
aから何個かとbから何個か選んでペア(ai, bj)を作る
各ペアはai < bjを満たす必要がある
最大で何ペア作れるかをO(N log N)で求める

貪欲法の戦略:
1. 両配列を昇順ソート
2. aの小さい方から順に、使える最小のbとペアにする
3. 大きいbを後のために残す（貪欲選択）
"""


def maximum_pairs(N: int, a: list[int], b: list[int]) -> int:
    """
    最大ペア数を計算する

    Args:
        N: 配列の要素数
        a: 整数配列a
        b: 整数配列b

    Returns:
        作成可能な最大ペア数
    """
    # 両配列を昇順ソート O(N log N)
    a_sorted = sorted(a)
    b_sorted = sorted(b)

    pair_count = 0
    b_index = 0  # bの現在のインデックス

    # aの各要素について、使える最小のbを探す
    for a_val in a_sorted:
        # ai < bjを満たす最小のbjを探す
        while b_index < N and b_sorted[b_index] <= a_val:
            b_index += 1

        # 使えるbが見つかった場合
        if b_index < N:
            pair_count += 1
            b_index += 1  # このbを使用済みにする

    return pair_count


def main() -> None:
    """メイン処理"""
    # 入力
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 答え
    result = maximum_pairs(N, a, b)
    print(result)


if __name__ == "__main__":
    main()
