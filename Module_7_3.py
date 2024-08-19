class WordsFinder:
    def __init__(self,*args):
        self.file_names = args

    def list_word(self):
        for i in self.file_names:
            with open(i,encoding='utf-8') as file:
                del_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
                string_file = file.read()
                string_file = string_file.lower()
                for j in del_symbols:
                    if j in string_file:
                        string_file = string_file.replace(j,' ')
                _list=string_file.split()
                return _list

    def get_all_words(self):
        all_words = dict()
        self.list_word()
        all_words.update({self.file_names: self.list_word()})
        return all_words


    def find(self, word):
        word = word.lower()
        j=1
        for i in self.list_word():
            if i == word:
                _dict = {self.file_names:j}
                return _dict
            else:
                j+=1

    def count(self, word):
        word = word.lower()
        summ = 0
        for i in self.list_word():
            if i == word:
                summ +=1
        _dict = {self.file_names:summ}
        return _dict

finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего