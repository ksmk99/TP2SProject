"""Modules for create interface, translate text and create sentences"""
from transformers import pipeline, set_seed


def generate_en_text(text, length):
    """Function generate English text"""
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    txt = generator(text, max_length=length,
                    num_return_sequences=1)[0]['generated_text']

    return txt


def generate_ru_text(text, length):
    """Function generate Russian text"""
    en_text = translate_text_to_en(text)
    generated_en_text = generate_en_text(en_text, length)
    generated_ru_text = translate_text_to_ru(generated_en_text)

    return generated_ru_text

