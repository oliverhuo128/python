# '`Hello World!`' in a Jupyter Notebook, and in a Python file

Let's use the Anaconda distribution to make a new Jupyter notebook, and a standalone Python file. 
In both of these, we'll run the traditional first program that prints out 'hello world'. 

We use notebooks to share ideas and example Python code with others. 
On the other hand, Python code for 'production applications' is typically included in standalone Python files, 
because they are easier to manage and maintain. 


## Jupyter Notebooks

(NB If you can already create and run Jupyter Notebooks using VSCode, feel free to adapt these instructions accordingly!)

We'll start with the Anaconda prompt, which is the normal Windows command prompt plus some Python commands. 
To create a new anaconda prompt, press the 'windows' key (sometimes known as the start key), 
and start typing 'anaconda prompt'. You should see a black window with white text, 
along with a flashing horizontal bar ('the 'prompt' or 'cursor') that shows you where to type.

We can also see that the cursor line is showing us a particular folder on our machine that it is currently 'working in'. 
This is called the 'current working directory' (A 'directory' is another name for 'folder'.)

In my case, it is 'C:\Documents\James' -- my home folder. We can type ‘dir’ <return> to list the contents of this folder.
We can also use the 'cd' command to change directory. For example, we can change to a sub-folder called 'python'. 
This is called a relative folder path, because it is relative to the current folder. 
An important relative path is the parent folder, which we can reference using 'dot dot'.  
In contrast, we can also use 'absolute' paths to specify a folder. 
These start from the top level of the file system: in Windows, this is a drive letter such as 'C:' or 'D:'. 
This ‘absolute path’ can be copied and pasted from a Windows Explorer address bar.


We'll use the anaconda prompt to start the Jupyter notebook. 
We suggest changing directory beforehand, to the folder where you are storing your Python work, so we use 'cd' to do this. Then, we type 'Jupyter notebook' and hit return. You should see a page on a browser, 
with several controls to create and view files and folders. 
We'll create a new Jupyter notebook, by selecting the corresponding command from the menu. 
This presents a new page, in a new tab, showing the notebook. 
First thing we'll do is change the name -- let's call it 'hello world'.
Then, in the next box, we type in the traditional first line of any programming journey, '`print('hello world')`'. 
Note the brackets, the single quotes, and also note that 'print' is in lower-case.  
We can run this program in a couple of ways: from the menu, from the toolbar, or the using the keyboard shortcut, which is 'control' plus 'enter'. 
Below our program, we should see the famous greeting printed out – which is the indication that our programming environment is functioning. 

## Standalone Python file.

Next, we'll run that same program as a standalone Python file. We can create that file in many ways: 
we'll use Jupyter notebook, but you could use notepad or any editor. 
Choose 'new ... text file', and rename this 'hello_world.py'. 
Note the underscore, and also the file 'extension' has changed from `.txt` to `.py` -- 
it's important to get this exactly correct.

In this Python file we'll write the same Python program -- 'print('hello world')'. 
We can copy the code using control-C and paste the code using control-V -- but always be on your guard when doing this, because it's an easy way to introduce bugs (errors) into your code. 
Be sure to save this file, either from the menu or by using 'Control-S'. 

We'll run this program from the Anaconda prompt. 
We won't be able to use the first Ananconda prompt -- it is still running Jupyter notebook, 
which you can see from the lines of output, and the lack of any prompt at the bottom. 
So we'll create another anaconda prompt, and use 'cd' to change directory to the correct folder. 
You can list the contents of this folder by typing 'dir' -- 
you should see both the notebook file and the regular Python file.  
We can run a Python program by typing 'python' (in lower case) and then the name of the Python file. 
So here, we'll type 'python hello_world.py'. 
Remember that the spelling of the filename must match exactly. 
You should now see the same famous phrase, printed out on the console. 
You have written the 'hello world' Python program, 
and run it in two different environments -- as a Jupyter notebook, and as a command-line program. 

Congratulations! 
