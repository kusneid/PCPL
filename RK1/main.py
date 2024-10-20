from operator import itemgetter

class Chapter:
    def __init__(self, id, chapterName, wordCount, documentID):
        self.id = id
        self.chapterName = chapterName
        self.wordCount = wordCount
        self.documentID = documentID

class Document:
    def __init__(self, id, name, path, author):
        self.id = id
        self.name = name
        self.author = author
        self.path = path

class ChaptersOfDocument:
    def __init__(self, doc, part):
        self.doc = doc
        self.part = part

documents = [
    Document(1,"kvshka","/doc/1.docx","kolya chernev"),
    Document(2,"elteh","/doc/2.docx","sofya grishkova"),
    Document(3,"text","/doc/3.txt","roma hudyakov"),
    Document(4,"otchet","/doc/5.docx","dima"),
    Document(5,"english","/doc/4.doc","slava"),
]

chapters = [
    Chapter(1,"general introduction",200,1),
    Chapter(2,"review",300,1),
    Chapter(3,"methods",150,2),
    Chapter(4,"results",100,3),
    Chapter(5,"discussion",50,3),
    Chapter(6,"general conclusion",250,4),
    Chapter(7,"summary",200,5),
    Chapter(8,"final chapter",250,5)
]

chapters_of_documents = [
    ChaptersOfDocument(documents[0],chapters[0]),
    ChaptersOfDocument(documents[1],chapters[0]),
    ChaptersOfDocument(documents[0],chapters[1]),
    ChaptersOfDocument(documents[1],chapters[2]),
    ChaptersOfDocument(documents[2],chapters[3]),
    ChaptersOfDocument(documents[2],chapters[4]),
    ChaptersOfDocument(documents[3],chapters[5]),
    ChaptersOfDocument(documents[4],chapters[6]),
    ChaptersOfDocument(documents[4],chapters[7])
]
def main():

    one_to_many = [(chapter.chapterName, chapter.wordCount, doc.name)
                   for doc in documents
                   for chapter in chapters
                   if chapter.documentID == doc.id]

    many_to_many_temp = [(doc.name, cd.doc.id, cd.part.id)
                         for doc in documents
                         for cd in chapters_of_documents if doc.id == cd.doc.id]

    many_to_many = [(chapter.chapterName, chapter.wordCount, doc_name)
                    for doc_name, doc_id, chapter_id in many_to_many_temp
                    for chapter in chapters if chapter.id == chapter_id]

    #1
    result1 = [item for item in one_to_many if item[0].startswith('r')]
    print("1:")
    for item in result1:
        print(f"раздел:{item[0]}, документ:{item[2]}")

    #2
    result2 = [(doc_name, min([word_count for chapter_name, word_count, name in one_to_many if name == doc_name]))
               for doc_name in set([doc_name for _, _, doc_name in one_to_many])]
    result2 = sorted(result2, key=itemgetter(1))
    print("\n2:")
    for doc_name, min_word_count in result2:
        print(f"документ:{doc_name}, минимальное кол-во слов в его разделах:{min_word_count}")


    #3
    result3 = sorted(many_to_many, key=itemgetter(0))
    print("\n3:")
    for chapter_name, word_count, doc_name in result3:
        print(f"раздел:{chapter_name}, документ:{doc_name}")

if __name__ == '__main__':
    main()
