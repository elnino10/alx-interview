## Starwars API

The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

## Concepts Needed:
- HTTP Requests in JavaScript:
  - Understanding how to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
  - [A Complete Guide to Making HTTP Requests in Node.js](https://www.memberstack.com/blog/node-http-request)
- Working with APIs:
  - Understanding the basics of RESTful APIs and how to interact with them.
  - Parsing JSON data returned by APIs.
  - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- Asynchronous Programming:
  - Managing asynchronous operations with callbacks, promises, and async/await syntax.
  - Handling API response data asynchronously.
  - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
- Command Line Arguments in Node.js:
  - Using the `process.argv` array to access command-line arguments passed to a Node.js script.
  - [How to Parse Command Line Arguments in Node.js](https://tecadmin.net/how-to-parse-command-line-arguments-in-nodejs/)
- Array Manipulation and Iteration:
  - Iterating over arrays and manipulating data structures to format and display character names.
  - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Task
Write a script that prints all characters of a Star Wars movie:
  - The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
  - Display one character name per line **in the same order as the “characters” list in the** `/films/` endpoint
  - You must use the [Star wars API](https://swapi-api.alx-tools.com/)
  - You must use the `request` module

```
elnino@elnino:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
elnino@elnino:~/0x06$ 
```
