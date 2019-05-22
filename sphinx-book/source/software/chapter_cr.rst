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

Ensure Code Is Complete
~~~~~~~~~~~~~~~~~~~~~~~
Do not commit work
that is half-finished, causing code to no longer compile and 
unit tests to break.

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