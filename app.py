from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)

def generateImgFromText(prompt, seed):
    return ""

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        formData = request.get_json()
        prompt = formData['prompt']
        seed = formData['seed']
        generated_count = formData['generated_count'] if formData['generated_count'] > 1 else 1
        is_random = bool(formData['random']) == True
        retVal = []

        while(generated_count >= 1):
            # Todo processing
            ret = {
                'prompt': prompt,
                'seed': random.randint(0, 99999999) if is_random else seed,
                'image': generateImgFromText(prompt=prompt, seed=seed)
            }
            retVal.append(ret)
            generated_count -= 1

        data = {
            'data': retVal
        }
        response = jsonify(data), 200
        return response
    except Exception as e:
        return jsonify({
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')