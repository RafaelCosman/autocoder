# Autocoder
`autocoder` is a command-line tool for automatically writing code directly in your repo. After installing, navigate to your project folder and then run `autocoder "<instructions for what you want to do>"`

For example:
- `cd my-repo`
- `autocoder "please write me a login page"`
- `autocoder "write me a webserver to serve the login page"`
- `autocoder "run the webserver"`
- `autocoder "please add styling to the login page so it looks better"`

Autocoder will also automatically catch exceptions thrown by code it runs, and will attempt to fix bugs.

## Demo Video (60s)
[![Demo Video](https://img.youtube.com/vi/LHN0sVsVulk/0.jpg)](https://www.youtube.com/watch?v=LHN0sVsVulk)

Features demoed
1. Writing new files
2. Running console commands
3. Debugging simple bugs
4. Editing files

Note: The OpenAI API actually takes several seconds to reply, this waiting time was edited out to make the video shorter. Thus the tool in practice is significantly slower than shown in the video.
