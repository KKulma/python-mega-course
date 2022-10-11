- you can deploy your app for free using cloud web servers such as [heroku](https://www.heroku.com/) or [pythonanywhere](https://www.pythonanywhere.com/)
- in prod, make sure you set debug to False in the code below (in 00-flask.py), as otherwise it may make your website prone to hacking  

```python
 __name__ == "__main__":
    app.run(debug=True)
```
