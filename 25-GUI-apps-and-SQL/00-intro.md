In order to create an executable file, follow the instructions below: 

1. Install pyinstaller: `pip install pyinstaller`
2. Run `pyinstaller --onefile --windowed frontend.py`
3. The file will come with an empty `books.db` file, so if you want to keep your existing db entries, just replace the db file from `dist/` location with the one we created earlier
4. COMMECT: I've had a mixed luck using the above command on Mac - it returns an .exe file even in OS X...