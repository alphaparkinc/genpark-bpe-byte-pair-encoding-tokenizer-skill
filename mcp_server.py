import sys
import json
from client import BPETokenizer

def main():
    bpe = BPETokenizer()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "train":
            bpe.train(params.get("texts", []), params.get("num_merges", 5))
            res = {"status": "trained", "merge_count": len(bpe.merges)}
        elif method == "tokenize":
            res = {"tokens": bpe.tokenize_word(params.get("word", ""))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
