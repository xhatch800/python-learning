def lesson(message):
    maxSepLen = 30
    sep = f"{'*' * max(len(message), maxSepLen)}"
    print(f"{sep}\n{message}\n{sep}")