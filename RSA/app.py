from flask import Flask, redirect, request, render_template, url_for
from algorithm import Algorithm
from generator import Generator

app = Flask(__name__)

@app.route('/rsa', methods=['GET', 'POST'])
def rsa():
    message = ''
    encrypted_message = ''
    decrypted_message = ''
    if request.method == 'POST':
        message = request.form['message']
        #message, encrypted_message, decrypted_message = algorithm.main(message)
        encrypted_message = algorithm.encrypt_message(message, algorithm.public_key)
        decrypted_message = algorithm.decrypt_message(encrypted_message, algorithm.private_key)

    return render_template('sending.html', message=message, encrypted_message=encrypted_message, decrypted_message=decrypted_message)

algorithm = Algorithm()
@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        primes = Generator.find_primes3(1000, 5000, 2)
        algorithm.generate_keys(primes[0], primes[1])
        return redirect(url_for('rsa'))
    else:
        return render_template('root.html')


if __name__ == '__main__':
    app.run(debug=True)