# More on Jupyter Notebooks

Let's learn some more about Jupyter notebooks. 
They are widely used by beginners, experts, and everybody in between. 
We will see how a notebook consists of content 'cells', how these can be managed, and how to format content. 
We're demonstrating on a Chrome browser. 
Some details will differ on other browsers.
You can also access notebook files using vs code. 
This will look significantly different, but the concepts and workflows are virtually the same. 

## Opening a notebook 

We'll start by opening a notebook. 
We'll open the Hello World notebook that we made in the previous section. 
If you don't have this to hand, don't worry, you can start with a new notebook and type this in again.
It's helpful to locate this notebook in a Windows explorer window. 

If you have Jupyter notebooks already open, and this notepad location is accessible by Jupyter, then you can navigate directly in this folder, and open the file. 
Otherwise, and in any case, you can run another Jupyter notebook. 
As usual, you can make a new Anaconda prompt by typing this into the run box. 
Or you could re-use one that's not doing anything else right now. 


We suggest changing directory before running Jupyter notebooks. 
An easy way to do this is to copy the address on the explorer window. 

## Renaming a notebook

Once it is open, we can find a couple of ways to rename the file, both from the notebook page, and the index page. 
The index page provides controls for moving files and folders. 
Alternatively, if the file is not open (closed), you can use Windows Explorer to do these same tasks. 
You can even use the command prompt to do these tasks! 
But that is quite a geeky option. 


Now let's look at the content of a Jupyter notebook. 
It's a list of content cells - each of these blocks is called a cell. 
If it has a green tag, then it's in edit mode -- you can type in the box. 
If it has a blue tag, then it's in command mode. 
You can switch between these modes using the 'escape' and 'return' keys. 
Try it out, now.

## The hash '`#`' Character in Python 

While we are in edit mode, let’s look at just one bit of python: how the hash character is used. 
I’ll copy and paste the original print statement, and edit the output text a little bit.

If I put a hash character at the front of any of these lines, we see that the formatting changes: 
we say that line is ‘commented out’. When we run that code cell, we see that now, that line is ignored. 
In fact, any text after the hash character is ignored by python. 

The main use of this feature is to write text ‘comments’ that other team-members can read, 
so that they can better understand the code. 
That’s why coders talk about disabling lines of code as ‘commenting them out’: 
by turning them into ‘comment’ lines, python will ignore them, hence they are disabled.

## Some Common Notebook Controls:

When we are in command mode, we can add cells below by hitting the 'b' key, and above by hitting the 'a' keys. 
These 'a' and 'b' keys are the quickest way of adding new cells. 
You can also do this from the menu at the top of the page. 
You can move selected cells up, or down, by selecting the appropriate command from the ‘edit’ menu. 
You can delete a cell by pressing ‘d’ key twice. 
The cells we have added so far are called 'code' cells -- they contain Python code. 
Another type of cell is called 'markdown'. 
These cells are designed to hold formatted text content, including headings, lists, tables, images, source code snippets and equations. 

## Markdown cells

When in command mode, we can switch the cell to markdown with 'm', and to code with 'y'. 
(We’re not sure why they chose 'y' as the shortcut key!)
Let's add some simple formatted text to the top cell. Special characters like '#', '*', '|' and '_' are used to format the text. 
When we 'run' the cell, we don't see these characters any more – they are used to format the text.
A single 'hash' character, followed by a space, gives a 'level 1 heading'. 
Two and three hash characters give second- and third- level headings. 
Let's 'run' this cell and see the formatted result.
A dash shows a bullet point, we can put a tab in front of a dash to make 'nested bullet points', that is: a set of sub-bullet points under the main point. 
(Actually, nesting one object within another, and using the indent to show this, is an important idea in Python.)
We can show italics by enclosing the text with a single asterisk. 
We can show bold font text by enclosing text in two asterisks – and no spaces. 
Remember that asterisks are needed at the end, as well as the beginning. 

## Including a web link as markdown content 

To make a link to a website, we need to use square brackets for the text, and normal brackets for the link. 
Let's make a link to a markdown cheat-sheet. 
We'll search for a markdown cheat-sheet, and then make a link to it from our notebook. 
We'll add the text for the link here, enclose it in square brackets, then add the actual link, in square brackets. 
When we run the markdown, we only see the text for the link, but we can click on the link, as usual. 
This cheat-sheet can be consulted for other markdown features, such as tables, images and equations.
We'll now review how code cells are run, before troubleshooting some potential issues. 
We can add some more code cells, with additional print statements, like this. 
We can run each code cell individually, or we can run the entire sequence, using the 'run all cells' command from the menu.
Notebooks are usually designed to be run from top to bottom, as a sequence. 
It's a nice feature of notebooks, that we can also run the code one cell at a time. 
That way, we can pause, inspect and  modify the sequence, as it runs. 
Also, note the number in square brackets on the left margin. 
This shows the order in which the code cells is run: number one is the first cell to be run, number two is the second, etc. 
The most recently executed cell has the highest number. 
