'''
Git is one of the most important tool every developer has to be aware of

Source control:
In real life, projects are huge and you are not the only developer working.
Source control enables multiple people work on same project from various locations

We have a copy of the project, but there is a centralized location up somewhere, maybe owned by the

company or somewhere on the internet that has the ultimate version that we each talk to to make sure

that we each have the same version.

Getting GitHub is a way to do this, to be able to use source control.

And as a matter of fact, it's the de facto way of doing this.

So like I said before, this is most likely the tool you'll be using every single day at your workplace.

So if I go to the GitHub website here, what it allows us to do is it's a place, a central place that

both Andre and Marci can talk to.

So even though we work on the same files, the same project.

I can ask this central location such as GitHub.

Hey, has Marcy made any changes?

And Marcy can ask.

Hey, has Andre made any changes?

And every once in a while you'll get something like this where we have cool background and super background,

where we have something called a merge conflict.

What GitHub allows us to do is say, Hey, I notice there is a merge conflict.

I see that you guys have both changed your background.

I don't know who's right, but here's the information.

Andrei Marcy, can you guys talk amongst yourself and figure it out?

That's pretty much the workflow.

So let's actually see what this looks like.

The first thing we want to do is set up a GitHub account.

If you haven't done it in the previous exercises, you absolutely should start a GitHub account.

It's free.

And like I said before, if you're a developer, you just need to have it.

It's where everybody puts their projects, it's where you work.

You'll be spending a lot of time on this website.

You might remember that when we had the GitHub project, I also told you to get GitHub for desktop.

Although we use that to make things simpler during the video, this is actually not the recommended

way of doing it.

It allows you to visually see and interact with GitHub, but it's kind of looked down upon by employers

It is not a good way since the code is exposed using the Github application. So better get used to the terminal.


1. Login to Github
2. create a repo
3. push the code using git commands.

Git commands:
git clone <project link>
git status - to see the status of what we have in the local folder.
git add <filename>


1. open CMD from your project folder path
2. config your credentials: username, email

	git config --global user.name "Sridhar"
	git config --global user.email "sridhar6261@gmail.com"

3. now initialize the folder: git init
 	github creates this local file to understand your files and push the code. creates a .git file in the folder.
4. to stage / stash the files: git add *
   	if you want to see what all files are staged: git status
5. commit all the code that is staged: git commit -m "commit message"
6. if doing for the first time or creating a repo for the first time follow this step. Else exclude this and go to step 7

                          git remote add origin "git repository link"

to tell local .git file where to push the code we have to give repo link. We do it using this command.
	eg: git remote add origin https://github.com/Sridhar36/python_zero_to_master.git
7.  git push origin master

note: git commands dont work unless you are in a .git folder. That is, in our case always open the cmd from the repo folder.

to get the copy of an online repository :

create a local folder
open cmd
git clone <repo link from git>

if you make changes and want to push them:

go to repo folder and open cmd
git status > gives the set of changes and their status.

git add <file> or git add *
git commit -m " "
git push

to take pull request:

git pull
'''



"""
1. open CMD from your project folder path 
2. config your credentials: username, email
	
	git config --global user.name "Sridhar"
	git config --global user.email "sridhar6261@gmail.com"
	
3. now initialize the folder: git init
 	github creates this local file to understand your files and push the code. creates a .git file in the folder.
4. to stage / stash the files: git add *
   	if you want to see what all files are staged: git status
5. commit all the code that is staged: git commit -m "commit message"
6. if doing for the first time or creating a repo for the first time follow this step. Else exclude this and go to step 7

                          git remote add origin "git repository link"   
	
to tell local .git file where to push the code we have to give repo link. We do it using this command.
	eg: git remote add origin https://github.com/Sridhar36/python_zero_to_master.git
7.  git push origin master 







note: git commands dont work unless you are in a .git folder. That is, in our case always open the cmd from the repo folder.

to get the copy of an online repository :

create a local folder
open cmd
git clone <repo link from git>

if you make changes and want to push them:

go to repo folder and open cmd 
git status > gives the set of changes and their status.

git add <file> or git add *
git commit -m " "
git push


if you want to take latest code from repo

	- git pull

direct master branch is not good option.
Becuase it allows anyone to push any change to master/main without any monitoring,.

If a newbie pushes some changes and that might possibly crash the app.


To avoid this: we use branching

we create branches for little features and work on them. Once that change is done we gonna merge the developed feature to the main master code or the main application we could say,.


to create a new branch: git branch < new branch name>
to get list of available branches: git branch
to move to branch we want: git checkout <branch name>

to push the changes:

git add *
git commit -m ""
git push 

On git hub it will show this separately as a yellow bar. Now you can click on it and add some message and raise a pull request.

Main repo owner can go through the changes and merge the PR.



"""