How to contribute to Pegelinux
==============================

Thank you for considering contributing to Pegelinux!

Support questions
-----------------

Please, don't use the issue tracker for this. Use one of the following
resources for questions about your own code:

* The Telegram group `pegelinux`_ .

.. _pegelinux: https://pegelinux.id/about

Reporting issues
----------------

- Describe what you expected to happen.
- If possible, include a `minimal, complete, and verifiable example`_ to help
  us identify the issue. This also helps check that the issue is not with your
  own code.
- Describe what actually happened. Include the full traceback if there was an
  exception.
- List your Python, Flask versions. If possible, check if this
  issue is already fixed in the repository.

.. _minimal, complete, and verifiable example: https://stackoverflow.com/help/mcve

Submitting patches
------------------

- Try to follow `PEP8`_, but you may ignore the line length limit if following
  it would make the code uglier.
- Or run `inv clean` to run black as pep8 formatter

First time setup
~~~~~~~~~~~~~~~~

- Download and install the `latest version of git`_.
- Configure git with your `username`_ and `email`_::

        git config --global user.name 'your name'
        git config --global user.email 'your email'

- Make sure you have a `GitHub account`_.
- Fork pegelinux to your GitHub account by clicking the `Fork`_ button.
- `Clone`_ your GitHub fork locally::

        git clone https://github.com/{username}/flask
        cd flask

- Add the main repository as a remote to update later::

        git remote add pegelinux https://github.com/nsiregar/pegelinux
        git fetch pegelinux

- Use pipenv::

        pipenv install
        pipenv shell

.. _GitHub account: https://github.com/join
.. _latest version of git: https://git-scm.com/downloads
.. _username: https://help.github.com/articles/setting-your-username-in-git/
.. _email: https://help.github.com/articles/setting-your-email-in-git/
.. _Fork: https://github.com/nsiregar/pegelinux/fork
.. _Clone: https://help.github.com/articles/fork-a-repo/#step-2-create-a-local-clone-of-your-fork

Start coding
~~~~~~~~~~~~

- Create a branch to identify the issue or feature you would like to work on (e.g.
  ``basic-test-suite``)
- Using your favorite editor, make your changes, `committing as you go`_.
- Try to follow `PEP8`_, but you may ignore the line length limit if following
  it would make the code uglier.
- Include tests that cover any code changes you make. Make sure the test fails
  without your patch. `Run the tests. <contributing-testsuite_>`_.
- Push your commits to GitHub and `create a pull request`_.
- Celebrate 🎉

.. _committing as you go: http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes
.. _PEP8: https://pep8.org/
.. _create a pull request: https://help.github.com/articles/creating-a-pull-request/

.. _contributing-testsuite:
