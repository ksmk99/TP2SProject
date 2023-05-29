from deep_translator import GoogleTranslator


def translate_text_to_ru(text):
    """Function translate text to Russian"""
    return GoogleTranslator(source='en', target='ru').translate(text)