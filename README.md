# Инвертированный список (Инвертированный индекс)

:woman_teacher: Условие задачи:

1. Реализовать алгоритм инвертированного индекса в заданном списке на языке программирования Python. 

---

:writing_hand: Немного о реализации:

Алгоритм Инвертированного индекса

Пусть у нас есть документы, которые содержат в себе следующую информацию:
-	Doc1 (id документа - 1): new home sales top forecasts 
-	Doc2 (id документа - 2): home sales rise in july 
-	Doc3 (id документа - 3): increase in home sales in july
-	Doc4 (id документа - 4): july new home sales rise
Чтобы построить инвертированный список для данной коллекции документов, необходимо:
1.	Составить таблицу последовательности терминов в каждом документе в сопровождении соответствующих идентификаторов документов;
    <div align="left">
        <img src="https://github.com/stud-programmist/-/blob/main/image/1.png" width= "250"/>
    </div>

2.	Отсортировать данную таблицу по алфавиту (по возрастанию от «а» до «я»);
    <div align="left">
        <img src="https://github.com/stud-programmist/-/blob/main/image/2.png" width= "250"/>
    </div>

3.	Сгруппировать одинаковые термины по слову;
    <div align="left">
        <img src="https://github.com/stud-programmist/-/blob/main/image/3.png" width= "250"/>
    </div>


4.	Упорядочить идентификаторы документов.
    <div align="left">
        <img src="https://github.com/stud-programmist/-/blob/main/image/4.png" width= "250"/>
    </div>
