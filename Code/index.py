
import get_tokens
import cleanup
import sentance_sampling

from flask import Flask
app = Flask(__name__)

source = ''
path = './texts/harry.txt'
with open(path, 'r') as f:
    source = f.read()
cleaned_text = cleanup.cleanup(source=source)
tokens = get_tokens.generate(source=cleaned_text)
chain = sentance_sampling.markov_chain(tokens=tokens)


@app.route('/')
def index():
    sentance = sentance_sampling.markov_jump(link=chain, length=45)
    return sentance
