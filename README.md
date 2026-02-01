# zed-cpp-utils
This is an utility useful to automate some boring stuff if you develop in C++ projects such creating new classes, remove them etc...
> Currently project is a workaround because Zed IDE does not support tasks which includes user input yet, and extension API are still limited
> **This project is "Highly Experimental", _use it at your own risk!_. It will be subject to multiple rework. Keep in mind it could break between releases.**

### Requirements
- python (3.x) being installed and in PATH

### How to install it
copy those files in you ".config/zed/" folder (%APPDATA%\Roaming\Zed if you are from Windows)

### How to use it
if you mainly work with C++ add a global task depending on your needs. 
this is an example of a `tasks.json` task to create a new class:
```Json

[
    {
        "label": "Create C++ Class",
        "command": "python3 /home/user/.config/zed/bin/cpp_cli.py --function 'create-class' --zed --rootpath $ZED_WORKTREE_ROOT"
    }
]

```

### ToDo:
- [ ] add class delete functionality
- [ ] rewrite it in a compile language (C++ or Rust) and packing it as static binary as release package to avoid dependencies hell between multiple hosts.
- [ ] add more features as needed
