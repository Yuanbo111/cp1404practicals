"""CP1404/CP5632 Practical - Programming Language client code.
Estimate: 15 minutes
Start time: 1:56
Actual: 12 minutes (Finished at 2:08)"""

from programming_language import ProgrammingLanguage  # or use prac_06.programming_language depending on path

def main():
    """Demo test code to show how to use ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
