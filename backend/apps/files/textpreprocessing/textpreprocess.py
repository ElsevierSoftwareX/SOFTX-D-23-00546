import collections
import re
from konlpy.tag import Kkma

# text 문장 단위 분할하기
def splitText(text):
    sens=collections.deque()
    sentences = re.split('\. |\? |\!', text)
    for item in sentences:
        sens.append(item)

    return sens

# 단어 단위 분할

def splitSen(sentences):
    words=[]
    for sen in sentences:
        tmp = sen.split(" ")
        for item in tmp:
            words.append(item)

    return words

#lemmazation
# 쪼개진 문장들의 동사 부분을 뽑아내 원형을 만드는 함수
def lemma(words):
    kkma = Kkma()

    for idx,word in enumerate(words):
        if len(word) <= 1:
            continue
        pos = kkma.pos(word)
        result = ""
        for i, item in enumerate(pos):
            # 동사
            # 1. ~~하다 : 건강하다. 등
            if item[1] == 'NNG':
                result += item[0]
            # 2. 동사형 형태소 : 쌓다. 감사하다. 등
            if item[1] == 'VV' or item[1] == 'VA' or item[1] == 'XSV':

                # ~되다 예외
                if item[1] == 'XSV' and item[0] == '되':
                    result += '하'
                else:
                    result += item[0]

                result += '다'

                # ~게(크게 등)
                if i < len(pos) - 1 and pos[i + 1][1] == 'ECD' and pos[i + 1][0] == '게':
                    result = ""
                break

        if len(result) > 0 and result[-1] == '다':
            words[idx]=result

    return words