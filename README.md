# Quick Track

Quick track is a _very_ quick and dirty scripted utility to ease the ability to check the location of a registered SPOT beacon using their APIs (particularly because I routinely lose the URL to view it manually). This script can be run via an AWS Lambda on a schedule, and updates are sent out via AWS SNS. 

The script relies on the existence of three additional files that should be located in the same directory (but are for obvs reasons not being included):

* **FEED_ID.txt** - this is the ID of the SPOT beacon and can be found in the SPOT map url
* **static_shortened.txt** - this file contains the link to SPOT on the map on their site. This file (and `shortened` in track.py) aren't necessary if you don't want to send out a map link in each text message
* **arn.txt** - this file contains the ARN of the SNS topic. Ensure that numbers that want to receive a text message from it are subscribed to the topic 

Ensure that you have a CloudWatch event set to trigger the lambda at whatever interval you desire. 

Lastly, also keep in mind that SPOT has a rate limit on how many times they allow API calls for a particular device. At the time of writing, you shouldn't be setting Quick Track up to run at intervals of less than 2.5 minutes. 

Feel free to modify and reuse as necessary - I'm releasing under a GNU GPL v3.0. I release this without warranty of any kind and under limited liability - you're liable for however you use it and whatever comes about from its use. 

Feel free to reach out if you have questions or improvements - I can be reached on Twitter via [@therealvdw](https://twitter.com/therealvdw). 

P.S. Quick Track was made to keep tabs on this guy: 

![#3spooky5me](spooky.png)
