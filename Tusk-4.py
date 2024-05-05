def get_cats_info(path):
    cat_list = []
    with open(path, 'r', encoding='utf-8') as fh:
        lines = fh.readlines()
    for line in lines:
        id, name, age = line.strip().split(',') 
        cat_list.append({'id': id, 'name': name, 'age': age})
        return cat_list
    
print(get_cats_info('cats.txt'))