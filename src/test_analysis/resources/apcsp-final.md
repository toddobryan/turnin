Bin-1
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
D
@@Bin-2
How do you write 17 as an 8 bit unsigned number?
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
B
@@Bin-3
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
A
@@Bin-4
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
A
@@Bin-5
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
B
@@Bin-6
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
A
@@Bin-7
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
B
@@Bin-8
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
E
@@Data-1
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
C
@@Data-2
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
C
@@Data-3
An elevator in a ten-story building is run by a computer program. Which of the following pieces of information could the program represent as a single bit? (There is more than one answer to this question.)
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
A,D
@@Data-4
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
A
@@Data-5
In designing a program to analyze traffic data, a programmer needs to determine which data is analog so that she can decide how to convert it to digital data. Which of these is analog data?
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
A
@@Data-6
Which of the following is true about the process of converting analog data into digital data?
@
The digital version contains all of the details of the analog data, as long as enough storage capacity is available.
@
To make the digital version be a more accurate representation of the analog data, the process should use fewer bits to represent each sample.
@
A longer interval between measured samples means more details will be captured in the conversion from analog to digital.
@
The digital version is a representation of the analog data but cannot include all of the details.
@
It is possible to recover the analog data from the digital data.
@
D
@@Data-7
Which of the following kinds of data must be compressed with a lossless compression algorithm to ensure that it's useful?
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
C
@@Data-8
You want to create a website with photos and are trying to decide whether to use lossy compression. Which of these is true?
@
Lossy compression algorithms reduce the file size, but they can only reduce up to 10% of the file size.
@
Lossy compression algorithms reduce the file size, but the compression is irreversible, so you need to store the original images if you ever want to display the photos at a higher quality.
@
Lossy compression algorithms reduce the file size, but your users will be unhappy because the images will clearly be lower quality.
@
Lossy compression algorithms don't reduce the file size, but they do appear to download faster because of some neat tricks.
@
Using lossy compression ensures that users can see the original quality of the photos you post.
@
B
@@Data-9
Which of the following is true of lossy compression?
@
You can reverse it to produce the original data?
@
You can compress the size as much as you want, as long as you are willing to give up more and more detail.
@
It's very useful for important data, like the text of books or medical records.
@
It generally takes up more space than lossless compression.
@
Almost no one uses it.
@
B
@@Data-10
Which of the following is a true statement about copyright and intellectual property?
@
When you create something, unless you register it with the copyright office, it is in the public domain.
@
The Creative Commons license ensures that other people can not use the licenser's content in their own works.
@
It is possible to provide a license that allows people to use content for non-commercial (not money-making) use, but restricts them from using it commercially (to make money).
@
Copyright is permanent. Once an item is copyrighted, it stays copyrighted forever.
@
All the content on YouTube is in the public domain.
@
C
@@Data-11
A mood-tracking app lets users enter data about how they're feeling. For each user report, it includes: user id, timestamp, a rating from 1-10 of their mood, and comments. Which of the following can not be determined from the data?
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
E
@@Data-12
A "red light camera" is a camera installed at street intersections that records whenever a car runs a red light. The camera records two images, one right before the car enters the intersection, and one after it's entered the intersection. In addition to the images, it records metadata about the incident: the date and time, the intersection location, the speed of the car, and the seconds elapsed past the light turning red. Which of these questions can be better answered by analyzing the metadata instead of the image data? (This question has multiple correct answers.)
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
B,D
@@Boolean-1
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
A
@@Boolean-2
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
D
@@Boolean-3
For which value of `x` and `y` is `(<= x y)` `#true`? This question may have multiple answers.
@
3, 4
@
2, 2
@
10, 5
@
-1, -5
@
A,B
@@Boolean-4
For which values of `name` would the expression `(string<=? "Todd" name)` be true? This question may have multiple answers.
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
A,B
@@Cond-1
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
B
@@Cond-2
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
C
@@Def-1
Which of the following is the correct way to translate f(x) = x[^2^] - 4 into Racket?
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
A
@@Def-2
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
B,C
@@Def-3
Which line(s) contain mistakes, either in style or correctness. This question may have multiple answers.
```racket
1. (define required-height 163)

2. ;; tall?: number -> boolean
3. ;; consumes: a person's height in cm
4. ;; produces: whether they're tall enough to ride a ride
   (define (tall? height)
5.   (>= height required-height))
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
A
@@Types-1
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
A
@@Types-2
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
B,E
@@Types-3
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
B
@@Types-4
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
D
@@Types-5
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
C
@@Design-1
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
C
@@Design-2
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
C
@@Design-3
Consider this template of a Racket function. Which numbered part represents the function's name?

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
A
@@Design-4
Consider this template of a Racket function. Which numbered part represents the types of the arguments the function consumes?

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
B
@@Design-5
Consider this template of a Racket function. Which numbered part represents the return type of the function?
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
C
@@Design-6
Consider this template of a Racket function. Which numbered part represents the example arguments you call the function with to test it?
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
D
@@Racket-1
Which of the following is the correct way to translate `2 + 3 · 4 - 5` to Racket?
@
`(- (+ 2 (* 3 4)) 5)`
@
`(+ (- 2 (* 3 4)) 5)`
@
`(- (* (+ 2 3) 4) 5)`
@
`(- (* 2 (+ 3 4)) 5)``
@
A
@@Image-1
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
A
@@Image-2
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
C
@@Image-3
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
B
@@Image-4
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
C
@@Image-5
`(above WITCH (beside WITCH WITCH))]
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
E
@@Image-6
`(rotate -45 (beside WITCH WITCH WITCH))]
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
B
@@Image-7
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
D
@@Image-8
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
D
@@Image-9
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
E

