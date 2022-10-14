- you can deploy your app for free using cloud web servers such as [heroku](https://www.heroku.com/) or [pythonanywhere](https://www.pythonanywhere.com/)
- in prod, make sure you set debug to False in the code below (in 00-flask.py), as otherwise it may make your website prone to hacking  

```python
 __name__ == "__main__":
    app.run(debug=True)
```


### CSS
Web browsers follow CSS rules to determine how a document should be displayed.
There are several ways to form CSS rules. It can be done via a set of properties, each with a value that updates the way the HTML content gets displayed. For example, a set of properties in the CSS might say the element should have a yellow background and a width that is 20 percent of that of the parent element. 
Alternatively, you can form CSS rules through selectors. As the name implies, selectors select an element or elements to apply to updated property values, for instance, the selector applying the CSS rules to every paragraph within an HTML document. 

Some working examples:
- [CSS styling](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Styling_a_biography_page)
- [how's CSS structured](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured)
- [The ultimate guide to CSS](https://skillcrush.com/blog/css/)
