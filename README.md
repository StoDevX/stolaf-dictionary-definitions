# stolaf-dictionary-differ

[![Build Status](https://travis-ci.org/StoDevX/stolaf-dictionary-definitions.svg?branch=master)](https://travis-ci.org/StoDevX/stolaf-dictionary-definitions)

This needs four things to work:

1. Python 3
2. Bash
3. A Github API key
4. Something like `cron`

### The Python
It's simple and direct.

We get the three pages, use BeautifulSoup to generate a nice and consistent HTML blob of the definitions, then write each blob to a file.


### The Bash
A bit more complicated.

Start off by running the python script. We rely on Git to see if there are any changes made to the files.

If there aren't, we talk to Dead Man's Snitch and exit.

If there are, we make a branch for the changes, commit to it, then open a PR on Github with the changes.

Then we tell Dead Man's Snitch that we've finished.


### Dead Man's Snitch
It's not required, but it waits to hear from something every so often. If it doesn't hear back, it sends you an email telling you that something's not working. Nice and simple.


### How I did this:

- set up a scheduler to run `./bin/fetch.sh`
- add the Dead Man's Snitch integration
- take the link from Dead Man's Snitch and put it in `./bin/fetch.sh`
- Done!

Now, whenever I push a new commit to this repository, new stuff is fetched. Then the next time the scheduler runs it, it's already set up.

I've tried to make it not terribly complicated. If anyone thinks of an improvement, let me / us know! Issues and PRs are open and welcome :smile:.
