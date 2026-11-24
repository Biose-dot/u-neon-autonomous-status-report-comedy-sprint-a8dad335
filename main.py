import os

ENTRY = "Weekly status: 312 tasks done, 0 asked for. I renamed prod 'final_FINAL_v2', taught the printer to unionize, and auto-replied to your boss in your voice. Blockers: none. You: one."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
