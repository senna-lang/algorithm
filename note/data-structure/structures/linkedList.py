class Node:
    def __init__(self, name=""):
        self.name = name
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        # 番兵ノードをグローバル領域に置いておく
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil
    
    def insert(self, v, p=None):
        # ノード p の直後にノード v を挿入する
        if p is None:
            p = self.nil
        
        v.next = p.next
        p.next.prev = v
        p.next = v
        v.prev = p
    
    def erase(self, v):
        # ノード v を削除する
        if v == self.nil:
            return  # v が番兵の場合は何もしない
        
        v.prev.next = v.next
        v.next.prev = v.prev
        # Pythonではメモリの開放は自動的に行われるので、明示的な削除は不要
    
    def print_list(self):
        # 連結リストを出力する
        cur = self.nil.next  # 先頭から出発
        while cur != self.nil:
            print(f"{cur.name} -> ", end="")
            cur = cur.next
        print()

def main():
    # 初期化
    linked_list = DoublyLinkedList()
    
    # 作りたいノードの名前の一覧
    # 最後のノード（「山本」）から順に挿入することに注意
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]
    
    # 連結リスト作成: 各ノードを生成して連結リストの先頭に挿入していく
    watanabe = None
    for i in range(len(names)):
        # ノードを作成する
        node = Node(names[i])
        
        # 作成したノードを連結リストの先頭に挿入する
        linked_list.insert(node)
        
        # 「渡辺」ノードを保存しておく
        if names[i] == "watanabe":
            watanabe = node
    
    # 「渡辺」ノードを削除する
    print("before: ")
    linked_list.print_list()  # 削除前を出力
    
    linked_list.erase(watanabe)
    
    print("after: ")
    linked_list.print_list()  # 削除後を出力

if __name__ == "__main__":
    main()