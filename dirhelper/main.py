import os


def list_dir(dir_path):
    print('list dir')
    try:
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(dir_path)
    except NotADirectoryError as e:
        print(e.args[0] + ' is not a directory')
        return

    for d in os.listdir(dir_path):
        print(d)






def init():
    if os.path.isfile('init'):
        return read_init()
    else:

        begin_dir = input('请输入目标初始目录: ')
        target_dir = input('请输入目标目录: ')
        try:
            os.path.isdir(begin_dir)
            os.path.isdir(target_dir)
        except NotADirectoryError as e:
            print(e)
        config = {
            'begin_dir': begin_dir,
            'target_dir': target_dir
        }
        write_init(config)

        return config


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


def check_begin_dir(config):
    begin_dir = config['begin_dir']
    file_list = list_dir(begin_dir)






def main():
    config = init()
    print(config)
    check_begin_dir(config)

if __name__ == '__main__':
    main()

