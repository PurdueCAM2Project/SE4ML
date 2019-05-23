Code Review
===========

.. warning::
   This chapter is in draft status.

Code review is a software quality assurance activity in which one or more people evaluate a program against some list of standards.
The program must be carefully inspected, line-by-line in order to ensure all defects are removed from the program.
Without a standard, code reviewers will miss defects due to improper code review techniques.
This chapter will cover how to perform a proper code review from start to finish.

Modern Code Review
------------------
In the past, the author of a change in code would sit down with reviewers to go through the code and find defects.
However, in recent years, code reviewers employ tools to make the process asynchronous, which means the reviewer can review the code at any time.
This approach is known as *modern code review*.

Both open-source and industry software projects utilize modern code review for reviewing code changes [Sadowski-Soderberg-Bacchelli]_—and for good reasons, as the benefits for reviewing code are abundant.
While code reviews require a large time investment, impressive returns have been shown from a multitude of companies.
For instance, code review at Hewlett-Packard was found to reduce the time for an application to get to market by 1.8 months [Grady-Van-Slack]_. However, the returns do not stop at simple gains in time efficiency.
Researchers at Microsoft have found that code review acts as a transfer of knowledge between the code reviewer and reviewee
Will use [Bacchelli-Bird]_

How To Start A Code Review
--------------------------

General Steps To Start A Code Review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#.  Make sure your local changes have been pushed to your working branch/fork.
    You can accomplish this by running:
    ::

        $ git push origin HEAD

#.  Using a project's respective version control 
    service (e.g. GitHub, BitBucket), create a
    pull request to merge your changes into the parent
    version. Provide a title for what the feature adds 
    and a longer desription with a change
    log. :numref:`pullrequest` and :numref:`pullrequestform`
    demonstrate an example pull request in GitHub.

    .. _pullrequest:
    .. figure:: cr/figures/pullrequest.png
       
       Press "Compare & Pull Request" to review your changes
       and submit a pull request.


    .. _pullrequestform:
    .. figure:: cr/figures/pullrequestform.png
       
       Pull requests should have a title summarizing the 
       new feature and a comment giving a more descriptive
       explaination of the changes the pull request will make.


#.  Request for another developer of the project to review
    your changes. Ideally, they should be an expert of the
    methods used to create the changes.

#.  Wait for (or bug) the assigned code reviewer to look over
    your changes. They may ask for you to clarify your methods
    or ask for you to make additional changes, so make sure you
    regularly check the pull request until it is rejected or
    accepted.

Making Nano-Commits
~~~~~~~~~~~~~~~~~~~

A *nano-commit* is the act of committing code in small, homogenous 
portions. In other words, the code is meant to complete a sub-task
of the overarching feature being implemented. During the development
process, making nano-commits can you help keep track of the work-flow.
For instance, if a bug is found, then you can sift through the small 
changes until the bug either disappears or changes. This will help you
make the necessary changes at the root, keeping the fix clean.

Some tasks you may consider keeping as separate commits are:

-   Refracting code before making changes to its logic;
-   Adding or modifying documentation;
-   Fixing a bug or creating a small feature;
-   Or changing configuration settings.

Keep in mind that you, as the developer, are responsible for
making code as smooth to review as possible. Nano-commits can
aid the code reviewer to follow your work-flow easily. Furthermore, 
while smaller commit sizes greatly reduce the likelihood of
creating bugs [Purushothaman-Perry]_, they still pose a risk
and should be reviewed for correctness.

Ensuring Your Code Is Complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before committing your code, it is wise to do a *personal code review* 
to locate as many issues as you can before passing it along to another 
person. In doing so, you will avoid potentially wasting time on several
more iterations of code review than necessary [Humphrey]_. While you
perform the personal code review, you should keep a checklist of
common mistakes to look for. By utilizing a checklist, you will 
ensure both efficiency and consistency from your personal code reviews.

Furthermore, it is important to be curteous of your code reviewer's 
time.  Your code should be ready for customers and void of any obvious
bugs. Ideally, the code reviewer should only have to make comments
regarding the implementation and not about major issues that need fixed. 
A study from Microsoft found that only around 15% of comments 
during code review address bugs [Czerwonka-Greiler-Tilford]_, which
indicates a greater emphasis on other areas, such as code styling or
long-term maintainability. It is also important to keep the responsibilities
of the code review in mind: it is not their job to fix your bugs; their
purpose is to notice and bring small, easy-to-miss issues to your attention
for you to go back and fix. If you submit incomplete code with known
issues, then you waste both your and your code reviewer's time. In
order to collaborate as a team and achieve results, it is important to
remain considerate of your collaborators efforts [Dreu-Weingart]_.

A change that causes external features to fail is a less obvious 
sign of incomplete code. With an extensive system of unit tests, 
these issues are more obvious by validating that a change does not 
damage older features. With this in mind, it is vital to implement 
unit tests alongside new features. Implementation of unit tests 
guarentees protection from hidden bugs. In a similar vein, failure 
to compile is another sign of a project containing incomplete code.
The error output of the compiler will normally indicate where the
issue is located, so it is vital to read and understand what it says.
It is crucial to verify that none of the unit tests fail and the
build successfully compiles *before* submitting the change for
a code review.

What to Review
--------------

Code Formatting and Styling
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comment Formatting and Styling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Code Logic
~~~~~~~~~~

Best Practice
~~~~~~~~~~~~~

Test Cases
~~~~~~~~~~

Things to Take into Consideration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. [Sadowski-Soderberg-Bacchelli] Modern Code Review: A Case Study at Google, https://sback.it/publications/icse2018seip.pdf
.. [Grady-Van-Slack] Key lessons in achieving widespread inspection use, https://ieeexplore.ieee.org/document/300084
.. [Bacchelli-Bird] Expectations, outcomes, and challenges of modern code review, https://dl.acm.org/citation.cfm?id=2486882
.. [Purushothaman-Perry] Toward Understanding the Rhetoricof Small Source Code Changes, https://ieeexplore.ieee.org/abstract/document/1463233
.. [Czerwonka-Greiler-Tilford] Code reviews do not find bugs: how the current code review best practice slows us down, https://dl.acm.org/citation.cfm?id=2819015
.. [Humphrey] The Personal Software Process, https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=5283
.. [Dreu-Weingart] Task Versus Relationship Conflict, Team Performance,and Team Member Satisfaction: A Meta-Analysis, https://psycnet.apa.org/record/2003-99635-017
