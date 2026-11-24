import os

LINE = "This morning the elevator died, so Mrs. Hartono from 3B carried my groceries up four floors, waved off my tip, and asked only that I water her basil while she visits her sister."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
