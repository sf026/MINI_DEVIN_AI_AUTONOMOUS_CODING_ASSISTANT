from agents.planner import plan_task
from agents.coder import generate_code
from agents.debugger import fix_code
from tools.file_manager import save_file
from sandbox.runner import run_code
from core.cleaner import clean_code, strip_preamble
from core.parser import parse_files
from core.validator import is_valid_python

import os


def save_and_report(files):
    for filename, content in files.items():
        path = os.path.join("output", filename)
        save_file(path, content)
        print(f"📄 {filename}\n")
        print(content)
        print()


def main():
    task = input("Enter your project idea: ")

    print("\n🧠 Planning")
    plan = plan_task(task)
    print(plan)

    print("\n💻 Generating Code")

    files = {}

    # 🔁 Generation loop
    for attempt in range(5):
        print(f"\n🔁 Generation Attempt {attempt + 1}")

        raw_output = generate_code(task)
        raw_output = strip_preamble(raw_output)   # ✅ strip "Here are..." lines
        files = parse_files(raw_output)

        if not files:
            files = {"app.py": raw_output}

        all_valid = True
        cleaned_files = {}

        for filename, content in files.items():
            content = clean_code(content)

            cleaned_lines = []
            for line in content.split("\n"):
                stripped = line.strip()
                if (
                    stripped.startswith("FILE:") or
                    stripped.endswith(".py:") or
                    (stripped.startswith("**") and stripped.endswith("**")) or
                    "input(" in stripped or
                    stripped.lower().startswith(("explanation", "i fixed", "here are", "here is"))
                ):
                    continue
                cleaned_lines.append(line)

            content = "\n".join(cleaned_lines)

            if not is_valid_python(content):
                print(f"❌ {filename} has syntax error → retrying")
                all_valid = False
                break

            cleaned_files[filename] = content

        if all_valid and cleaned_files:
            print("✅ All files valid!")
            files = cleaned_files
            break
    else:
        print("⚠️ Falling back to simple generation...")
        simple_code = generate_simple_code(task)
        simple_code = strip_preamble(simple_code)
        simple_code = clean_code(simple_code)
        files = {"app.py": simple_code}

    print("\n📁 Generated Files")
    save_and_report(files)

    print("\n🚀 Running Code")

    # 🔁 Run + auto-fix loop
    for i in range(3):
        print(f"\n--- Run Attempt {i + 1} ---")
        output, error = run_code("output/app.py")

        if not error:
            print("✅ SUCCESS OUTPUT:\n")
            print(output)
            break

        print(f"❌ Error detected (Attempt {i + 1}): {error}")

        if i < 2:
            print("🔧 Attempting auto-fix...")

            # Read all current saved files
            broken_code = ""
            for filename in files:
                path = os.path.join("output", filename)
                try:
                    with open(path, "r") as f:
                        broken_code += f"FILE: {filename}\n{f.read()}\n\n"
                except Exception:
                    pass

            fixed_raw = fix_code(broken_code, error)
            fixed_raw = strip_preamble(fixed_raw)   # ✅ strip "Here are the corrected files:"
            fixed_files = parse_files(fixed_raw)

            if fixed_files:
                # Validate before saving
                all_ok = True
                for filename, content in fixed_files.items():
                    content = clean_code(content)
                    if not is_valid_python(content):
                        print(f"❌ Fixed {filename} still has syntax error")
                        all_ok = False
                        break
                    fixed_files[filename] = content

                if all_ok:
                    for filename, content in fixed_files.items():
                        path = os.path.join("output", filename)
                        save_file(path, content)
                        print(f"🔁 Re-saved: {path}")
                    files = fixed_files
            else:
                print("⚠️ Could not parse fixed output, keeping previous files")

    print("\n🎯 Process Complete")


if __name__ == "__main__":
    main()