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


How To Start Code Review
------------------------
#. Make sure your local changes have been pushed to your working branch/fork by running `git push origin
#. Using a projects respective version control tool (e.g., Git), make a pull request to merge your changes into the parent version. 

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