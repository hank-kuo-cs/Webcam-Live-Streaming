from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.env = 'production'


@app.route('/')
def website():
    return render_template('main.html')


@app.route('/api/track/updateID', methods=['POST'])
def update_id():
    request_data = request.get_json()
    print(request_data)

    if not request_data or 'id' not in request_data:
        return jsonify({'message': 'data format error, must be {\'id\': \'a\'}'}), 400

    f = open('/opt/lampp/htdocs/NCTU/test/id.txt', 'w')
    f.write(request_data['id'])
    f.close()

    return jsonify({'message': 'success'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
