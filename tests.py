import pytest


from main import BooksCollector

class TestBooksCollector:


    def test_init_books_genre(self,books):
        books.add_new_book('Улисс')
        assert books.books_genre == {'Улисс':''}

    def test_init_favorites(self,books):
        books.favorites.append('Улисс')
        assert books.favorites == ['Улисс']

    def test_init_genre(self,books):
        lst_1 = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books.genre == lst_1

    def test_init_genre_age_rating(self,books):
        lst_2 = ['Ужасы', 'Детективы']
        assert books.genre_age_rating == lst_2

    def test_add_new_book_in_books_genre(self,books):
        books.add_new_book('Улисс')
        assert 'Улисс' in books.books_genre

    @pytest.mark.parametrize('book',['Улисс','Задача','Гиперион'])
    def test_add_new_book_have_no_genre(self,books,book):
        books.add_new_book(book)
        assert books.get_book_genre(book) == ''

    def test_set_book_genre_add_from_list(self,books):
        book = 'Улисс'
        books.add_new_book(book)
        genre = 'Комедии'
        books.set_book_genre(book,genre)
        assert books.books_genre == {'Улисс':'Комедии'}

    def test_get_book_genre_for_name(self,books):
        book = 'Улисс'
        books.add_new_book(book)
        genre = 'Комедии'
        books.set_book_genre(book, genre)
        assert books.get_book_genre(book) == 'Комедии'

    def test_get_books_with_specific_genre_add_in_list(self,books):
        books.add_new_book('Улисс')
        books.set_book_genre('Улисс','Ужасы')
        assert books.get_books_with_specific_genre('Ужасы') == ['Улисс']

    @pytest.mark.parametrize('book,genres',[['Улисс','Ужасы'],['Задача','Детективы'],['Гиперион','Фантастика']])
    def test_get_books_genre(self,books,book,genres):
        books.add_new_book(book)
        books.set_book_genre(book,genres)
        assert books.get_books_genre() == books.books_genre

    def test_get_books_for_children_age_book_with_rating_genre_not_in_list(self,books):
        books.add_new_book('Улисс')
        books.set_book_genre('Улисс', 'Ужасы')
        assert books.get_books_for_children() == []

    def test_get_books_for_children_add_in_list(self,books):
        books.add_new_book('Гиперион')
        books.set_book_genre('Гиперион', 'Фантастика')
        assert books.get_books_for_children() == ['Гиперион']

    def test_add_book_in_favorites_if_list_is_empty(self,books):
        books.add_new_book('Улисс')
        books.set_book_genre('Улисс', 'Ужасы')
        books.add_book_in_favorites('Улисс')
        assert books.favorites == ['Улисс']

    def test_delete_book_from_favorites_after_add(self,books):
        books.add_new_book('Улисс')
        books.set_book_genre('Улисс', 'Ужасы')
        books.add_book_in_favorites('Улисс')
        books.delete_book_from_favorites('Улисс')
        assert books.favorites == []

    def test_get_list_of_favorites_(self,books):
        books.add_new_book('Улисс')
        books.set_book_genre('Улисс', 'Ужасы')
        books.add_book_in_favorites('Улисс')
        assert 'Улисс' in books.get_list_of_favorites_books()




