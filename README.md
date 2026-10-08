Project Descriptions

The two programs are:

- `grade_reporter.py`
- `bug_hunt.py`

1. Grade Reporter

The `grade_reporter.py` program uses a `for` loop to go through a list of scores.

It uses `if`, `elif`, and `else` to give each score a grade:

- 80 and above = A
- 70 to 79 = B
- 50 to 69 = C
- Below 50 = F

The program also uses a running total to add all the scores together.

 Example

```text
85: A
72: B
90: A
64: C
48: F
Total score: 359
```
2. Bug Hunt

The `bug_hunt.py` program uses a `while` loop to count down from 5 to 1.

The original program had a logic bug because it used:

```python
count += 1
```

This increased the number instead of decreasing it, so the loop continued forever.

I fixed the bug by changing it to:

```python
count -= 1
```

The program then counts down correctly and stops when the count reaches 0.

 Correct Output

```text
Count: 5
Count: 4
Count: 3
Count: 2
Count: 1
Done!
```
 What I Learned

Through this assignment, I practiced:

- Using a `for` loop to repeat work.
- Using `if`, `elif`, and `else` to make decisions.
- Building a running total inside a loop.
- Understanding how a `while` loop stops.
- Finding and fixing a logic error that did not produce a Python error message.
- Understanding the difference between increasing and decreasing a variable using `+=` and `-=`.
