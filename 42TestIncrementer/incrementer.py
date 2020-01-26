import re
import sys
import os
import random
import string


def main():
    methods = {}  # Hold the methods in the 42 file.

    if len(sys.argv) > 2:  # Check to make sure there is a filepath.
        filename = sys.argv[1]
        if os.path.isfile(filename):
            with open(filename) as f:
                lines = f.readlines()  # We can safely do this as we don't expect a 42 file to be too large...
                for line in lines:  # Check for methods.
                    if line.startswith("reuse") or line.startswith("Cache"):  # We can ignore the reuse or cache line.
                        continue
                    elif re.match("\bmethod\b", line):  # Get a list of methods.
                        index = line.find("method")
                        new_line = line[index + 7::]  # Get name of method. +7 chars for " method ".
                        method_name = ""
                        param_type = ""
                        for c in new_line:
                            if c != "(":  # Get the method name up until the list of parameters
                                method_name += c
                            elif c == "(":
                                break
                        bracket_index = new_line.find("(")
                        for c in new_line[bracket_index + 1::]:
                            if c != " ":
                                param_type += c
                            if c == " ":
                                break

                        methods[method_name] = param_type
                for line in lines:  # Check for methods called.
                    for method in methods.keys():
                        if methods[method] == "Num" or "S":  # We can trivially mutate ints and strings.
                            if method in line:
                                if "method" not in line:  # Make sure we're not getting method declarations.
                                    new_line = ""
                                    method_index = line.find(method)
                                    new_line += line[:method_index:] + method + "("  # The updated method call.
                                    args = line[len(method) + method_index::]
                                    if args[0] == "(":
                                        tmp = args[1]
                                        try:
                                            int(tmp)  # It's a number.

                                            num_str = ""
                                            for c in args[1:]:
                                                if c != "N":
                                                    num_str += c
                                                else:
                                                    break
                                            val = int(num_str)

                                            if len(sys.argv) > 3:
                                                cmd_arg = sys.argv[3]
                                                try:
                                                    cmd_arg = int(cmd_arg)
                                                    val += cmd_arg
                                                except ValueError:
                                                    val += random.randint(1, 55)
                                                final_val = len(new_line)
                                            else:
                                                val += random.randint(1, 55)
                                                new_line += str(val) + "Num))"
                                                final_val = len(new_line)

                                        except ValueError:  # It's a string.
                                            tmp_str = ""
                                            if args[2] == "\"":
                                                for c in args[3:]:
                                                    if c != "\"":
                                                        tmp_str += c
                                                    else:
                                                        break
                                            new_line += "S\""
                                            if len(sys.argv) > 3:
                                                tmp_str += sys.argv[3]
                                            else:
                                                # Working with ASCII chars as other char sets are out of scope.
                                                tmp_str += "".join(
                                                    random.choice(string.ascii_letters) for _ in range(2))
                                            new_line += tmp_str
                                            final_val = len(tmp_str)
                                    new_index = method_index + len(method) + final_val
                                    for c in line[new_index::]:
                                        new_line += c
                                    index = lines.index(line)
                                    lines.remove(line)
                                    lines.insert(index, new_line)
            open(sys.argv[2], "w")
            for e in lines:
                print(e, file=open(sys.argv[2], "a"))

        else:
            print("File not found!")


main()
