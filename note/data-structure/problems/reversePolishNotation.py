"""
逆ポーランド記法 (Reverse Polish Notation, RPN) の評価

問題 9.2: 逆ポーランド記法で記述された式を評価するアルゴリズム

逆ポーランド記法とは:
- 演算子を後置記法で記述する方式
- 例: (3 + 4) * (1 - 2) → 3 4 + 1 2 - *

アルゴリズム:
1. 左から順に要素を読む
2. 数値ならスタックに積む
3. 演算子なら、スタックから2つ取り出して計算し、結果をスタックに積む
4. 最後にスタックに残った値が答え

時間計算量: O(N) (N は要素数)
空間計算量: O(N) (スタックの最大サイズ)
"""


def evaluate_rpn(tokens: list[str]) -> int:
    """
    逆ポーランド記法で記述された式を評価する

    Args:
        tokens: 逆ポーランド記法で記述された式のトークンリスト
                例: ["3", "4", "+", "1", "2", "-", "*"]

    Returns:
        評価結果の整数値

    Raises:
        ValueError: 不正な式の場合
    """
    if not tokens:
        raise ValueError("Empty expression")

    stack: list[int] = []

    for token in tokens:
        # 演算子かどうかを判定
        if token in ["+", "-", "*", "/"]:
            # スタックから2つの値を取り出す
            if len(stack) < 2:
                raise ValueError(f"Invalid expression: not enough operands for {token}")

            # 注意: 後から取り出した値が左オペランド、先に取り出した値が右オペランド
            right = stack.pop()
            left = stack.pop()

            # 演算を実行
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                # 整数除算を使用
                if right == 0:
                    raise ValueError("Division by zero")
                # Pythonの整数除算は負の数で注意が必要
                # -3 // 2 = -2 だが、切り捨てではなく切り下げ
                result = int(left / right)

            stack.append(result)
        else:
            # 数値の場合、スタックに積む
            try:
                num = int(token)
                stack.append(num)
            except ValueError:
                raise ValueError(f"Invalid token: {token}")

    # 最終的にスタックには1つの値だけが残るはず
    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands")

    return stack[0]


def infix_to_rpn(expression: str) -> list[str]:
    """
    中置記法を逆ポーランド記法に変換する (おまけ機能)

    Args:
        expression: 中置記法の式 (例: "(3+4)*(1-2)")

    Returns:
        逆ポーランド記法のトークンリスト

    Note:
        簡易実装のため、空白区切りの式を想定
        例: "( 3 + 4 ) * ( 1 - 2 )"
    """
    # 演算子の優先順位
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    output: list[str] = []
    operator_stack: list[str] = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (
            token[0] == "-" and len(token) > 1 and token[1:].isdigit()
        ):
            # 数値の場合
            output.append(token)
        elif token in precedence:
            # 演算子の場合
            while (
                operator_stack
                and operator_stack[-1] != "("
                and precedence.get(operator_stack[-1], 0) >= precedence[token]
            ):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # "(" を除去

    # 残った演算子を全て出力
    while operator_stack:
        output.append(operator_stack.pop())

    return output
