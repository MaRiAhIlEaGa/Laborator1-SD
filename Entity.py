class Car:
    def __init__(self, modelCar, brandCar, tokenCar, buyingpriceCar, sellingpriceCar):
        self.tokenCar = tokenCar
        self.modelCar = modelCar
        self.brandCar = brandCar
        self.buyingpriceCar = buyingpriceCar
        self.sellingpriceCar = sellingpriceCar

    def get_condition(self, condition):
        if condition == "model":
            return self.modelCar
        elif condition == "brand":
            return self.brandCar
        elif condition == "token":
            return self.tokenCar
        elif condition == "buyingprice":
            return self.buyingpriceCar
        elif condition == "sellingprice":
            return self.sellingpriceCar
        else:
            print("Invalid condition!")

    def set_tokenCar(self, token_car):
        self.tokenCar = token_car

    def set_modelCar(self, modelCar):
        self.modelCar = modelCar

    def set_brandCar(self, brandCar):
        self.brandCar = brandCar

    def set_buyingpriceCar(self, buyingpriceCar):
        self.buyingpriceCar = buyingpriceCar

    def set_sellingpriceCar(self, sellingpriceCar):
        self.sellingpriceCar = sellingpriceCar

    def __str__(self):
        return "Car: " + self.get_condition("model") + " " + self.get_condition("brand") + " " + \
            self.get_condition("token") + " " + str(self.get_condition("buyingprice")) + " " + \
            str(self.get_condition("sellingprice"))


car = Car("Chevrolet", "Malibu", "fuvjx4hgj4", 4236, 4199)
print(car.get_condition("buyingprice"))