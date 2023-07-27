# to install googletrans module in your system
# pip install googletrans

# importing googletrans library to do the language translations
import googletrans

# let's see what is inside googletrans
# print(dir(googletrans))

# lets do the translation now
language_translator = googletrans.Translator()


# let's create a function to extract the list of languages
def get_languages():

    # let's see what all languages can our translator work with
    language_info = googletrans.LANGUAGES

    #  empty language list
    language_list = []

    # iterating over the dictionary
    for language in language_info.items():

        # extracting the languages and adding it to the language list
        language_list.append(language[1])

    # let's return the list
    return language_list

# let's create a function to extract the list of abrreviations
def get_abbreviations():

    # let's see what all languages can our translator work with
    language_info = googletrans.LANGUAGES

    #  empty language list
    abbreviation_list = []

    # iterating over the dictionary
    for language in language_info.items():

        # extracting the languages and adding it to the language list
        abbreviation_list.append(language[0])

    # let's return the list
    return abbreviation_list