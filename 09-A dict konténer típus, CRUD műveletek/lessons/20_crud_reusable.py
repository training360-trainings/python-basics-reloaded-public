def find_item(id, items):
    for item in items:
        if item['id'] == id:
            return item
    return None


def update_item(id, updated_item, items):
    index = items.index(find_item(id, items))
    if index is not None:
        items[index].update(updated_item)
    return items[index]


def create_item(item, items):
    item.update({'id': items[-1]['id'] + 1})
    items.append(item)
    return item


def remove_item(id, items):
    item = find_item(id, items)
    items.remove(item)
