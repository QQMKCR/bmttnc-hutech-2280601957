from flask import Flask, request, jsonify
from cipher.caeser import CaeserCipher
app = Flask(__name__)

#Ceaeser Cipher algorithm
caeser_cipher = CaeserCipher()

@app.route("/api/caeser/encrypt", methods=["POST"])
def ceaser_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted_text = caeser_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/caeser/decrypt", methods=["POST"])
def ceaser_decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted_text = caeser_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)