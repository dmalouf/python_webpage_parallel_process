# python_webpage_parallel_process
A webpage that fires off another Python script in the background, letting the user move on without stopping background task.

This was little project that was based on my need to fire-off a process that was not bound to a web-user staying on the webpage.  I thought it might be fun to use Python for this (instead of my 'native' PHP).

In short:

1. ```index.py``` takes ```index.html``` as a template and sends it to the user
2. In this example, the user's POST, query-string, etc. goes to ```main.py``` which.
  1. fires off ```backgroundTask.py```
  2. sends back to the user that all is well
3. ```backgroundTask.py``` is the 'background task' which runs even after main.py is done sending the 'all is well' back to the browser
  1. for my need, this background task runs for about 5 minutes
