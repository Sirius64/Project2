from flask import request, render_template
from Project1_Flask import app, forms


@app.route('/')
@app.route('/search', methods=["GET", "POST"])
def search():
    search_form = forms.SearchBooksLists(request.form)

    if request.method == 'POST':
        # retrieve the input data
        genre_list = search_form.genre_list_input.data
        date_chosen = search_form.date_chosen_input.data
        current_date = search_form.current_date_input.data

        # store the form data
        nyt_books = forms.get_data(genre_list, date_chosen, current_date)

        # return the results page
        return render_template('results.html', form=search_form, results=nyt_books)

    # return the search page
    return render_template('search.html', form=search_form)
