"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['somefile.txt', '*'],
            "answer": True,
            "explanation": "* matches everything"
        },
        {
            "input": ['other.exe', '*'],
            "answer": True,
            "explanation": "* matches everything"
        },
        {
            "input": ['my.exe', '*.txt'],
            "answer": False,
            "explanation": "filename should ends with \".txt\" but \".exe\" found "
        },
        {
            "input": ['log1.txt', 'log?.txt'],
            "answer": True,
            "explanation": "? matches any single character (in this case it is \"1\""
        },
        {
            "input": ['log12.txt', 'log?.txt'],
            "answer": False,
            "explanation": "? matches any single character. Not more than one"
        },
        {
            "input": ['log12.txt', 'log??.txt'],
            "answer": True,
            "explanation": "? matches any two character"
        }
    ],
    "Extra": [
        {
            "input": ['log12.txt', '**'],
            "answer": True,
            "explanation": "** works the same as *"
        },
        {
            "input": ['file19.txt', '*z*'],
            "answer": False,
            "explanation": "\"z\" should be somewhere inside the filename"
        },
        {
            "input": ['l.txt', '???*'],
            "answer": True,
            "explanation": "Filename should be 3 chars long"
        },
        {
            "input": ['txt', '????*'],
            "answer": False,
            "explanation": "Filename should be 4 chars long"
        },
        {
            "input": ['name.txt', 'name.txt'],
            "answer": True,
            "explanation": "filename matches itself"
        },
        {
            "input": ['name.txt', 'name.exe'],
            "answer": False,
            "explanation": "filename matches itself"
        },
        {
            "input": ['apache1.log', '*.*'],
            "answer": True,
            "explanation": "filename should have an extension"
        },
        {
            "input": ['12apache1.log', '*.*'],
            "answer": True,
            "explanation": "filename should have an extension"
        },
        {
            "input": ['12apache1', '*.*'],
            "answer": False,
            "explanation": "filename should have an extension"
        },
        {
            "input": ['name.txt', 'name.???'],
            "answer": True
        },
        {
            "input": ['name.exe', 'name.???'],
            "answer": True
        },
        {
            "input": ['name....', 'name.???'],
            "answer": True
        },
        {
            "input": ['name....', 'name.*'],
            "answer": True
        }
    ]
}
