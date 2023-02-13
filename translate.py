from googletrans import Translator

# Create a Translator object
translator = Translator()

# Get the sentence and target language from the user
sentence = input("Enter the sentence to be translated: ")
target_lang = input("Enter the target language (e.g. 'es' for Spanish): ")

# Translate the sentence to the target language
translation = translator.translate(sentence, dest=target_lang)

# Print the translation
print(translation.text)
