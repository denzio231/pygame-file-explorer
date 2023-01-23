import subprocess,os
def run(stuff):
    result = subprocess.run(stuff, stdout=subprocess.PIPE)
    return result
def mkdir(dir_name):
    return run(['mkdir',dir_name])
def cd(dir_name):
    os.chdir(dir_name)
def ls():
    return run(['ls'])
def pwd():
    return run(['pwd'])
def dirs():
    hello = ls()
    dir = hello.stdout.decode()
    dir = dir.split('\n')
    del dir[-1]
    return dir
def path():
    hello = pwd()
    path = hello.stdout.decode()
    path = path.replace('\n','')
    to_return = []
    dump = ''
    for i in path:
        dump += i
        if i == '/':
            to_return.append(dump)
            dump = ''
    to_return.append(dump)
    return to_return

