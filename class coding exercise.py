class Animal:
    """Animal class"""

    def __init__(self, name, species, age):
        self.__name = name
        self.__species = species
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, new_name):
        print('Setting name')
        self.__name = new_name
    
    @species.setter
    def species(self,new_species):
        print('Setting species')
        self.__species = new_species

    @age.setter
    def age(self, new_age):
        print('Setting age')
        self.__age = new_age

    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name

    @species.deleter
    def species(self):
        print('Deleting species')
        del self.__species

    @age.deleter
    def age(self):
        print('Deleting age')
        del self.__age
    
    def move(self):
        print(str(self.__name__)+ "is moving.")

    def sleep(self):
        print(str(self.__name__) + "is sleeping.")
    
    def eat(self):
        print(str(self.__name__) + "is eating.")
    
    def protect(self):
        print(str(self.__name__) + "is protecting itself.")

#===========================================================================================

class Book:
    """Book class"""

    def __init__(self, title, publisher, genre, year):
        self.__title = title
        self.__publisher = publisher
        self.__genre = genre
        self.__year = year
    
    @property
    def title(self):
        return self.__title
    
    @property
    def publisher(self):
        return self.__publisher

    @property
    def genre(self):
        return self.__genre

    @property
    def year(self):
        return self.__year

    @title.setter
    def title(self, new_title):
        print('Setting title')
        self.__title = new_title
    
    @publisher.setter
    def publisher(self,new_publisher):
        print('Setting publisher')
        self.__publisher = new_publisher

    @genre.setter
    def genre(self, new_genre):
        print('Setting genre')
        self.__genre = new_genre

    @year.setter
    def year(self, new_year):
        print('Setting year')
        self.__year = new_year

    @title.deleter
    def title(self):
        print('Deleting title')
        del self.__title

    @genre.deleter
    def genre(self):
        print('Deleting genre')
        del self.__genre

    @publisher.deleter
    def publisher(self):
        print('Deleting publisher')
        del self.__publisher
    
    @year.deleter
    def year(self):
        print('Deleting year')
        del self.__year

    def read(self):
        print('The book' + str(self.__title) + 'is being read.')

#====================================================================================

class Vehicle:
    """Vehicle class"""

    def __init__(self, make, model, vin, year):
        self.__make = make
        self.__model = model
        self.__vin = vin
        self.__year = year
    
    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model 

    @property
    def vin(self):
        return self.__vin

    @property
    def year(self):
        return self.__year

    @make.setter
    def title(self, new_make):
        print('Setting make')
        self.__nake = new_make
    
    @model.setter
    def publisher(self,new_model):
        print('Setting model')
        self.__model = new_model

    @vin.setter
    def genre(self, new_vin):
        print('Setting vin')
        self.__vin = new_vin

    @year.setter
    def year(self, new_year):
        print('Setting year')
        self.__year = new_year

    @make.deleter
    def make(self):
        print('Deleting make')
        del self.__make

    @model.deleter
    def model(self):
        print('Deleting model')
        del self.__model

    @vin.deleter
    def vin(self):
        print('Deleting vin')
        del self.__vin
    
    @year.deleter
    def year(self):
        print('Deleting year')
        del self.__year

    def park(self):
        print('The' + str(self.__make) + str(self.__model) + 'is in park.')

    def reverse(self):
        print('The' + str(self.__make) + str(self.__model) + 'is in reverse.')

    def neutral(self):
        print('The' + str(self.__make) + str(self.__model) + 'is in neutral.')

    def drive(self):
        print('The' + str(self.__make) + str(self.__model) + 'is in drive.')

    def park(self):
        print('The' + str(self.__make) + str(self.__model) + 'is in park.')

    def manual(self):
        print('The' + str(self.__make) + str(self.__model) + 'is in manual.')

    def rightturn(self):
        print('The' + str(self.__make) + str(self.__model) + 'is making a right turn.')
    
    def leftturn(self):
        print('The' + str(self.__make) + str(self.__model) + 'is making a left turn.')