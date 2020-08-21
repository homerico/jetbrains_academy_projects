import os
import sys


def read_file(url_file_path):
    with open(url_file_path, 'r') as fread:
        return fread.read()


def write_file(url_file_path, content):
    with open(url_file_path, "w") as fin:
        fin.write(content)


def path(filename: str):
    return args[1] + "/" + filename + ".txt"


def is_url(_input: list):
    if _input[0] in possible_sites:
        return True
    return False


def print_website(website: str, is_back: bool = False):
    path_file = path(website)
    if os.path.exists(path_file):
        print(read_file(path_file))
    elif website in possible_sites:
        content = possible_sites[website]
        write_file(path_file, content)
        print(content)
    if not is_back:
        browse_history.append(website)


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''
args = sys.argv
browse_history = []
possible_sites = {"bloomberg": bloomberg_com, "nytimes": nytimes_com}

if not os.path.exists(args[1]):
    os.mkdir(args[1])
while True:
    _input = input().rsplit(".", 1)
    if is_url(_input):
        print_website(_input[0])
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

