word=input()
perfect=True
v1="a"
v2="e"
v3="i"
v4="o"
v5="u"

if v1 not in word or v2 not in word or v3 not in word or v4 not in word or v5 not in word:
    perfect=False
elif word.index(v1) > word.index(v2) or word.index(v2) > word.index(v3) or word.index(v3) > word.index(v4) or word.index(v4) > word.index(v5):
    perfect=False
elif word.count(v1)<word.count(v2) or word.count(v2)<word.count(v3) or word.count(v3)<word.count(v4) or word.count(v4)<word.count(v5):
    perfect=False

if perfect:
    print("It is a perfect word")
else:
    print("It is not a perfect word")