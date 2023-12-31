# bayesian-language-identifier
```bayesian-language-identifier``` labels text fragments according to their most probable language of origin.

Args:
* ```languagemodels```: directory holding each language model (unigram frequency list), formatted as text files
* ```input.txt```: text file holding each sentence and its respective gold-standard language code

Returns:
* ```output.txt``` : text file holding each sentence, its respective gold-standard language code, an enumeration of each language's probability of being the sentence's language, and the "result", i.e., the language with the highest calculated probability.

To run: 
```
src/run.sh input/language_models input/input.txt output/output.txt
```
PROJECT 5 OF LING473 (09/07/2021)
