"""
Ellie Yun's Flask API.
"""

from flask import Flask, render_template, send_from_directory, abort
import config, logging
log = logging.getLogger(__name__)
app = Flask(__name__)

forbidden_symbols = ["//", "~", ".."]

@app.route('/<path:f_name>')
def find_file(f_name):
    # parse DOCROOT from the .ini file
    options = config.configuration()
    DOCROOT = options.DOCROOT
    log.info(DOCROOT)
    check_symbol = [symbol for symbol in forbidden_symbols if symbol in f_name]
    
    if len(check_symbol) > 0:
        abort(403)
    
    return send_from_directory(DOCROOT, f_name), 200

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(e):
    return render_template('404.html'),404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
