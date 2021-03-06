
import get_tokens
import cleanup
import sentance_sampling

from flask import Flask, render_template
from flask import request
app = Flask(__name__)

source = ''
source_path = './texts/harry.txt'

with open(source_path, 'r') as file:
    source = file.read()

start_stop_tokens=('\u0391', '\u03a9') 
clean_source = cleanup.cleanup(source=source)
tokens = get_tokens.generate(source=clean_source)
order = 2
source_map = sentance_sampling.markov_path(token_list=tokens, order=order)

@app.route('/')
def home():
    number_of_words = 150
    sentence = sentance_sampling.markov_walk(path=source_map, distance=number_of_words, start_stop_tokens=start_stop_tokens)
    return render_template('index.html', sentence=sentence)

   
if __name__ == '__main__':
    print(source_map['\u03a9'])
    sentence = sentance_sampling.markov_walk(path=source_map, distance=50, start_stop_tokens=start_stop_tokens)
    print(sentence)