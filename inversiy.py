from abc import ABC, abstractmethod

# Абстрактный класс StorySource, от которого будут зависеть наши источники
class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

# Класс Book, который наследует от StorySource
class Book(StorySource):
    def get_story(self):
        print("Чтение интересной истории")

# Класс AudioBook, который также наследует от StorySource
class AudioBook(StorySource):
    def get_story(self):
        print("Чтение интересной истории вслух")

# Класс StoryReader, который будет зависеть от абстракции StorySource
class StoryReader:
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

# Основная часть программы

# Создаем объекты класса Book и AudioBook
book = Book()
audioBook = AudioBook()

# Создаем объекты класса StoryReader, передавая в них объекты класса Book и AudioBook
readerBook = StoryReader(book)
readerAudioBook = StoryReader(audioBook)

# Используем созданные ранее объекты
readerBook.tell_story()         # Выведет: Чтение интересной истории
readerAudioBook.tell_story()    # Выведет: Чтение интересной истории вслух
