from Project1_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms.fields import SelectField, DateField, BooleanField


class SearchBooksLists (FlaskForm):
    # url for requesting the list of names
    api_key = ''
    list_names_url = 'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key=nLVLYKs3UG744X6k7NoEaY6fGlhiAnF5'
    response = requests.get(list_names_url).json()

    # retrieve the list of names and save it in a json file
    nyt_list_names_file_name = "Project1_Flask\\JSON_Files\\nyt_list_names.json"
    main_functions.save_to_file(response, nyt_list_names_file_name)

    # read the json file and extract all the names in an array of tuples
    nyt_list_names = main_functions.read_from_file(nyt_list_names_file_name)
    name_list = []
    for x in range(len(nyt_list_names['results'])):
        name_list.append((nyt_list_names['results'][x]['list_name_encoded'], nyt_list_names['results'][x]['list_name']))

    # instantiate the required input fields and add the current parameters for the genre options
    genre_list_input = SelectField(choices=[(x, y) for x, y in name_list])
    date_chosen_input = DateField('')
    current_date_input = BooleanField('Most recent List.')


def get_data(genre_list, date_chosen, current_date):
    # read the api key file
    api_key_dict = main_functions.read_from_file("Project1_Flask\\JSON_Files\\api_key.json")
    api_key = api_key_dict["my_key"]

    # define the base api url
    book_review_url = "https://api.nytimes.com/svc/books/v3/"

    # url for current {date} and {list} choice
    if current_date and genre_list is not None:
        search_url = book_review_url + "lists/current/" + genre_list + ".json?api-key=" + api_key
        # print("1")
    # url for chosen date and chosen genre
    elif date_chosen is not None and genre_list is not None:
        search_url = book_review_url + "lists/" + str(date_chosen) + "/" + genre_list + ".json?api-key=" + api_key
        # print("2")
    # url for no date selected and default genre
    elif not current_date and date_chosen is None and genre_list is not None:
        search_url = book_review_url + "lists/current/" + genre_list + ".json?api-key=" + api_key
        # print("3")

    # receive the response
    response = requests.get(search_url).json()

    # save the response
    nyt_response_file_name = "Project1_Flask\\JSON_Files\\NYT_response.json"
    main_functions.save_to_file(response, nyt_response_file_name)

    # read the saved response
    list_info = main_functions.read_from_file(nyt_response_file_name)

    # return the response
    return list_info
