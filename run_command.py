from subprocess import Popen, PIPE


class RunCommand:
    def __init__ (self, cmd):
        self.cmd = cmd

    def do (self):
        with Popen (
                self.cmd,
                shell=True,
                stdout=PIPE,
                stderr=PIPE
        ) as proc:
            proc.communicate()
            return proc.returncode
