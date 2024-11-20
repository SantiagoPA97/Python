def get_product(**data):
    print(data)
    print(data["name"])


get_product(id="id", name="iPhone", price=699, description="A phone")
