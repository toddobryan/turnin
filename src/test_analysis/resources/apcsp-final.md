Bin-1,D
How many different values can be represented by 5 bits?
@
5
@
10
@
25
@
32
@
255
@
5 bits can represent 5^2^ (or 32) different values.
@@Bin-2,B
How do you write 17 as an 8-bit unsigned number?
@
10001000
@
00010001
@
11101111
@
10010001
@
11001100
@
17 = 2^4^ (=16) + 2^0^ (=1), so 00010001.
@@Bin-3,A
In order, how many bits do you need to represent: 0-255 unsigned, -32 to 31 signed, and -8 to 7 signed?
@
8, 6, 4
@
16, 5, 3
@
8, 5, 4
@
16, 8, 4
@
8, 5, 3
@
0-255 is 256 different values, and since 2^8^=256, you need 8 bits. -32 to 31 is 64=2^6^ 
different values, and -8 to 7 is 16=2^4^ different values. So you need 8, 6, and 4 bits.
@@Bin-4,A
What do the _signed_ 8-bit binary numbers `10011000` and `01001000` represent in decimal?
@
-104 and 72
@
25 and 18
@
-103 and 72
@
-104 and 18
@
-18 and 103
@
In signed numbers, the leftmost bit is negative and all the rest are positive.
-128 + 16 + 8 = -104 and 64 + 8 = 72, so -104 and 72.
@@Bin-5,B
How many bytes does the hexadecimal number `A0F2` represent?
@
1
@
2
@
3
@
4
@
5
@
Every hexadecimal digit represents 16 different values (0-9 and A-F), so each
hexadecimal digit is 4 bits. 4 hexadecimal digits is 16 bits, and since each byte
is 8 bits, `A0F2` would be 2 bytes.
@@Bin-6,A
Which of the following is the hexadecimal representation of the binary number `10011100`?
@
`9C`
@
`9B`
@
`39`
@
`156`
@
`-100`
@
Since each hexadecimal digit corresponds to 4 bits, you can convert 4 bits at
a time. `1001` is 8+1=9, and `1100` is 8+4=12. Since `A`=10, `B`=11, `C`=12, etc.,
the equivalent hex number would be `9C`.
@@Bin-7,B
How do you write `-3` as a 4-bit signed number?
@
`1111`
@
`1101`
@
`1011`
@
`1100`
@
`1001`
@
The place values for a 4-bit signed number would be -8, 4, 2, 1. -3 = -8 + 4 + 1,
-3 is `1101`.
@@Bin-8,E
Which of the following decimal numbers _can not_ be exactly represented as a binary floating point number?
@
`0.25`
@
`1.5`
@
`0.125`
@
`21.0`
@
`3.3`
@
In the same way that decimal numbers have 1/10, 1/100, 1/1000, etc., places after
the decimal point, binary numbers have 1/2, 1/4, 1/8, etc., places after the
binary point. A decimal number can only represent fractions exactly if the
denominator is completely divisible by some combination of 2 and 5 (because the 
base 10 is 2 times 5). A binary number can only represent fractions exactly 
if the denominator is a power of 2. `0.25` is 1/4, `1.5` is 3/2, `0.125` is 1/8,
`21.0` is 21/1 (remember, 1 is 2^0^), and `3.3` is 33/10. `3.3` would be a
repeating binary number.
@@Data-1,C
Which of the following will _not_ result in an _overflow error_?
@
Adding `200` and `100` using 8-bit unsigned binary
@
Adding `-5` and `-4` using 4-bit signed binary
@
Subtracting `-3` from `-6` using 4-bit signed binary
@
Adding `5` and `11` using 4-bit unsigned binary
@
Subtracting `3` from `-6` using 4-bit signed binary
@
Remember than an _overflow error_ results when the result of a math operation
can't fit in the number of bits available.

  * `200 + 100 = 300`, but 8 unsigned bits can only store the values `0` to `255`.
  * `-5 + -4 = -9`, but 4 signed bits can only store the values `-8` to `7`.
  * `-6 - (-3) = 3`, which fits. (Yes, that was tricky. Remember that subtracting a negative is the same as adding a positive.)
  * `5 + 11 = 16`, but 4 unsigned bits can only store the values `0` to `15`.
  * `-6 - 3 = -9`, but 4 signed bits can only store the values `-8` to `7`.

@@Data-2,C
Which of the following is probably _not_ the result of _round-off error_?
@
Finding the area of a circle results in a slightly different answer on your and your friend's computer
@
Dividing 1 by 3 results in `0.33333333331` on a calculator
@
Multiplying two very large integers results in an error
@
Squaring a calculator's value for [pi] has wrong digits near the end
@
Multiplying `0.1` by `10` results in `0.9999999999999999`
@
Remember that a _round-off error_ occurs when a binary number can't store the 
exact value of a number, either because it's irrational or because it's a
non-terminating value. Multiplying two integers doesn't involve any fractional
or irrational values, so the error would be an _overflow error_, not a
_round-off error_. All the other answers deal with irrational or non-terminating
(in binary) values.
@@Data-3,AD=1,A=0.5,D=0.5
An elevator in a ten-story building is run by a computer program. Which of the 
following pieces of information could the program represent as a single bit? 
(There is more than one answer to this question.)
@
Whether the _Door Closed_ button has been pressed
@
Which floor is selected
@
Which floors the _UP_ button has been pressed on
@
Whether the _Emergency Call_ button has been pressed
@
Which floor the elevator is on
@
A single bit can only store two values: 0 and 1, on or off, true or false.
Whether the _Door Closed_ or _Emergency Call_ buttons on the elevator have been
pressed are both true or false values. Since there are ten stories in the
building, all the other answers would require a few bits to represent.
@@Data-4,A
In ASCII, one byte of information represents one letter. Which of the following represents `MANUAL` in ASCII?
@
`01001101 01000001 01001110 01010101 01000001 01001100`
@
`01000001 01001101 01001110 01010101 01000001 01001100`
@
`01001100 01001101 01000001 01001110 01010101 01000001`
@
`01001101 01000001 01000001 01010101 01001110 01001100`
@
`01000001 01001110 01010101 01000001 01001100 01001101`
@
You don't need to have memorized ASCII for this problem. Just realize that to
spell `MANUAL`, the second and fifth bytes have to be `A` and so must match.
The only answer where that's the case has `01000001` in the second and fifth spots.
@@Data-5,A
In designing a program to analyze traffic data, a programmer needs to determine
which data is analog so that she can decide how to convert it to digital data.
Which of these is analog data?
@
Each car's location
@
Each car's license plate number
@
Each car's speed to the nearest mile per hour, read by a tower-mounted radar gun
@
The number of occupants of each car
@
Each car's make, model, and year
@
Analog data is continuous, but digital data is discrete--it is broken up into
units that aren't separated into smaller parts. Only the car's location data is
analog--you could keep measuring more and more accurately, basically forever.
Each of the other kinds of data has only a finite number of possible values.
@@Data-6,D
Which of the following is true about the process of converting analog data into digital data?
@
The digital version contains all of the details of the analog data, 
as long as enough storage capacity is available.
@
To make the digital version be a more accurate representation of the analog data,
the process should use fewer bits to represent each sample.
@
A longer interval between measured samples means more details will be captured
in the conversion from analog to digital.
@
The digital version is a representation of the analog data but cannot 
include all of the details.
@
It is possible to recover the analog data from the digital data.
@
When you convert analog data to digital data, you're converting a continuous,
variable stream into a stream of discrete blocks with only a finite number of
possible values. Here's why each answer is right or wrong:

  * "The digital version contains all of the ..." You can never _completely_
    capture analog data, no matter how much storage you have.
  * "To make the digital version..." You should actually use more bits to
    represent each sample if you want the digital version to be more accurate.
  * "A longer interval..." 
    To get more details, use a shorter interval between samples.
  * "The digital version is a representation..." This is exactly right.
  * "It is possible to recover..." Unfortunately, when you convert from analog
    to digital, you lose some data you can never get back.

@@Data-7,C
Which of the following kinds of data must be compressed with a lossless 
compression algorithm to ensure that it's useful?
@
Pictures from a camera phone
@
Audio from a concert
@
Text from a computer program
@
Video from a streaming service
@
Pictures served across the web
@
Lossy compression gives up some details in order to save space. That's not a
problem for pictures and audio, usually, since our brains don't miss the details.
But getting even one character in a computer program wrong could break the
program. You have to compress text for computer programs using lossless
compression.
@@Data-8,B
You want to create a website with photos and are trying to decide whether to
use lossy compression. Which of these is true?
@
Lossy compression algorithms reduce the file size, but they can only
reduce up to 10% of the file size.
@
Lossy compression algorithms reduce the file size, but the compression is
irreversible, so you need to store the original images if you ever want
to display the photos at a higher quality.
@
Lossy compression algorithms reduce the file size, but your users will be 
unhappy because the images will clearly be lower quality.
@
Lossy compression algorithms don't reduce the file size, but they do 
appear to download faster because of some neat tricks.
@
Using lossy compression ensures that users can see the original quality
of the photos you post.
@
Lossy compression gives up some detail in exchange for saving on space.

  * "only reduce up to 10%" is nonsense. You can reduce as much as you want,
    if you're willing to give up detail. (At some point, however, you've
    probably lost all the value.)
  * "but the compression is irreversible" is true. This is the problem with
    lossy compression.
  * "your users will be unhappy" The key word in this answer is "clearly".
    If you try to compress too much, you could make your users unhappy, but
    almost all the images we see on the web have been compressed and most people
    don't care.
  * "don't reduce the file size" is nonsense designed to appeal to conspiracy
    theorists.
  * "users can see the original quality" is exactly what lossy compression
    doesn't do.

@@Data-9,B
Which of the following is true of lossy compression?
@
You can reverse it to produce the original data.
@
You can compress the size as much as you want, as long as you are willing to 
give up more and more detail.
@
It's very useful for important data, like the text of books or medical records.
@
It generally takes up more space than lossless compression.
@
Almost no one uses it.
@
The key idea about lossy compression is that "You can compress the size 
as much as you want, as long as you are willing to give up more and more 
detail." The other answers are true of _lossless_ compression, except the
"Almost no one uses it." one, which isn't true of lossy or lossless compression.
@@Data-10,C
Which of the following is a true statement about copyright and intellectual 
property?
@
When you create something, unless you register it with the copyright office, 
it is in the public domain.
@
The Creative Commons license ensures that other people can not use the 
licenser's content in their own works.
@
It is possible to provide a license that allows people to use content for
non-commercial (not money-making) use, but restricts them from using it 
commercially (to make money).
@
Copyright is permanent. Once an item is copyrighted, it stays copyrighted
forever.
@
All the content on YouTube is in the public domain.
@
The only one of these that is true is that it is possible to create a license
that allows for non-commercial, but not commercial, use. This is exactly what
the Creative Commons and other open source licenses are for. Allowing people
to freely use content, subject to the stipulations of the creator.
@@Data-11,E
A mood-tracking app lets users enter data about how they're feeling. For each 
user report, it includes: user id, timestamp, a rating from 1-10 of their mood, 
and comments. Which of the following can not be determined from the data?
@
Which user posts the most reports
@
Which time of day people tend to be in the best mood
@
The average mood for each user based on their reports
@
Which user writes the most comments
@
The times at which people in a certain country feel the best
@
Nothing about the country the user is in is mentioned in the data reports.
Therefore, it would be impossible to determine the times at which people in a
certain country feel the best.
@@Data-12,BD=1,B=0.5,D=0.5
A "red light camera" is a camera installed at street intersections that records 
whenever a car runs a red light. The camera records two images, one right 
before the car enters the intersection, and one after it's entered the 
intersection. In addition to the images, it records metadata about the incident: 
the date and time, the intersection location, the speed of the car, 
and the seconds elapsed past the light turning red. Which of these questions 
can be better answered by analyzing the metadata instead of the image data? 
(This question has multiple correct answers.)
@
What car models are most associated with running red lights?
@
Which intersections have the greatest number of red light runners?
@
What is the frequency of pedestrians in or near the intersection during an incident?
@
What is the average speed of a car when it runs a red light?
@
Are males or females more likely to run red lights?
@
The metadata is listed and using it we could figure out which intersections have
the greatest number of red light runners, and the average speed when a car runs
a red light. For the other possible answers, we'd have to actually look at the
picture that was taken, and hope that it was clear enough and got enough of the
scene that we could answer the question.
@@Boolean-1,A
For which values of `p` and `q` is `(and p q)` `#true`?
@
`#true` and `#true`
@
`#true` and `#false`
@
`#false` and `#true`
@
`#false` and `#false`
@
`(and b1 b2)` is only `#true` if both `b1` and `b2` are both `#true`.
@@Boolean-2,D
For which values of `p` and `q` is `(or p q)` `#false`?
@
`#true` and `#true`
@
`#true` and `#false`
@
`#false` and `#true`
@
`#false` and `#false`
@
`(or b1 b2)` is only `#false` if `b1` and `b2` are both `#false`.
@@Boolean-3,AB=1,A=0.5,B=0.5
For which values of `x` and `y` is `(<= x y)` `#true`? This question may have 
multiple answers.
@
3, 4
@
2, 2
@
10, 5
@
-1, -5
@
Because `3 <= 4` and `2 <= 2`, "3, 4" and "2, 2" are the correct answers. 10 is 
not less than or equal to 5, and -1 is not less than or equal to -5.
@@Boolean-4,AB=1,A=0.5,B=0.5
For which values of `name` would the expression `(string<=? "Todd" name)` 
be true? This question may have multiple answers.
@
`"Todd"`
@
`"Vedant"`
@
`"Anirudh"`
@
`"Steve"`
@
`"Eduardo"`
@
`string<=?` uses alphabetical order. `(string<=? "Todd" name)` will be `#true` 
if `name` is equal to or comes after `"Todd"`. Since `"Anirudh"`, `"Steve"`, and
`"Eduardo"` come before `"Todd"`, `"Todd"` and `"Vedant"` are the right answers.
@@Cond-1,B
What is the value of the following expression if `age` is `10`, `44`, and `100`?

```racket
(cond
  [(< age 44) "millennial"]
  [(< age 11) "gen-α"]
  [(< age 29) "gen-z"]
  [(< age 78) "boomer"]
  [(< age 59) "gen-x"]
  [else "silent"])
 ```
@
`"gen-α"`, `"gen-x"`, `"silent"`
@
`"millennial"`, `"boomer"`, `"silent"`
@
`"gen-α"`, `"gen-z"`, `"boomer"`
@
`"silent"`, `"millennial"`, `"boomer"`
@
`"gen-α"`, `"boomer"`, `"silent"`
@
Remember that the conditions in the `cond` are checked in order, and we stop when
the first one is `#true`. Since `10 < 44`, the first answer is `"millennial"`.
`44` won't be `#true` until the `"boomer"` line, and `100` will get to the `else`.
@@Cond-2,C
What order should the question-answer pairs appear in for this `cond` expression to provide the correct generation for a given person's age?

```racket
(cond
  [(< age 44) "millennial"] 1
  [(< age 11) "gen-α"]      2
  [(< age 29) "gen-z"]      3
  [(< age 78) "boomer"]     4
  [(< age 59) "gen-x"]      5
  [else "silent"])          6
```
@
1, 2, 3, 4, 5, 6 (as written)
@
6, 5, 4, 3, 2, 1
@
2, 3, 1, 5, 4, 6
@
6, 4, 5, 1, 3, 2
@
1, 3, 5, 2, 4, 6
@
Since the `cond` conditions are checked in order, you have to make sure that no
earlier condition catches a value some other condition should catch. In this case,
you'd want the age checks arranged from smallest to largest, since we're using `<`.
(If we were using `>`, we'd have to arrange them from largest to smallest.) So,
the order of the lines should be `11`, `29`, `44`, `59`, `78`. Also, `else` always
has to be the last line, so you could eliminate any answer where 6 wasn't the last
line. The correct order is 2, 3, 1, 5, 4, 6.
@@Def-1,A
Which of the following is the correct way to translate f(x) = x^2^ - 4 into Racket?
@
```racket
(define (f x)
  (- (expt x 2) 4))
```
@
```racket
(define f(x)
  (- (expt x 2) 4))
```
@
```racket
(define (f x)
  (- (expt 2 x) 4))
```
@
```racket
(define (f x)
  (- 4 (expt 2 x)))
```
@
```racket
(define f(x)
  x^2 - 4)
```
@
This question makes you look for the differences between the answers.
Get rid of the two answers that have `f(x)` instead of `(f x)`. The other two
wrong ones are equivalent to 4-2^x^ and 2^x^-4. The correct answer is x^2^,
which is written `(expt x 2)` in Racket.
@@Def-2,BC=1,B=0.5,C=0.5
Which line(s) contain mistakes, either in style or correctness. This question may have multiple answers.

```racket
1. ;; min: number number -> number
2. ;; consumes two numbers
3. ;; produces the minimum number
4. (define (min a b)
     (cond
5.     [(< a b) a]
       [else b]))
```
@
1
@
2
@
3
@
4
@
5
@
The `consumes` and `produces` lines are both missing colons.
@@Def-3,A=1,AE=1
Which line(s) contain mistakes, either in style or correctness. This question may have multiple answers.

```racket
1. (define required-height 163)

2. ;; tall?: number -> boolean
3. ;; consumes: a person's height in cm
4. ;; produces: whether they're tall enough to ride a ride
5. (define (tall? height)
     (>= height required-height))
```
@
1
@
2
@
3
@
4
@
5
@
Constants should be written in `ALL_CAPS`, so line 1 should be 
`(define REQUIRED-HEIGHT 163)`. If you picked line 1 or lines 1 and 5, you get
full credit. (Since this question didn't say there were multiple answers,
picking line 5 only isn't right, since the real problem is in line 1.)
@@Types-1,A
What is the type of the expression `-3`? (This question has one or two correct answers)
@
`number`
@
`string`
@
`image`
@
`boolean`
@
`color`
@
`-3` is a `number`.
@@Types-2,BE=1,B=0.5,E=0.5
What is the type of the expression `"red"`? (This question has one or two correct answers)
@
`number`
@
`string`
@
`image`
@
`boolean`
@
`color`
@
`"red"` can be used as a `"color"` or a `"string"`.
@@Types-3,B
What is the type of the expression `"true"`? (This question has one or two correct answers)
@
`number`
@
`string`
@
`image`
@
`boolean`
@
`color`
@
Trick question. `#true` is a `boolean`. `"true"` is a `string`.
@@Types-4,D
What is the type of the expression `(< 3 4)`? (This question has one or two correct answers)
@
`number`
@
`string`
@
`image`
@
`boolean`
@
`color`
@
`(< 3 4)` is `#true`. This is a `boolean`.
@@Types-5,C
What is the type of the expression `(circle 15 "solid" "blue")`? (This question has one or two correct answers)
@
`number`
@
`string`
@
`image`
@
`boolean`
@
`color`
@
When this expression is evaluated, you get an `image`.
@@Design-1,C
What are the steps of the design recipe in the order that you _do_ them?

```
1. Header/Skeleton
2. Test Cases
3. Contract
4. Body
5. Run/Test
6. Purpose
```
@
1, 2, 3, 4, 5, 6
@
2, 3, 4, 5, 6, 1
@
3, 1, 6, 2, 4, 5
@
3, 6, 1, 4, 2, 5
@
3, 4, 1, 2, 5, 6
@
Contract (3), Header/Skeleton (1), Purpose (6); Test Cases (2); 
Body (4); Run/Test (5)
@@Design-2,B
What are the steps of the design recipe in the order that they _appear_ in the editor?

```
1. Header/Skeleton
2. Test Cases
3. Contract
4. Body
5. Run/Test
6. Purpose
```
@
1, 2, 3, 4, 6
@
3, 6, 1, 4, 2
@
3, 1, 6, 2, 4
@
3, 6, 1, 2, 4
@
6, 3, 1, 4, 2
@
Contract (3), Purpose (6), Header/Skeleton (1), Body (4), Test Cases (2). You
can't see Run/Test in DrRacket, you just press the Run button.
@@Design-3,A
Consider this template of a Racket function. Which numbered part represents 
the function's name?

```
;; __1__: __2__ -> __3__
;; consumes: __4__
;; produces: __5__
(define (__1__ __6__)
  ___7___)

(check-expect (__1__ __8__) __9__)
```
@
1
@
2
@
4
@
6
@
9
@
The function's name shows up at the beginning of the contract and the header and
is the function that gets called in all the test cases. That's number 1.
@@Design-4,B
Consider this template of a Racket function. Which numbered part represents the 
types of the arguments the function consumes?

```
;; __1__: __2__ -> __3__
;; consumes: __4__
;; produces: __5__
(define (__1__ __6__)
___7___)

(check-expect (__1__ __8__) __9__)
```
@
1
@
2
@
4
@
6
@
9
@
The types of the arguments (also called parameters) that the function consumes
show up in the contract before the arrow. That's number 2.
@@Design-5,C
Consider this template of a Racket function. Which numbered part represents 
the return type of the function?

```
;; __1__: __2__ -> __3__
;; consumes: __4__
;; produces: __5__
(define (__1__ __6__)
  ___7___)

(check-expect (__1__ __8__) __9__)
```
@
1
@
2
@
3
@
6
@
7
@
The function's return type appears after the arrow in the contract.
That's number 3.
@@Design-6,D
Consider this template of a Racket function. Which numbered part represents 
the example arguments you call the function with to test it?

```
;; __1__: __2__ -> __3__
;; consumes: __4__
;; produces: __5__
(define (__1__ __6__)
  ___7___)

(check-expect (__1__ __8__) __9__)
```
@
5
@
6
@
7
@
8
@
9
@
In each `check-expect`, you write 
`(check-expect (function-to-test args ...) expected-value)`. Number 8 is where
those arguments you're using to test the function go.
@@Racket-1,C
Which of the following is the correct way to translate `2 + 3 · 4 - 5` to Racket?
@
`(+ (- 2 (* 3 4)) 5)`
@
`(+ (- 2 (* 3 4)) 5)`
@
`(- (+ 2 (* 3 4)) 5)`
@
`(- (* (+ 2 3) 4) 5)`
@
`(- (* 2 (+ 3 4)) 5)`
@
Fully parenthesizing `((2 + (3 · 4)) - 5)` according to order of operations and
then moving each operator to the beginning of its closest parentheses (and
changing the dot to `*`) gives us `(- (+ 2 (* 3 4)) 5)`.
@@Image-1,A
`(flip-vertical (beside WITCH WITCH WITCH))`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Three witches beside each other, but flipped top to bottom, so the head is down
and the broom is up. (You can tell the difference between `flip-vertical` and 
`rotate-180` because in `rotate-180` the left and right sides switch. In other
words, the back of the witch's broom would be on the right in `rotate-180`, but
stay on the left with `flip-vertical`.)
@@Image-2,C
`(beside WITCH WITCH WITCH)`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Three witches beside each other.
@@Image-3,B
`(beside (above WITCH WITCH) WITCH)`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Two witches above each other on the left, with a single witch beside them. The
key here is that there's no `align`, so the witch on the right will be centered
vertically with respect to the witches on the left.
@@Image-4,C
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Three witches, each rotated 45 degrees clockwise, on top of each other.
@@Image-5,E
`(above WITCH (beside WITCH WITCH))`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
A witch on top of two witches. Because there's no `align`, the witch on top will
be centered between the two witches under it.
@@Image-6,B
`(rotate -45 (beside WITCH WITCH WITCH))`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Three witches next to each other, but then the whole row is rotated 45 degrees
clockwise.
@@Image-7,D
`(rotate-cw (above WITCH WITCH WITCH))`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Three witches on top of each other, but then the whole picture is rotated 90 degrees
clockwise. That means the witches will be facing down.
@@Image-8,D
`(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Three witches next to each other, but each one has been flipped left-to-right.
@@Image-9,E
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))`
@
`(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
@
`(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
@
`(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
@
`(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
@
`(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
@
Three witches next to each other, but each one has been rotated 90 degrees
counter-clockwise.
