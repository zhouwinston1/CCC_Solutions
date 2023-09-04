orig = input()
cypher = input()
translate = input()

texts = {}

origArr = [str(text) for text in str(orig)]
cypherArr = [str(text) for text in str(cypher)]
tranArr = [str(text) for text in str(translate)]

for createDict in range(len(origArr)):
    texts[cypherArr[createDict]] = origArr[createDict]

translated = []

for loop in tranArr:
    if loop in cypherArr:
        translated.append(texts[loop])
    else:
        translated.append(".")

print(''.join(translated))


