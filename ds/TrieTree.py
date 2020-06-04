class TrieTree:
    def __init__(self, size, char2id, word_list, values):
        self.base = [0 for i in range(size)]
        self.check = [0 for i in range(size)]
        self.check_size = size
        self.word_list = word_list
        self.char2id = char2id
        self.values = values
        self.l = 1

    def build(self):
        self.dfs(1, 0, len(self.word_list), 0)

    def dfs(self, s, start, end, char_idx):
        next_node = []
        # 終端文字は最初にしか来ないので処理
        is_end = len(self.word_list[start]) == char_idx
        if is_end:
            prev_char = '#'
        else:
            prev_char = self.word_list[start][char_idx]

        # 次に遷移できる文字の一覧を作成
        for i in range(start+1, end):
            char = self.word_list[i][char_idx]
            if char != prev_char:
                next_node += [[start, i, self.char2id[prev_char]]]
                start = i
                prev_char = char
        next_node += [[start, end, self.char2id[prev_char]]]
        
        # 現在のノードが分岐のない自明な終端なら，親ノードに値を格納
        if len(next_node) == 1 and next_node[0][2] == 0:
            self.base[s] = -self.values[next_node[0][0]]
            return

        # 使用可能なcheckのindexを探索
        x = self.l
        is_find = False
        while not is_find:
            is_find = True
            for _, _, ki in next_node:
                if self.check[x+ki] != 0:
                    is_find = False
                    x += 1
                    break
        
        # baseとcheckの更新処理
        self.base[s] = x
        for i, _, ki in next_node:
            self.check[x+ki] = s
            if ki == 0:
                self.base[x+ki] = -self.values[i]
        
        # 次の文字への遷移
        for ns, ne, ki in next_node:
            if ki != 0:
                self.dfs(x+ki, ns, ne, char_idx+1)
    
    def search(self, query):
        s = 1
        results = []
        for i in range(len(query)):
            t = self.base[s]
            if s == self.check[t] and self.base[t]< 0:
                results += [[query[:i], -self.base[t]]]
            t = self.base[s] + self.char2id[query[i]]
            if t >= self.check_size or s != self.check[t]:
                return results
            if self.base[t] < 0:
                results += [[query[:i+1], -self.base[t]]]
                return results
            s = t
        t = self.base[s]
        if s == self.check[t] and self.base[t]< 0:
            results += [[query[:len(query)], -self.base[t]]]
        return results

if __name__ == '__main__':
    S = input()
    # 文字idは1から割り振って，0は終端文字
    char2id = {'#':0, 'a':1, 'b':2, 'c':3, 'd':4}
    # wordsはsortしておく
    words = ['a', 'ac', 'b', 'cab', 'cd']
    # valuesは単語idとか出現コスト
    values = [1, 2, 3, 4, 5]
    # 第一引数は適当に大きめの数字を取る(あまり良くない...)
    trie = TrieTree(16, char2id, words, values)
    trie.build()
    print(trie.base)
    print(trie.check)
    # results = trie.search('abcd')
    results = trie.search(S)
    print(results)
