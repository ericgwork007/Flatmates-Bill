#When the file turns green after being added to git, which means it is added to the staging area and ready to commit.
#When we enabled git through VCS -> git, the .git folder got created in the project file directory.

from translate import Translator
from greets import greetings

translator = Translator(to_lang='pt')

for g in greetings:
    print(translator.translate(g).title())