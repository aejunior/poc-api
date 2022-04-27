#!/usr/bin/env python3
from flask import Flask
import json, aiofiles, os


app = Flask(__name__)
data = []

@app.route('/', methods=['GET'])

def welcome():
    return ":D"

@app.route('/api/angeloni')
async def angeloni():
    data = []
    async with aiofiles.open('angeloni.jl', mode='r') as f:
        async for line in f:
            data.append(json.loads(line))
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)