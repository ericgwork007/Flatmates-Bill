#When the file turns green after being added to git, which means it is added to the staging area and ready to commit.
#When we enabled git through VCS -> git, the .git folder got created in the project file directory.

from greets import greetings

for g in greetings:
    print(g.title())