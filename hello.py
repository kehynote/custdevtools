#!/usr/bin/python
#-*- coding:utf-8 -*-


from flask import Flask,jsonify
from kehydb.db import TestDB

# Flask
app = Flask(__name__)

@app.route('/')
def index():
  return u"你好，世界";

@app.route('/tests')
def listTest():
  testDB = TestDB()
  rows = testDB.listTest();

  return jsonify({"data":rows});


if __name__ == '__main__':
  app.run(debug=True)