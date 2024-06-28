def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    word_count(text)
    num_words = word_count(text)
    
    print(f"{num_words} words found in the book")

    


def word_count(book):
        return len(book.split())
       

def book_text(path):
      with open(path) as f:
        return f.read()
     
    
    



main()