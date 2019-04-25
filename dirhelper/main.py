import os
import difflib

target_distinct_list = [
    'System Volume Information',
    '$RECYCLE.BIN'
]

begin_distinct_list = [
    'torrent'
]


def list_dir(dir_path, dir_type):
    print('list dir')
    try:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(dir_path)
    except NotADirectoryError as e:
        print(e.args[0] + ' is not a directory')
        return

    path = []
    for d in os.listdir(dir_path):
        full_path = os.path.join(dir_path, d)
        file_type = 'file'
        if os.path.isdir(full_path):
            file_type = 'dir'
        ext = os.path.splitext(d)[1]

        if dir_type == 'begin':
            if ext in begin_distinct_list:
                continue

        if dir_type == 'target':
            if file_type == 'file' or d in target_distinct_list:
                continue

        path_format = {}
        path_format['type'] = file_type
        path_format['path'] = full_path
        if file_type == 'file':
            path_format['name'] = os.path.splitext(d)[0]
        else:
            path_format['name'] = d
        path.append(path_format)

    return path


def init():
    if os.path.isfile('init'):
        return read_init()
    else:
        config = {
            'begin_dir':  check_dir('请输入需查找的目录: '),
            'target_dir': check_dir('请输入移动目标目录: ')
        }
        write_init(config)

        return config


def check_dir(hint):
    try:
        dir_path = input(hint)
        res = os.path.isdir(dir_path)
        if not res:
            raise NotADirectoryError

    except NotADirectoryError as e:
        return check_dir('目录不存在, ' + hint)

    return dir_path


def write_init(config):
    print('write init')
    with open('init', 'w') as f:
        for i, d in config.items():
            f.write(i + ' = ' + d + '\n')


def read_init():
    print('read init')
    config = {}
    try:
        with open('init') as f:
            line = f.readline()
            while line:
                line = line.split('=')
                key = line[0].strip(' \n')
                val = line[1].strip(' \n')
                config[key] = val
                line = f.readline()

    except FileNotFoundError as e:
        print(e)

    return config


def string_similar(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


def move_similar(dir_list):
    print('move similar')
    for d in dir_list:
        print("文件 %s, 移动到目录 %s\n" %(d['begin_path'], d['target_path']))
        file_move(d)

def file_move(file):
    print('file move')


def main():
    config = init()
    print(config)
    begin_dir_file_list = list_dir(config['begin_dir'], 'begin')
    if len(begin_dir_file_list) == 0:
        print('开始目录没有任何文件')

    target_dir_list = list_dir(config['target_dir'], 'target')

    similar_list = []
    unmatched_list = []
    for (i, d) in enumerate(begin_dir_file_list):
        similar = {}
        has_matched = False
        for (ii, dd) in enumerate(target_dir_list):
            if dd['type'] == 'dir':
                rate = string_similar(d['name'], dd['name'])
                if rate > 0.8:
                    has_matched = True
                    similar['begin_index'] = i
                    similar['begin_name'] = d['name']
                    similar['begin_path'] = d['path']
                    similar['target_index'] = ii
                    similar['target_name'] = dd['name']
                    similar['target_path'] = dd['path']
                    similar['rate'] = rate

        if similar:
            similar_list.append(similar)
        if not has_matched:
            unmatched_list.append(d)

    print(similar_list)
    move_similar(similar_list)
    print(unmatched_list)

if __name__ == '__main__':
    main()

