
library(keras)

lines = readr::read_lines('cleaned186.txt', 
                          #skip_empty_rows = T, 
                          locale = readr::locale(encoding = "WINDOWS-1251"))

##########
lines = lines[nchar(lines)>0]

## initialize tokenizer and fit
tokenizer <- text_tokenizer() %>% 
  fit_text_tokenizer(lines)

## inspect word_index 
tokenizer$word_index 




sequences = texts_to_sequences(tokenizer, lines)
sequences = pad_sequences(sequences, maxlen = 10)


## modes
texts_to_matrix(tokenizer, lines, mode = "binary")

texts_to_matrix(tokenizer, lines, mode = "tfidf")









save_text_tokenizer(tokenizer, 'tokenizer')





