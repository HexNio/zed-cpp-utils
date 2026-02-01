#!/usr/bin/env python3

import argparse
import os
import re
import sys

HEADER_TEMPLATE = """
#ifndef {guard}
#define {guard}

class {class_name}
{{
public:
    {class_name}();
    ~{class_name}() = default;

private:

}};

#endif // {guard}
"""

SOURCE_TEMPLATE = """#include "{class_name_h}.h"

{class_name}::{class_name}(){{}};

"""


def generate_files(class_name: str, rel_path: str):
    base_dir = os.path.abspath(os.getcwd())
    target_dir = os.path.join(base_dir, rel_path)
    guard = f"{class_name.upper()}_H"

    os.makedirs(target_dir, exist_ok=True)

    header_path = os.path.join(target_dir, f"{class_name.lower()}.h")
    source_path = os.path.join(target_dir, f"{class_name.lower()}.cpp")

    if os.path.exists(header_path) or os.path.exists(source_path):
        sys.exit("Error: target files already exist.")

    with open(header_path, "w") as h:
        h.write(HEADER_TEMPLATE.format(class_name=class_name, guard=guard))

    with open(source_path, "w") as c:
        c.write(
            SOURCE_TEMPLATE.format(
                class_name=class_name, class_name_h=class_name.lower()
            )
        )

    return header_path, source_path


def find_cmakelists(rootpath: str):
    for root, _, files in os.walk(rootpath):
        if "CMakeLists.txt" in files:
            return os.path.join(root, "CMakeLists.txt")
    return None


def update_cmakelists(cmake_path: str, header: str, source: str):
    with open(cmake_path, "r") as f:
        content = f.read()

    add_exec_pattern = re.compile(
        r"add_executable\s*\(\s*([^\s\)]+)(.*?)\)",
        re.S,
    )

    match = add_exec_pattern.search(content)
    if not match:
        sys.exit("Error: no add_executable() found.")

    target_name = match.group(1)
    sources_block = match.group(2)

    rel_header = os.path.relpath(header, os.path.dirname(cmake_path))
    rel_source = os.path.relpath(source, os.path.dirname(cmake_path))

    if rel_header in sources_block or rel_source in sources_block:
        return

    new_sources = sources_block.rstrip() + f"\n    {rel_source}\n    {rel_header}\n"
    new_add_exec = f"add_executable({target_name}{new_sources})"
    updated = content[: match.start()] + new_add_exec + content[match.end() :]

    with open(cmake_path, "w") as f:
        f.write(updated)


def main():
    parser = argparse.ArgumentParser(
        description="Generate C++ class and update CMakeLists.txt"
    )

    _ = parser.add_argument(
        "-f",
        "--function",
        required=True,
        choices=["create-class"],
        help="Invoke a specific function",
    )

    _ = parser.add_argument("--zed", action="store_true", help="Zed IDE mode")

    _ = parser.add_argument(
        "--rootpath", required=True, help="Project root to search for CMakeLists.txt"
    )

    args = parser.parse_args()

    zed_mode = args.zed
    relative_path = "."

    if zed_mode:
        print("zed mode active")

    # Function dispatch
    if args.function == "create-class":
        class_name = input("Enter class name: ").strip()
        relative_path = input("Enter where you want to place this class: ").strip()
        if not class_name:
            sys.exit("Error: class name cannot be empty")
    else:
        sys.exit("Error: no --function is specified")

    header, source = generate_files(class_name, relative_path)

    cmake = find_cmakelists(args.rootpath)
    if not cmake:
        sys.exit("Error: no CMakeLists.txt found.")

    update_cmakelists(cmake, header, source)

    print("Generated:")
    print(" ", header)
    print(" ", source)
    print("Updated:", cmake)


if __name__ == "__main__":
    main()
