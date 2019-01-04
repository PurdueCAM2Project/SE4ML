[![Build Status](https://travis-ci.com/PurdueCAM2Project/SE4ML.svg?branch=master)](https://travis-ci.com/PurdueCAM2Project/SE4ML) [![DOI](https://zenodo.org/badge/130437979.svg)](https://zenodo.org/badge/latestdoi/130437979)


# Downloading

We are working to set up a nicer web page (for students and other users).

In the meantime, you can download the latest prerelease by visiting [Releases](https://github.com/PurdueCAM2Project/SE4ML/releases).

Profs. Lu and Thiruvathukal do point releases as new material appears. We are not even close to 1.0 yet, but hope to do a major release sometime this semester.

# Synopsis

This is a work in progress by Profs. Yung-Hsiang Lu (Purdue) and George K. Thiruvathukal (Loyola University Chicago).
We'll be discussing methods for software development/engineering and machine learning.


# Notes on Deployment Process

We were interested to figure out how to use Travis to build LaTeX books hosted on GitHub. Note that we are well aware of collaborative LaTeX tools (e.g. Overleaf and Authorea). However, these tools don't support the distributed workflows of Git. Because we ultimately hope to take advantage of pull requests, we need a GitHub (or equivalent) system to manage changes to this book.

GitHub provides support for [Releases](https://help.github.com/articles/creating-releases/), which is a replacement for downloads. You can create releases based on a `git tag`. Combined with a _continuous integration_ system like [Travis](https://travis-ci.org), you can ensure your LaTeX book _builds successfully_ and, if tagged, _deploys_ to GitHub Releases for your repository.

You can see the latest details in my `.travis.yml` file. But here is walkthrough.

- Use the _newer_ style containers at Travis.

  ```
  sudo: false
  language: python
  ```

- Declare the needed LaTeX packages. Keep in mind that although you can use `texlive-full`, you'll come to regret it quickly. Choosing the full install takes almost 10-15 minutes in my testing. So I have carefully selected the packages that work with Ubuntu 14.04. (yes, that's what Travis is using. Ugh.)

  ```
  addons:
    apt:
      packages:
      - latex-xcolor
      - texlive-base
      - texlive-latex-base
      - texlive-latex-recommended
      - texlive-fonts-recommended
      - texlive-fonts-extra
      - texlive-latex-extra
      - texlive-formats-extra
      - texlive-bibtex-extra
      - texlive-humanities
      - texinfo
      - texlive-science
      - latexmk
  ```

- Create your LaTeX book. In my case, I use a Makefile for this. We're going to switch to `latexmk` soon but are having some problems with it, hence the additional package you see in the above.

  ```
  script:
  - make book
  ```

- Now here is where things get a bit dicey. You need to declare what you want to deploy--and how you're going to do it. In this case, I'm deploying to our project at `PurdueCAM2Project/SE4ML`. In order for this to work, you need to take some preliminary steps. I'll go through each of these.

- There have been a number of changes to Travis lately, owing to the corresponding changes also happening at GitHub, where apps are being phased in and services phased out, respectively. So you will be moving to `travis-ci.com` (as opposed to `travis-ci.org`). You should set up the `travis` gem (from Ruby) if you haven't done so already. This gives you command line support to set up the following block of YAML code (mostly).

  `travis setup releases --pro`


  ```
  deploy:
    provider: releases
    api_key:
      secure: NA6E8nfyjpc8clNYP9pT5jBKK95ughnNoneki/V87zvBWg8xFWz58A8ltnFW7ulGn41p2QGZ0tRVysn72bC27X/Ditlr+W8LsLODpLWhXrY6eVp1mTQsYY5DBRKv5fAxCNz5ttQywSz03V8SgJyM4inQlJo9WNzZ7EKt+/MGgh7NIGAxQYc6G8LqvnoDNmbYAMz7ewtyOkEbZvCRrMqCZn/06qFnf4/l14RYsIacnpRyiakRylssA5piiNCG0H5NV772vrPNttDMWFSm/Oi7Z4U9G/uvpX9s0ylZRXJEmn3OGZkonvc15Q2MK0FCxM5AutDzlS+vLGcMFCKdLiV+b7AMN8E/iCJSC8sR036VIc1GLlRUvn+KlL8Txt3wa1i09gmo7cLEtwwrtP8svOnItyqCOyQ/y59ZBLIynhFcrEpg3v/03TblU9j7+c0cJ+tHv3CLh373q1QzZH4XOi+Xy23aRRwRM1sxWBoS398p/51lj54er865E8Nc7NfoINilO1v/yNLFEi7gRSs8rBbzq09u4KIavmel5xTsdQ+KDwmt+tDdTj0Oj5OJWci8dsz1v24xOXNf9BntlDw8wRsV4Ksxe0fppifoGm9/O+6HqXyA5PdVS0ehWVjOIdR1sA92NFCUFXhP0xBidowlD1PvvihYo6aqQYbvp2UL5qw2m3E=
    file:
      - "se4ml.pdf"
    skip_cleanup: true
    on:
      repo: PurdueCAM2Project/SE4ML
      tags: true
  ```

  I say _mostly_ because not all of what you see here is added to your .travis.yml automagically. First, the `api_key:`. You need to use `travis encrypt` to create this. You also need to add the `skip_cleanup: true` and `on: repo:` key you see here (with your own repo-specific info).  We do not cover API keys here as this is easy to do within GitHub, and there are plenty of resources that explain how to do it. Lastly, don't forget the `on: tags:` key. You need to set this in order to trigger a release anytime you apply a tag and push it to your repo. In my case, I don't want every commit to trigger a release--just the milestones (major and minor). We use simple versioning like `v0.1` or `v0.1.1` at this stage. But any legitimate tagging scheme will work. If you `git tag` it, the release will show up.

  The `file:` key is used to list any files you'd like to be deployed to GitHub Releases for your project. These files will be _in addition to_ the .zip and .tar.gz (tarball) that are done by default. (I am still working on how to disable those. My release is simply the .pdf for those who want to view the book in progress.)

# Acknowledgments

- The general resource at [Travis CI](https://docs.travis-ci.com/user/deployment/releases/) provides a useful overview.

- This page by [Victor Hurdagaci](https://www.victorhurdugaci.com/github-releases-travis) describes his experiences and is a helpful starting point. I hope some of the additional details provided above will prove helpful.


# Questions?

Please don't hesitate to contact me (gkthiruvathukal). See my profile for contact information.
