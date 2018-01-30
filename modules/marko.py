import markovify, requests, sys
from inscriptis import get_text
from colorama import Fore, init

init(autoreset=True)

def gen_markov(f=None, u=None):
    if f:
        with open(f) as f:
            print(Fore.GREEN + '[+] Parsing text file.') 
            text = f.read()

    elif u:
        print(Fore.GREEN + '[+] Parsing specified URL.')
        r = requests.get(u)
        text = get_text(r.text)
    print(Fore.GREEN + '[+] Generating a model.')
    model = markovify.Text(text)
    print(Fore.GREEN + '[+] Attempting to generate a Markov chain.')
    markov_text = model.make_short_sentence(140)
    return markov_text

def gen_from_hist(filepath):
    with open(filepath) as f:
        text_model = markovify.Text(f, retain_original=False)
    print(text_model.make_sentence())

# marokvify's the model and generates txt for a tweet
def construct_twt(markov_text, handle=None):
    if markov_text == None:
        print(Fore.RED + '[!] Failed to generate a Markov chain. Exiting.')
        sys.exit(1)
    else:
        if handle:
            print(Fore.GREEN + '[+] Constructing your tweet, and tweeting at ' + handle)
            twt_txt = '[Marko]\n'+ handle + ' ' + markov_text
        else:
            print(Fore.GREEN + '[+] Constructing your tweet.')
            twt_txt = '[Marko]\n' + markov_text
        return twt_txt

