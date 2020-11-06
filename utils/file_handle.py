def extension(name):
    str_len = len(name)
    new_name = name[str_len - 4: str_len]
    if new_name in ['jpeg']:
        return '.{0}'.format(new_name)
    return new_name


if __name__ == '__main__':
    print(extension('123456.jpeg'))
