"""
Explantion

n &-n returns the rightmost 1 bit in n.

A quick note for people unfamiliar with C-like syntax: the & operator is a bitwise AND. This means taking two numbers and combining them bit-by-bit, producing a 1 only if both inputs are also 1. Here's a quick example:

11010101 
01001100 
-------- 
01000100 

Now, lets look at how negation works with binary numbers. Generally, we store integers like 1 or 2 as 32 or 64 bit numbers. However, for simplicity, lets pretend we're only working with 8 bits--the principles are the same. So 11, for example, would look like:

00001011 

One simple way to do negation is so-called "one's complement". To make a number negative, all we do is flip all the bits. So -11 would be:

11110100 

If this was actually the method we used, then n & -n would always be 0. Since we complemented the number, not a single bit remains unchanged!

However, in reality, we use a slightly different method to do negation: "two's complement". To get -11, we would first flip all the bits and then add 1 to the result. So we would get:

11110101 

Since we added 1 to the previous result, there is always going to be exactly 1 bit that's 1 between both numbers. In this case, it's the rightmost bit, so 11 & -11 is 1. The reason this worked is that we did not have to carry any bits after adding 1 to the complemented number.

Now lets look at 12 and -12. 12 is 00001100; the flipped version is 11110011. If we added 1 to 11110011, we would need to carry twice: 11110100. Now look at how they're anded together:

00001100 
11110100 
-------- 
00000100 

So the result of 12 & -12 is 4, which is the bit we had to carry our addition to. And this is always equal to the rightmost 1 in the positive number!

So this is why n & -n returns the rightmost 1 bit in n. Also note how, thanks to two's complement, the rightmost 1 bit in n is also the rightmost 1 bit in -n.

Similar Tricks

A good source to find similar bit-twiddling tricks is the book Hacker's Delight which contains a bunch of such tricks, varying in complexity, with explanations.

Another option is to write a computer program that searches for efficient bit-twiddling programs like this: a superoptimizer. The Hacker's Delight website actually contains a very simple superoptimizer which it calls "a Hacker's Assistant".

The book has also been a source of benchmarks for new superoptimization systems like STOKE. In some cases, the superoptimizer even managed to find algorithmically distinct programs for the same tasks!


"""


def solution(n):
    return n & -n


print(solution(5))  # 1
print(solution(6))  # 2
print(solution(72))  # 8
