import os
import subprocess

import sublime, sublime_plugin


def preprocess(data):

    l = subprocess.Popen(
        "echo $HOME", shell=True, stdout=subprocess.PIPE
    ).stdout  # get path of home directory
    path = l.read()
    path = path.decode("utf-8")
    path = path.split("\n")
    path = path[0] + "/file"

    with open(path, "wb") as f:
        f.write(data.encode("utf-8"))

    p = subprocess.Popen(["black", path], stdout=subprocess.PIPE)
    out = p.stdout.read()

    with open(path, "rb") as f:
        data = f.read()

    os.remove(path)

    return data.decode("utf-8")


class AdornCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():  # get user selection
            if not region.empty():  # if selection not empty then
                s = self.view.substr(region)  # assign s variable the selected region
                replace = preprocess(s)
                self.view.replace(edit, region, replace)  # replace content in view
