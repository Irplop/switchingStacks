# switchingStacks


Given two equal piles of balls A and B of size c

Remove a random number of balls from A
Remove a (different) random number of balls from B
Put the balls removed from A into B
Put the balls removed from B into A

Repeat this until the piles are equal again

How many times on average do you have to do this to get equal again?

NOTE: the random number removed can be all of the balls or no balls


I have run the simulation of this many times (4 million).  The ratio of starting size c to iterations seems to be around 1.35

Where is this number coming from?  How can I derive this number? 

I tried using markov chains but I don't know enough about them to utilize them.  Also I'm not sure if they are appropriate since there is a final state.

My actuary friend says I should look into the geometric distribution but I'm not sure how to apply it since the sizes change.

I simulated a stack of c = 4:

--

Using Absorbing Markov Chains I got absolute values for c= 2 to 100

To get my final answer, I got the numerator and denominator of the answer and then plugged the sequences into wolfram alpha to get the closed form
