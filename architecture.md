## How the SSG works

The vast majority of our coding will happen in the src/ directory because almost all of the work is done in steps 2 and 3 above. Here's a rough outline of what the final program will do when it runs:

1. Delete everything in the /public directory.
2. Copy any static assets (HTML template, images, CSS, etc.) to the /public directory.
3. Generate an HTML file for each Markdown file in the /content directory. For each Markdown file:
    - Open the file and read its contents.
    - Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
    - Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
        - Raw markdown -> TextNode -> HTMLNode
4. Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
5. Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.
6. Write the full HTML string to a file for that page in the /public directory.

## How we're gonna build it
We're not going to build the program in the same order that it runs... that's often not the best way to build large projects. Instead, we'll tackle individual problems that we know we'll need to solve and use unit tests to make sure they work as expected. We'll put the pieces together into a working program as we get close to the end.