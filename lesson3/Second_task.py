from json import loads, dumps
from csv import DictReader

with open('users.json', 'r') as file:
    j = file.read()
    n = loads(j)
    # print(n[0])
    # print(len(n))
    # print(type(n))
with open('books.csv') as f:
    reader = DictReader(f)
    all_books = []
    # Итерируемся по данным делая из них словари
    for row in reader:
        new_book = {}
        for some_name in ['Title', 'Author', 'Height']:
            new_book[some_name] = row[some_name]
        all_books.append(new_book)
    # print(all_books)

    all_students = []
    for each in n:
        new_person = {}
        for some_name in ['name', 'gender', 'address']:
            new_person[some_name] = each[some_name]
        all_students.append(new_person)
    print(all_students)
    print(type(all_students))
    index = 0
    j = []
    for each in all_students:
        if all_books[index] is not None:
            each['books'] = [all_books[index]]
        else:
            each['books'] = []
        j.append(each)
        index += 1
    out_file = {'user': j}
    print(j)
with open('new_json.json', 'w') as file:
    s = dumps(out_file, indent=4)
    file.write(s)

# def new_people(inf_people):
#     new_person = {}
#     for some_name in ['name', 'gender', 'address']:
#         new_person[some_name] = inf_people[some_name]
#     return new_person
