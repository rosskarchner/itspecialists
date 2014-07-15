# We Are All IT Specialists

This is a demo site, built with Sheer

# What does it do?

When you run 'sheer index' inside this directory, all of the "IT Specialist" jobs will be pulled from usajobs.gov and loaded into Elasticsearch.

When you run 'sheer serve' inside this directory, and point your browser at 127.0.0.1:7000, you'll be able to peruse those jobs at your leisure, and even search them!

# Is that it?

There's also an animated US Flag

# How do I make it work?

### Step 1: Get elasticsearch and python 2.7


That is beyond the scope of this document. Be sure to install virtualenv and virtualenvwrapper!

http://virtualenvwrapper.readthedocs.org/en/latest/

### Step 2: Install Sheer

Check out the sheer Github project:
```
$ git clone https://github.com/cfpb/sheer.git
```
create a virtualenv for sheer:
```
$ mkvirtualenv sheer
```

The new virtualenv will activate right away. to activate it later on (say, in a new terminal session) use the command "workon sheer"

Install sheer into the virtualenv with the -e flag (which allows you to make changes to sheer itself):

```
$ pip install -e ~/path/to/sheer
```

Install sheer's python requirements:

```
$ pip install -r ~/path/to/sheer/requirements.txt
```

You should now be able to run the sheer command:
```
$ sheer

usage: sheer [-h] [--debug] {inspect,index,serve} ...
sheer: error: too few arguments
```

That means it's working!

### Step 3: Explore the demo



1) check out this here repo into some directory on your machine
2) cd [checkout directory]
3) do this

```
sheer index
```



```
$ sheer serve
```

And browse to http://localhost:7000

You may also want to check out http://localhost:7000/api/v1/q/jobs.json

Enjoy!

