# bayesian-language-identifier
A naïve Bayesian classifier that labels text fragments according to their most probable language of origin.

Args:
* sys.argv[1]: a directory holding each language model (unigram frequency list), formatted as text files
* sys.argv[2]: a text file holding each sentence and its respective gold-standard language code

Returns:
* sys.argv[3]: a text file holding each sentence, its respective gold-standard language code, an enumeration of each language's probability of being the sentence's language, and the "result", i.e., the language with the highest calculated probability.

To run: 
```
python3 ./main.py ./language_models ./input.txt ./output.txt
```
PROJECT 5 OF LING473 (09/07/2021)
