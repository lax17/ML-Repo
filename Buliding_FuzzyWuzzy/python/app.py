from fuzzywuzzy import process,fuzz
from flask import Flask,render_template,request
import json

#app initalization

app = Flask(__name__,template_folder='../templates',static_folder="../static")


#main index page route

@app.route('/')
def home():
    return render_template('index.html')

scorer_dict = \
    {
    'fuzz.ratio':fuzz.ratio,
    'fuzz.partial_ratio': fuzz.partial_ratio,
    'fuzz.token_set_ratio': fuzz.token_set_ratio,
    'fuzz.token_sort_ratio': fuzz.token_sort_ratio,
    'fuzz.partial_token_set_ratio': fuzz.partial_token_set_ratio,
    'fuzz.partial_token_sort_ratio': fuzz.partial_token_sort_ratio,
    'fuzz.WRatio': fuzz.WRatio,
    'fuzz.QRatio': fuzz.QRatio,
    'fuzz.UWRatio': fuzz.UWRatio,
    'fuzz.UQRatio': fuzz.UQRatio
}

def scorer_generator_function(first_text,second_text):
    print(first_text,second_text)
    ratio = []
    for score in scorer_dict :
        # ratio = process.extract(first_text,second_text,limit=1,scorer=scorer_dict[score])
        ratios=scorer_dict[score](first_text,second_text)
        ratio.append({"scorer_name":score,"similarity_score":str(ratios)+"%"})
    return ratio


@app.route('/fuzzyWuzzyScorers',methods=['POST'])
def fuzzyWuzzyScorers():
    first_text = request.form['input_text_first']
    second_text = request.form['input_text_second']
    ratios= scorer_generator_function(first_text,second_text)
    print(ratios)
    return json.dumps(ratios)


if  __name__ =="__main__":
    app.run(port=5000,debug=True)