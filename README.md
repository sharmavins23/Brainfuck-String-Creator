# Brainfuck String Creator

This project takes in a string and generates the required Brainfuck code to
print that string out.

It's important to note that there are little to no optimizations within the
actual generated Brainfuck code; The generator sacrifices compile time largely
to increase memory space to an extreme amount. There are some optimizations on
string length via looping for simplicity, however.

Special thanks to [pocmo](https://github.com/pocmo/) for the
[Python-Brainfuck](https://github.com/pocmo/Python-Brainfuck) interpretor.

## Why?

Why not?

## How?

The naive implementation was to simply convert the ASCII value to the
corresponding decimal values, and concatenate a series of increment, print, and
decrement instructions to print out words. Needless to say, this is absurdly
complicated to read, and ended up in extremely large code.

The simpler solution is to iterate and generate words. Generally, this would be
done easiest by finding a common factor between characters and generating a word
using one singular loop. However, the solution I've opted to implement is to
simply generate the code for each character separately. This results in every
character being comprised of the follows:

```bf
+a+[>++++++++++<-]+b+   Increment a series of counters for the number
.<                      Print the byte, and shift back to the counter
+a+[>----------<-]-b-   Decrement a series of counters for the number.
```

In this example, `a` and `b` represent the number of repetitions of the
surrounding characters. For calculating `a` and `b`, one can simply use the
following:

```py
a = num // 10
b = num %  10
```

This generates the individual characters, and the code for multiple characters
can simply be concatenated. No, this is NOT the most optimal way of writing
Brainfuck code, and it's not even close. It's simply a way that one can
streamline the procedure.

# License TL;DR

This project is distributed under the MIT license. This is a paraphrasing of a
[short summary](https://tldrlegal.com/license/mit-license).

This license is a short, permissive software license. Basically, you can do
whatever you want with this software, as long as you include the original
copyright and license notice in any copy of this software/source.

## What you CAN do:

-   You may commercially use this project in any way, and profit off it or the
    code included in any way;
-   You may modify or make changes to this project in any way;
-   You may distribute this project, the compiled code, or its source in any
    way;
-   You may incorporate this work into something that has a more restrictive
    license in any way;
-   And you may use the work for private use.

## What you CANNOT do:

-   You may not hold me (the author) liable for anything that happens to this
    code as well as anything that this code accomplishes. The work is provided
    as-is.

## What you MUST do:

-   You must include the copyright notice in all copies or substantial uses of
    the work;
-   You must include the license notice in all copies or substantial uses of the
    work.

If you're feeling generous, give credit to me somewhere in your projects.
