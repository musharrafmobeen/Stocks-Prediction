from flask import Flask, request, render_template
from StocksData import prediction, return_graph_url

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/Predict', methods=['GET', 'POST'])
def foo():
    if request.method == 'POST':
        Company_Name = request.form['Company_Name']
        Date = request.form['Date']
        predictions = prediction(Company_Name,Date)
        graph_name = return_graph_url()
        return render_template('Prediction.html', Open=predictions[0][0], High=predictions[0][1], Low=predictions[0][2], Close=predictions[0][3], Volume=predictions[0][4], graph=graph_name )

if __name__ == '__main__':
    app.debug = True
    app.run()
   


