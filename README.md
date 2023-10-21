# assaultbot
-----------ARCHIVED REPO-----------

Given that Elon's changes to Twitter's free API call limits have dealt a death blow to novelty bots, I see no reason to keep this repo active.

Maybe some day I'll decide to make this a Mastodon or Bluesky (lol) bot, but I doubt it. I think I've outgrown this shit.

It's been fun. RIP @assaultwords.

--------------------------------------------------
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

There are a couple other things you can configure, such as tweet frequency, and tweet prefix/postfix. Read the script comments for more info.

The latest version of this script makes use of the Wordfilter Python module. (The original version is still there, tagged with -NOFILTER.) Whatever your personal opinons on MUH FREE SPEECH may be, Twitter has community guidelines in its TOS, and if we want to play in their playground, we need to abide by them and ensure that our bots do not use racist, sexist, ableist, -phobic, or targeting language-- or else we may inadvertently be an asshole to someone, or even find ourselves permabanned. Inside the script, I add a couple of words to the default filter list that I don't want my particular bot tweeting; feel free to revise according to your needs by reviewing the manpage at https://pypi.python.org/pypi/wordfilter.
