"""Module for translate text"""
from deep_translator import GoogleTranslator


def translate_text_to_en(text):
    """Function translate text to English"""
    return GoogleTranslator(source='auto', target='en').translate(text)


def translate_text_to_ru(text):
    """Function translate text to Russian"""
    return GoogleTranslator(source='en', target='ru').translate(text)