import json
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, OWL, RDFS, XSD

g = Graph()
g.parse("books_base.ttl", format='turtle')

books = Namespace('http://rpcw.di.uminho.pt/2024/livros/')

def format_uri(name):
    return URIRef(books + name.strip().replace(" ", "_").replace(",", "").replace("'", "").replace("<", "(").replace(">", ")"))

with open("dataset_2.json", "r", encoding='utf-8') as file:
    content = json.load(file)

def add_list_data_properties(tipo, value, book_uri):

    if type(value) is list:
        for v in value:
                g.add((book_uri, tipo, Literal(v)))
    else:
         g.add((book_uri, tipo, Literal(value)))

def add_value2set(conjunto, value):
    
    if type(value) is not list:
        conjunto.add(value)
    else:
        for v in value:
            conjunto.add(v)


autores = set()
personagens = set()
genres = set()
linguas = set()
publicadores = set()
premios = set()
formatoLivro = set()

for book in content: 
    add_value2set(autores, book["author"])
    add_value2set(personagens, book["characters"])
    add_value2set(genres, book["genres"])
    add_value2set(linguas, book["language"])
    add_value2set(publicadores, book["publisher"])
    add_value2set(premios, book["awards"])
    add_value2set(formatoLivro, book["bookFormat"])

for index, a in enumerate(list(autores)):
    id_author = "a" + str(index + 1)
    author_uri = format_uri(id_author)

    if((author_uri, RDF.type, books.Autor)) not in g:
            g.add((author_uri, RDF.type, OWL.NamedIndividual))
            g.add((author_uri, RDF.type, books.Autor))
            g.add((author_uri, books.id_autor, Literal(id_author)))
            g.add((author_uri, books.nome_autor, Literal(a)))

for index, a in enumerate(list(personagens)):
    id_personagem = "a" + str(index + 1)
    personagem_uri = format_uri(id_personagem)

    if((author_uri, RDF.type, books.Autor)) not in g:
            g.add((author_uri, RDF.type, OWL.NamedIndividual))
            g.add((author_uri, RDF.type, books.Autor))
            g.add((author_uri, books.id_autor, Literal(id_author)))
            g.add((author_uri, books.nome_autor, Literal(a)))

for book in content:
    book_uri = format_uri(book["isbn"])

    # Adicionar novo livro caso não exista
    if (book_uri, RDF.type, books.Livro) not in g:
        g.add((book_uri, RDF.type, OWL.NamedIndividual))
        g.add((book_uri, RDF.type, books.Livro))

    # Adiconar data properties do Livro
    g.add((book_uri, books.title, Literal(book["title"].replace(" ", "_").replace("'", "").replace("<", "(").replace(">", ")").replace("|"," ").replace('"', "").replace("\t", " ").replace("#", "").replace("\\", "_"))))
    add_list_data_properties(books.setting, books["setting"], book_uri)
    g.add((book_uri, books.series, Literal(book["series"])))
    add_list_data_properties(books.ratingsByStars, books["ratingsByStars"], book_uri)
    g.add((book_uri, books.rating, Literal(book["rating"])))
    g.add((book_uri, books.publishDate, Literal(book["publishDate"])))
    g.add((book_uri, books.price, Literal(book["price"])))
    g.add((book_uri, books.pages, Literal(book["pages"])))
    g.add((book_uri, books.numRatings, Literal(book["numRatings"])))
    g.add((book_uri, books.likedPercent, Literal(book["likedPercent"])))  
    g.add((book_uri, books.isbn, Literal(book["isbn"])))
    g.add((book_uri, books.firstPublishDate, Literal(book["firstPublishDate"])))
    g.add((book_uri, books.description, Literal(book["description"])))
    g.add((book_uri, books.coverImg, Literal(book["coverImg"])))
    g.add((book_uri, books.bookId, Literal(book["bookId"])))
    g.add((book_uri, books.bbeScore, Literal(book["bbeScore"])))
    g.add((book_uri, books.bbeVotes, Literal(book["bbeVotes"])))
    g.add((book_uri, books.edition, Literal(book["edition"])))

    for index, a in enumerate(list(book["author"])):
        id_author = "a" + str(index + 1)
        author_uri = format_uri(id_author)
        g.add((book_uri, books.escreveu, author_uri))

    # Adicionar Genres se não existirem
    for gen in book["genres"]:
        genre_uri = format_uri(gen.replace(" ", "_").replace("'", "").replace("<", "(").replace(">", ")").replace("|"," ").replace('"', "").replace("\t", " ").replace("#", "").replace("\\", " "))

        if (genre_uri, RDF.type, books.Genre) not in g:
            g.add((genre_uri, RDF.type, OWL.NamedIndividual))
            g.add((genre_uri, RDF.type, books.Genre))
            g.add((genre_uri, books.id_genre, Literal(gen)))
        
        g.add((book_uri, books.classificadoComo, genre_uri))

    # Adicionar Personagem caso não existam
    for c in book["characters"]:
        personagem_uri = format_uri(c.replace(" ", "_").replace("'", "").replace("<", "(").replace(">", ")").replace("|"," ").replace('"', "").replace("\t", " ").replace("#", "").replace("\\", " "))

        if (personagem_uri, RDF.type, books.Personagem) not in g:
            g.add((personagem_uri, RDF.type, OWL.NamedIndividual))
            g.add((personagem_uri, RDF.type, books.Personagem))
            g.add((personagem_uri, books.id_personagem, Literal(c)))

        g.add((personagem_uri, books.pertencemA, book_uri))

    # Adicionar Formato do Livro caso não exista

    bookFormat_uri = format_uri(book["bookFormat"].replace(" ", "_").replace("'", "").replace("<", "(").replace(">", ")").replace("|"," ").replace('"', "").replace("\t", " ").replace("#", "").replace("\\", " "))

    if((bookFormat_uri, RDF.type, books.FormatoLivro)) not in g:
        g.add((bookFormat_uri, RDF.type, OWL.NamedIndividual))
        g.add((bookFormat_uri, RDF.type, books.FormatoLivro))
        g.add((bookFormat_uri, books.id_format, Literal(book["bookFormat"])))
    
    g.add((book_uri, books.formato, bookFormat_uri))

    # Adicionar Publicador caso não exista
    publisher_uri = format_uri(book["publisher"].replace(" ", "_").replace("'", "").replace("<", "(").replace(">", ")").replace("|"," ").replace('"', "").replace("\t", " ").replace("#", "").replace("\\", " "))

    if((publisher_uri, RDF.type, books.Publicador)) not in g:
        g.add((publisher_uri, RDF.type, OWL.NamedIndividual))
        g.add((publisher_uri, RDF.type, books.Publicador))
        g.add((publisher_uri, books.id_publisher, Literal(book["publisher"])))
    
    g.add((book_uri, books.publicadoPor, publisher_uri))

    # Adicionar Prémios caso não existam
    for a in book["awards"]:
        premio_uri = format_uri(a.replace(" ", "_").replace("'", "").replace("<", "(").replace(">", ")").replace("|"," ").replace('"', "").replace("\t", " ").replace("#", "").replace("\\", " "))

        if (premio_uri, RDF.type, books.Prémios) not in g:
            g.add((premio_uri, RDF.type, OWL.NamedIndividual))
            g.add((premio_uri, RDF.type, books.Prémios))
            g.add((premio_uri, books.id_awards, Literal(a)))

        g.add((book_uri, books.recebeu, premio_uri))

    # Adicionar Lingua caso não exista
    lingua_uri = format_uri(book["language"].replace(" ", "_").replace("'", "").replace("<", "(").replace(">", ")").replace("|"," ").replace('"', "").replace("\t", " ").replace("#", "").replace("\\", " "))

    if((lingua_uri, RDF.type, books.Língua)) not in g:
        g.add((lingua_uri, RDF.type, OWL.NamedIndividual))
        g.add((lingua_uri, RDF.type, books.Língua))
        g.add((lingua_uri, books.id_lingua, Literal(book["language"])))
    
    g.add((book_uri, books.escritoEm, lingua_uri))

g.serialize("books.ttl", format='turtle')