import os
import requests
from importlib.machinery import SourceFileLoader
import json


def create_file(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)


def write_file(name, content):
    with open(name, 'wb') as f:
        f.write(content)


def redirect(url):
    rsp = requests.get(url, allow_redirects=False, verify=False)
    return redirect(rsp.headers['Location']) if 'Location' in rsp.headers else rsp


def download_file(name, ext):
    if ext.startswith('http'):
        write_file(name, redirect(ext).content)
    else:
        write_file(name, str.encode(ext))


def init_py(path, name, ext):
    create_file(path)
    py_name = path + name + '.py'
    download_file(py_name, ext)
    return SourceFileLoader(name, py_name).load_module().Spider()


def str2json(content):
    return json.loads(content)


def init(ru, extend):
    ru.init([""])


def homeContent(ru, filter):
    result = ru.homeContent(filter)
    return json.dumps(result, ensure_ascii=False)


def homeVideoContent(ru):
    result = ru.homeVideoContent()
    return json.dumps(result, ensure_ascii=False)


def categoryContent(ru, tid, pg, filter, extend):
    result = ru.categoryContent(tid, pg, filter, str2json(extend))
    return json.dumps(result, ensure_ascii=False)


def detailContent(ru, array):
    result = ru.detailContent(str2json(array))
    return json.dumps(result, ensure_ascii=False)


def playerContent(ru, flag, id, vipFlags):
    result = ru.playerContent(flag, id, str2json(vipFlags))
    return json.dumps(result, ensure_ascii=False)


def searchContent(ru, key, quick):
    result = ru.searchContent(key, quick)
    return json.dumps(result, ensure_ascii=False)


def run():
    pass


if __name__ == '__main__':
    run()
