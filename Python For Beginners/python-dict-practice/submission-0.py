from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    key_dict={}

    for i in range(len(word)):
        if word[i] in key_dict:
            key_dict[word[i]]+=1
        else:
            key_dict[word[i]]=1
    return key_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
