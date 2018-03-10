# assaultbot
A Twitter bot that tweets words from a dictionary, with optional prefix and postfix pre/ap-pended.

Based on tweepy.

You will need to edit the script and insert your Twitter API details, or it will not work! Fill out the form at https://apps.twitter.com/ and populate the generated details in the indicated locations within the script.

Also be sure to install the required libraries using the provided requirements file.

```bash
pip install -r requirements.txt
```

To use the script, pass it an argument pointing to a text file containing one word per line. A sample dictionary.txt file is included.

```bash
./assaultbot.py dictionary.txt
```

There are a couple other things you can configure, such as tweet frequency, and tweet prefix and postfixes. Read the script comments for more info.
