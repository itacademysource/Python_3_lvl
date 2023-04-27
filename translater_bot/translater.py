from translatepy import Translator
from translatepy.models import TranslationResult


def translater(text: str, language: str = 'en') -> TranslationResult:
    """Функция для перевода текста на любой из языков

    :param text: текст, который нужно перевести
    :param language: язык, на который булем переводить
    :return: TranslationResult
    """
    translator = Translator()
    result = translator.translate(text, language)
    return result
