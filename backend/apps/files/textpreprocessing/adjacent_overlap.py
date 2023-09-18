import collections

pronounList=['이','그','저','이것','그것','저것','무엇','여기','저기','거기','어디',
        '저희','본인','그대','귀하','너희','당신','여러분','임자','자기','자네','이런',
         '그들','그녀','당신','저희','놈','얘','걔','쟤','누구']


#All lemmas
def adjacent_sentence_overlap_all_lemmas(now,target,kkma):

    pos_now = kkma.pos(now)
    pos_target=kkma.pos(target)
    lemma=collections.defaultdict()
    sum=0

    for item in pos_now:
        lemma[item[1]]=1

    for item in target:
        try:
            if lemma[item[1]]==1:
                lemma[item[1]]+=1
                sum+=1
        except:
            continue

    return sum

def adjacent_sentence_overlap_all_lemmas_normed(now,target,kkma):
    pos_now = kkma.pos(now)
    pos_target=kkma.pos(target)
    lemma=collections.defaultdict()

    for item in pos_now:
        lemma[item[1]]=1

    for item in target:
        try:
            if lemma[item[1]]==1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_all_lemmas(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        lemma[item[0]] = 1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_all_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        lemma[item[1]] = 1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]]+=1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]]+=1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_all_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag=False

    for item in pos_now:
        lemma[item[1]] = 1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag=True
                break
        except:
            continue

    if flag==False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_all_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        lemma[item[0]] = 1

    for item in target1:
        try:
            if lemma[item[0]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue

    return 0


#content lemmas
def adjacent_sentence_overlap_content_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()
    sum = 0

    for item in pos_now:
        if "NN" in item[1] or "V" in item[1] or "MA" in item[1]:
            lemma[item[1]]=1

    for item in target:
        try:
            if lemma[item[1]]==1:
                lemma[item[1]]+=1
                sum+=1
        except:
            continue

    return sum

def adjacent_sentence_overlap_content_lemmas_normed(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "NN" in item[1] or "V" in item[1] or "MA" in item[1]:
            lemma[item[1]]=1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_content_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "NN" in item[1] or "V" in item[1] or "MA" in item[1]:
            lemma[item[0]]=1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_content_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        if "NN" in item[1] or "V" in item[1] or "MA" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]] += 1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]] += 1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_content_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "NN" in item[1] or "V" in item[1] or "MA" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_content_lemmas(now,target1, target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "NN" in item[1] or "V" in item[1] or "MA" in item[1]:
            lemma[item[0]]=1

    for item in target1:
        try:
            if lemma[item[0]]  == 1 and ("NN" in item[1] or "V" in item[1] or "MA" in item[1]):
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]] == 1 and ("NN" in item[1] or "V" in item[1] or "MA" in item[1]):
                return 1
        except:
            continue

    return 0


#function lemmas
def adjacent_sentence_overlap_function_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()
    sum = 0

    for item in pos_now:
        if ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]]+=1
                sum += 1
        except:
            continue

    return sum

def adjacent_sentence_overlap_function_lemmas_normed(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_function_lemmas(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
            lemma[item[0]] = 1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_function_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        if ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]] += 1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]] += 1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_function_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_function_lemmas(now,target1, target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
            lemma[item[0]]=1

    for item in target1:
        try:
            if lemma[item[0]]  == 1 and ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]] == 1 and ("J" in item[1] or "E" in item[1]) and (item[1] != "MAJ" or item[1] != "SE"):
                return 1
        except:
            continue

    return 0


#noun lemmas
def adjacent_sentence_overlap_noun_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()
    sum = 0

    for item in pos_now:
        if "N" in item[1] and item[1] != "ON":
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]]+=1
                sum += 1
        except:
            continue

    return sum

def adjacent_sentence_overlap_noun_lemmas_normed(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "N" in item[1] and item[1] != "ON":
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_noun_lemmas(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "N" in item[1] and item[1] != "ON":
            lemma[item[0]] = 1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_noun_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        if "N" in item[1] and item[1] != "ON":
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]] += 1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]] += 1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_noun_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "N" in item[1] and item[1] != "ON":
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_noun_lemmas(now,target1, target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "N" in item[1] and item[1] != "ON":
            lemma[item[0]]=1

    for item in target1:
        try:
            if lemma[item[0]]  == 1 and ("N" in item[1] and item[1] != "ON"):
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]]  == 1 and ("N" in item[1] and item[1] != "ON"):
                return 1
        except:
            continue

    return 0


#verb lemmas
def adjacent_sentence_overlap_verb_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()
    sum = 0

    for item in pos_now:
        if "V" in item[1] and (item[1] != "XPV" or item[1] != "XSV"):
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]]+=1
                sum += 1
        except:
            continue

    return sum

def adjacent_sentence_overlap_verb_lemmas_normed(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "V" in item[1] and (item[1] != "XPV" or item[1] != "XSV"):
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_verb_lemmas(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "V" in item[1] and (item[1] != "XPV" or item[1] != "XSV"):
            lemma[item[0]] = 1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_verb_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        if "V" in item[1] and (item[1] != "XPV" or item[1] != "XSV"):
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]] += 1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]] += 1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_verb_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "V" in item[1] and (item[1] != "XPV" or item[1] != "XSV"):
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_verb_lemmas(now,target1, target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "V" in item[1] and (item[1] != "XPV" or item[1] != "XSV"):
            lemma[item[0]]=1

    for item in target1:
        try:
            if lemma[item[0]]  == 1 and ("V" in item[1] and (item[1] != "XPV" or item[1] != "XSV")):
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]]  == 1 and ("V" in item[1] and (item[1] != "XPV" or item[1] != "XSV")):
                return 1
        except:
            continue

    return 0


#adjective lemmas
def adjacent_sentence_overlap_adjective_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()
    sum = 0

    for item in pos_now:
        if "VXA" in item[1] or "VA" in item[1]:
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]]+=1
                sum += 1
        except:
            continue

    return sum

def adjacent_sentence_overlap_adjective_lemmas_normed(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "VXA" in item[1] or "VA" in item[1]:
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_adjective_lemmas(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "VXA" in item[1] or "VA" in item[1]:
            lemma[item[0]] = 1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_adjective_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        if "VXA" in item[1] or "VA" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]] += 1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]] += 1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_adjective_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "VXA" in item[1] or "VA" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_adjective_lemmas(now,target1, target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "VXA" in item[1] or "VA" in item[1]:
            lemma[item[0]]=1

    for item in target1:
        try:
            if lemma[item[0]]  == 1 and ("VXA" in item[1] or "VA" in item[1]):
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]]  == 1 and ("VXA" in item[1] or "VA" in item[1]):
                return 1
        except:
            continue

    return 0


#adverb lemmas
def adjacent_sentence_overlap_adverb_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()
    sum = 0

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]]+=1
                sum += 1
        except:
            continue

    return sum

def adjacent_sentence_overlap_adverb_lemmas_normed(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_adverb_lemmas(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[0]] = 1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_adverb_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]] += 1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]] += 1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_adverb_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_adverb_lemmas(now,target1, target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[0]]=1

    for item in target1:
        try:
            if lemma[item[0]]  == 1 and ("MAG" in item[1] or "MAJ" in item[1]):
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]]  == 1 and ("MAG" in item[1] or "MAJ" in item[1]):
                return 1
        except:
            continue

    return 0

#대명사는 아직 미구현~
#pronoun lemmas
def adjacent_sentence_overlap_pronoun_lemmas(now, target, kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()
    sum = 0

    oneLetterPronounFlag = False

    for pron in pronounList:

        for i, word in enumerate(lemma):

            # 이 책, 이 사람, 저 때 등 이,그,저 + @인 경우
            if oneLetterPronounFlag == True:
                oneLetterPronounFlag = False
                type[word] = type[word] + 1
                sum += 1
                continue

            # 대명사를 내포하는지 체크 또한 접속사일 경우 제외
            if word[0:len(pron)] == pron:
                type[word] = type[word] + 1
                sum += 1

            # 단 '이', '그', '저'는 한글자로만 사용되므로 예외
            elif (pron == '이' and word == '이') or (pron == '그' and word == '그') or (pron == '저' and word == '저'):
                oneLetterPronounFlag = True

    return sum

def adjacent_sentence_overlap_pronoun_lemmas_normed(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[1]] = 1

    for item in target:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue
    return 0

def binary_adjacent_sentence_overlap_pronoun_lemmas(now,target,kkma):
    pos_now = kkma.pos(now)
    target = kkma.pos(target)
    lemma = collections.defaultdict()

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[0]] = 1

    for item in target:
        try:
            if lemma[item[0]] == 1:
                return 1
        except:
            continue
    return 0

def adjacent_two_sentence_overlap_pronoun_lemmas(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()

    sum = 0

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                lemma[item[1]] += 1
        except:
            continue

    for item in target2:
        try:
            if lemma[item[1]] == 2:
                lemma[item[1]] += 1
                sum += 1
        except:
            continue

    return sum

def adjacent_two_sentence_overlap_pronoun_lemmas_normed(now,target1,target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[1]]=1

    for item in target1:
        try:
            if lemma[item[1]] == 1:
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[1]] == 1:
                return 1
        except:
            continue

    return 0

def binary_adjacent_two_sentence_overlap_pronoun_lemmas(now,target1, target2,kkma):
    pos_now = kkma.pos(now)
    target1 = kkma.pos(target1)
    target2 = kkma.pos(target2)
    lemma = collections.defaultdict()
    flag = False

    for item in pos_now:
        if "MAG" in item[1] or "MAJ" in item[1]:
            lemma[item[0]]=1

    for item in target1:
        try:
            if lemma[item[0]]  == 1 and ("MAG" in item[1] or "MAJ" in item[1]):
                flag = True
                break
        except:
            continue

    if flag == False:
        return 0

    for item in target2:
        try:
            if lemma[item[0]]  == 1 and ("MAG" in item[1] or "MAJ" in item[1]):
                return 1
        except:
            continue

    return 0
#noun&pronoun lemmas
