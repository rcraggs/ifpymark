# ifpymark
conditionally exclude sections from a markdown file


In your markdown document include sections such as 

```markdown
# Heading


<!-- START:HINTS -->
Hidden Section
<!-- END:HINTS -->

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo

<!-- START:ANOTHER -->
Hidden Section
<!-- END:ANOTHER -->

consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<!-- START:HINTS -->
Hidden Section
<!-- END:HINTS -->
```

you can generate the file without certain sections by doing 

```bash
python3 pyifmark.py -e HINTS -e ANOTHER myMarkdownFile.md
```
