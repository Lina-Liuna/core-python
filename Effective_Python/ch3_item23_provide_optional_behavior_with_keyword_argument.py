# you can assign keyword arguments withing the parentheses of a function call.
# you can mix and match keyword and positional arguments.
import collections

acronym_words = {
    'FYI': 'For your information',
    'BTW': 'By the way',
    'GR8': 'Great',
    'IDK': 'I don\'t know',
    'IDC': 'I don\'t care',
    'JK' : 'Just kidding',

}

def words(word, meaning):
    print(f'{word}:{meaning}')

#words(**acronym_words)     #error, dont find word and meaning
acronym_words = {
    'word': 'FYI',
    'meaning': 'For your information',
}
words(**acronym_words)