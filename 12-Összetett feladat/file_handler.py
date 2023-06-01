def read_file(path):
    with open(path, 'r') as f:
        content = []
        for line in f:
            id, author, title = line.rstrip().split(';')
            content.append({'id': id, 'title': title, 'author': author})
        return content


def write_file(path, content):
    with open(path, 'w') as f:
        for i in content:
            f.write(f'{i["id"]};{i["title"]};{i["author"]}\n')
