# zed-cpp-utils
This is an utility useful to automate some boring stuff if you develop in C++ projects such creating new classes, remove them etc...
> Currently project is a workaround because Zed IDE does not support tasks which includes user input yet, and extension API are still limited

> **This project is "Highly Experimental", _use it at your own risk!_. It will be subject to multiple rework. Keep in mind it could break between releases.**

### Requirements
- python (3.x) being installed and in PATH

### How to install it
1. copy the `bin/` folder and paste it inside your **_.config/zed/_** folder (or **_%APPDATA%\Roaming\Zed_** if you are from Windows)
2. append/add this task i you global or project task
 
_this is an example of a `tasks.json` task to create a new class:_
```Json

[
    {
        "label": "Create C++ Class",
        "command": "python3 /home/user/.config/zed/bin/cpp_cli.py --function 'create-class' --zed --rootpath $ZED_WORKTREE_ROOT"
    }
]

```

### How to use it

1. invoke it in Zed using `ctrl+shift+p`
2. fill the needed data using terminal prompt
3. that's it

### ToDo:
- [ ] Add class delete functionality
- [ ] Add UI (TBD)
- [ ] Rewrite it in a compile language (C++ or Rust) and packing it as static binary as release package to avoid dependencies hell between multiple hosts.
- [ ] Add more features as needed
