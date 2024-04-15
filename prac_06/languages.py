from prac_06.programming_language import ProgrammingLanguage

def main():
    languages = []
    
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages.append(python)
    languages.append(ruby)
    languages.append(visual_basic)
    print(languages)
    print(ruby)
    
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
    
    
main()