import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import SavedTotal

app = Flask(__name__)


@app.route('/retrieve')
def retrieve():
    code = request.args.get('code', None)

    if code is None:
        return render_template('retrieve.jinja2')
    else:
        try:
            saved_total = SavedTotal.get(SavedTotal.code == code)
        except SavedTotal.DoesNotExist:
            return render_template('retrieve.jinja2', error="Code not found.")

        session['total'] = saved_total.value

        return redirect(url_for('add'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

