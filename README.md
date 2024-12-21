# Advent of Code 2024 journal

**Day 1:**
Not much to say, was an easy routine task.

**Day 2:**
First task was pretty straight forward, but things got a little complecated in the second. My initial idea did not take into account when the first level is wrong, but even after fixing this there was one scenario where a report was misslabeled, took me a while to figure it out, turn out sometimes the wrong level is the one that is before the currently checked one.
The solution itself is not the best, probably not the best runtime.

**Day 3:**
ALWAYS check if you are using the correct input! I wasted so many hours on the part 2 of this task. I created 4 different solutions, neither of them did the job. After a while I realised it didn't provide the correct output because I screwed up at didn't use the proper input... At least the screw up made me learn some regex.

**Day 4:**
Wordsearch. It was a pretty easy task, both parts, just needed some proper input handling and when it was done, it was smooth sailing.

**Day 5:**
I wanted to work with classes on this one so I decided to go for java instead of python. Since I worked with java it took some time to set up the infrastructure for the task, but when it was done, both parts took like 2 minutes. Just checking if a list is ordered and ordering it if it is not.

**Day 6:**
A 2D puzzle, figuring out a guard's patrol path. Part 1 was pretty easy, just simulated the guard's path and got the result. Part 2 on the other hand... I still have no idea how to tackle it so I will leave this for another day since I relly need to catch up on the other days. (Did this task on 20th of Dec)

**Day 7:**
This one took me a bit, the first part just needed some string handling and after I got that one figured out I just solved it with the evaluate function. The second part is not the best solution, actually it was easier without the evaluate function, I wrote my own version of it so it better fit the task, but the algorithm is REALLY slow, it had a 10+ minute runtime, but it provided the correct answer so I'll take it. 

**Day 10:**
This was a nice challange, needed to think it through to get a fairly easy solution, altough it helped that I accidentally solved part2 while trying to solve part1 :D

**Day 11:**
I almost pulled my hair out over this one. Part 1 was easily done with the brute force method, just split the stones 25 times. When it came to part 2 I was surprised to see it only asks me what happens if we blink 75 times. I was like, so I will just replace a 25 with 75 and we are done. Yeeeee, nope. First I tried to find a faster way of calculating the end result, took me a decent amount of time to figure it out. In the process I decided to switch to cpp from python to help with the runtime. It was a good choice in some ways, bad in others. The end code would probably work fine in python as well but would have been much easier to write.
But since I did it in cpp, I had to learn a lot of new things. I used unordered_maps for the first time, I had to figure out how to hash a pair of integers and I also ran into the problem of integer overflowing which I had to solve.
Overall, I probably made it unnecessarily hard, but it was a really good learning experience.

**Day 12:**
Simple, fun challange, part 1 and 2 are similar just needed a different way of calculation. I was able to figure it out fairly quickly.

**Day 13:**
Still in the works, I was able to figure out part 1 quickly, but the second part needs a bit more thinking, I postponed the solution to part 2 to a later day.

**Day 14:**
Part 1 was pretty simple, altough I had some trouble figuring out a bug (basicly an index was 1 off). Part 2 was really interesting, at first I tought "how the hell am I supposed to know how the christmas tree should look like", but I started plotting the robots' positions, first on a tiny 5*5 plot, but that didn't lead to any result, then I tought maybe trying larger plots would help, but I would have had to generate thousands of images so I looked for a better way. I figured out what the average security score for a set of positions were, and if at any given second the security score was off, I plotted those positions. With this approch, the solution was found quickly. Overall, this was a fun challange, had me think differently and I also got some much needed experience using pyplot.

![part-2-solution](https://github.com/user-attachments/assets/6be92b27-fb10-4ec0-a462-5713476d027f)

**Day 15:**
This is my least favourite puzzle so far, it is mostly grunt work, also I made it hair pulling for myself by accidentally using the wrong input for testing, took me half an hour to figure that one out, after that is was smooth sailing with some bugfixes. But with this one, debugging was pretty annoying, lot of indexing, easy to get them wrong in a few places.

**Day 16:**
Holy moly. I spent 6 hours on the 16th on just the first part alone, I did not manage to complete it, I stayed up until 8 a.m. because I was trying to solve the problem. My first try was with a recursive algorithm which got way too convoluted way too quickly. At some point I decided to go to sleep and when I woke up, it just came to me: Do not overcomplicate it you moron! Part 2 in progress...
