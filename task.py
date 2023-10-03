
class MathUtils:
    @staticmethod
    def multiply(x, y):
        return x*y
    
math = MathUtils()
print(math.multiply(8,23))
    

class DateUtils:
    @classmethod
    def is_valid_date(cls, date:str):
        part = date.split('-')
        count = 0
        for i in part:
            if i.isdigit():
                count += 1

        if count == 3 and int(part[1]) <= 12 and int(part[2]) <= 31:
            return True
        else:
            return False

print(DateUtils.is_valid_date('2023-12-31'))


class StringUtils:
    @staticmethod
    def is_palindrome(string:str):
        if string == string[::-1]:
            return True
        else:
            return False
        
string = StringUtils()
print(string.is_palindrome('loll'))


from math import pi
class Shape:
    @staticmethod
    def get_circle_area(radius):
        return pi*radius**2
    
shape = Shape()
print(shape.get_circle_area(7))


class FileUtils:
    @classmethod
    def get_file_extension(cls, file_name: str):
        if '.' in file_name:
            i = file_name.find('.')
            return file_name[i:]
        else:
            return 'пуст'
        

print(FileUtils.get_file_extension('main.py'))