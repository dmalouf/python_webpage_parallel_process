# python_webpage_parallel_process
A webpage that fires off another Python script in the background, letting the user move on without stopping background task.

This was little project that was based on my need to fire-off a process that was not bound to a web-user staying on the webpage.  I thought it might be fun to use Python for this (instead of my 'native' PHP).

In short
# index.py takes index.html as a template, tweaks it a bit, and sends it to the user
# the user's POST goes to main.py which.
## fires off makeItSo.py
## sends back to the user that all is well
# makeItSo.py is the 'background task' which runs even after main.py is done
## for my need, this background task runs for about 5 minutes

