def extract_title(markdown):
    """Extract the H1 title from the given markdown content."""
    for line in markdown.splitlines():
        stripped_line = line.strip()
        if stripped_line.startswith("# "):
            return stripped_line[2:].strip()
    raise ValueError("No H1 title found in markdown")
