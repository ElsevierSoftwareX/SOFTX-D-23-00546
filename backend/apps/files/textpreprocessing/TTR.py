import collections


# 단어 전체 ttr
def lemmaTtr(words):
    types = collections.defaultdict(int)
    for word in words:
        types[word] = types[word] + 1

    return len(types) / len(words)


# 단어 50개단위 TTR
def lemmaMattr(words):
    if len(words) < 50:
        return -1
    idx = 0
    ttr = 0.0
    cnt = 0
    while idx <= len(words):
        types = collections.defaultdict(int)
        ttrList = words[idx:idx + 50]
        if len(ttrList)==0:
            return 0
        for word in ttrList:
            types[word] = types[word] + 1
        cnt += 1
        ttr += len(types) / len(ttrList)
        idx += 50
    if cnt==0:
        return 0
    return ttr / cnt


# 어휘형태소(명사 동사 형용사 부사) 개수의 비율
def lexicalDensityTokens(words, kkma):
    cnt = 0
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            totalCnt += len(pos)
            if "NN" in morp[1] or "V" in morp[1] or "MA" in morp[1]:
                cnt += 1

    return cnt / totalCnt


# 어휘형태소 종류의 비율
def lexicalDensityTypes(words, kkma):
    type = collections.defaultdict(int)
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            totalCnt += len(pos)
            if "NN" in morp[1] or "V" in morp[1] or "MA" in morp[1]:
                type[morp[0]] = type[morp[0]] + 1

    return len(type) / totalCnt


def contentTtr(words, kkma):
    type = collections.defaultdict(int)
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            if "NN" in morp[1] or "V" in morp[1] or "MA" in morp[1]:
                try:
                    type[morp[0]] = type[morp[0]] + 1
                except:
                    type[morp[0]]=0
                totalCnt += 1

    return len(type) / totalCnt


def functionTtr(words,kkma):
    type = collections.defaultdict(int)
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            if ("J" in morp[1] or "E" in morp[1]) and(morp[1]!="MAJ" or morp[1]!="SE"):
                type[morp[0]] = type[morp[0]] + 1
                totalCnt += 1

    return len(type) / totalCnt


def functionMattr(words,kkma):

    if len(words) < 50:
        return -1
    idx = 0
    ttr = 0.0
    cnt = 0
    while idx <= len(words):
        type = collections.defaultdict(int)
        leng=0
        ttrList = words[idx:idx + 50]
        for word in ttrList:
            pos = kkma.pos(word)
            leng+=len(pos)
            for morp in pos:
                if ("J" in morp[1] or "E" in morp[1]) and (morp[1] != "MAJ" or morp[1] != "SE"):
                    type[morp[0]] = type[morp[0]] + 1
        cnt += 1
        ttr += len(type) / leng
        idx += 50

    return ttr / cnt

def nounTtr(words,kkma):

    type = collections.defaultdict(int)
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            if "N" in morp[1] and morp[1] != "ON":
                type[morp[0]] = type[morp[0]] + 1
                totalCnt += 1

    return len(type) / totalCnt

def verbTtr(words,kkma):
    type = collections.defaultdict(int)
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            if "V" in morp[1] and (morp[1] != "XPV" or morp[1] != "XSV"):
                type[morp[0]] = type[morp[0]] + 1
                totalCnt += 1

    return len(type) / totalCnt


def adjTtr(words,kkma):
    type = collections.defaultdict(int)
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            if "VXA" in morp[1] or "VA" in morp[1]:
                type[morp[0]] = type[morp[0]] + 1
                totalCnt += 1
    if totalCnt==0:
        return 0
    return len(type) / totalCnt

def advTtr(words,kkma):
    type = collections.defaultdict(int)
    totalCnt = 0

    for word in words:
        pos = kkma.pos(word)
        for morp in pos:
            if "MAG" in morp[1] or "MAJ" in morp[1]:
                type[morp[0]] = type[morp[0]] + 1
                totalCnt += 1
    if totalCnt==0:
        return 0
    else:
        return len(type) / totalCnt

#대명사
def prpTtr(words,kkma,pronounList):
    pronounNum=0
    type = collections.defaultdict(int)

    lemma=kkma.pos(words)

    oneLetterPronounFlag = False

    for pron in pronounList:

        for i, word in enumerate(lemma):

            # 이 책, 이 사람, 저 때 등 이,그,저 + @인 경우
            if oneLetterPronounFlag == True:
                oneLetterPronounFlag = False
                type[word] = type[word] + 1
                pronounNum+=1
                continue

            # 대명사를 내포하는지 체크 또한 접속사일 경우 제외
            if word[0:len(pron)] == pron:
                type[word] = type[word]+1
                pronounNum+=1

            # 단 '이', '그', '저'는 한글자로만 사용되므로 예외
            elif (pron == '이' and word == '이') or (pron == '그' and word == '그') or (pron == '저' and word == '저'):
                oneLetterPronounFlag = True


    return len(type),pronounNum, len(type)/pronounNum

#명사와 대명사, 대명사는 나중에~
def argumentTtr(uniqueNoun,nounNum,uniquePronoun,pronounNum):

    return (uniquePronoun+uniqueNoun)/(nounNum+pronounNum)


def bigramLemmaTtr(words):

    n=2
    ngrams = []
    for b in range(0, len(words) - n + 1):
        ngrams.append(tuple(words[b:b + n]))
    uniquengrams=set(ngrams)

    return len(uniquengrams)/len(ngrams)


def trigramLemmaTtr(words):
    n = 3
    ngrams = []
    for b in range(0, len(words) - n + 1):
        ngrams.append(tuple(words[b:b + n]))
    uniquengrams = set(ngrams)

    return len(uniquengrams) / len(ngrams)
