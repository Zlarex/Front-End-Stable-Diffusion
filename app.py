from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)

def generateImgFromText(prompt, seed):
    return "https://camo.githubusercontent.com/ec8cf13388b98a7133c6850afcf17ab4af5042802e0229c49f2242ea36d37090/68747470733a2f2f7261772e6769746875622e636f6d2f6d696b6f6c616c7973656e6b6f2f6c656e612f6d61737465722f6c656e612e706e67"
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

        generated_count = generated_count if generated_count <= 4 else 4

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