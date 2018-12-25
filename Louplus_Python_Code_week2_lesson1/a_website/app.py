#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,url_for,redirect,render_template,request,abort
import json
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


class Files():
    path = "/home/shiyanlou/files"
    def __init__(self):
        self._files=self._read_all_files()
    def _read_all_files(self):
        result={}
        for filename in os.listdir(self.path):
            file_path = os.path.join(self.path,filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result
    def get_title(self):
        return [item['title'] for item in self._files.values()]
    def get_file(self,filename):
        return self._files.get(filename)
files=Files()

@app.route('/')
def index():
    return render_template('index.html',titlelist=files.get_title())

@app.route('/files/<filename>')
def file_index(filename):
    file_item=files.get_file(filename)
    if not  file_item:
        abort(404)
    return render_template('file.html',file_item=file_item)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run()
