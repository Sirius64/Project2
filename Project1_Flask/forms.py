from Project1_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField

from wtforms.fields import SelectField, DateField, BooleanField


class SearchBooksLists (FlaskForm):
    api_key = ''
    list_names_url = 'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key=nLVLYKs3UG744X6k7NoEaY6fGlhiAnF5'
    response = requests.get(list_names_url).json()

    nyt_list_names_file_name = "Project1_Flask\\JSON_Files\\nyt_list_names.json"
    main_functions.save_to_file(response, nyt_list_names_file_name)

    nyt_list_names = main_functions.read_from_file(nyt_list_names_file_name)
    name_list = []
    for x in range(len(nyt_list_names['results'])):
        name_list.append((nyt_list_names['results'][x]['list_name_encoded'], nyt_list_names['results'][x]['list_name']))

    genre_list_input = SelectField(choices=[(x, y) for x, y in name_list])
    date_chosen_input = DateField('')
    current_date_input = BooleanField('Most recent List.')

    # list_input = RadioField(choices=[('list', 'View Book Lists?'), ('review', 'View Book Reviews?')])
    # option_input = RadioField(choices=[('history', 'View History?'), ('overview', 'View Overview?')])
    # title_input = StringField('Title?')
    # author_input = StringField('Author?')


def get_data(genre_list, date_chosen, current_date):
    # , lists, option, title, author):
    api_key_dict = main_functions.read_from_file("Project1_Flask\\JSON_Files\\api_key.json")
    api_key = api_key_dict["my_key"]

    # author = author.replace(" ", "%20", len(author))
    # title = title.replace(" ", "%20", len(title))

    book_review_url = "https://api.nytimes.com/svc/books/v3/"

    print(date_chosen)
    print(str(date_chosen))

    # url for {date} {list} choice
    if current_date and genre_list is not None:
        search_url = book_review_url + "lists/current/" + genre_list + ".json?api-key=" + api_key
        # print("1")
    elif date_chosen is not None and genre_list is not None:
        search_url = book_review_url + "lists/" + str(date_chosen) + "/" + genre_list + ".json?api-key=" + api_key
        # print("2")
    elif not current_date and date_chosen is None and genre_list is not None:
        search_url = book_review_url + "lists/current/" + genre_list + ".json?api-key=" + api_key
        # print("3")

    # if lists == 'list':
    #     if option == "history":
    #         # url for best sellers history
    #         search_url = book_review_url + "lists/best-sellers/history.json"
    #         if title != "":
    #             search_url = search_url + "?title=" + title + "&api-key=" + api_key
    #         elif author != "":
    #             search_url = search_url + "?author=" + author + "&api-key=" + api_key
    #     elif option == "overview":
    #         # url for top 5 best sellers list in a given date
    #         search_url = book_review_url + "lists/overview.json"
    #         if date_chosen != "":
    #             search_url = search_url + "?published_date=" + date_chosen
    #     else:
    #         # url for {date} {list} choice
    #         if date_chosen != "" and genre_list != "":
    #             search_url = book_review_url + "lists/" + date_chosen + "/" + genre_list + ".json?api-key=" + api_key
    #         elif genre_list != "":
    #             search_url = book_review_url + "lists/current/" + genre_list + ".json?api-key=" + api_key
    # else:
    #     # url for review
    #     search_url = book_review_url + "reviews.json"
    #     if title != "":
    #         search_url = search_url + "?title=" + title + "&api-key=" + api_key
    #     elif author != "":
    #         search_url = search_url + "?author=" + author + "&api-key=" + api_key
    #     elif title != "" and author != "":
    #         search_url = search_url + "?title=" + title + "&author=" + author + "&api-key=" + api_key

    response = requests.get(search_url).json()

    nyt_response_file_name = "Project1_Flask\\JSON_Files\\NYT_response.json"
    main_functions.save_to_file(response, nyt_response_file_name)

    list_info = main_functions.read_from_file(nyt_response_file_name)

    return list_info
