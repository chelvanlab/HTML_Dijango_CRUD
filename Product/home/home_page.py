from flask import abort, render_template, request, jsonify

from . import home


@home.route('/')
def homepage():
    return render_template('home/index.html', title="Welcome")


@home.route('/tables')
def viewtables():
    return render_template("home/view_tables.html")


@home.route('/gettables', methods=['GET'])
def gettables():
    pass


