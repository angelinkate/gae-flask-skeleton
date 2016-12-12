# -*- coding: utf-8 -*-

# Import the Flask Framework
from flask import Flask, Response, Request, session, url_for, redirect, \
    render_template, abort, g, flash, _app_ctx_stack, request

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

@app.teardown_appcontext
def close_context(exception):
    return

@app.before_request
def before_request():
    g.user = None

@app.route('/')
def hello():
    res = Response('hElLo')
    return res

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
