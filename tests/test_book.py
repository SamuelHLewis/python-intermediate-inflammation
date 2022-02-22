import pytest

@pytest.mark.parametrize(
    "Title, Author, Expected",
    [["A book", "Me", "A book by Me"]],
    ids=["Standard input"]
)
def test_book(Title, Author, Expected):
    """Test whether Book generates expected return value"""
    from book.book import Book
    book = Book(Title, Author)
    assert str(book) == Expected
