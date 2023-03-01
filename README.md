# ChatWrap
ChatGPT Wrapper
A simple Wrapper that uses the <code>openai</code> python library and adds compatibility for the same engines that run ChatGPT. This may seem weird for those who are new to openai and there are a few options for model engines depending on what you are doing:
- Text response: There are multiple where the best one is <code>"text-davinci-003"</code> although there are babbage, ada and more
- Content Filtering: There is only one called <code>"content-filter-alpha"</code>
- Code Completion: There are two current engines the davinci and the cushman engines
The difference between the kinds of engines are what their specialized purpose is and should be used accordingly. This repository does not provide any API keys for free and must be given by the developer or user.
There are the following classes:
- <code>Code</code>
- <code>Filter</code>
- <code>Chat</code>
- <code>Image</code>
If you want to view the following functions and their uses and documentation please see the [ChatWrap Stub](https://github.com/Ixonblitz-MatOS/ChatWrap/blob/main/Chatwrap.pyi)
