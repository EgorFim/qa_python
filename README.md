# qa_python
==================================================================== test session starts ====================================================================
platform win32 -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0 -- C:\yandex\qa_python\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\yandex\qa_python
collected 18 items                                                                                                                                            

tests.py::TestBooksCollector::test_init_books_genre PASSED                                                                                             [  5%] 
tests.py::TestBooksCollector::test_init_favorites PASSED                                                                                               [ 11%] 
tests.py::TestBooksCollector::test_init_genre PASSED                                                                                                   [ 16%] 
tests.py::TestBooksCollector::test_init_genre_age_rating PASSED                                                                                        [ 22%] 
tests.py::TestBooksCollector::test_add_new_book_in_books_genre PASSED                                                                                  [ 27%]
tests.py::TestBooksCollector::test_add_new_book_have_no_genre[\u0423\u043b\u0438\u0441\u0441] PASSED                                                   [ 33%] 
tests.py::TestBooksCollector::test_add_new_book_have_no_genre[\u0417\u0430\u0434\u0430\u0447\u0430] PASSED                                             [ 38%] 
tests.py::TestBooksCollector::test_add_new_book_have_no_genre[\u0413\u0438\u043f\u0435\u0440\u0438\u043e\u043d] PASSED                                 [ 44%] 
tests.py::TestBooksCollector::test_set_book_genre_add_from_list PASSED                                                                                 [ 50%] 
tests.py::TestBooksCollector::test_get_book_genre_for_name PASSED                                                                                      [ 55%] 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_add_in_list PASSED                                                                    [ 61%] 
tests.py::TestBooksCollector::test_get_books_genre[\u0423\u043b\u0438\u0441\u0441-\u0423\u0436\u0430\u0441\u044b] PASSED                               [ 66%] 
tests.py::TestBooksCollector::test_get_books_genre[\u0417\u0430\u0434\u0430\u0447\u0430-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 72%] 
tests.py::TestBooksCollector::test_get_books_genre[\u0413\u0438\u043f\u0435\u0440\u0438\u043e\u043d-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 77%]
tests.py::TestBooksCollector::test_get_books_for_children_age_book_with_rating_genre_not_in_list PASSED                                                [ 83%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_if_list_is_empty PASSED                                                                       [ 88%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites_after_add PASSED                                                                         [ 94%] 
tests.py::TestBooksCollector::test_get_list_of_favorites_books_after_add PASSED                                                                        [100%] 

==================================================================== 18 passed in 0.04s ===================================================================== 