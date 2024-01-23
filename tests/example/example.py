import json

from pagidantic import pagidantic

# retrieve data from generated.json file and convert it to python object

with open("tests/example/generated.json") as f:
    object_list = json.load(f)


pagination = pagidantic(object_list, page_limit=2, start_page=0)


# get current returned page
def get_current_page():
    return pagination.response


print(get_current_page())


# get next pageg
def get_next_page():
    return pagination.get_next()


print(get_next_page())


# get previous page
def get_previous_page():
    return pagination.get_previous()


print(get_previous_page())


# get page by number
def get_page_by_number():
    return pagination.get_page_response(page_number=0)


print(get_page_by_number())


# get total pages
def get_total_pages():
    return pagination.total_pages


print(get_total_pages())


# Count total objects
def count_total_objects():
    return pagination.total


print(count_total_objects())
