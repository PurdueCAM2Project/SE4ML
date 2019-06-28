Version Control
===============

Software Versions
-----------------

No writer can finish a good book in one shot. A book needs to be writen
section by section and chapter by chapter. The writing is likely
reviewed and revised multiple times. If you watch a movie DVD, you can
find Deleted Scenes— the sections that have been made but never used in
the actual movie. Any non-trivial work needs to be created gradually and
improved over and over again before it is ready. Developing software is
no different: functionality is added gradually. Sometimes, finished
functions need to change because customers’ needs have changed,
competitors have introduced new features and modifications are needed,
new regulations are announced, or new standards are issued. All of these
mean that software must be developed in small pieces; these pieces are
called version.

There is no widely accepted definition of a version, just like there is
no specific definition what should be considered as a chapter in a book.
One may consider each additional line as a new version while another may
consider a completely implemented and fully tested feature as a version.
Generally speaking, a version should be self-contained and a complete
unit, like a section or a chapter in a book. The tools that manage
versions are called version control. When multiple people work together,
version control becomes essential to ensure proper coordination.

There are many version control systems, such CVS (concurrent version
system) and SVN (subversion). This book uses git for version control. It
is a distributed version control system, meaning that there can be two
types of repositories: One is on each user’s computer; the other is
shared by all users. The advantage of a distributed version control
system will become clear after explaining how people collaborate
developing software.

The version control system git is a set of programs managing files. You
can run git on your own computer. You can also set up a git server
shared by multiple people. Alternatively, you can use websites that
offer version control functions; examples include github.com and
bitbucket.org. This book uses github as an example. You can find entire
books talking about git as well as thousands of web postings about how
to use github. The toolset git has many different functions and github
offers many different ways to accomplish the same goals. This book does
not intend to replace those materials. Instead, this book provides
enough details for common needs. Readers interested knowing more can
easily find additional documentations.

github
------

.. _figure-github1:

.. figure:: vc/figures/github1.png
   :alt: github website

   github website

.. _figure-github2:

.. figure:: vc/figures/github2.png
   :alt: Students and teachers can apply for free repositories.

   Students and teachers can apply for free repositories.

This book chooses github for three reasons: (1) It is widely used. (2)
It is free for education purposes. (3) It is supported by many tools
other than the github website. :numref:`figure-github1` shows the
website of github and the portal for an education account. Signing up in
github is easy, as shown in :numref:`figure-github3`. After
creating an account, a repository can be created as shown in
:numref:`figure-github4`. This website has many
options: the name of the repository, whether it is public or private,
whether to initialize the repository with README, etc.
:numref:`figure-github5` shows the options for creating a new
repository:

.. _figure-github3:

.. figure:: vc/figures/github3.png
   :alt: Create an account in github

   Create an account in github

.. _figure-github4:

.. figure:: vc/figures/github4.png
   :alt: Create a repository in github

   Create a repository in github

.. _figure-github5:

.. figure:: vc/figures/github5.png
   :alt: A new repository

   A new repository

.. _figure-github6:

.. figure:: vc/figures/github6.png
   :alt: The repository has been created.

   The repository has been created.

-  Repository name: pythonexamples

-  Description: sample programs written in Python

-  Public

-  Check “Initialize this repository with a README”

-  Select “Add .gitignore: Python”

-  Select “Add a license: Apache License 2.0”

:numref:`figure-github5` and :numref:`figure-github6` shows the repository
after it has been created. As can be seen on the website, there are many
options changing this repository. For example, it is possible adding new
files or uploading files. It is also possible editing an file by
clicking the pen icon.

Clone a Repository
------------------

A more common way of using a repository, however, is to clone the
repository on another computer, as illustrated in
:numref:`figure-gitclone`.

.. _figure-gitclone:

.. figure:: vc/figures/gitclone.png
   :alt: Using git clone command creates a repository on another computer.

   Using git clone command creates a repository on another computer.

To clone a repository, it is necessary knowing the path in github.
:numref:`figure-github7` shows the path of the repository.

.. _figure-github7:

.. figure:: vc/figures/github7.png
   :alt: Cloning a repository may use HTTPS or SSH.

   Cloning a repository may use HTTPS or SSH.

To clone the repository, starts a Terminal in Linux and type the git
clone command. In the following example, $ is the command prompt for the
Terminal.

::

   $ git clone https://github.com/yhluprog/pythonexamples.git

The command clones the repository and the following message is shown:

::

   Cloning into 'pythonexamples'...
   remote: Enumerating objects: 5, done.
   remote: Counting objects: 100% (5/5), done.
   remote: Compressing objects: 100% (5/5), done.
   remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
   Unpacking objects: 100% (5/5), done.
   Checking connectivity... done.

After cloning the repository, a directory (also called folder) with the
name pythonexamples is created. This can be shown using the ls command:

::

   $ ls
   pythonexamples/

Inside this directory, there are already two files: LICENSE and
README.md. The is a hidden file .gitignore. It is hidden because it
starts with . and is not shown by the ls command. To show a hidden file,
it is necessary using the ls -a command. Additionally, a hidden
directory (ending with /) called .git is also shown.

::

   $ cd pythonexamples/
   $ ls -a
   ./  ../  .git/  .gitignore  LICENSE  README.md

Enter the directory using the cd command and use the ls command to see
the files and directories.

::

   $ cd .git
   $ ls
   branches/  config  description  HEAD  hooks/  index  
   info/  logs/  objects/  packed-refs  refs/

Among them, config stores the information about the remote repository.
The more command can show the content of the file:

::

   $ more config
   [core]
       repositoryformatversion = 0
       filemode = true
       bare = false
       logallrefupdates = true
   [remote "origin"]
       url = https://github.com/yhluprog/pythonexamples.git
       fetch = +refs/heads/*:refs/remotes/origin/*
   [branch "master"]
       remote = origin
       merge = refs/heads/master

The line starting with url is the path used in git clone. The concept of
branch will be explained later in this chapter.

Commit and Push
---------------

There are many different methods modifying a repository. The first
method modifies an existing file. Use a text editor and add the
following line to README.md:

::

   This repository demonstrates how to use commit, push, and branch.

::

   $ git commit
   On branch master
   Your branch is up-to-date with 'origin/master'.
   Changes not staged for commit:
       modified:   README.md

After adding this line, use the git commit command to show which file
has been changed:

What does this mean? It says a file README.md has been changed but it
has not been committed. The next question is the difference between
changes and commit. Modifications are often reviewed and revised
multiple times; these changes are transient and do not need to be
recorded in the repository. When the modifications are satisfactory, the
file is ready to “take a snapshot” by creating a new version. The
command to take a snapshot is git commit.

The earlier git commit shows the candidate(s) for commit. A candidate
can be a files that has been modified (README.md in this example). This
command has not committed any changes yet and has not created a new
version. To commit the change of a specific file, it is necessary adding
the file’s name as shown in the following example

::

   $ git commit -m "add a line" README.md 
   [master 26317f0] add a line
    1 file changed, 2 insertions(+)

.. _figure-gitcommit:

.. figure:: vc/figures/gitcommit.png
   :alt: After several changes, git commit creates a new version and stores it in the local repository.

   After several changes, git commit creates a new version and stores it in the local repository.

In this command, -m means the commit message and this commit message is
“add a line”. The name of the file, README.md, is included to indicate
which file to take a snapshot and a new version is created. This new
version is visible at only the local repository, not the remote
repository (in github). To make the changes visible in github, another
command git push is needed.

::

   $ git push
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   Counting objects: 3, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 343 bytes | 0 bytes/s, done.
   Total 3 (delta 1), reused 0 (delta 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/yhluprog/pythonexamples.git
      883333a..26317f0  master -> master

The git push command needs an user name and the password because it does
not allow everyone to push and modify the repository. The rest of the
message can be ignored for now. :numref:`figure-gitpush` shows
the typical workflow of using github: Use git push to modify the remote
repository after several git commit commands creating new versions on
the local repository.

.. _figure-gitpush:

.. figure:: vc/figures/gitpush.png
   :alt: Typical workflow of using github

   Typical workflow of using github

:numref:`figure-github8` shows the github website after git
push. The changes are clearly marked: if a new line is added, a “+” sign
is added in front. Similarly, if a line is deleted, a “-” sign is added
in front (not shown in this example).

.. _figure-github8:

.. figure:: vc/figures/github8.png
   :alt: The website of github shows the change.

   The website of github shows the change.

Add and Remove Files
--------------------

The examples so far only modify an existing file: README.md added by
github when the repository is created. This section explains how to add
and remove files or directories. Use a text editor to create the
following simple Python program (without the line numbers).

.. code:: python

   #!/usr/bin/python3
   # hello.py

   def printhello():
     print("Hello Python")
     
   if __name__== "__main__":
     printhello()

The git add command informs the intention of adding this file to the
repository. It is important to know that this file has not been added
yet. To actually add this file, it is necessary using the git commit
command followed by a message and the name of the file to be added, as
shown below.

::

   $ git add hello.py
   $ git commit -m "add a new file to print hello" hello.py
   [master 1ed761d] add a new file to print hello
    1 file changed, 7 insertions(+)
    create mode 100755 hello.py

The git push command modifies the repository in github

::

   $ git push
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   Counting objects: 3, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 365 bytes | 0 bytes/s, done.
   Total 3 (delta 1), reused 0 (delta 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/yhluprog/pythonexamples.git
      26317f0..1ed761d  master -> master

.. _figure-github10:

.. figure:: vc/figures/github10.png
   :alt: The added file hello.py is listed in github.

   The added file hello.py is listed in github.

A directory can be created using the mkdir command in Linux. Adding a
file in a directory automatically to the repository adds the directory.

To remove a file, use the git rm command, followed by git commit. If git
push is used, the file is also removed from github.

::

   $ git rm hello.py
   rm 'hello.py'
   $ git commit -m "remove the file" hello.py
   [master 3357bae] remove the file
    1 file changed, 7 deletions(-)
    delete mode 100755 hello.py
   $ git push
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   Counting objects: 2, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (2/2), done.
   Writing objects: 100% (2/2), 221 bytes | 0 bytes/s, done.
   Total 2 (delta 1), reused 0 (delta 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/yhluprog/pythonexamples.git
      1ed761d..3357bae  master -> master

It is important to know that the deleted file does not disappear. It is
still stored in the history of the repository. In github, clicking the
commit history shows all the changes over time, as shown in
:numref:`figure-github11`.

.. _figure-github11:

.. figure:: vc/figures/github11.png
   :alt: The commit history.

   The commit history.

It is also possible using the git log command to see the history in the
reverse chronological order (the most recent first):

::

   $  git log
   commit 3357baed98088aacc452a1135ff16739fe64cab6
   Author: XXXX
   Date:   YYYY

       remove the file

   commit 1ed761dbd9a70c6b38a7d788dd3afc19d33f3b9a
   Author: XXXX
   Date:   YYYY

       add a new file to print hello

   commit 26317f089e64f8fd10b7d4a5dc96fad1bdccab7f
   Author: XXXX
   Date:   YYYY

       add a line

   commit 883333a9c3177b5e3d826addb15b8ebf4caf7b8c
   Author: XXXX
   Date:   YYYY

       Initial commit

Collaboration using github
--------------------------

Does does “hub” in github mean? Think of it as an airline hub or a bus
hub, where travellers come from many different places in order to change
flights or bus lines. Similarly, github allows collaborators to share
and exchange. Adding collaborators would be easy, by clicking Settings
and Collaborators, as shown in :numref:`figure-github9`.

.. _figure-github9:

.. figure:: vc/figures/github9.png
   :alt: Add collaborators to a repository.

   Add collaborators to a repository.

Two people may share and modify the same repository in github in the way
depicted in :numref:`figure-githubcollaborate`. In this figure,
the numbers in black ovals indicate steps within individual’s local
repository. The numbers in white ovals indicate steps involving the
remote repository. :numref:`figure-githubcollaborate` shows two
people start from the same remote repository. This is not necessary. It
is possible to clone the remote repository after many modifications have
already been made by another person.

.. _figure-githubcollaborate:

.. figure:: vc/figures/githubcollaborate.png
   :alt: Workflow of two people upading the same repository in github.

   Workflow of two people upading the same repository in github.

Each person starts by cloning the same repository in github. After
cloning, each person can work independently without interfering with
each other. Each person can also commit multiple times creating multiple
versions on their local repositories. When one decides it is time to
share a version with the other person, this version is pushed to the
shared repository in github. Before anything is pushed, the local
repository should be updated by using the git pull command to ensure any
changes by the other person is reflected. Otherwise, the changes by the
other person may be erased by the new push. Even though the erased
changes can be recovered, pushing without pulling first creates
unnecessary trouble and is impolite.

This following is an example of running the git pull command while
writing this book. It says two files, README.md and python.tex, have
been modified by a collaborator (maybe several collaborators).

::

   $ git pull
   remote: Enumerating objects: 16, done.
   remote: Counting objects: 100% (16/16), done.
   remote: Compressing objects: 100% (11/11), done.
   remote: Total 16 (delta 7), reused 14 (delta 5), pack-reused 0
   Unpacking objects: 100% (16/16), done.
   From https://github.com/PurdueCAM2Project/SE4ML
      7e25147..5051695  master     -> origin/master
    * [new tag]         v0.6       -> v0.6
    * [new tag]         v0.7       -> v0.7
    * [new tag]         v0.6.1     -> v0.6.1
   Updating 7e25147..5051695
   Fast-forward
    README.md                  |   8 ++--
    software/python/python.tex | 221 ++++++-----------
    2 files changed, 101 insertions(+), 128 deletions(-)

Now is a good time explaining the advantage of distributed version
control systems like git. :numref:`figure-githubcollaborate`
shows three repositories: one remote and shared in github and two local
repositories by two different people. These two people can change the
files on their local repositories without affecting the other person. In
fact, they can commit many times creating multiple versions before
pushing any changes and make the changes visible to the other person. An
obvious question is when one should commit and when one should push.

The answer to the first question (when to commit) is simple: commit
anytime as one wishes. Since commit does not affect the shared
repository, it is acceptable committing changes that are incomplete or
even contain errors (i.e., “bugs”). Committing creates a new version
with a message; this new version is searchable by the message. When one
decides the changes are “good enough” to stay for now, it is time to
commit and create a new version. One may experiment different methods
implementing a feature with different versions. Each method can be a new
version or even several versions. As long as the versions are not
pushed, the experiments do not cause any problem to the other people
sharing the same github repository. Version control cannot help if one
does not commit. Thus, a good rule is “when in doubt, commit”.

[page:whengitpush] The answer to the second question (when to push) is a
little more complex because the pushed changes are visible by the other
people. The general rule about pushing is “Do you want the other people
to see your changes?” If the answer is yes, then push the changes. If
the answer is no, then do not push yet. Now, the question becomes “When
would you like people to see the changes?” Usually, the pushed changes
should be functional and fully debugged. Incomplete or buggy changes
should not be pushed (unless they are needed by some other people to
complete or to debug). Sometimes, several people working on related
things and the push by each individual is incomplete. Instead, they need
to coordinate their pushes so that their work can be integrated. Page 
will talk about branches as a way to push changes without directly
affecting the other people.

In most cases, no problem occurs when two or more people modify the same
remote repository. If one person modifies a file and another person
modifies a different file, git simply takes the changes by both people
in the latest versions (typically called “merge” the changes). Even if
two people modify the same file, git may still be able to add the
changes from both people. In rare cases, however, conflicts may occur
when two people modify the same file and the changes are too similar for
git to determine what to do. Conflicts appear in the the following
markers.

::

   <<<<<<< 
   content from one version
   =======
   content from the other version
   >>>>>>> 

Conventionally, the person that wants to push later is responsible
discovering and resolving conflicts by doing git pull before git push.
To resolve conflicts, the person that discovers conflicts should examine
the differences and determines which to keep and which to discard.

A few general rules can reduce the chances of conflicts: First,
communicate and coordinate with collaborators often. Second, do git pull
and git push often so that conflicts can be discovered earlier when only
a few lines of conflicts exist. In order to do git push often, it is
imperative to focus on one specific problem (e.g., adding one feature,
or fixing one bug) at any moment, finish the work, and then push it.

A common mistake among beginning git users is to do several things
simultaneously and take too long to finish any of them. During the time,
these users cannot do git push because the incomplete work would break
others’ changes. When they do git push finally, many things have changed
in the repositories by other users and conflicts likely occur. Resolving
these conflicts takes a lot of efforts. The situation can easily become
worse and worse: When these beginners discover that git push creates
conflicts, they hesitate to do git push. Consequently, they do git push
less and less often and wherever they do, more and more conflicts occur.
Eventually, they are so afraid that they stop doing git push completely.
They no longer contribute and will soon be released from the projects.

.. _section:git:branches:

Branches
--------

So far all changes occur on the master branch. This is evident because
the output of every git commit command shows “master”. There is only one
branch, the master branch. Modifying the master branch direclty is
actually not recommended. Instead, the master branch should be reserved
for the stable versions (also called the release versions).

Page  said one should not push buggy code. This is restricted to the
master branch. If multiple branches are used, it is acceptable pushing
buggy code to some branches for collaborators to inspect. This section
uses integer partition as an example showing how branches may be used.
Integer partition means breaking a positive integer into the sum of
several positive integers. Usually, the original number itself is also
an acceptable partition.

More details about integer partition can be found in Chapter 14 of “Intermediate C
Programming”

Section 9.3 of “Discrete and Combinatorial Mathematics” 
This is the subject for an entire
book

Below are some example integer partitions:

::


   1 = 1    2 = 1 + 1    3 = 1 + 1 + 1      4 = 1 + 1 + 1 + 1
              = 2          = 1 + 2            = 1 + 1 + 2
                           = 2 + 1            = 1 + 2 + 1
                           = 3                = 1 + 3
                                              = 2 + 1 + 1
                                              = 2 + 2
                                              = 3 + 1
                                              = 4

Imagine that one wishes to write a program that receives a positive
integer and prints all partitions. The git branch command shows the
current branch. Since no new branch has been created yet, it shows the
master branch

::

   $ git branch
   * master

If a name is given after git branch, a new branch is created. The
following command creates a new branch called partition.

::

   $ git branch partition

To change to the newly created branch, use the git checkout command:

::

   $ git checkout partition
   Switched to branch 'partition'

The git branch command shows two branches and the current working branch
is called partition.

::

   $ git branch
     master
   * partition

This is the first version of the program:

.. code:: python

   #!/usr/bin/python3
   # partition.py

   import sys

   def printArray(arr, ind):
     for i in range(0, ind - 1):
       print (str(arr[i]) + ' + ', end='')
     print (str(arr[ind - 1]))

   def partitionHelp(arr, ind, left):
     if (left == 0):
       printArray(arr, ind)
     for i in range(1, left + 1):
       arr[ind] = i
       partitionHelp(arr, ind + 1, left - i)

   def partition(val):
     print('== Partition ' + str(val) + ' ==')
     arr = [0] * val
     partitionHelp(arr, 0, val)
     
   if __name__== "__main__":
     if (len(sys.argv) < 2):
       sys.exit('Need a positive integer')
     val = int(sys.argv[1])
     if (val <= 0):
       sys.exit('Need a positive integer')
     partition(val)

This file is called partition.py but the name is not restricted by the
branch’s name. This file can be added to the local repository using the
git add and git commit commands:

::

   $ git add partition.py 
   $ git commit -m "add the program for integer partition" partition.py 
   [partition 810a670] add the program for integer partition
    1 file changed, 29 insertions(+)
    create mode 100755 partition.py

Even though the partition branch has already been created earlier, it is
known only locally and it does not exist in the remote repository. Thus,
the git push command has to specify the new name of the branch by adding
origin. The command is

::

   $  git push origin partition
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   Counting objects: 3, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 584 bytes | 0 bytes/s, done.
   Total 3 (delta 1), reused 0 (delta 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   remote: 
   remote: Create a pull request for 'partition' on GitHub by visiting:
   remote:      https://github.com/yhluprog/pythonexamples/pull/new/partition
   remote: 
   To https://github.com/yhluprog/pythonexamples.git
    * [new branch]      partition -> partition

On github website, the new branch can be seen:

.. _figure-github12:

.. figure:: vc/figures/github12.png
   :alt: A new branch has been added to github.

   A new branch has been added to github.

The file partition.py is available only in the partition branch, not in
the master branch, as shown in :numref:`figure-github134`.

.. _figure-github134:
.. _figure-github13:

.. figure:: vc/figures/github13.png
   :alt: The file partition.py is in the partition branch.

   The file partition.py is in the partition branch. Also, github says, "This branch is 1 commit ahead of master."


.. figure:: vc/figures/github14.png
   :alt: The file partition.py is not in the master branch.

   The file partition.py is not in the master branch.

The Python file is called partition.py; the local and the remote
branches are called partition. There is no reason why they must have the
same name. The following steps show how to rename the file. by using the
git mv command (mv means move). Of course, this has to be followed by
the git commit and the git push commands.

::

   $ git mv partition.py intpart.py
   $ git commit -m "rename the file" intpart.py 
   $ git commit -m "deleted" partition.py
   [partition 872d9c3] rename the file
    1 file changed, 30 insertions(+)
    create mode 100755 intpart.py
   $ git push origin partition
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   Counting objects: 3, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 574 bytes | 0 bytes/s, done.
   Total 3 (delta 1), reused 0 (delta 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/yhluprog/pythonexamples.git
      810a670..872d9c3  partition -> partition
   [partition 4b61bbf] deleted
    1 file changed, 29 deletions(-)
    delete mode 100755 partition.py

It is possible to have different names for the local and the remote
branches but there is no obvious advantages and can cause unnecessary
confusion. Thus, they will be kept the same.

A branch can also have multiple commits and pushes. The intpart.py
program uses both odd numbers and even numbers. It will give users the
options to use only odd numbers or only even numbers by specifying -o or
-e flag. Obviously, if -e is used, only even numbers can be partitioned.
The new program is listed below:

.. code:: python

   #!/usr/bin/python3
   # intpart.py

   import sys
   import argparse

   def printArray(arr, ind):
     for i in range(0, ind - 1):
       print (str(arr[i]) + ' + ', end='')
     print (str(arr[ind - 1]))

   def partitionHelp(arr, ind, left, odd, even):
     if (left == 0):
       printArray(arr, ind)
     '''
     There are four conditions when this i is used
     1. not odd and not even: 
     2. odd and i is odd
     3. even and i is even
     '''
     for i in range(1, left + 1):
       if ((not odd) and (not even)):
         arr[ind] = i 
       elif (odd and (i % 2)):
         arr[ind] = i
       elif (even and ((i % 2) == 0)):
         arr[ind] = i
       else:
         continue # do not use this value of i
       partitionHelp(arr, ind + 1, left - i, odd, even)

   def partition(args):
     # print (args)
     odd = args.odd
     even = args.even
     val = args.value
     if (odd and even):
       sys.exit('-e and -o cannot be both set')
     if (even and (val % 2)):
       sys.exit('-e cannot partition an odd number')
     print('== Partition ' + str(val) + ' ==')
     if (odd):
       print('== Using only odd numbers ==')
     if (even):
       print('== Using only even numbers ==')
     arr = [0] * val
     partitionHelp(arr, 0, val, odd, even)

   def checkArgs(args = None):
     parser = argparse.ArgumentParser(description='parse arguments')
     parser.add_argument('-o', '--odd', action='store_true',
                         help = 'odd numbers only', default = False)
     parser.add_argument('-e', '--even',action='store_true',
                         help = 'even numbers only', default = False)
     parser.add_argument('value', type = int,
                         help = 'number to parition')
     pargs = parser.parse_args(args)
     return pargs
     
   if __name__== "__main__":
     args = checkArgs(sys.argv[1:])
     partition(args)

When partitioning 4, is 1 + 1 + 2 considered the same as 1 + 2 + 1, as
well as 2 + 1 + 1? The program intpart.py treats them as different
partitions. The next change is to have the option whether orders matter.
If the order does not matter (i.e., 1 + 1 + 2, 1 + 2 + 1, and 2 + 1 + 1
are considered as equivalent or duplicates), one simple way to eliminate
duplicates is by restricting the latter numbers must not be smaller than
earlier numbers. This eliminates 1 + 2 + 1 and 2 + 1 + 1 because they do
not meet the requirement. The new program is listed below:

.. code:: python

   #!/usr/bin/python3
   # intpart.py

   import sys
   import argparse

   def printArray(arr, ind):
     for i in range(0, ind - 1):
       print (str(arr[i]) + ' + ', end='')
     print (str(arr[ind - 1]))

   def partitionHelp(arr, ind, left, odd, even, order):
     if (left == 0):
       printArray(arr, ind)
     '''
     There are four conditions when this i is used
     1. not odd and not even: 
     2. odd and i is odd
     3. even and i is even
     '''
     for i in range(1, left + 1):
       if (order and (ind != 0) and (arr[ind - 1] > i)):
         # orders do not matter
         # the numbers must not be decreasing
         continue
       if ((not odd) and (not even)):
         arr[ind] = i 
       elif (odd and (i % 2)):
         arr[ind] = i
       elif (even and ((i % 2) == 0)):
         arr[ind] = i
       else:
         continue # do not use this value of i
       partitionHelp(arr, ind + 1, left - i, odd, even, order)

   def partition(args):
     # print (args)
     odd = args.odd
     even = args.even
     order = args.order
     val = args.value
     if (odd and even):
       sys.exit('-e and -o cannot be both set')
     if (even and (val % 2)):
       sys.exit('-e cannot partition an odd number')
     print('== Partition ' + str(val) + ' ==')
     if (odd):
       print('== Using only odd numbers ==')
     if (even):
       print('== Using only even numbers ==')
     arr = [0] * val
     partitionHelp(arr, 0, val, odd, even, order)

   def checkArgs(args = None):
     parser = argparse.ArgumentParser(description='parse arguments')
     parser.add_argument('-o', '--odd', action='store_true',
                         help = 'odd numbers only', default = False)
     parser.add_argument('-e', '--even',action='store_true',
                         help = 'even numbers only', default = False)
     parser.add_argument('-r', '--order',action='store_true',
                         help = 'orders do not matter', default = False)
     parser.add_argument('value', type = int,
                         help = 'number to parition')
     pargs = parser.parse_args(args)
     return pargs
     
   if __name__== "__main__":
     args = checkArgs(sys.argv[1:])
     partition(args)

Now the program is ready to be moved to the stable master branch. This
will be done in three steps: (1) go to the master branch using the git
checkout command; (2) merge the partition branch to the master branch
using the git merge command; (3) delete the partition branch using the
git branch -d command. The git branch command is used to check which
branch is used right now and whether any other branch exists. At can be
seen, the last git branch shows only the master branch. The last command
deletes the branch at github.

::

   $ git checkout master
   Switched to branch 'master'
   Your branch is up-to-date with 'origin/master'.
   $ git branch
   * master
     partition
   $ git merge partition
   Updating 3357bae..d9ee8e1
   Fast-forward
    intpart.py | 70 +++++++++++++++++++++++++++
    1 file changed, 70 insertions(+)
    create mode 100755 intpart.py
   $ git branch -d partition
   Deleted branch partition (was d9ee8e1).
   $ git branch
   * master
   $ git push
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   Total 0 (delta 0), reused 0 (delta 0)
   To https://github.com/yhluprog/pythonexamples.git
      3357bae..d9ee8e1  master -> master
   $ git push origin --delete partition
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   To https://github.com/yhluprog/pythonexamples.git
    - [deleted]         partition

A common mistake among beginning git users is that they do not merge
branches. They keep changing their own branches. They want to show to
their collaborators that they are contributing by frequently pushing
improvements to the repositories. However, if the improvements stay in
the branches that are not merged, these improvements are not actually
useful. Most branches should have short lives: Each branch is created
for one specific purpose. It is documented, developed, tested,
committed, merged, and then deleted.

Pull Requests
-------------

Creating a branch does not inform collaborators. This is reasonable
because a branch may have many versions that are not ready to be shared.
When a version is ready, collaborators may be informed by using a pull
request. A pull request should be initiated from a branch other than the
master branch because the master should be the stable branch. A pull
request may serve one or more purposes, including (1) The version in the
branch is ready to be inspected by one or more collaborators before
being merged to the master branch. (2) The version needs to be
integrated with the work by collaborators. (3) The version has some
problems and the person that creates this version does not know how to
solve the problems. This person asks collaborators to help.

Suppose one wants to add another option that excludes the number itself
in integer partition. For example, to partition 5, valid options include
4 + 1, 2 + 3, and 2 + 1 + 2; however, 5 itself is not accepted. This
person creates a new branch called partition_not_self. The following
command, with -b, can simultaneously create a branch and switch to the
branch.

::

   $ git checkout -b partition_not_self
   Switched to a new branch 'partition_not_self'
   $ git branch
     master
   * partition_not_self

The following code is an attempt for this option. However, when -s is
added, no partition is printed at all.

.. code:: python

   #!/usr/bin/python3
   # intpart.py

   import sys
   import argparse

   def printArray(arr, ind):
     for i in range(0, ind - 1):
       print (str(arr[i]) + ' + ', end='')
     print (str(arr[ind - 1]))

   def partitionHelp(arr, ind, left, odd, even, order, notself):
     if (left == 0):
       printArray(arr, ind)
     '''
     There are four conditions when this i is used
     1. not odd and not even: 
     2. odd and i is odd
     3. even and i is even
     '''
     maxi = left + 1
     if (notself):
       maxi = left
     for i in range(1, maxi):
       if (order and (ind != 0) and (arr[ind - 1] > i)):
         # orders do not matter
         # the numbers must not be decreasing
         continue
       if ((not odd) and (not even)):
         arr[ind] = i 
       elif (odd and (i % 2)):
         arr[ind] = i
       elif (even and ((i % 2) == 0)):
         arr[ind] = i
       else:
         continue # do not use this value of i
       partitionHelp(arr, ind + 1, left - i, odd, even, order, notself)

   def partition(args):
     # print (args)
     odd = args.odd
     even = args.even
     order = args.order
     val = args.value
     notself = args.notself
     if (odd and even):
       sys.exit('-e and -o cannot be both set')
     if (even and (val % 2)):
       sys.exit('-e cannot partition an odd number')
     print('== Partition ' + str(val) + ' ==')
     if (odd):
       print('== Using only odd numbers ==')
     if (even):
       print('== Using only even numbers ==')
     arr = [0] * val
     partitionHelp(arr, 0, val, odd, even, order, notself)

   def checkArgs(args = None):
     parser = argparse.ArgumentParser(description='parse arguments')
     parser.add_argument('-o', '--odd', action='store_true',
                         help = 'odd numbers only', default = False)
     parser.add_argument('-e', '--even',action='store_true',
                         help = 'even numbers only', default = False)
     parser.add_argument('-r', '--order',action='store_true',
                         help = 'orders do not matter', default = False)
     parser.add_argument('-s', '--notself',action='store_true',
                         help = 'not to include itself', default = False)
     parser.add_argument('-v', '--value', type=int,
                         help = 'number to parition')
     pargs = parser.parse_args(args)
     return pargs
     
   if __name__== "__main__":
     args = checkArgs(sys.argv[1:])
     partition(args)

The person writing this program wants to get help from a collaborator by
creating a pull request. :numref:`figure-github15` and :numref:`figure-github18`
show how to create a pull request on github and assign it to a
collaborator.

.. _figure-github15:

.. figure:: vc/figures/github15.png
   :alt: Create pull request on the github website.

   Create pull request on the github website.

.. _figure-github18:

.. figure:: vc/figures/github18.png
   :alt: Assign it to a specific collaborator.

   Assign it to a specific collaborator.

A pull request can automatically mark the line-by-line changes as shown
in :numref:`figure-github16` and :numref:`figure-github17`.

.. _figure-github16:

.. figure:: vc/figures/github16.png
   :alt: The pull request can show the line-by-line differences.

   The pull request can show the line-by-line differences.

.. _figure-github17:

.. figure:: vc/figures/github17.png
   :alt: The pull request can show the line-by-line differences.

   The pull request can show the line-by-line differences.

The pull request can also include comments in addition to the commit
message.

.. _figure-github19:

.. figure:: vc/figures/github19.png
   :alt: The pull request allows comments.

   The pull request allows comments.

:numref:`figure-github2` shows an example of a response of the
pull request. Usually, responses are in the form of suggestions to
improve code or questions for clarification.

.. _figure-github20:

.. figure:: vc/figures/github20.png
   :alt: Response of a pull request.

   Response of a pull request.

Issues
------

Pull requests are restricted to the users that have write permissions.
Issues can be raised by people that have no write permissions.
:numref:`figure-githubissue` shows an example of an issue of a
possible error in this book.

.. _figure-githubissue:

.. figure:: vc/figures/githubissue2.png
   :alt: Issue is another way to communicate.

   Issue is another way to communicate. 

Release this Book
-----------------

This book is continuously released: every time a new version is ready,
it is released.

::

   $ git tag v0.5
   $ git push --tags
   Username for 'https://github.com': yhluprog
   Password for 'https://yhluprog@github.com': 
   Total 0 (delta 0), reused 0 (delta 0)
   To https://github.com/PurdueCAM2Project/SE4ML.git
    * [new tag]         0.5 -> 0.5

Set Up SSH Key
--------------

Using SSH keys is helpful to avoid entering username and password when pushing local changes to a remote repository.

Ensure you have ssh-keygen on your system:

::

   $ which ssh-keygen
   /usr/bin/ssh-keygen

We do not cover installation of basic Unix tools here; however, this tool is provided on all modern Unix systems, including OS X and Windows (using Windows Subsystem for Linux).


Generate your private/public key pair.
In this example, we use the RSA algorithm with 2048-bit keys. 

::

   $ ssh-keygen -t rsa -b 2048
   Generating public/private rsa key pair.
   Enter file in which to save the key (/home/thiruvathukal/.ssh/id_rsa): gkthiruvathukal
   Enter passphrase (empty for no passphrase): 
   Enter same passphrase again: 
   Your identification has been saved in gkthiruvathukal.
   Your public key has been saved in gkthiruvathukal.pub.
   The key fingerprint is:
   SHA256:8KETYZ4cAtMCDNMXP8IadYv6DjzuNpN0f67W7oCRtKM thiruvathukal@penguin
   The key's randomart image is:
   +---[RSA 2048]----+
   |*ooo+.=          |
   | oo+oO =         |
   |  .o= X .        |
   |   = + * .       |
   |  o = o S        |
   | ..o.+ .         |
   | .Eoo...         |
   | .=+  o.o        |
   | ooo...*+        |
   +----[SHA256]-----+


Display the public key. This is what you need to upload to GitHub.

::

   $ cat gkthiruvathukal.pub
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXiY/Bn1ZrwVqy6W6g8dPL1QQ5QnRojF4UmhbRihER7nefoSS9c6kwoD7cnD8fM2UINiRYI56j7vek1qqH09SstmnuKQLNf6tJqYgcRUguSQRqhS+yjJ2HLkm/GCXXrja/SFTHjspLwgZRsQFWK8yZXNSPZZnxUOXI3UBc4z2nTQ+MclhU0VzcbJhH9LeqyvKNtiTRjhVXF8wXJzWRQ8wVPKvd2Jl8fYqfoExRAAHDBEmxQyTraawA8J5cNS24EWAoKIR4rT9H7u1UKGjyoII53U137IsPG5SCZ9rNG/XAzF7GC18S+MbBwJ9W5LjaaGEqy0UOq2FtF3UMGdFtxSCV thiruvathukal@penguin

.. note:: The keys used here (public and private) were only used for testing and have already been deleted.

.. figure:: vc/figures/githubprofile.png
   :alt: Github profile settings

   Select settings in github settings

	  
Upload key to GitHub.

.. figure:: vc/figures/ssh-key-add-key.png
   :alt: Copy/paste public key in GitHub SSH Config

   Copy/paste public key in GitHub SSH Config

Successful upload of key

.. figure:: vc/figures/ssh-key-success.png
   :alt: Successful upload shows fingerprint

   Successful upload shows fingerprint


Add Host entry in `~/.ssh/config`:

::

   Host gkthiruvathukal-github
      HostName github.com
      IdentityFile ~/.ssh/gkthiruvathukal



Now try cloning a repository with a git-style location and the newly created Host entry:

::

   $ git clone git@gkthiruvathukal-github:PurdueCAM2Project/SE4ML
   Cloning into 'SE4ML'...
   remote: Enumerating objects: 75, done.
   remote: Counting objects: 100% (75/75), done.
   remote: Compressing objects: 100% (38/38), done.
   remote: Total 1772 (delta 47), reused 61 (delta 35), pack-reused 1697
   Receiving objects: 100% (1772/1772), 10.82 MiB | 5.45 MiB/s, done.
   Resolving deltas: 100% (898/898), done.


As you can see, adding an entry to `~/.ssh/config` creates a pseudo-hostname that can be used as the hostname in a git-style URL.

While it is not strictly required to create a Host entry in `~/.ssh/config`, you may find it convenient to have separate entries if you have multiple git identities (i.e. different GitHub accounts for different projects). Given that we as co-authors have multiple identities on git, we have written these instructions to be as general as possible.

If you have already generated a default identity such as `id_dsa` or `id_rsa`, just upload the file `id_dsa.pub` or `id_rsa.pub` to GitHub. and use `git@github.com` in the git location string.


