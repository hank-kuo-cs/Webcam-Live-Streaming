import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.env = 'production'
CORS(app)


def write_id_txt(s: str):
    f = open('/eva_data/hank/VST/HW4/id.txt', 'w')
    f.write(s)
    f.close()


@app.route('/')
def website():
    return render_template('main.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'pikachu.jpg', mimetype='image/vnd.microsoft.icon')


@app.route('/api/track/runTracker', methods=['GET'])
def run_tracker():
    os.system('./run_tracker.sh')
    return jsonify({'message': 'success'}), 200


@app.route('/api/track/updateID', methods=['POST'])
def update_id():
    request_data = request.get_json()
    print(request_data)

    if not request_data or 'id' not in request_data:
        return jsonify({'message': 'data format error, must be {\'id\': \'a\'}'}), 400

    write_id_txt(request_data['id'])

    return jsonify({'message': 'success'}), 200


@app.route('/api/track/cleanData', methods=['GET'])
def clean_data():
    os.system('rm -rf /eva_data/hank/VST/HW4/stream_raw/*')
    os.system('rm -rf /eva_data/hank/VST/HW4/stream_det/*')
    write_id_txt('all')

    return jsonify({'message': 'success'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
