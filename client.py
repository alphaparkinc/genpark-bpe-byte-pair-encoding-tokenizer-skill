import collections

class BPETokenizer:
    """
    Byte-Pair Encoding (BPE) Subword Tokenizer.
    Trains vocabulary merge rules and tokenizes raw strings.
    """
    def __init__(self):
        self.merges = {}

    def train(self, texts, num_merges=10):
        corpus = [" ".join(list(word)) + " </w>" for text in texts for word in text.split()]
        for _ in range(num_merges):
            pairs = collections.defaultdict(int)
            for word in corpus:
                symbols = word.split()
                for i in range(len(symbols) - 1):
                    pairs[(symbols[i], symbols[i + 1])] += 1
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            self.merges[best] = "".join(best)
            new_corpus = []
            for word in corpus:
                symbols = word.split()
                new_symbols = []
                idx = 0
                while idx < len(symbols):
                    if idx < len(symbols) - 1 and (symbols[idx], symbols[idx + 1]) == best:
                        new_symbols.append("".join(best))
                        idx += 2
                    else:
                        new_symbols.append(symbols[idx])
                        idx += 1
                new_corpus.append(" ".join(new_symbols))
            corpus = new_corpus

    def tokenize_word(self, word):
        symbols = list(word) + ["</w>"]
        for pair, merged in self.merges.items():
            new_symbols = []
            idx = 0
            while idx < len(symbols):
                if idx < len(symbols) - 1 and (symbols[idx], symbols[idx + 1]) == pair:
                    new_symbols.append(merged)
                    idx += 2
                else:
                    new_symbols.append(symbols[idx])
                    idx += 1
            symbols = new_symbols
        return symbols
