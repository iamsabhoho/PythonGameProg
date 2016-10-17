import myLib as ml

sampletext = 'Lyrics'
text = ml.readText(sampletext)
#print(type(text))
#print(ml.readText(sampletext))

ml.findNextWord('the', text)
