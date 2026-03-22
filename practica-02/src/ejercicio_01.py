text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

def count_words(text):
    """Cuenta el número total de palabras en el texto."""

    words = text.split()
    return len(words)

def count_lines(text):
    """Cuenta el número total de líneas en el texto."""

    lines = text.splitlines()
    return len(lines)

def print_text_analysis(text=text):
    """Analiza el texto y muestra el total de palabras, líneas y el promedio de palabras por línea."""
    
    total_words = count_words(text)
    total_lines = count_lines(text)
    avg_per_line = total_words / total_lines

    print(f"Total de líneas: {total_lines}")
    print(f"Total de palabras: {total_words}")
    print(f"Promedio de palabras por línea: {avg_per_line:.2f}", end="\n\n")

    print(f"Líneas por encima del promedio ({avg_per_line:.2f}):")
    for line in text.splitlines():
        line_word_count = len(line.split())
        if line_word_count > avg_per_line:
            print(f"- \"{line}\" ({line_word_count} palabras)")

if __name__ == "__main__":
    print_text_analysis()
