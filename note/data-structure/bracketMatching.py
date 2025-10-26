"""
括弧列の判定と対応関係の検出

問題 9.3: 括弧列が正しいかを判定し、各括弧の対応関係を O(N) で求める

正しい括弧列の条件:
1. '(' と ')' が同数
2. 左から見て、任意の位置で ')' の数が '(' の数を超えない
3. すべての '(' に対応する ')' が存在する

アルゴリズム:
1. スタックを使用
2. '(' が来たらその位置(インデックス)をスタックに積む
3. ')' が来たらスタックから取り出し、対応関係を記録
4. 最後にスタックが空なら正しい括弧列

時間計算量: O(N) (N は文字列長)
空間計算量: O(N) (スタックの最大サイズ)
"""

from typing import Optional


def check_brackets(s: str) -> tuple[bool, dict[int, int]]:
    """
    括弧列が正しいかを判定し、各括弧の対応関係を返す

    Args:
        s: 括弧列の文字列（'(' と ')' のみ）

    Returns:
        タプル (is_valid, matching)
        - is_valid: 括弧列が正しいかどうか
        - matching: 括弧の対応関係を表す辞書
          key: '(' の位置、value: 対応する ')' の位置
          key: ')' の位置、value: 対応する '(' の位置

    Examples:
        >>> check_brackets("(())")
        (True, {0: 3, 1: 2, 2: 1, 3: 0})

        >>> check_brackets("(()")
        (False, {})
    """
    if not s:
        return (True, {})

    stack: list[int] = []  # '(' の位置を保存するスタック
    matching: dict[int, int] = {}  # 括弧の対応関係

    for i, char in enumerate(s):
        if char == "(":
            # 開き括弧の場合、その位置をスタックに積む
            stack.append(i)
        elif char == ")":
            # 閉じ括弧の場合
            if not stack:
                # スタックが空なら、対応する '(' がないので不正
                return (False, {})

            # スタックから '(' の位置を取り出す
            open_pos = stack.pop()

            # 対応関係を記録（双方向）
            matching[open_pos] = i  # '(' → ')'
            matching[i] = open_pos  # ')' → '('
        else:
            # '(' と ')' 以外の文字があれば不正
            return (False, {})

    # 最後にスタックが空なら正しい括弧列
    is_valid = len(stack) == 0

    if not is_valid:
        # 対応していない '(' が残っている場合は無効
        return (False, {})

    return (is_valid, matching)


def visualize_brackets(s: str) -> str:
    """
    括弧列の対応関係を視覚的に表示する

    Args:
        s: 括弧列の文字列

    Returns:
        対応関係を示す文字列表現
    """
    is_valid, matching = check_brackets(s)

    if not is_valid:
        return f"不正な括弧列: {s}"

    lines = []
    lines.append(f"括弧列: {s}")
    lines.append(f"位置  : {' '.join(str(i % 10) for i in range(len(s)))}")
    lines.append("")

    # 各開き括弧について対応関係を表示
    for i, char in enumerate(s):
        if char == "(":
            close_pos = matching[i]
            lines.append(f"  {i} 文字目 '(' ←→ {close_pos} 文字目 ')'")

    return "\n".join(lines)


def find_matching_bracket(s: str, pos: int) -> Optional[int]:
    """
    指定位置の括弧に対応する括弧の位置を返す

    Args:
        s: 括弧列の文字列
        pos: 括弧の位置

    Returns:
        対応する括弧の位置。対応がない場合は None
    """
    is_valid, matching = check_brackets(s)

    if not is_valid:
        return None

    return matching.get(pos)


def get_depth_at_position(s: str, pos: int) -> Optional[int]:
    """
    指定位置での括弧のネスト深さを返す

    Args:
        s: 括弧列の文字列
        pos: 位置

    Returns:
        ネスト深さ。不正な括弧列の場合は None
    """
    is_valid, _ = check_brackets(s)

    if not is_valid or pos < 0 or pos >= len(s):
        return None

    depth = 0
    for i in range(pos + 1):
        if s[i] == "(":
            depth += 1
        elif s[i] == ")":
            depth -= 1

    return depth


def main() -> None:
    """使用例とテストケース"""
    print("=== 括弧列の判定と対応関係の検出 ===\n")

    test_cases = [
        "(())",  # 正しい括弧列
        "(()(()))()",  # 正しい括弧列（複雑）
        "(((",  # 不正（閉じていない）
        ")))",  # 不正（開いていない）
        "())()",  # 不正（途中で不正）
        "",  # 空文字列（正しい）
        "()",  # 最小の正しい括弧列
        "(()())",  # 正しい括弧列
    ]

    for s in test_cases:
        print(f"テストケース: '{s}'")
        is_valid, matching = check_brackets(s)

        if is_valid:
            print("  結果: 正しい括弧列 ✓")
            if matching:
                print("  対応関係:")
                # 開き括弧のみ表示（見やすくするため）
                for i in sorted(matching.keys()):
                    if i < matching[i]:  # 開き括弧のみ
                        print(f"    {i} ←→ {matching[i]}")
            print()
            print(visualize_brackets(s))
        else:
            print("  結果: 不正な括弧列 ✗")

        print("-" * 50)
        print()

    # 特定の括弧の対応を調べる例
    print("\n=== 特定の括弧の対応関係 ===")
    s = "(()(()))()"
    print(f"括弧列: {s}")
    print(f"位置  : {' '.join(str(i % 10) for i in range(len(s)))}")
    print()

    for pos in [0, 3, 5, 7]:
        matching_pos = find_matching_bracket(s, pos)
        if matching_pos is not None:
            print(
                f"  位置 {pos} '{s[pos]}' の対応: 位置 {matching_pos} '{s[matching_pos]}'"
            )

    # ネスト深さの例
    print("\n=== ネスト深さ ===")
    s = "(()(()))"
    print(f"括弧列: {s}")
    print(f"位置  : {' '.join(str(i % 10) for i in range(len(s)))}")
    print(
        f"深さ  : {' '.join(str(get_depth_at_position(s, i) or 0) for i in range(len(s)))}"
    )


if __name__ == "__main__":
    main()
