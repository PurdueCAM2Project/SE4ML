<<<<<<< HEAD
# Building the Book in Sphinx

## First time setup:

1. For all Python work, I always recommend using a virtual environment. This assumes we are using Python 3. Start
by making sure Python's `venv` support is installed. Virtual environments allow you to update your Python libraries and dependencies w/o root. Root is only required for setting up the initial Python virtual environment support.

  ```
  sudo apt install python3-venv
  ```

2. Create virtual environment:

  ```
  python3 -m venv ~/myenv
  ```

  The above creates a virtual environment in ~/myenv. You can use any name you like.


3. Source the virtual environment

  ```
  source ~/myenv/bin/activate
  ```

  or

  ```
  . ~/myenv/bin/activate
  ```

4. Install Sphinx in virtual environment

  ```
  pip install -r requirements.txt
  ```


5. Do a sanity check:

  ```
  which python
  which python3
  which sphinx-build
  ```

  If you do not see the full path to `~/myenv/bin` in the results of `which`, you are not in the virtual environment.

## Building the book in your virtualenv:


0. Make sure you are in the `sphinx-book` folder

  ```
  cd sphinx-book
  ```

1. Build the Sphinx book:
  ```
  make clean
  make html
  make latexpdf
  ```

  I recommend always doing `make clean` before any build, similar to LaTeX work. This ensures any cached data are cleared out.

2. Check the build results (Linux only shown here):

  ```
  xdg-open build/latex/SoftwareEngineeringforMachineLearning.pdf
  xdg-open build/html/index.html
  ```

=======
# Building the Book in Sphinx

## First time setup:

1. For all Python work, I always recommend using a virtual environment. This assumes we are using Python 3. Start
by making sure Python's `venv` support is installed. Virtual environments allow you to update your Python libraries and dependencies w/o root. Root is only required for setting up the initial Python virtual environment support.

  ```
  sudo apt install python3-venv
  ```

2. Create virtual environment:

  ```
  python3 -m venv ~/myenv
  ```

  The above creates a virtual environment in ~/myenv. You can use any name you like.


3. Source the virtual environment

  ```
  source ~/myenv/bin/activate
  ```

  or

  ```
  . ~/myenv/bin/activate
  ```

4. Install Sphinx in virtual environment

  ```
  pip install -r requirements.txt
  ```


5. Do a sanity check:

  ```
  which python
  which python3
  which sphinx-build
  ```

  If you do not see the full path to `~/myenv/bin` in the results of `which`, you are not in the virtual environment.

## Building the book in your virtualenv:


1. Build the Sphinx book:
  ```
  make clean
  make html
  make latexpdf
  ```

  I recommend always doing `make clean` before any build, similar to LaTeX work. This ensures any cached data are cleared out.

2. Check the build results (Linux only shown here):

  ```
  xdg-open build/latex/SoftwareEngineeringforMachineLearning.pdf
  xdg-open build/html/index.html
  ```

>>>>>>> d0656bd158170401dfaff23a3704ca4eab2a0b8c
