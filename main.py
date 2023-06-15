import sys
import os
import math

# initialize a dictionary with each key representing a language model
models = dict.fromkeys(["swe", "ita", "dut", "swh", "fin", "spa", "nob", "dan",
                        "gla", "eng", "por", "pol", "deu", "fra", "tgl"])

# read in the language model's content
for filename in os.listdir(sys.argv[1]):
    pathname = os.path.join(sys.argv[1], filename)

    with open(pathname, 'r', encoding='utf8') as f:
        info = f.read().splitlines()
        d = {}

        # create a dictionary with each word as a key and each frequency as a value
        for line in info:
            pair = line.split("\t")
            d[pair[0]] = int(pair[1])

        # assign each word-freq dictionary as a value to respective language keys in models dictionary
        lang = [os.path.basename(pathname)[0:3]][0]
        models[lang] = d

# read in the input content
with open(sys.argv[2], 'r', encoding='utf8') as i:
    input_text = i.read().splitlines()
    c = []

    # create a list of tuples, with each tuple storing the language ID as a string and the sentence as a list
    for line in input_text:
        tupval = line.split("\t")
        c.append((tupval[0], tupval[1].split()))

    # create the output file
    with open(sys.argv[3], 'w', encoding='utf8') as g:
        for (idtag, sentence) in c:
            g.write(idtag + "\t" + " ".join(sentence) + "\n")

            # initialize dictionary with language ID as keys and probabilities as the values
            prob = dict.fromkeys(
                ["swe", "ita", "dut", "swh", "fin", "spa", "nob", "dan", "gla", "eng", "por", "pol", "deu", "fra",
                 "tgl"], 0.0)

            for word in sentence:
                for lang in prob:
                    number_of_words = sum(models[lang].values())

                    if word in models[lang]:
                        w_i = word
                    else:
                        w_i = "<UNK>"

                    # calculate word frequency divided by number of words in language
                    w_i_probability = models[lang][w_i] / number_of_words

                    # update each language's total probability
                    prob[lang] += math.log(w_i_probability, 10)

            for lang in prob:
                g.write(lang + "\t" + str(prob[lang]) + "\n")

            result = max(prob, key=prob.get)
            g.write("result" + "\t" + result + "\n" + "\n")