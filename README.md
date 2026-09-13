# CIS261_WK10_VIBE.-
# CIS261_WK10_VIBE

**Student Grade Calculator** — built with VIBE (Visual Interactive Based Education) in GitHub Codespaces.

Ahmed Waqar Qayum Khan · CIS261 · Week 10 Lab

---

## About

A Python program that manages student records, calculates averages and letter grades, and saves everything to a file so the data survives between runs. Built by prompting an AI coding assistant, then reviewing, testing, and refining what it produced.

## Features

- Add student records (name, ID, three test scores)
- Automatic average and letter grade calculation
- Formatted table of all students
- Class statistics — highest, lowest, class average, grade distribution
- Case-insensitive name search
- Saves to `student_grades.txt`, loads on startup
- Exit with menu option 5 or the ESC key

## Grading scale

| Average | Grade |
|---------|-------|
| 90–100  | A |
| 80–89   | B |
| 70–79   | C |
| 60–69   | D |
| below 60| F |

## Data structure

The lab offered two options. I chose **Option A — a list of dictionaries**, since Week 8 of this course covered dictionaries and file I/O and this reinforces that material.

Each record:

```python
{
    'name': 'Alice Johnson',
    'id': 'S1001',
    'test1': 95.0,
    'test2': 88.0,
    'test3': 92.0,
    'average': 91.67,
    'grade': 'A'
}
```

## File format

Pipe-delimited, seven fields per line:

```
name|id|test1|test2|test3|average|grade
```

Example:

```
Alice Johnson|S1001|95.00|88.00|92.00|91.67|A
Bob Smith|S1002|78.00|82.00|75.00|78.33|C
Jamie Smith|S1003|65.00|98.00|75.00|79.33|C
```

## Running it

```bash
python VIBE.py
```

Menu:

```
1. Add New Student
2. Display All Students
3. Search by Name
4. View Class Statistics
5. Save and Exit
   (or type ESC to save and exit)
```

---

## VIBE development process

### The prompt

I gave VIBE the program purpose, data requirements, all nine features, the data structure choice, the file format, and additional requirements — being specific up front rather than asking vaguely for "a grade program."

### What I changed after reviewing the output

VIBE's first draft worked but had gaps. Each fix below is marked with a `[VIBE REFINEMENT]` comment in the code at the function it changed.

1. **Input validation** — a bare `float(input(...))` crashed on letter input. Added a retry loop with `try`/`except`.
2. **ESC exit** — the first draft only exited on menu option 5. The spec also requires ESC, so I added that at the menu prompt.
3. **Empty list guard** — statistics called `max()`, `min()`, and divided by `len()` on an empty list, raising `ValueError` and `ZeroDivisionError`. Added a guard returning zeros.
4. **Score range** — scores above 100 and below 0 were accepted. Added range checking.
5. **Malformed file lines** — one bad line crashed the whole loader. Now it validates the field count and skips bad rows with a warning.

### Test data

| Name | ID | Test 1 | Test 2 | Test 3 | Average | Grade |
|------|-----|--------|--------|--------|---------|-------|
| Alice Johnson | S1001 | 95 | 88 | 92 | 91.67 | A |
| Bob Smith | S1002 | 78 | 82 | 75 | 78.33 | C |
| Jamie Smith | S1003 | 65 | 98 | 75 | 79.33 | C |

Class average: 83.11

### Testing checklist

- [x] Add multiple students
- [x] Average and grade calculated correctly
- [x] Formatted table displays
- [x] Search finds a name that exists
- [x] Search handles a name that doesn't exist
- [x] Class statistics correct
- [x] Saves to file in pipe format
- [x] Loads from file on restart
- [x] Menu option 5 exits and saves
- [x] ESC exits and saves
- [x] Rejects letters, scores over 100, negative scores

---

## Takeaway

The useful lesson was that a specific prompt gets you a working first draft fast, but it doesn't get you a finished program. Everything I fixed was an edge case — bad input, empty data, a corrupt file — which is exactly where AI-generated code tends to be thin. Reviewing and testing the output mattered as much as writing the prompt.