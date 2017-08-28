# Creating a Simple HTML Webpage

The modern internet as we know it is visualized by the initial work done by the physicist Tim Berners-Lee, who invented HTML (Hyper Text Markup Language) in the early 90's.  Originally the spec for HTML consisted of 18 'tags' or components.  Nearly 30 years later HTML has evolved quite a bit supporting something like 188 tags, but still holds to the original schema developed by Berners-Lee.

Even with all the new tools available to the web-developer, building a simple webpage describing yourself remains very simple.

## <tags>

HTML is considered a mark up language rather than a programming language. Meaning that the "code" or markup that is complied is used to visualize something rather than do a task.

Every webpage on the internet starts with the following code...

```HTML
<html>
  <head>
    <title>The Meaning of Life</title>
  </head>
  <body>
    <h1>What is the meaning of life?</h1>
    <p>The answer is simply, <b>42</b></p>
  </body>
</html>
```

Ok, so this example is a bit over the top, but the idea hold true regardless.  Every webpage needs the `<html>`, `<head>` and `<body>` tags.

Using HTML tags is really simple.  They all **open** then **close**.  Open/closing tags refers to the `<tag>` then `</tag>` syntax.  Some tags such as the image tag do not allow for inner HTML (the HTML inside of a tag) but still "close" all the same.

For example using the image tag

```html
<img src="https://imgs.xkcd.com/comics/tags.png">
```

is the same as:

```html
<img src="https://imgs.xkcd.com/comics/tags.png" />
```

## Learning more

The website [w3 schools](https://www.w3schools.com/) has a complete set of tutorials and demos on building webpages with HTML.  For the HTML lessons [click here](https://www.w3schools.com/html/html_intro.asp).
