from mock_data import mock_data

# class Dog:


me = {
    "name": "Justine",
    "last": "Rivera",
    "email": "test@mail.com",
    "age": 30,
    "hobbies": [],
    "address": {
            "street": "main",
            "number": "42"
    }
}


def print_data():
    print(me["name"])
    print(me["name"] + " " + me["last"])

# print_data()


def test_list():
    print("list")
    names = []

    # add elements to a list
    names.append("Justine")
    names.append("Christian")

    print(names)

    # get elements from list
    print(names[0])
    print("--------- using for loop")

    for name in names:
        print(name)
    print("------sublist")
    # sublist list list[<skip> : <take>]
    print(names[1:2])


# test_list()

def product_search(id):
    print("search a product in the catalog")
    found = False
    for prod in mock_data:
        if prod["_id"] == id:
            found = True
            print(prod)
            return(prod)
    if not found:
        print("Error: Product not found")
        return None


product_search("222")
product_search(234)


def search_by_category(category):
    print("searching my category")
    # to the magic

    # return a list of products
    # or empty list of none found

    search_by_category("bracelet")
    search_by_category("wrong")
