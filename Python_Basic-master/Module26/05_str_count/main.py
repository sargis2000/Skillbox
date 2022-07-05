from collections.abc import Generator
import os


def gen_dir(file_path: str) -> Generator:
    for i in os.listdir(file_path):
        new_path = os.path.join(file_path, i)
        if os.path.isdir(new_path):
            yield from gen_dir(file_path=new_path)
        elif new_path.endswith('.py'):
            with open(new_path, 'r') as file:
                lines = [line for line in file if
                         not line.strip().startswith("#")
                         and line.strip() != '']
            yield new_path, len(lines)


for path, counts in gen_dir('/home/sargis/PycharmProjects'):
    print(path, counts)
