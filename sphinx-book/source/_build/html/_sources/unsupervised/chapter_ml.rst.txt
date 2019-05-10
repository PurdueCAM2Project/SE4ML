Machine Learning
==================

Learning Objectives

- Learn what machine learning is 
  
- Understand the strength and limitations 
  
- Distinguish  unsupervised learning,  supervised learning,  reinforcement learning, and transfer  learning

  
Decision Problems
-----------------

Machine learning means using computer programs to discover patterns
(i.e., *learn*) from data.  How is this different from typical
computer programs?

Bring an Umbrella or Not
^^^^^^^^^^^^^^^^^^^^^^^^

Let us consider a "decision problem": Should you
bring an umbrella or not?  This should be easy, right?  You can decide
based on "*whether it is raining or not*".  This is simple enough.  If
you always follow this rule, you will soon encounter situations when
this rule is not good.  Maybe it is not raining right now but it is
expected to rain soon. Thus, you add one more rule: "*Bring an
umbrella if it is raining or it is expected to rain.*".  If you follow
these rules, you will soon discover that they are still insufficient.
If you are going to walk in covered areas (such as subway stations or
shopping malls), maybe you do not need an umbrella.  Thus, you add
another rule: "*Bring an umbrella if it is raining or it is expected
to rain and you will walk in an uncovered area.*" Things can become
really complicated.  If you are carrying a box and it does not rain
heavily, maybe you do not want to take an umbrella because it is
inconvenient to carry the box and to hold an umbrella at the same
time. As a result, the rules become "*Bring an umbrella if it is
raining or it is expected to rain and you will walk in an uncovered
area. Do not bring an umbrealla if it does not rain heavily and you
are carrying a box.*" The rules become more and more complex.  You may
also want to consider whether it is windy. If it is, you may want to
wear a raincoat instead of bringing an umbrella. If you want to ride a
bike, you may want to choose a rain coat instead of an umbrella.
Maybe it is very hot and you want to walk in rain to cool.  As you can
see, this decision problem has so many different scenarios and writing
all these as ``if-else`` conditions becomes really complex.

Cross a Stree Intersection
^^^^^^^^^^^^^^^^^^^^^^^^^^


If you drive a car, should you cross a street intersection or not?
You may think this is really easy: "*If the traffic light is green,
cross the intersection.*" Sometimes, you cannot enter the inserction
because it is blocked by vehicles already. If you enter the
intersection, you will park at the intersection and worsen traffic
jam. Thus, you add another rule: "*If the traffic light is green and
the intersection is not blocked, cross the intersection.*" If you hear
the siren of an ambulance, you should allow it to pass first.  You add
another condition: "*If the traffic light is green and the
intersection is not blocked and there is no siren, cross the
intersection.*" If there is a jaywalker, you don't want to hit the
person.  You add another rule: "*If the traffic light is green and the
intersection is not blocked and there is no siren and there is no
jaywalker, cross the intersection.*" If there is a construction and a
flagman, you should follow the flagman's instruction, not the traffic
light.  You can keep adding more and more rules to cover many
different scenarios.  This decision problem may consider many factors
and writing down these rules become increasingly complex and
difficult.

Approve a Mortgate Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are a bank manager and evaluate mortgage applications, how do
you decide whether to approve or not?  If you approve the application
and the person pays regularly, your bank makes money from fees and
interests.  If the person fails to pay (called "defaults"), the bank
may lose money. It is possible that the bank does not lose money if
the house's value is sufficient to cover the mortgage (through
foreclosure). Foreclosure can be a lengthy process and most banks want
to avoid it.  How do you decide? Maybe you decide based on the
person's regular income: "* If an applicant's monthly income is more
than twice the mortgage payment, approve the application.*"
If you do this, your bank will likely lose a lot of money because you
need to consider other factors, for example, whether the person
already has a lot of debt. You probably also want to consider whether
this person has a record of failing to pay bills.  If the house is not
in a popular location, you definitely want to avoid the possibility of
foreclosure. If the person has been doing business with the bank for
several years, you might trust this person more than a new customer.
Do you want to consider whether this person already owns one or more
houses?  Should you consider this person's age?  Would the marital
status affect your decision?  You may want to consider the economy as
well. If economy is strong, this applicant is likely to keep the
current job or even get a raise; thus, this applicant is likely to pay
the mortgage. If economy is weak, this applicant may lose the current
job and fails to pay.  If you want to consider many factors, are some
factors are more important than the others? How do you choose the
important factors?  This problem, again, shows that considering many
factors and writing down the rules become increasingly complex and
difficult.

Decisions and Feedback
----------------------

In our everyday life, we make hundreds of decisions: what clothes to
wear, where to go for lunch, what to buy in a store, what birthday
gift to send to a friend, etc.  The previous examples show that
decision problems often need to consider many factors.  The reason we
need to consider many factors is to prevent making wrong decisions.
What are "wrong" decisions? If you bring an umbrella and it does not
rain, is it a wrong decision?  If you do not bring an umbrella and it
rain heavily, it is a wrong decision.  Some wrong decisions have
negligible consequences: bringing an umbrella (if it is small and
light) without using it may not be a big problem.  Some wrong
decisions can have dire consequences: approving a mortgage and it
defaults, the bank loses a lot of money.  The definition of "wrong"
decisions may not be so obvious.  A bank may deny all mortgage
applications that have slight chances of defaults. This may completely
avoid defaults but the bank also loses opportunities making money from
the applications that may, but do not, default.  In this case,
"preventing defaults" and "making money" are two related but different
goals.  After knowing the result of a decision, we may conclude that
it is a right or a wrong decision. This is the "feedback" of the
decision.  With the feedback, we hope to make better decisions in the
future. For example, if the bank approves a mortgage and it defaults,
the bank would probably deny the next application that is "similar" to
the defaulted one.  The problem is how to determine two mortgage
applications are "similar".  For some problems, it is impossible (or
almost impossible) to know whether a wrong decision has been
made. Suppose you are the bank manager and you deny a mortgage
application. You will not know whether this person would be able to
pay mortgage regularly because you have denied the application.


Knowledge in Data
-----------------


The examples described earlier are decision problems: whether to bring
an umbrella, whether to enter a traffic intersection, whether to
approve a mortgage application, etc. Each problem needs to consider
many factors and it is not always clear which factor is more important
than the other. One way to solve these problems is to examine similar
scenarios in the past and their results: if the current mortgage
application is "similar" to one that was approved in the past, was
that approval a right decisoin (i.e., did not default)?  Instead of
writing rules, this new approach uses past data to guide future
decisions.  This is what *machine learning* can be helpful: computer
programs discover (i.e., "learn") patterns from data.  Past data may
help decide which factors are important for making decisions if the
past data and the new decision problem have similar patterns.  Having
similar patterns is an essential assumption in machine learning.
Think about how humans learn: a person observes something and then
when the person sees similar problems, the person uses past knowledge
and experience to infer or derive the solutions for the new problems.
If a person has never seen anything similar, the person would not able
to draw from past knowledge or experience.


Machine learning relies on the assumption that past observations and
new, unseen, situations have similar patterns.  This assumption is
essential to the success of machine learning.  Imagine that you are
the bank manager and have discovered a good way to determine whether
to approve or deny mortgage applications.  If you move to another city
or another country, your method may be wrong more often than you
expect. Maybe the demographics are different. Maybe the cultural norms
are different.  Maybe the real estate markets are different.  This
indicates that your machine learning method has its limitations.  You
may need to add some more data into building your knowledge about the
new problem.

There are different types of learning: *Supervised learning* means
that there is a "teacher" telling a student what is right or
wrong. Imagine that a teacher shows images of flowers and tell
students that these are flowers. The teacher shows another image of an
elephant and says that it is an elephant.  *Unsupervised learning* has
no teacher. Imagine that you want to stock your store on a Friday
evening for sales on Saturday.  There is no correct answer what
products you should put on shelves.  You can analyze the past sales
records, together with factors such as weather and season.  You may
also want to consider whether there is a major sport event on that
Saturday.  This is different from supervised learning because there is
no teacher telling you "Yes, you should stock this item on shelves."
or "No, do not stock that item because few people will buy it this
coming Saturday."  Unsupervised learning is often used to discover
(unknown) properties in data, for example, what people buy on a
Saturday.  The third type of learning is called *reinforcement
learning*.  It considers sequences of actions (such as moves in chess)
and the rewards (such as winning a chess game) of these actions.
Reinforcement learning is different from supervised learning because
most decisions cannot be consider right or wrong. Some decisions such
as checkmate are obviously right decisions but the effects of most
decisions are unkonwn until much later. Instead, the sequence of
decisions leads to a result, either winning or losing. Reinforcement
learning is usually used for developing strategies solving problems
through sequences of actions.  The fourth type of learning is called
*transfer learning*.  The knowledge learned from the sample data is
"transferred" to a new set of test data.  An analogy is that a person
learns English and then uses the knowelege about sentence structures
and tenses to learn French.

Supervised learning may be the most familar form of learning: babies
learn parents' faces when the parents say "Daddy" and "Mommy".
Students learn from teachers in classrooms.  Supervised learning,
however, can be expensive because teachers are needed.  As computer
technologies improve, acquiring data becomes very easy and
inexpensive.  Spending $100, you can buy a video camera and the it can
easily generate thousands of images (more precisely, video frames) per
day. Teachig computer the information in the images requires humans as
teachers because computer programs cannot perfectly analyze images
yet.  Teaching computers by marking what is in the images is called
*labeling* or *annnotating*.  In some cases, labeling can be
crowdsourced.  Labeling one million images by humans would not be
easy. In some other cases, the "teachers" of computers must have
special qualifications; for example, medical images are evaluated by
trained medical doctors.


Unsupervised learning can be applied when a person mimicks the
behaviors of another person.  Imagine that you have a vacation in USA
and hear people saying "hello" when they meet.  Even though nobody
(i.e., there is no teacher) tells you what it means, you start saying
"hello" when you meet people.  This is an example of unsupervised
learning.  Unsupervised learning can also be used to discover patterns
in data, for example, people that buy apples are liekly to buy organes
also.  Web search engines are examples of unsupervised learning.
These engines analyze many websites and rank websites for different
search keywords. There is no "teacher" specifying the correct orders.

Define Learning
---------------

We have talked about "learning" without actually defining it.  What
is learning?
In ``Machine Learning by Tom M. Mitchell``, machine learning is defined
as 


**A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.**


To explain this in a more intuitive way, a computer program can learn
if it can get better by doing something more.  One way to understand
learning is by comparing it with something that cannot learn. Consider
the calculator program on your mobile phone. It does not get better
after you use it.  In contrast, a program that determines whether an
email is spam may get better after you mark some emails as spam.  By
marking spam emails, you play the role of a teacher and this is an
example of supervised learning.

This definition does not speficy what is "experience".  From
computers' viewpoint, the experience often refers to "data".  If more
data is used (assuming the data follows specific patterns), then the
computer program can perform better (such as making more correct
decisions in mortgage applications).  What is machine learning really?
Machine learning is pretty broad (and somewhat vague).  In this book
(and many other books), machine learning refers to "statistical
learning" or "data-driven discovery": finding information from data.
Successful machine learning often requires vast amounts of data to
learn from.  Machine learning discovers patterns in the data and uses
the patterns to predict or infer that unseen data has the same (or
similar) patterns.  For example, a computer program may discover that
a person has a high debt-income ratio is likely to default in a
mortgage.  If a future mortgage applicant has a high debt-income
ratio, the program could suggest denying the application due to the
higher risk.

As explained earlier, machine learning can be used when many factors
need to be considered.  Machine learning has already been used in many
applications, such as improving customer relationships, making
financial decisions, diagnosize illness, identify spam emails,
recognize speeches and objects in images.

Limitations of Machine Learning
-------------------------------

Machine learning is not perfect; machine learning has some
limitations.  First, what can be learned depends on the input data. If
some important pieces of data are missing (for example, there are no
cases of high debt-income ratios), then the computer program cannot
learn.  To think of this in a different way, a person that grows up
inland and has never seen a cargo ship will thus not know existence of
cargo ships.  Second, it is difficult to determine when the data is
sufficient or representative.  The patterns are unknown (otherwise,
there is no need to learn) so it is hard to tell when there is enough
data to discover the patterns.  Third, the data may be "biased" and it
is not easy to define success. Imagine that you are designing a
machine learning program to diagnose a rare illness.  If a person has
this illness, the program says "Yes"; otherwise, the program says,
"No".  Suppose the probability of this illness is one out of 100,000
people.  The program would be 99.999\% accurate if it always says
"No".  However, this high accuracy does not really help.
Fourth, each machine learning program reflects a specific machine model
that is designed to recognize the patterns in the data.  Different
models have different capabilities: some models can recognize complex
patterns and some others cannot.

Black Swan Events
-----------------

If an event has never happened, people may think it will never happen.
A "black swan event" (``The Black Swan by Nassim Nicholas Taleb``) is
something that has never been seen before and thus considered
impossible.  People used to believe that swans must be
white. Apparently, it is not possible to learn by looking at white
swans and infer the existence of a black swan.  Black swan events are
actually everywhere, if you pay close attention.  Before 1969/07/20,
nobody could expect that a man would be able to walk on the
moon. Before April 2010, nobody would expect a volcano eruption could
cause worldwide disruption of air travel.  Before the first iPhone was
announced, there was no iPhone. Before Michael Phelps won 28 Olympic
medals, nobody had won 28 Olympic medals.


If something has been observed, it is definitely possible.  After a
black swan has been seen, people know that swans can be black.  If
something has not been observed, it is difficult to say whether it is
impossible or not. Maybe it can be observed later.

Even though black swan events cannot be inferred from known patterns,
it is possible to predict the occurrence by some people that are
willing to challenge these patterns and consider possibilities that
have no been observed (i.e., learned). This is where "imagination" and
"creativity" come in.  Even though machine learning can be very
helpful, the current form of machine learning (statistical learning)
does not have imagination or creativity.
