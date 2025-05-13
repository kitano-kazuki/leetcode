# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth


from typing import List


def fullJustify(words : List[str], maxWidth:int) -> List[str]:
    original_maxWidth = maxWidth
    result = []
    word_length_list = [len(word) for word in words]

    idx = 0
    sum_of_word_length = 0
    num_of_words = 0

    while idx < len(words):
        while True:
            num_of_words += 1
            if idx + num_of_words - 1 < len(words):
                sum_of_word_length += word_length_list[idx + num_of_words - 1]
                minimum_length = sum_of_word_length + (num_of_words - 1)
                if minimum_length > maxWidth:
                    sum_of_word_length -= word_length_list[idx + num_of_words - 1]
                    num_of_words -= 1
                    break
            else:
                num_of_words -=1
                maxWidth = sum_of_word_length + num_of_words - 1
                break
                
        remaining_space = maxWidth - sum_of_word_length
        space_between = remaining_space // (num_of_words - 1) if num_of_words != 1 else maxWidth - sum_of_word_length
        space_extra = remaining_space % (num_of_words - 1) if num_of_words != 1 else 0
        result_str = ""
        for i, word in enumerate(words[idx:idx + num_of_words]):
            result_str += word
            if i == num_of_words - 1 and num_of_words != 1:
                break
            result_str = result_str + (" " * space_between)
            if space_extra != 0:
                result_str += " "
                space_extra -= 1

        if len(result_str) != original_maxWidth:
            result_str = result_str + (" " * (original_maxWidth - maxWidth))
        result.append(result_str)
        idx = idx + num_of_words
        num_of_words = 0
        sum_of_word_length = 0

    return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
exptected_output = [
   "This    is    an",
   "example  of text",
   "justification.  "
]
result = fullJustify(words, maxWidth)

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
exptected_output = [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
result = fullJustify(words, maxWidth)
print(result)

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
exptected_output = [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
result = fullJustify(words, maxWidth)