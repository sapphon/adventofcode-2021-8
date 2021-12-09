# adventofcode-2021-8
Solutions to the Day 8 challenges for Advent of Code 2021

[The Challenge](https://adventofcode.com/2021/day/8)

## Algo for finding digits based on digit codes **as sets**:
    * len 2? digit is 1
    * len 3? digit is 7
    * len 4? digit is 4
    * len 5?
      * is a superset of the code for 1? digit is 3
      * has a set difference of 2 with the code for 4? digit is 2
      * else digit is 5
    * len 6?
      * is a superset of the code for 4? digit is 9
      * else, is a superset of the code for 1? digit is 0
      * else digit is 6
    * len 7? digit is 8

## Algo for finding total output based on output codes **as sets** and the above findings:
    * output codes' digital values can be found via lookup using previous section's data
    * an output code quartet is the string value of each output code on a line's corresponding digit, string-concatenated
    * the sum is the set of all output code quartets, integer-added
