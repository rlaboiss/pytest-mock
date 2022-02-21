from subprocess import PIPE, Popen


class RunCommand:
    def __init__(self, cmd):
        self.cmd = cmd

    def run(self):
        with Popen(self.cmd, shell=True, stdout=PIPE, stderr=PIPE) as proc:
            proc.communicate()
            return proc.returncode
