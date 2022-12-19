from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def generateImgFromText(prompt, seed):
    return "oke"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    formData = request.get_json()
    prompt = formData['prompt']
    seed = formData['seed']
    retVal = []

    # Todo processing
    ret = {
        'prompt': prompt,
        'seed': seed,
        'image': generateImgFromText(prompt=prompt, seed=seed)
    }
    retVal.append(ret)

    data = {
        'data': retVal
    }
    response = jsonify(data), 200
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')