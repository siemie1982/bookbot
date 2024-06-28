def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = word_count(text)
    chars_dict = char_count(text)
    char_numb = char_list(chars_dict)
    

    
    print(f"---Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    print()
    for item in char_numb:
          print(f"the' {item['char']}' character was found {item['num']} times")

    print("end report")
    
    

   
def word_count(book):
        return len(book.split())
       

def book_text(path):
      with open(path) as f:
        return f.read()

def char_count(booktext):
     char_dict = {}
     for i in booktext.lower():
            if i.isalpha():
                if i not in char_dict:
                        char_dict[i]= 1
                else:
                        char_dict[i]+= 1        
     return char_dict

def sort_on(d):
    return d["num"]

def char_list(char_dict):
      char_lst = []
      for ch in char_dict:
            char_lst.append({"char":ch, "num": char_dict[ch]})
            char_lst.sort(reverse=True, key=sort_on)
     
      return char_lst


def prnt_count(char_numb):
      char_numb.sort(reverse=True, key=sort_on)
      
     
    
    



main()