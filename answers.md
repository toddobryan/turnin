1. (Bin-1, v1=33, v2=18) Correct: v1: C; v2: D\
   How many different values can be represented by 5 bits?
     * v1=B,v2=E. 5
     * v1=E,v2=B. 10
     * v1=A,v2=C. 25
     * v1=C,v2=D. 32
     * v1=D,v2=A. 255

2. (Bin-2, v1=34, v2=12) Correct: v1: E; v2: B\
   How do you write 17 as an 8-bit unsigned number?
     * v1=D,v2=A. 10001000
     * v1=E,v2=B. 00010001
     * v1=A,v2=E. 11101111
     * v1=B,v2=C. 10010001
     * v1=C,v2=D. 11001100

3. (Bin-3, v1=11, v2=27) Correct: v1: B; v2: D\
   In order, how many bits do you need to represent: 0-255 unsigned, -32 to 31 signed, and -8 to 7 signed?
     * v1=B,v2=D. 8, 6, 4
     * v1=D,v2=C. 16, 5, 3
     * v1=A,v2=B. 8, 5, 4
     * v1=C,v2=E. 16, 8, 4
     * v1=E,v2=A. 8, 5, 3

4. (Bin-4, v1=5, v2=14) Correct: v1: E; v2: C\
   What do the _signed_ 8-bit binary numbers `10011000` and `01001000` represent in decimal?
     * v1=E,v2=C. -104 and 72
     * v1=A,v2=B. 25 and 18
     * v1=C,v2=A. -103 and 72
     * v1=D,v2=D. -104 and 18
     * v1=B,v2=E. -18 and 103

5. (Bin-5, v1=16, v2=5) Correct: v1: E; v2: C\
   How many bytes does the hexadecimal number `A0F2` represent?
     * v1=A,v2=D. 1
     * v1=E,v2=C. 2
     * v1=B,v2=B. 3
     * v1=C,v2=E. 4
     * v1=D,v2=A. 5

6. (Bin-6, v1=40, v2=21) Correct: v1: D; v2: C\
   Which of the following is the hexadecimal representation of the binary number `10011100`?
     * v1=D,v2=C. `9C`
     * v1=A,v2=A. `9B`
     * v1=B,v2=B. `39`
     * v1=E,v2=E. `156`
     * v1=C,v2=D. `-100`

7. (Bin-7, v1=22, v2=38) Correct: v1: B; v2: C\
   How do you write `-3` as a 4-bit signed number?
     * v1=D,v2=B. `1111`
     * v1=B,v2=C. `1101`
     * v1=C,v2=A. `1011`
     * v1=A,v2=D. `1100`
     * v1=E,v2=E. `1001`

8. (Bin-8, v1=27, v2=10) Correct: v1: B; v2: D\
   Which of the following decimal numbers _can not_ be exactly represented as a binary floating point number?
     * v1=E,v2=E. `0.25`
     * v1=A,v2=A. `1.5`
     * v1=C,v2=B. `0.125`
     * v1=D,v2=C. `21.0`
     * v1=B,v2=D. `3.3`

9. (Data-1, v1=24, v2=13) Correct: v1: E; v2: C\
   Which of the following will _not_ result in an _overflow error_?
     * v1=C,v2=D. Adding `200` and `100` using 8-bit unsigned binary
     * v1=D,v2=A. Adding `-5` and `-4` using 4-bit signed binary
     * v1=E,v2=C. Subtracting `-3` from `-6` using 4-bit signed binary
     * v1=A,v2=E. Adding `5` and `11` using 4-bit unsigned binary
     * v1=B,v2=B. Subtracting `3` from `-6` using 4-bit signed binary

10. (Data-2, v1=4, v2=31) Correct: v1: A; v2: C\
    Which of the following is probably _not_ the result of _round-off error_?
      * v1=B,v2=E. Finding the area of a circle results in a slightly different answer on your and your friend's computer
      * v1=C,v2=D. Dividing 1 by 3 results in `0.33333333331` on a calculator
      * v1=A,v2=C. Multiplying two very large integers results in an error
      * v1=D,v2=B. Squaring a calculator's value for [pi] has wrong digits near the end
      * v1=E,v2=A. Multiplying `0.1` by `10` results in `0.9999999999999999`

11. (Data-3, v1=28, v2=19) Correct: v1: AD,A=1/2,D=1/2; v2: AE,E=1/2,A=1/2\
    An elevator in a ten-story building is run by a computer program. Which of the 
    following pieces of information could the program represent as a single bit? 
    (There is more than one answer to this question.)
      * v1=A,v2=E. Whether the _Door Closed_ button has been pressed
      * v1=C,v2=B. Which floor is selected
      * v1=B,v2=D. Which floors the _UP_ button has been pressed on
      * v1=D,v2=A. Whether the _Emergency Call_ button has been pressed
      * v1=E,v2=C. Which floor the elevator is on

12. (Data-4, v1=38, v2=2) Correct: v1: D; v2: E\
    In ASCII, one byte of information represents one letter. Which of the following represents `MANUAL` in ASCII?
      * v1=D,v2=E. `01001101 01000001 01001110 01010101 01000001 01001100`
      * v1=C,v2=C. `01000001 01001101 01001110 01010101 01000001 01001100`
      * v1=E,v2=D. `01001100 01001101 01000001 01001110 01010101 01000001`
      * v1=B,v2=B. `01001101 01000001 01000001 01010101 01001110 01001100`
      * v1=A,v2=A. `01000001 01001110 01010101 01000001 01001100 01001101`

13. (Data-5, v1=3, v2=25) Correct: v1: D; v2: C\
    In designing a program to analyze traffic data, a programmer needs to determine
    which data is analog so that she can decide how to convert it to digital data.
    Which of these is analog data?
      * v1=D,v2=C. Each car's location
      * v1=E,v2=A. Each car's license plate number
      * v1=B,v2=B. Each car's speed to the nearest mile per hour, read by a tower-mounted radar gun
      * v1=A,v2=E. The number of occupants of each car
      * v1=C,v2=D. Each car's make, model, and year

14. (Data-6, v1=32, v2=35) Correct: v1: E; v2: C\
    Which of the following is true about the process of converting analog data into digital data?
      * v1=A,v2=B. The digital version contains all of the details of the analog data, 
      as long as enough storage capacity is available.
      * v1=C,v2=D. To make the digital version be a more accurate representation of the analog data,
      the process should use fewer bits to represent each sample.
      * v1=D,v2=E. A longer interval between measured samples means more details will be captured
      in the conversion from analog to digital.
      * v1=E,v2=C. The digital version is a representation of the analog data but cannot 
      include all of the details.
      * v1=B,v2=A. It is possible to recover the analog data from the digital data.

15. (Data-7, v1=20, v2=20) Correct: v1: D; v2: B\
    Which of the following kinds of data must be compressed with a lossless 
    compression algorithm to ensure that it's useful?
      * v1=A,v2=C. Pictures from a camera phone
      * v1=C,v2=D. Audio from a concert
      * v1=D,v2=B. Text from a computer program
      * v1=B,v2=E. Video from a streaming service
      * v1=E,v2=A. Pictures served across the web

16. (Data-8, v1=39, v2=3) Correct: v1: D; v2: E\
    You want to create a website with photos and are trying to decide whether to
    use lossy compression. Which of these is true?
      * v1=E,v2=A. Lossy compression algorithms reduce the file size, but they can only
      reduce up to 10% of the file size.
      * v1=D,v2=E. Lossy compression algorithms reduce the file size, but the compression is
      irreversible, so you need to store the original images if you ever want
      to display the photos at a higher quality.
      * v1=B,v2=B. Lossy compression algorithms reduce the file size, but your users will be 
      unhappy because the images will clearly be lower quality.
      * v1=A,v2=C. Lossy compression algorithms don't reduce the file size, but they do 
      appear to download faster because of some neat tricks.
      * v1=C,v2=D. Using lossy compression ensures that users can see the original quality
      of the photos you post.

17. (Data-9, v1=8, v2=7) Correct: v1: A; v2: A\
    Which of the following is true of lossy compression?
      * v1=B,v2=D. You can reverse it to produce the original data.
      * v1=A,v2=A. You can compress the size as much as you want, as long as you are willing to 
      give up more and more detail.
      * v1=D,v2=E. It's very useful for important data, like the text of books or medical records.
      * v1=E,v2=C. It generally takes up more space than lossless compression.
      * v1=C,v2=B. Almost no one uses it.

18. (Data-10, v1=35, v2=26) Correct: v1: D; v2: D\
    Which of the following is a true statement about copyright and intellectual 
    property?
      * v1=A,v2=E. When you create something, unless you register it with the copyright office, 
      it is in the public domain.
      * v1=E,v2=C. The Creative Commons license ensures that other people can not use the 
      licenser's content in their own works.
      * v1=D,v2=D. It is possible to provide a license that allows people to use content for
      non-commercial (not money-making) use, but restricts them from using it 
      commercially (to make money).
      * v1=B,v2=A. Copyright is permanent. Once an item is copyrighted, it stays copyrighted
      forever.
      * v1=C,v2=B. All the content on YouTube is in the public domain.

19. (Data-11, v1=12, v2=41) Correct: v1: D; v2: E\
    A mood-tracking app lets users enter data about how they're feeling. For each 
    user report, it includes: user id, timestamp, a rating from 1-10 of their mood, 
    and comments. Which of the following can not be determined from the data?
      * v1=A,v2=C. Which user posts the most reports
      * v1=C,v2=A. Which time of day people tend to be in the best mood
      * v1=E,v2=D. The average mood for each user based on their reports
      * v1=B,v2=B. Which user writes the most comments
      * v1=D,v2=E. The times at which people in a certain country feel the best

20. (Data-12, v1=6, v2=33) Correct: v1: AC,C=1/2,A=1/2; v2: AE,A=1/2,E=1/2\
    A "red light camera" is a camera installed at street intersections that records 
    whenever a car runs a red light. The camera records two images, one right 
    before the car enters the intersection, and one after it's entered the 
    intersection. In addition to the images, it records metadata about the incident: 
    the date and time, the intersection location, the speed of the car, 
    and the seconds elapsed past the light turning red. Which of these questions 
    can be better answered by analyzing the metadata instead of the image data? 
    (This question has multiple correct answers.)
      * v1=D,v2=B. What car models are most associated with running red lights?
      * v1=C,v2=A. Which intersections have the greatest number of red light runners?
      * v1=B,v2=D. What is the frequency of pedestrians in or near the intersection during an incident?
      * v1=A,v2=E. What is the average speed of a car when it runs a red light?
      * v1=E,v2=C. Are males or females more likely to run red lights?

21. (Boolean-1, v1=30, v2=30) Correct: v1: B; v2: A\
    For which values of `p` and `q` is `(and p q)` `#true`?
      * v1=B,v2=A. `#true` and `#true`
      * v1=A,v2=C. `#true` and `#false`
      * v1=C,v2=D. `#false` and `#true`
      * v1=D,v2=B. `#false` and `#false`

22. (Boolean-2, v1=29, v2=36) Correct: v1: D; v2: A\
    For which values of `p` and `q` is `(or p q)` `#false`?
      * v1=B,v2=C. `#true` and `#true`
      * v1=C,v2=D. `#true` and `#false`
      * v1=A,v2=B. `#false` and `#true`
      * v1=D,v2=A. `#false` and `#false`

23. (Boolean-3, v1=14, v2=32) Correct: v1: CD,C=1/2,D=1/2; v2: BD,D=1/2,B=1/2\
    For which values of `x` and `y` is `(<= x y)` `#true`? This question may have 
    multiple answers.
      * v1=C,v2=D. 3, 4
      * v1=D,v2=B. 2, 2
      * v1=A,v2=A. 10, 5
      * v1=B,v2=C. -1, -5

24. (Boolean-4, v1=1, v2=15) Correct: v1: CE,C=1/2,E=1/2; v2: DE,E=1/2,D=1/2\
    For which values of `name` would the expression `(string<=? "Todd" name)` 
    be true? This question may have multiple answers.
      * v1=C,v2=E. `"Todd"`
      * v1=E,v2=D. `"Vedant"`
      * v1=A,v2=B. `"Anirudh"`
      * v1=D,v2=A. `"Steve"`
      * v1=B,v2=C. `"Eduardo"`

25. (Cond-1, v1=41, v2=17) Correct: v1: E; v2: B\
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
      * v1=C,v2=D. `"gen-α"`, `"gen-x"`, `"silent"`
      * v1=E,v2=B. `"millennial"`, `"boomer"`, `"silent"`
      * v1=A,v2=E. `"gen-α"`, `"gen-z"`, `"boomer"`
      * v1=D,v2=A. `"silent"`, `"millennial"`, `"boomer"`
      * v1=B,v2=C. `"gen-α"`, `"boomer"`, `"silent"`

26. (Cond-2, v1=18, v2=9) Correct: v1: C; v2: A\
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
      * v1=D,v2=C. 1, 2, 3, 4, 5, 6 (as written)
      * v1=B,v2=B. 6, 5, 4, 3, 2, 1
      * v1=C,v2=A. 2, 3, 1, 5, 4, 6
      * v1=A,v2=E. 6, 4, 5, 1, 3, 2
      * v1=E,v2=D. 1, 3, 5, 2, 4, 6

27. (Def-1, v1=19, v2=24) Correct: v1: B; v2: C\
    Which of the following is the correct way to translate f(x) = x^2^ - 4 into Racket?
      * v1=B,v2=C. 
      ```racket
      (define (f x)
        (- (expt x 2) 4))
      ```
      * v1=E,v2=B. 
      ```racket
      (define f(x)
        (- (expt x 2) 4))
      ```
      * v1=D,v2=A. 
      ```racket
      (define (f x)
        (- (expt 2 x) 4))
      ```
      * v1=A,v2=E. 
      ```racket
      (define (f x)
        (- 4 (expt 2 x)))
      ```
      * v1=C,v2=D. 
      ```racket
      (define f(x)
        x^2 - 4)
      ```

28. (Def-2, v1=17, v2=4) Correct: v1: CE,C=1/2,E=1/2; v2: BC,C=1/2,B=1/2\
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
      * v1=A,v2=D. 1
      * v1=C,v2=C. 2
      * v1=E,v2=B. 3
      * v1=D,v2=A. 4
      * v1=B,v2=E. 5

29. (Def-3, v1=2, v2=37) Correct: v1: B,BE; v2: D,DE\
    Which line(s) contain mistakes, either in style or correctness. This question may have multiple answers.
    
    ```racket
    1. (define required-height 163)
    
    2. ;; tall?: number -> boolean
    3. ;; consumes: a person's height in cm
    4. ;; produces: whether they're tall enough to ride a ride
       (define (tall? height)
    5.   (>= height required-height))
    ```
      * v1=B,v2=D. 1
      * v1=C,v2=B. 2
      * v1=A,v2=C. 3
      * v1=D,v2=A. 4
      * v1=E,v2=E. 5

30. (Types-1, v1=26, v2=23) Correct: v1: E; v2: E\
    What is the type of the expression `-3`? (This question has one or two correct answers)
      * v1=E,v2=E. `number`
      * v1=D,v2=A. `string`
      * v1=A,v2=B. `image`
      * v1=C,v2=D. `boolean`
      * v1=B,v2=C. `color`

31. (Types-2, v1=13, v2=34) Correct: v1: AC,C=1/2,A=1/2; v2: AE,A=1/2,E=1/2\
    What is the type of the expression `"red"`? (This question has one or two correct answers)
      * v1=D,v2=D. `number`
      * v1=C,v2=A. `string`
      * v1=B,v2=C. `image`
      * v1=E,v2=B. `boolean`
      * v1=A,v2=E. `color`

32. (Types-3, v1=36, v2=40) Correct: v1: A; v2: A\
    What is the type of the expression `"true"`? (This question has one or two correct answers)
      * v1=D,v2=B. `number`
      * v1=A,v2=A. `string`
      * v1=E,v2=C. `image`
      * v1=B,v2=D. `boolean`
      * v1=C,v2=E. `color`

33. (Types-4, v1=31, v2=39) Correct: v1: B; v2: D\
    What is the type of the expression `(< 3 4)`? (This question has one or two correct answers)
      * v1=A,v2=A. `number`
      * v1=E,v2=C. `string`
      * v1=C,v2=B. `image`
      * v1=B,v2=D. `boolean`
      * v1=D,v2=E. `color`

34. (Types-5, v1=23, v2=6) Correct: v1: B; v2: B\
    What is the type of the expression `(circle 15 "solid" "blue")`? (This question has one or two correct answers)
      * v1=D,v2=E. `number`
      * v1=A,v2=C. `string`
      * v1=B,v2=B. `image`
      * v1=E,v2=D. `boolean`
      * v1=C,v2=A. `color`

35. (Design-1, v1=10, v2=1) Correct: v1: B; v2: E\
    What are the steps of the design recipe in the order that you _do_ them?
    
    ```
    1. Header/Skeleton
    2. Test Cases
    3. Contract
    4. Body
    5. Run/Test
    6. Purpose
    ```
      * v1=A,v2=A. 1, 2, 3, 4, 5, 6
      * v1=E,v2=C. 2, 3, 4, 5, 6, 1
      * v1=B,v2=E. 3, 1, 6, 2, 4, 5
      * v1=D,v2=D. 3, 6, 1, 4, 2, 5
      * v1=C,v2=B. 3, 4, 1, 2, 5, 6

36. (Design-2, v1=15, v2=29) Correct: v1: B; v2: B\
    What are the steps of the design recipe in the order that they _appear_ in the editor?
    
    ```
    1. Header/Skeleton
    2. Test Cases
    3. Contract
    4. Body
    5. Run/Test
    6. Purpose
    ```
      * v1=C,v2=A. 1, 2, 3, 4, 6
      * v1=B,v2=B. 3, 6, 1, 4, 2
      * v1=D,v2=E. 3, 1, 6, 2, 4
      * v1=A,v2=C. 3, 6, 1, 2, 4
      * v1=E,v2=D. 6, 3, 1, 4, 2

37. (Design-3, v1=21, v2=11) Correct: v1: D; v2: B\
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
      * v1=D,v2=B. 1
      * v1=A,v2=D. 2
      * v1=B,v2=C. 4
      * v1=E,v2=A. 6
      * v1=C,v2=E. 9

38. (Design-4, v1=7, v2=16) Correct: v1: E; v2: C\
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
      * v1=D,v2=D. 1
      * v1=E,v2=C. 2
      * v1=C,v2=B. 4
      * v1=B,v2=E. 6
      * v1=A,v2=A. 9

39. (Design-5, v1=25, v2=8) Correct: v1: A; v2: C\
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
      * v1=E,v2=B. 1
      * v1=B,v2=E. 2
      * v1=A,v2=C. 3
      * v1=D,v2=A. 6
      * v1=C,v2=D. 7

40. (Design-6, v1=9, v2=28) Correct: v1: C; v2: E\
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
      * v1=E,v2=B. 5
      * v1=B,v2=D. 6
      * v1=D,v2=A. 7
      * v1=C,v2=E. 8
      * v1=A,v2=C. 9

41. (Racket-1, v1=37, v2=22) Correct: v1: E; v2: B\
    Which of the following is the correct way to translate `2 + 3 · 4 - 5` to Racket?
      * v1=A,v2=C. `(+ (- 2 (* 3 4)) 5)`
      * v1=B,v2=D. `(+ (- 2 (* 3 4)) 5)`
      * v1=E,v2=B. `(- (+ 2 (* 3 4)) 5)`
      * v1=C,v2=A. `(- (* (+ 2 3) 4) 5)`
      * v1=D,v2=E. `(- (* 2 (+ 3 4)) 5)`

42. (Image-1, v1=42, v2=42) Correct: v1: A; v2: A\
    `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

43. (Image-2, v1=43, v2=43) Correct: v1: C; v2: C\
    `(beside WITCH WITCH WITCH)`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

44. (Image-3, v1=44, v2=44) Correct: v1: B; v2: B\
    `(beside (above WITCH WITCH) WITCH)`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

45. (Image-4, v1=45, v2=45) Correct: v1: C; v2: C\
    `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

46. (Image-5, v1=46, v2=46) Correct: v1: E; v2: E\
    `(above WITCH (beside WITCH WITCH))`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

47. (Image-6, v1=47, v2=47) Correct: v1: B; v2: B\
    `(rotate -45 (beside WITCH WITCH WITCH))`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

48. (Image-7, v1=48, v2=48) Correct: v1: D; v2: D\
    `(rotate-cw (above WITCH WITCH WITCH))`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

49. (Image-8, v1=49, v2=49) Correct: v1: D; v2: D\
    `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`

50. (Image-9, v1=50, v2=50) Correct: v1: E; v2: E\
    `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))`
      * v1=A,v2=A. `(above/align "left" WITCH (beside WITCH WITCH))` or `(flip-vertical (beside WITCH WITCH WITCH))`
      * v1=B,v2=B. `(rotate -45 (beside WITCH WITCH WITCH))` or `(beside (above WITCH WITCH) WITCH)`
      * v1=C,v2=C. `(above (rotate -45 WITCH) (rotate -45 WITCH) (rotate -45 WITCH))` or `(beside WITCH WITCH WITCH)`
      * v1=D,v2=D. `(rotate-cw (above WITCH WITCH WITCH))` or `(beside (flip-horizontal WITCH) (flip-horizontal WITCH) (flip-horizontal WITCH))`
      * v1=E,v2=E. `(beside (rotate-ccw WITCH) (rotate-ccw WITCH) (rotate-ccw WITCH))` or `(above WITCH (beside WITCH WITCH))`
