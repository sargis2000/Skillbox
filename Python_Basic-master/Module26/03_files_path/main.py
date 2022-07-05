from collections.abc import Generator
import os
path = input('Enter path')
name = input('Enter File name')


def gen_files_path(current_dir: str, user_path: str = '/') -> Generator:
    if current_dir in os.listdir(user_path):
        user_path = os.path.join(user_path, current_dir)
        for i in os.listdir(user_path):
            yield os.path.join(user_path, i)
    else:
        return None


for link in gen_files_path(current_dir=name, user_path=path):
    print(link)



