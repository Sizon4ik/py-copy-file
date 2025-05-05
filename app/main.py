import os


def copy_file(command: str) -> None:
    command_lst = command.split()
    if ((len(command_lst) == 3 and command_lst[0] == "cp"
         and os.path.isfile(command_lst[1]))
            and command_lst[1] != command_lst[2]):
        with (open(command_lst[1], "rb") as f,
              open(command_lst[2], "wb") as f_copy):
            for line in f.readlines():
                f_copy.write(line)
