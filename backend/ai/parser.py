def parse_steps(text: str):
    lines = text.strip().split("\n")
    steps = []

    for line in lines:
        clean = line.strip().lower()

        # Skip intro-style lines
        if "here are" in clean:
            continue

        clean = line.strip().lstrip("-•1234567890. ").strip()

        if clean:
            steps.append(clean)

    return steps[:5]