from flask import Flask, render_template, request
from translate import Translator  # Import the Translator from the translate library
from googletrans import LANGUAGES  # Still using LANGUAGES from googletrans for language options

app = Flask(__name__)

def translate_text(text, target_lang="fr"):
    translator = Translator(to_lang=target_lang)  # Set the target language
    return translator.translate(text)  # Translate the text

@app.route('/main', methods=['GET', 'POST'])
def main():
    translatedtext = "Your translated text will appear here..."
    cfrom = "en"
    cto = "hi"
    if request.method == 'POST':
        cfrom = request.form.get('convertfrom')  # Language to convert from
        cto = request.form.get('convertto')       # Language to convert to
        text = request.form.get('inputtext')     # Text to be translated
        
        # Ensure the target language is valid and input text is provided
        if cto and text:  
            print(f"Converting from: {cfrom}, to: {cto}, text: {text}")
            translatedtext = translate_text(text, cto)  # Translate the text
        else:
            translatedtext = "Please select a target language and enter text."
            
    return render_template('index.html', translatedtext=translatedtext, lang=LANGUAGES, cfrom=cfrom, cto=cto)

if __name__ == '__main__':
    app.run(debug=True)
