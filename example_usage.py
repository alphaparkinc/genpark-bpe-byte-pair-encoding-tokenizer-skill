from client import BPETokenizer

def main():
    print("=== Testing Byte-Pair Encoding (BPE) Tokenizer ===")
    bpe = BPETokenizer()
    bpe.train(["low", "lowest", "newer", "wider"], num_merges=3)
    toks = bpe.tokenize_word("low")
    print("Tokenized 'low':", toks)
    assert len(toks) > 0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
