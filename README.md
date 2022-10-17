# PYTHON-TEST-by-TD
## Problems
### Must-have
Please write a "text sanitizer" application in any OOP languages (Python 3 preferred)
- receive CLI arguments "source" & "target"
- read a text file from "source" as an input data
- sanitize the input text (receive string and return string)
  - lowercase the input
  - replace "tab" with "____"
- generate simple statistic
  - count number of occurrence of each alphabet.
- print output(both sanitized text & statistic) to console.
### Nice-to-have
Please write the extensible code to support the following requirements
1. the source of input & the form of output might be changed in the future. (e.g. it might read data from database or write to file at the specified arg 
"location" instead.)
2. we might have more steps to "sanitize" text in the future as well as new statistic calculation.
3. we might receive the "source" & "target" arguments from config file instead of relying on CLI args.
