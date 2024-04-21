from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    response = openai.Image.create(model="dall-e-3", quality="standard" ,prompt=prompt, n=1 ,  size="1024x1024")
    image_url = response.data[0].url
    return render_template('result.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True, port=5003)


