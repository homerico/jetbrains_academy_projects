import os
import sys
import requests


def read_file(url_file_path):
    with open(url_file_path, 'r') as fread:
        return fread.read()


def write_file(url_file_path, content):
    with open(url_file_path, "w", encoding="utf-8") as fin:
        fin.write(content)


def path(filename: str):
    return args[1] + "/" + filename + ".txt"


def is_url(_input: list) -> bool:
    if len(_input) == 2 or os.path.exists(path(_input[0])):
        return True
    return False


def print_website(website: list, is_back: bool = False):
    path_file = path(website[0])
    if os.path.exists(path_file):
        print(read_file(path_file))
    else:
        headers = {"user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"}
        url = "https://" + ".".join(website)
        content = requests.get(url, headers=headers).text
        print(content)
        write_file(path_file, content)

    if not is_back:
        browse_history.append(website)


args = sys.argv
browse_history = []

if not os.path.exists(args[1]):
    os.mkdir(args[1])
while True:
    _input = input().rsplit(".", 1)
    if is_url(_input):
        print_website(_input)
    elif _input[0] == "exit":
        break
    elif _input[0] == "back":
        try:
            browse_history.pop()
            print_website(browse_history.pop(), is_back=True)
        except IndexError:
            pass
    else:
        print("error: invalid url")
