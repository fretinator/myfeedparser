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

	print "--------------------------------"
	print "Reading " + d.feed.title + "..."
	#print d.feed.subtitle
	print "--------------------------------"

	for post in d.entries:
		#print post.title
		#print post.link 
		#print post.updated
		#print post.updated_parsed + "\n"
		myItems.append(post)

myItems.sort(reverse=True, key=lambda item: item.updated_parsed if hasattr(item, 'updated_parsed') else "zzzzzzzz")

for item in myItems:
	print item.title
	print item.link
	if hasattr(item, 'updated'):
		print item.updated + "\n"
	else:
		print "Unknown update time"
