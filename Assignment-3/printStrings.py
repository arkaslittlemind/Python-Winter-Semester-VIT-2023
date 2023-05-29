def print_even_length_words(string):
    words = string.split()
    
    for word in words:
        if len(word) % 2 == 0:
            print(word)



string = "Arka loves Arsenal Football Club"
print_even_length_words(string)