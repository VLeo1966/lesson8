from abc import ABC, abstractmethod

# Абстрактный класс для форматирования отчетов
class Formatted(ABC):

    @abstractmethod
    def format(self, report):
        pass

# Класс для текстового форматирования отчетов
class TextFormatted(Formatted):

    def format(self, report):
        print(f"Заголовок: {report.title}")
        print(f"Содержание: {report.content}")

# Класс для HTML-форматирования отчетов
class HtmlFormatted(Formatted):

    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

# Класс для создания отчетов
class Report:

    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)

# Пример использования
if __name__ == "__main__":
    # Создание отчета в текстовом формате
    report = Report('Заголовок отчета', 'Это текст отчета, его тут много', TextFormatted())
    report.docPrinter()

    print("\n---\n")

    # Создание отчета в формате HTML
    report = Report('Заголовок отчета', 'Это текст отчета, его тут много', HtmlFormatted())
    report.docPrinter()
