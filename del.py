import os
import glob


def remove_migrations():
    res = glob.glob('*/migrations/*', recursive=True)
    for file_path in res:
        if file_path.endswith('__pycache__'):
            file_path = file_path+'/*'
            sub_res = glob.glob(file_path)
            for file_path in sub_res:
                os.remove(file_path)
        elif not file_path.endswith('__init__.py'):
            os.remove(file_path)
    print('Migration files removed')


def remove_file_by_extension(ext):
    sub_res = glob.glob('/**/*.' + ext)
    cnt = 0
    for file_path in sub_res:
        os.remove(file_path)
        cnt += 1
    print(str(cnt) + ' ' + ext + ' files removed')


# remove_migrations()
remove_file_by_extension('pyc')
print('done')
