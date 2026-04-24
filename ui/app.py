import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

from agents.planner import plan_task
from agents.coder import generate_code, generate_simple_code
from agents.debugger import fix_code
from tools.file_manager import save_file
from sandbox.runner import run_code
from core.cleaner import clean_code, strip_preamble
from core.parser import parse_files
from core.validator import is_valid_python

st.set_page_config(page_title="Mini Devin", layout="wide")
st.title("🤖 Mini Devin - AI Coding Assistant")

task = st.text_input("Enter your project idea:")

if st.button("🚀 Generate Project"):
    if not task.strip():
        st.warning("⚠️ Please enter a project idea first.")
        st.stop()

    # ── 1. PLANNING ────────────────────────────────────────────────
    st.subheader("🧠 Planning")
    with st.spinner("Planning your project..."):
        plan = plan_task(task)
    st.text(plan)

    # ── 2. CODE GENERATION (with retry loop) ───────────────────────
    st.subheader("💻 Generating Code")
    files = {}

    for attempt in range(5):
        with st.spinner(f"Generation attempt {attempt + 1}/5..."):
            raw_output = generate_code(task)
            raw_output = strip_preamble(raw_output)
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
                st.warning(f"⚠️ `{filename}` has syntax error — retrying...")
                all_valid = False
                break

            cleaned_files[filename] = content

        if all_valid and cleaned_files:
            st.success(f"✅ Valid code generated on attempt {attempt + 1}")
            files = cleaned_files
            break
    else:
        st.warning("⚠️ Falling back to simple generation...")
        with st.spinner("Generating simple fallback..."):
            simple_code = generate_simple_code(task)
            simple_code = strip_preamble(simple_code)
            simple_code = clean_code(simple_code)
        files = {"app.py": simple_code}

    # ── 3. SAVE & DISPLAY FILES ────────────────────────────────────
    st.subheader("📁 Generated Files")

    for filename, content in files.items():
        path = os.path.join("output", filename)
        save_file(path, content)
        st.markdown(f"**📄 {filename}**")
        st.code(content, language="python")

    # ── 4. RUN + AUTO-DEBUG LOOP ───────────────────────────────────
    st.subheader("🚀 Running Code")

    for i in range(3):
        st.info(f"▶️ Run attempt {i + 1}/3")

        with st.spinner("Running..."):
            output, error = run_code("output/app.py")

        if not error:
            st.success("✅ Success!")
            st.code(output, language="text")
            break

        st.error(f"❌ Error (Attempt {i + 1}):\n{error}")

        if i < 2:
            st.info("🔧 Auto-fixing error...")

            # Read ALL output files for full context
            broken_code = ""
            for filename in files:
                path = os.path.join("output", filename)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        broken_code += f"FILE: {filename}\n{f.read()}\n\n"
                except Exception:
                    pass

            with st.spinner("Asking LLM to fix the error..."):
                fixed_raw = fix_code(broken_code, error)
                fixed_raw = strip_preamble(fixed_raw)

            fixed_files = parse_files(fixed_raw)

            if fixed_files:
                all_ok = True
                for filename, content in fixed_files.items():
                    content = clean_code(content)
                    if not is_valid_python(content):
                        st.warning(f"⚠️ Fixed `{filename}` still has syntax error")
                        all_ok = False
                        break
                    fixed_files[filename] = content

                if all_ok:
                    for filename, content in fixed_files.items():
                        path = os.path.join("output", filename)
                        save_file(path, content)
                    st.success("🔁 Files updated — retrying run...")
                    files = fixed_files
            else:
                st.warning("⚠️ Could not parse fix — keeping previous files")
    else:
        st.error("❌ All 3 run attempts failed. Try a simpler project idea.")

    st.subheader("🎯 Process Complete")