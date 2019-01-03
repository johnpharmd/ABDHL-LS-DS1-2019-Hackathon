import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import SongRetrieved

app = Flask(__name__)


@app.route('/retrieve')
def retrieve():
    code = request.args.get('code', None)

    if code is None:
        return render_template('retrieve.jinja2')
    else:
        try:
            song_retrieved = SongRetrieved.get(SongRetrieved.code == code)
        
        except Exception as e:
            return render_template('retrieve.jinja2', error="Code not found.")

        return redirect(url_for('add'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

