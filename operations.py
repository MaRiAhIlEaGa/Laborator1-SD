import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} took {total_time:.10f} seconds')
        return result
    return wrapper


class Search_Maria:
    def __init__(self, cars_list, token):
        self.cars_list = cars_list
        self.token = token

    @timeit
    def binary_search(self):
        left = 0
        right = len(self.cars_list)
        while left <= right:
            mij = int((left + right) / 2)
            if self.cars_list[mij].get_condition("token") == self.token:
                return self.cars_list[mij]
            elif self.token < self.cars_list[mij].get_condition("token"):
                right = mij + 1
            else:
                left = mij - 1
        return None


class Sort_Maria:
    def __init__(self, cars_list, condition):
        self.cars_list = cars_list
        if condition == 1:
            self.comparator = self.sort_by_token
        elif condition == 2:
            self.comparator = self.sort_by_brand_and_model
        elif condition == 3:
            self.comparator = self.sort_by_brand_and_model_and_token
        elif condition == 4:
            self.comparator = self.sort_by_profit

    @staticmethod
    def sort_by_token(car1, car2):
        if car1.get_condition("token") < car2.get_condition("token"):
            return True
        elif car1.get_condition("token") == car2.get_condition("token"):
            return None
        return False

    @staticmethod
    def sort_by_brand_and_model(car1, car2):
        if car1.get_condition("brand") < car2.get_condition("brand"):
            return True
        elif car1.get_condition("brand") == car2.get_condition("brand"):
            if car1.get_condition("model") < car2.get_condition("model"):
                return True
        return False

    @staticmethod
    def sort_by_brand_and_model_and_token(car1, car2):
        if car1.get_condition("brand") < car2.get_condition("brand"):
            return True
        elif car1.get_condition("brand") == car2.get_condition("brand"):
            if car1.get_condition("model") < car2.get_condition("model"):
                return True
            elif car1.get_condition("model") == car2.get_condition("model"):
                if car1.get_condition("token") < car2.get_condition("token"):
                    return True
        return False

    @staticmethod
    def sort_by_profit(car1, car2):
        profit_car1 = car1.get_condition("sellingprice") - car1.get_condition("buyingprice")
        profit_car2 = car2.get_condition("sellingprice") - car2.get_condition("buyingprice")
        if profit_car1 < profit_car2:
            return True
        elif profit_car1 == profit_car2:
            return None
        return False

    @timeit
    def bubble_sort(self):
        for car1 in self.cars_list:
            for car2 in self.cars_list:
                if self.comparator(car1, car2):
                    car1_model = car1.get_condition("model")
                    car2_model = car2.get_condition("model")
                    car1.set_modelCar(car2_model)
                    car2.set_modelCar(car1_model)
                    car1_brand = car1.get_condition("brand")
                    car2_brand = car2.get_condition("brand")
                    car1.set_brandCar(car2_brand)
                    car2.set_brandCar(car1_brand)
                    car1_token = car1.get_condition("token")
                    car2_token = car2.get_condition("token")
                    car1.set_tokenCar(car2_token)
                    car2.set_tokenCar(car1_token)
                    car1_buyingprice = car1.get_condition("buyingprice")
                    car2_buyingprice = car2.get_condition("buyingprice")
                    car1.set_buyingpriceCar(car2_buyingprice)
                    car2.set_buyingpriceCar(car1_buyingprice)
                    car1_sellingprice = car1.get_condition("sellingprice")
                    car2_sellingprice = car2.get_condition("sellingprice")
                    car1.set_sellingpriceCar(car2_sellingprice)
                    car2.set_sellingpriceCar(car1_sellingprice)
        return self.cars_list

@timeit
class Sort_Diana:
    def __init__(self, cars_list, sort_condition):
        self._ = cars_list
        if sort_condition == 1:
            self.comparator = self.sort_by_token
        elif sort_condition == 2:
            self.comparator = self.sort_by_brand_and_model
        elif sort_condition == 3:
            self.comparator = self.sort_by_brand_and_model_and_token
        elif sort_condition == 4:
            self.comparator = self.sort_by_profit

    @staticmethod
    def sort_by_token(car1, car2):
        if car1.get_condition("token") < car2.get_condition("token"):
            return True
        elif car1.get_condition("token") == car2.get_condition("token"):
            return None
        return False

    @staticmethod
    def sort_by_brand_and_model(car1, car2):
        if car1.get_condition("brand") < car2.get_condition("brand"):
            return True
        elif car1.get_condition("brand") == car2.get_condition("brand"):
            if car1.get_condition("model") < car2.get_condition("model"):
                return True
        return False

    @staticmethod
    def sort_by_brand_and_model_and_token(car1, car2):
        if car1.get_condition("brand") < car2.get_condition("brand"):
            return True
        elif car1.get_condition("brand") == car2.get_condition("brand"):
            if car1.get_condition("model") < car2.get_condition("model"):
                return True
            elif car1.get_condition("model") == car2.get_condition("model"):
                if car1.get_condition("token") < car2.get_condition("token"):
                    return True
        return False

    @staticmethod
    def sort_by_profit(car1, car2):
        profit_car1 = car1.get_condition("sellingprice") - car1.get_condition("buyingprice")
        profit_car2 = car2.get_condition("sellingprice") - car2.get_condition("buyingprice")
        if profit_car1 < profit_car2:
            return True
        elif profit_car1 == profit_car2:
            return None
        return False

    def merge_sort(self, cars):
        if len(cars) > 1:
            mid = len(cars) // 2
            sub_cars1 = cars[:mid]
            sub_cars2 = cars[mid:]

            self.merge_sort(sub_cars1)
            self.merge_sort(sub_cars2)

            i = j = k = 0

            while i < len(sub_cars1) and j < len(sub_cars2):
                if self.comparator(sub_cars1[i], sub_cars2[j]):
                    cars[k] = sub_cars1[i]
                    i += 1
                elif not self.comparator(sub_cars1[i], sub_cars2[j]):
                    cars[k] = sub_cars1[i]
                    j +=1
                k += 1

            while i < len(sub_cars1):
                cars[k] = sub_cars1[i]
                i += 1
                k += 1

            while j < len(sub_cars2):
                cars[k] = sub_cars2[j]
                j += 1
                k += 1

        return cars

class Search_Diana:
    def __init__(self, entity_list, search_condition):
        self.entity_list = entity_list
        self.search_condition = search_condition

    @timeit
    def secventail_search(self):
        for entity in self.entity_list:
            if entity.get_condition("token") == self.search_condition:
                return entity
        return None