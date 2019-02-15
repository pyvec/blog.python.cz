Title:  PyLadies Snake Workshop
Date: 2019-02-12 00:00:00
Author: Petr Viktorin

> Další příspěvek v angličtině!
> Píšu to pro širší publikum než pro naše obvyklé čtenáře, a nechce se mi to
> překládat :)


On Saturday, February 2, PyLadies Brno organized a “Snake workshop”.

Let me first write a bit about the overall concept.
For info about this specific event, jump to “The Saturday” below.


## PyLadies CZ Beginners' courses

[PyLadies CZ](https://pyladies.cz/) is an informal group of people that (among other things) organize
3-month Python courses for women (mostly beginners).
These courses have been going on for about 5 years in Brno, and have heavily
influenced the workshop, so let me write a bit on how they're organized.

The *organizers* are alumni of past courses – the very people that want to
learn make the courses happen possible.
They coordinate sign-ups, make sure they have a room with internet access,
respond to questions, and so on.

The *lecturer* knows the material deeply and comes to teach.
Often, this is done by external people – often it's my role,
and I'm not a PyLady :)
Thanks to the organizers, the lecturer doesn't need to deal with logistics,
registration or catering, and can focus on transferring knowledge.

And then there are *coaches*, something like teaching assistants – people who
help attendees with individual problems.
These can be experienced programmers, or people who have gone through
the last semester's course and are just a bit ahead.
Most of what the coaches do is trivial: finding mismatched parentheses,
files saved in wrong directories (or not saved at all), or typos.
Since it's perfectly OK for a coach to not know something (they can always
ask someone more experienced), this is a great opportunity for alumni to
see how much they learned since *they* were complete beginners.
And since the role needs no preparation, it's a great way for anyone to give
a few hours back to the community.

The whole thing is free for attendees, volunteer-organized, and budget-less
(companies are happy to provide a venue with internet, and while there are
minor expenses like sticky notes or candy for prizes, they usually aren't
worth the paperwork to get expensed).
It's also fully open – teaching materials are [available] to anyone to go
through or adapt.
This semester, PyLadies CZ are planning to run 7 forks of the beginners' course
in 4 cities (see [pyladies.cz](https://pyladies.cz/)).
Organization in each city is relatively independent.

[available]: https://naucse.python.cz/course/pyladies/

![Beginner PyLadies on the workshop, with coaches in the back]({filename}/images/snake2019-20190202_084911.jpg)


## The Snake workshop

The full-day event we had on Saturday is a relatively new addition to the
“curriculum”.
It's modeled after the very successful [Django Girls](https://djangogirls.org/) workshops, where attendees
who haven't programmed before build a web application (a blog) in just one day.
The Snake workshop has beginners make a *game* ([Snake]) in just one day.

Similarly to Django Girls workshops, the Snake workshop targets complete
beginners – prerequisites are on the level of installing Python, unzipping
an archive or sending an e-mail.

Unlike Django Girls, the Snake workshop tries to make things easier for
everyone: organizers, teachers, and attendees. Specifically:

* There are less technologies to learn: rather than Python, HTML, CSS and
  databases, there's Python and a bit of graphics.
* With a single lecturer rather than small coach-led groups, it's not
  a problem if a coach doesn't show up.
  Also, the coaches can be relative beginners.
  (This format does introduce a single point of failure, though.)

It's still impossible to learn (and remember) programming in a single day,
so the workshop is positioned as a “pilot episode” for a regular 3-month
course.
As a “pilot”, the workshop should serve these purposes:

* Give people an overview of what learning programming looks like – hopefully,
  the message is that it's fun and rewarding, but that it will require lots
  of time.
* Filter out people who'd drop out after the first few lessons of the course.
* Give an overview of Python's the basic data types and building blocks,
  which should be helpful because the 3-month course is “bottom-up” (introduces
  elementary concepts and builds on them), so the “big picture” only reveals
  itself near the end.

[Snake]: https://en.wikipedia.org/wiki/Snake_(video_game_genre)

![See the coaches coaching!]({filename}/images/snake2019-20190202_152819.jpg)


## The Saturday

The last instance of the Snake workshop happened on Saturday, February 2nd.
This was the 4th run so far (after the first trial for PyLadies in
Hradec Králové in March 2018, one for PyLadies Brno in September
2018, and one open for anyone in October 2018).

For this workshop, [Red Hat] provided the venue (Plutonium & Neptunium meeting
rooms in the TPB-C office) and food (of which there was a lot; thank you!).

[Red Hat]: https://www.redhat.com/en/global/czech-republic

I was the lecturer and I handled the Red Hat sponsorship.

We had an almost full house – more than 39 attendees plus 8
coaches/organizers.
(The listed capacity of the rooms is 40, but we fit comfortably.)

We spent the morning (well, until 14:00) explaining basic concepts (numbers,
expressions, strings, functions, conditions, lists, dicts, imports, loops, …)
and the afternoon with the game.
Based on the feedback to date, everyone enjoyed the show.
There were smiles throughout; the coaches were kind and helpful, and I'd say
the attendees learned as much as they could in a day.

![The importance of good ol' pen & paper]({filename}/images/snake2019-20190202_162002.jpg)

Of course, nothing is perfect – and there's a lot to improve for next time.


### What didn't work

I didn't manage time well, and I'd need about 30 more minutes at the end.
Some people were already leaving, so I rushed through the end – which didn't
help either the attendees or the coaches.
(For next time, I already have a plan to shuffle the materials around and
drop 30 minutes of less interesting stuff.)

Also, there was too much food in the end.
We had a generous sponsorship from Red Hat *and* people ordered their own
lunches.
This one is entirely on me as the link between the sponsor and the organizers;
next time I will coordinate better.

Finally, I did not request spare laptops in time.
Usually, Red Hat Regional IT is happy to lend a few out-of-warranty machines,
which are very helpful when some attendee's computer stops working, turns
out to be too slow, or has glitchy graphics.
I forgot to request them in a reasonable time, so we didn't have them.
Thankfully, they weren't needed – but hardware problems could have ruined the
atmosphere of the workshop.

![Not quite there yet]({filename}/images/snake2019-20190202_173055.jpg)


### And as for me...

I think I'm addicted to this workshop.

It ticks the tree factors of intrinsic motivation: autonomy (deciding what
to teach and what to leave out in a time-limited workshop),
mastery (working on something that can always be improved) and purpose (helping
people understand my passion, not to mention the whole “underrepresented
minorities” thing that I'm not really going into here).

I have a hard time interacting with people, and I've found that it's mostly
because I don't think I have anything to say that would be interesting to them.
But that disappears in front of a class, with a clear expectations of what to
explain and a clear level of pre-requisites I can build on.
I know a few introverts who had similar experiences as lecturers/coaches,
and I'd recommend any geek to try teaching an *interested* audience :)

Anyway, I was throroughly exhausted at the end, after ten hours of live coding.
I think I'll wait a few months before doing this again.


![Thanks to the sponsor & organizers]({filename}/images/snake2019-20190202_084946.jpg)

Thank you to everyone involved – the organizers, the coaches,
Red Hat GWS & BIPI, and the attendees.
Let's do more of these!
