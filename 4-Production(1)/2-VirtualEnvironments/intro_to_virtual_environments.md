# An Introduction to Virtual Environments

- We can have many installations of Python on our computer. These exists at different path locations. We can say we have many different Python 'environments'.
- One will be set as the default version which is accessed when you write `python` in a command prompt / powershell.
- In an anaconda prompt, when you write `python` you are specifically asking for the anaconda version of python.
- Each Python installation/environment will be able to see all the packages stored on the PYTHONPATH (the path where that particular version of python is installed).
- When we start new projects, it is useful to create a new environment, which we just call a 'virtual'* environment.
- This fresh new environment will only contain Python, and a few key tools required to make Python work. When we need another modules/packages, we need to explicitly install them using a package manager e.g. `pip` or `conda`.
- This way, only the requirements of our project exist in our environment and nothing more. So when we need to share our code, or get it running on another person's machine, we can simply hand them the `requirements.txt` file (or equivalent) and they have everything they need to recreate the environment to run our code.

> \* The word virtual is used in a lot of different contexts, and it can mean a lot of different things.
> In this context, it simply means another folder on your computer with another version of Python installed.
> Don't let the word scare you!
