from flask import Flask, request, jsonify
from together_ai import generate_youtube_script

app = Flask(__name__)

# Route for generating YouTube script based on user prompt
@app.route('/generate-script', methods=['POST'])
def generate_script():
    data = request.json
    user_prompt = data.get('prompt', '')

    if not user_prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # Call the Together.ai API through a helper function
    try:
        response = generate_youtube_script(user_prompt)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
