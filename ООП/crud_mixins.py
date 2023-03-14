class CreateMixin:
    def product_create(self, title, price):
        #self.__class__ - обращение к классу, который наследовался от этого миксина
        model = self.__class__
        pop = model()
        _id = model._id
        pop.title = title
        pop.price = price
        pop.id = _id
        model.object[_id] = pop
        model._id += 1


class DeleteMixin:
    def delete_product(self, p_id):
        model = self.__class__
        model.object.pop(p_id)

class ReadMixin:
    def product_detail(self, p_id):
        model = self.__class__
        pop = model.object.get(p_id)
        print({"id":pop.id, "title":pop.title, "price":pop.price})

class UpdateMixin:
    def product_update(self, p_id, title, price):
        model = self.__class__
        pop = model.object.get(p_id)
        pop.title = title
        pop.price = price

class ProductCrud(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    object = {}
    _id = 1
    

crud = ProductCrud()
crud.product_create("Samsung Note 20 Ultra", 50000)
crud.product_create("Iphone 14 Pro Max", 100000)
crud.product_detail(2)
crud.product_update(2,"Pocophone F4", 120000)
crud.product_detail(2)
crud.product_create("Iphone 14 Pro Max", 100000)
crud.product_detail(3)
crud.delete_product(3)



