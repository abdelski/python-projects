from flask import Flask
from scraper import run as scrape_runner
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/abc', methods=['GET'])
def abc_view():  # put application's code here
    return 'Hello ABC!'

@app.route('/box', methods=['POST'])
def box_office_scraper_view():  # put application's code here
    scrape_runner()
    return 'Done'


if __name__ == '__main__':
    app.run()
