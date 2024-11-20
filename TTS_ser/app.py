from flask import Flask, request, send_file
import edge_tts
import asyncio
import tempfile

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data['text']
    voice = data['voice']
    rate = float(data['rate'])
    
    async def generate_speech():
        # Apply the rate as a percentage change to the default rate
        rate_percent = int((rate - 1) * 100)
        rate_option = f"+{rate_percent}%" if rate_percent >= 0 else f"{rate_percent}%"
        
        communicate = edge_tts.Communicate(text, voice, rate=rate_option)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            await communicate.save(temp_file.name)
            return temp_file.name

    audio_file = asyncio.run(generate_speech())
    return send_file(audio_file, mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(debug=True)