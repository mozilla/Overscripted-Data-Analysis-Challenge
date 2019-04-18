### What is there in call_stack?

A first glance shows it as something that is hard to make sense of.
For example,
`'zc@https://www.google-analytics.com/analytics.js:5:1365\nma@https://www.google-analytics.com/analytics.js:29:36\nmc@https://www.google-analytics.com/analytics.js:28:228\nJc@https://www.google-analytics.com/analytics.js:44:414\npc@https://www.google-analytics.com/analytics.js:41:72\nN.create@https://www.google-analytics.com/analytics.js:57:62\nX/b[a]@https://www.google-analytics.com/analytics.js:25:84\nZ.v@https://www.google-analytics.com/analytics.js:55:105\nZ.D@https://www.google-analytics.com/analytics.js:54:277\nN.N@https://www.google-analytics.com/analytics.js:59:235\nrc@https://www.google-analytics.com/analytics.js:48:506\nz@https://www.google-analytics.com/analytics.js:48:538\n@https://www.google-analytics.com/analytics.js:59:361\n@https://www.google-analytics.com/analytics.js:1:2'`

To understand more, we need to know what a call stack is. [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Glossary/Call_stack) define it as:
"A call stack is a mechanism for an interpreter (like the JavaScript interpreter in a web browser) to keep track of its place in a script that calls multiple functions — what function is currently being run and what functions are called from within that function, etc."

There are multiple functions in the `call_stack` and the [OpenWPM code,](https://github.com/RuizhiYou/OpenWPM/blob/RunThis/automation/Extension/firefox/data/content.js) that ran the crawl, would help in knowing how the data is structured.

First thing to notice is that the stack contains information about multiple functions, all of which are separated by `\n`.

The OpenWPM code takes a trace and takes the fourth element from trace which it calls `callSite`. `callSite` is then split where `@` appears and the result is called `callSiteParts`. `callSiteParts`'s the second part is taken which undergoes `rsplit` ,ie it is converted to a list of only three elements, and is called `items`. `columnNo` , `lineNo` and `scriptFileName` are the last, second last and third last elements of items, respectively. `funcName` is the first argument of `callSiteParts`.

The return format is `FUNC_NAME@FILENAME:LINE_NO:COLUMN_NO`. Using this format, we can easily get information about function name, filename, line number and column number, after separating on `\n`.

Example:
Taking the example mentioned above, if we split at `\n` and take the first part, we have `zc@https://www.google-analytics.com/analytics.js:5:1365`.
Here,
Function name is `zc`
File name is `https://www.google-analytics.com/analytics.js`
Line number is `5`
Column number is `1365`

This can help in identifying trackers.