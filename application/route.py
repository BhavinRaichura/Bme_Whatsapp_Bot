from application import app
from flask import Flask, request, url_for, render_template, redirect

@app.route("/")
def home():
    return "<h1>hello world</h1>"