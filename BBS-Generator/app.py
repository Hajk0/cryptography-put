from flask import Flask, render_template
import random
from generator import generateBBS
from test import Test

app = Flask(__name__)

random_binary: int = None
random_number: int = None
seed: int = None
p: int = None
q: int = None
M: int = None
length: int = None

@app.route('/')
def generate():
    global random_binary, random_number, seed, p, q, M, length
    random_binary, random_number, seed, p, q, M, length = generateBBS()
    # Tests
    test = Test()
    single_bits_test = test.single_bits_test(random_binary, length)
    series_test = test.series_test(random_binary, length)
    long_series_test = test.long_series_test(random_binary, length)
    poker_test = test.poker_test(random_binary, length)

    return render_template('index.html', random_number=random_number, random_binary=random_binary
                           , seed=seed, p=p, q=q, M=M, length=length, single_bits_test=single_bits_test
                           , series_test=series_test, long_series_test=long_series_test, poker_test=poker_test)


if __name__ == '__main__':
    app.run(debug=True)