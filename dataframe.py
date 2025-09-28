from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd

#initialise Flask app
app = Flask(__name__)
CORS(app)

def load_corpus(file):
    try:
        df = pd.read_excel(file, engine='openpyxl')
        return df

    except FileNotFoundError:       #for when the file is not found
        print(f"File not found. Please ensure '{file}' is in the correct directory.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

corpus_df = load_corpus('corpus_words.xlsx')
idioms_df = load_corpus('Zulu_Idioms.xlsx')

@app.route('/api/translations', methods=['GET']) # api endpoint for the translations page
@cross_origin()
def get_data():
    corpus_data = corpus_df.to_dict('records')
    return jsonify(corpus_data)

@app.route('/api/idioms', methods=['GET'])  # api endpoint for the idioms page
@cross_origin()
def get_idioms():
    idioms_data = idioms_df.to_dict('records')
    return jsonify(idioms_data)


if __name__ == '__main__':
    app.run(debug=True)
