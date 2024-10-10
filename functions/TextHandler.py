import re


def get_Sentences(text:str):
    sentence_pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s')
    sentences = sentence_pattern.split(text)
    sentences = [sentence.strip() + ('' if i == len(sentences) - 1 else sentence_pattern.findall(text)[i]) for i, sentence in enumerate(sentences)]
    return sentences


def combined_Words(words:list):
    combined_words = []
    current_words = []
    for word in words:
        if len(' '.join(current_words + [word])) <= 20:
            current_words.append(word)
        else:
            combined_words.append(' '.join(current_words))
            current_words = [word]           
    if current_words:
        combined_words.append(' '.join(current_words))
    return combined_words