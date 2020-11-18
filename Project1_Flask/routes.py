from flask import request, render_template

from Project1_Flask import app, forms


@app.route('/')
@app.route('/search', methods=["GET", "POST"])
def search():
    search_form = forms.SearchBooksLists(request.form)

    if request.method == 'POST':
        """Assign to the following variables the input values by the user"""
        # state = search_form.state_input.data
        # startdate = search_form.startdate_input.data
        # enddate = search_form.enddate_input.data

        genre_list = search_form.genre_list_input.data
        date_chosen = search_form.date_chosen_input.data
        current_date = search_form.current_date_input.data

        # lists = search_form.list_input.data
        # option = search_form.option_input.data
        # title = search_form.title_input.data
        # author = search_form.author_input.data

        """Pass the variables above as arguments to the get_data function 
        and assign the return value to fda_recall"""
        nyt_books = forms.get_data(genre_list, date_chosen, current_date)  # , lists, option, title, author)

        return render_template('results.html', form=search_form, results=nyt_books)
        # statename=state, startdate=startdate, "No."
        # enddate=enddate, recall=nyt_books)

    return render_template('search.html', form=search_form)
