# book_info = "f. scott fitzgerald ;  the great gatsby ; 1925 ; ISN 978-0-7432-7356-5 ; 180 ; 2799"
# book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
# book_info = "jane austen ;  pride and prejudice  ; 1813 ; ISN 978-0-19-953556-9 ; 279 ; 1820.33434"
# book_infp

# components = book_info.split(" ; ")

# author, book_title, year_published, isbn, no_of_pages, cost = components
# author = author.title()
# book_title = book_title.strip().title()
# isbn = isbn.replace("ISN", "ISBN")
# cost = "₦{0:.2f}".format(float(cost))
























print(f"""The book {book_title} was written by {author} and published in {year_published}.
It has {no_of_pages} pages and {isbn} and costs {cost}.""")