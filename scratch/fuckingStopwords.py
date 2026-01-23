stop_words = []
word = ""
while word != "STOP":
    word = input()
    if word == "STOP":
        break
    stop_words.append(word)
sentence = []
word = ""
while word != "STOP":
    word = input()
    if word == "STOP":
        break
    sentence.extend(word.split())
sentence = [word.lower() for word in sentence]
remaining_words = set(sentence)-set(stop_words)
to_print = ''
# format it back into a sentence
for word in sentence:
    if word in remaining_words:
        to_print += word + " "
print(to_print)