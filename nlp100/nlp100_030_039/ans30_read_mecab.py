
def read_mecab(f):
    sentences = []
    words = []
    while True:
        line = f.readline()
        print(line)
        if not line:
            break
        if line == 'EOS':
            # なぜここに入らない..
            sentences.append(words)
            words = []
            continue
        # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
        surface, feature_csv = line.split('\t')
        features = feature_csv.split(',')
        d = {
            'surface': surface,
            'base': features[6],
            'pos': features[0],
            'pos1': features[1]
        }
        words.append(d)
    return sentences




with open('input/neko.txt.mecab', mode='r', encoding='utf-8') as f:
    sentences = read_mecab(f)
    print(sentences)