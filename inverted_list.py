""" Функция создания инвертированного списка """
def inverted_list(doc_list):
        index = {} 
        terms = []
        """Разбиваем строки на отдельные термины(слова)"""
        for word in doc_list:
            terms.append(word.split())
        #print(terms)
        """Создаю инвентированный список. Цикл включает в себя несколько пунктов алгоритма,
           о котороых будет сказано далее"""
        for i, element in enumerate(terms):
            #print(i, element)
            """Цикл, который создаёт словарь, где ключом будет являться термины из файла,
            а значения - id-документа или набор id-документов,
            если это слово встречается в нексольких документах"""
            for term in element:
                """Условие позволяет сгруппировать одинаковые термины.
                   Если условие истинно, то в словарь добавляется термин и id-документа.
                   В противном случае к уже сушествующему термину добавится новое значение"""
                if term not in index:
                    index[term] = [i+1]
                else:
                    index[term].append(i+1)
        return index

   
""" Создание набора документов в виде списка """

doc_list =["breakthrough drug for schizophrenia", "new schizophrenia drug",
           "new approche for treatment of schizophrenia", "new hopes for schizophrenia patients"]

""" Вызов Функции создания инвертированного списка """
inver_list = inverted_list(doc_list)

"""Вывод инвертированного списка, где пара 'термин id-документа' расположены в алфавитном порядке"""
print(dict(sorted(inver_list.items())))

