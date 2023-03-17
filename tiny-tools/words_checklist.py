import collections

import pandas as pd
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib
import os
from pathlib import Path
from PIL import Image
import img2pdf
import common

from fpdf import FPDF

class WordsList:
    def words_diagram(self, words, meaning):
        words_df = pd.DataFrame(
            meaning,
            index= words,
            columns=['new words list']
        )

        matplotlib.rc('figure', figsize=(10, 5))
        for key in words:
            words_df.style.set_properties(subset=[key], **{'width': '1000000px'})

        words_df.plot()
        plt.show()

    def words_to_pdf(self, font_type, pdf_name, words_dict):

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.page_mode = "FULL_SCREEN"
        pdf.add_font('TeachersStudent-Regular', '',os.path.join(os.path.dirname(os.path.realpath(__file__)), "font", 'TeachersStudent-Regular.ttf'),uni=True)
        # pdf.add_font('KGPrimaryDotsLinedNOSPACE', '', font_type, uni=True)
        pdf.set_font('TeachersStudent-Regular', '', 10)
        pdf.add_page()
        for rank, (word, meaning_example) in enumerate(words_dict.items(), 1):

            pdf.cell(w=2, h=10, txt=f'{rank}:{word}:{meaning_example[0]}', ln=1)
        pdf.output(pdf_name, 'F')

    def new_words(self):
        mark = '-'
        print(f'\n{mark*20}New Words{mark*80}\n')
        new_words = collections.defaultdict(list)

        new_words = {
            'stride': ['walk with long, decisive steps.', 'he strode across the road'],
            'collation': ['the action of collating something or a light informal meal',
                          'data management and collation, lunch '
                          'wwas a collation of salami, olives, '
                          'and rye bread'],
            'trivial': ['of little value or importance', 'the story spends too much time on trivial matters'],
            'reliant': ['dependent on someone or something', 'self-reliant'],
            'oars': [
                'a pole with a flat blade, pivoting in an oar lock, used to row or steer a boat through the water.',
                ''],
            'conviction': ['a firmly held belief or opinion',
                           'He said he was enjoying his new job, but his voice lacked conviction'],
            'chisel': ['A cutting tool used to remove parts os stone, wood, or metal by pushing when the sharp '
                       'edge is against the material'],
            'acronym': ['akrenim, an abbreviation formed from the initial letters of other words', ''],
            'tabular': ['consisting of or presented in columns or tables', 'a tabular presentation of running costs'],
            'utilize': ['make practical and effective use of',
                        'Vitamin C helps your body utilize the iron present in your diet,'
                        'Our school should utilize a FULL DAY SCHEDULE for all students.'],

            'denim': [' a sturdy cotton twill fabric, typically blue, used for jeans, overalls, and other clothing',
                      'Hes wearing faded denims and cowboy boots'],
            'cumbersome': ['large or heavy and therefore difficult to carry or use; unwieldy',
                           'cumbersome diving suits; organizations with cumbersome hierarchical structures'],
            'migrate': ['move from one part of something to another',
                        'as fall arrives, the birds migrate south'],
            'nuisance': [' a person, thing, or circumstance causeing inconvenience or annoyance',
                         'I hope youre not going to make a nuisance of yourself. '],
            'spawn': ['(of a fish, frog, mollusk, crustacean, etc.) release or deposit eggs',
                      'the fish spawn among fine-leaved plants'],
            'ancillary': ['providing support to primary activities or industry, system',
                          'the development of ancillary services to support its products'],
            'batch': ['a quantity of goods produced at one time',
                      'a batch of cookies'],
            'raptor': ['a bird of prey', 'egle, hawk, falcon, owl are all raptors'],
            'hydra': ['a minute freshwater with tubular body and a ring of tentacles around the mouth'],
            'Parentheses': ['xiaokuohao'],
            'brackets': ['kuohao'],
            'zodiac': ['xingzuo'],
            'cascade': ['a small watefall, typically one of several that fall in stages down a steep rocky slope',
                        'a process whereby something, typically information or knowledge, is successively passed on',
                        'the greater the number of people who are are well briefed, the wider the cascade effect'],
            'sporadic': ['occurring at irregular itervals or only in a few places; scattered or isolated',
                         'sporadic fighting broke out',
                         'the mail carrier comes every  day but the plumber\'s visits are sporadic - he comes as needed'],

            'poly': ['many, much'],
            'morph': ['change smoothly from one image to another by small gradual steps using computer animation techs',
                      'a morph is phonological string that cannot be broken down into smaller constituents that have '
                      'a lexicogrammatical function.',
                      'means a transforming, to transform, to change.',
                      'shape, form',
                      ],
            'polymorphism': ['polymorphism describes how objects can take on many shapes by inheriting attributes '
                             'from parent classes'],
            'polymorph': ['change into many shapes'],
            'amorphous': ['not havingg a fixed shape'],
            'canonical': ['related to or according to a rule, principle, or law, especially in the christian church',
                          'a canonical rule'],
            'trisect': ['divide (sth) into three parts, typically three equal parts'],
            'Thesaurus': [' a book or electronic resource that lists words in groups of synonyms and related concepts',
                          'I am going to need a thesaurus to come up with sunonyms for stupid'],
            'plot': ['the main events of a play, novel, movie, or similar work, devised and presented by the writer'
                     'as an iterrelated sequence.'],
            'Boilerplate': ['the term of boilerplate refers to standardized text, copy, documents, methods'
                            'or procedures that may be used over again without making major changes to the original'],

            'algebra': ['the part of mathematics in which letters and other general symbols are used to '
                        'represent numbers and quantities in formulae  and equations',
                        'courses in algebra, geometry, and Newtonian physics'],
            'approximation': ['a value or quantity that is nearly but not exactly correct',
                              'these figures are only approximations',
                              'a thing that is similar to something else, but is not exactly the same',
                              'the band smashed up their equipment in an approximation of rock star behavior'],
            'vaguely': ['in a way that is uncertain, indefinite or unclear, roughly',
                        'he veguely remembered talking to her once'],
            'pitfall': ['a hidden or unsuspected danger or difficulty',
                        'a covered pit used as a trap'],
            'bizarre': ['very strange or unusual, especially so as to cause interest or amusement',
                        'her bizarre dresses and outrageous hairdos'],
            'transition': ['undergo or cause to undergo a process or period of transition',
                           'he transitined into filmmaking easily',
                           'adopt permanently the outward or physical characteristics that match ones'
                           'gender identity'],
            'quota': ['a fixed share of something that a person or group is entitled to receive or '
                      'is bound to contribute',
                      ''],
            'hygiene': ['conditions or practices conductive to maintaining health and preventing disease,'
                        'especially throuogh cleanliness',
                        'poor standards of food hygiene']

            }

        for rank, (word, meaning_example) in enumerate(new_words.items(), 1):


            print(f'#{rank}: word = {word}; meaning_example = {list(meaning_example)}')
        return new_words

words_lists=WordsList()
newwords= words_lists.new_words()
font = '/Users/linaliu/books/font/ttf_here/Arial.ttf'
pdfname = '/Users/linaliu/books/fonts/new_words/newwords.pdf'
words_lists.words_to_pdf(font, pdfname, newwords)
