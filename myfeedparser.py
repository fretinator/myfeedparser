#! /usr/bin/python

import feedparser

feeds = {
		'http://www.reddit.com/r/python/.rss',
		'http://www.buzzfeed.com/tech.xml',
		'http://rss.cnn.com/rss/cnn_topstories.rss',
		'http://rss.slashdot.org/Slashdot/slashdot',
		'http://feeds.christianitytoday.com/christianitytoday/ctmag'
}

myItems = []

for feed in feeds:
	d = feedparser.parse(feed);

	# Try to get date the current feed was built

	print("--------------------------------")
	print("Reading " + d.feed.title + "...")
	#print d.feed.subtitle
	print("--------------------------------")

	for post in d.entries:
		if not(hasattr(post, 'updated')) and hasattr(d, 'lastBuildDate'):
			post['updated'] = d['lastBuildDate']

		myItems.append(post)

myItems.sort(reverse=True, key=lambda item: item.updated if hasattr(item, 'updated') else "zzzzzzzz")

for item in myItems:
	print(item.title)
	print(item.link)
	if hasattr(item, 'updated'):
		print(item.updated + "\n")
	else:
		print("Unknown update time\n")
