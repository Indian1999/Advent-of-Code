#Advent of Code 2024 journal

**Day 1:**
Not much to say, was an easy routine task.

**Day 2:**
First task was pretty straight forward, but things got a little complecated in the second. My initial idea did not take into account when the first level is wrong, but even after fixing this there was one scenario where a report was misslabeled, took me a while to figure it out, turn out sometimes the wrong level is the one that is before the currently checked one.
The solution itself is not the best, probably not the best runtime.

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
