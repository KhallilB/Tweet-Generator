
import get_tokens
import cleanup
import sentance_sampling

from flask import Flask 
from flask import request
app = Flask(__name__)

source = ''
source_path = './texts/harry.txt'

with open(source_path, 'r') as file:
    source = file.read()
clean_source = cleanup.cleanup(source=source)
tokens = get_tokens.generate(source=clean_source)
source_map = sentance_sampling.markov_path(token_list=tokens)

@app.route('/')
def index():
    number_of_words = 10 if request.args.get('num') is None else int(request.args.get('num'))
    sentence = sentance_sampling.markov_walk(path=source_map, distance=number_of_words)
    return sentence

if __name__ == '__main__':
    print(source_map['\u03a9'])
    sentence = sentance_sampling.markov_walk(path=source_map, distance=50)
    print(sentence)