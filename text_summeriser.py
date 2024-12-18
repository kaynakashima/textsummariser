import spacy

nlp = spacy.load("en_core_web_sm")

text = """
Amazon's delivery estimates are based on various factors, including shipping speed, item availability, 
and your location. While Amazon Prime members often experience faster shipping times, it's not uncommon 
for packages to arrive earlier than the estimated delivery date. However, this isn't guaranteed, as delivery 
times can vary due to factors like carrier schedules and unforeseen delays.
"""

#processesing the word data

doc = nlp(text=text)

word_dict = {}

for word in doc:
    word = word.text.lower()

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

#print (word_dict)

#scoring sentences

#(index, sentence, score)
sentences = []

sentence_score = 0

for i, sentence in enumerate(doc.sents):
    for word in sentence:
        word = word.text.lower()
        sentence_score += word_dict[word]

    sentences.append((1, sentence.text.replace("\n",""), sentence_score/len(sentence)))

#print(sentences)

#sorting the sentences
sorted_sentence = sorted(sentences, key=lambda x: -x[2])

top_three = sorted(sorted_sentence[:3], key=lambda x: x[0])

summary_text = ""

for sentence in top_three:
    summary_text += sentence[1] + ""

print(summary_text)







