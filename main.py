# Задание: Нужно написать класс, описывающий координаты на карте. Должно быть два параметра, latitude и longitude.
#
# Класс должен уметь:
# - При принте объекта нужно отображать значение координаты
# - При складывании двух объектов на выходе должен получиться третий объект со скалярной суммой двух предыдущих
#
# Фича для прошаренных:
# - Класс должен иметь метод, при обращении к которому нужно отобразить координату на карте (Гуглим библиотеку geoplotlib)
import geoplotlib


class GeoTag:
    def __init__(self, latitude, longitude):
        """Constructor"""
        self.latitude = latitude
        self.longitude = longitude

        coordinates = (str(self.latitude) + ',' + str(self.longitude))

    def __str__(self):
        return '({}, {})'.format(self.latitude, self.longitude)

    def __add__(self, other):
        return '({}, {})'.format(self.latitude + other.latitude, self.longitude + other.longitude)

    def show_coords(self):
        data = ({'lat': [self.latitude], 'lon': [self.longitude]})
        geoplotlib.set_window_size(600, 600)
        geoplotlib.dot(data)
        geoplotlib.show()

if __name__ == '__main__':
    geo = GeoTag(54.629148, 39.734928)
    geo2 = GeoTag(16, 12)
    print(geo)
    print(geo2)

    geo.show_coords()
    print(geo.__add__(geo2))
