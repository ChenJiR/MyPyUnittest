import time
import io
import sys
import unittest
from . import log
from .. import setting


class _TestResult(unittest.TestResult):
    def __init__(self, verbosity=1):
        super().__init__(verbosity)
        self.outputBuffer = io.StringIO()
        self.raw_stdout = None
        self.raw_stderr = None
        self.success_count = 0
        self.failure_count = 0
        self.skip_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.result = []
        self._case_start_time = 0
        self._case_run_time = 0

    def startTest(self, test):
        self._case_start_time = time.time()
        super().startTest(test)
        self.raw_stdout = sys.stdout
        self.raw_stderr = sys.stderr
        sys.stdout = self.outputBuffer
        sys.stderr = self.outputBuffer

    def complete_output(self):
        self._case_run_time = time.time() - self._case_start_time
        if self.raw_stdout:
            sys.stdout = self.raw_stdout
            sys.stderr = self.raw_stderr

        result = self.outputBuffer.getvalue()
        self.outputBuffer.seek(0)
        self.outputBuffer.truncate()
        if result and setting.show_print_in_console:
            log._print(result.strip())
        return result

    def stopTest(self, test):
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        super().addSuccess(test)
        output = self.complete_output()
        self.result.append((0, test, output, '', self._case_run_time))

    def addError(self, test, err):
        self.error_count += 1
        super().addError(test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str, self._case_run_time))
        log.error('TestCase Error')
        if setting.show_error_traceback:
            log.error(_exc_str)

    def addSkip(self, test, reason):
        self.skip_count += 1
        super().addSkip(test, reason)
        self.result.append((3, test, "", "", 0.0))

    def addFailure(self, test, err):
        self.failure_count += 1
        super().addFailure(test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str, self._case_run_time))
        log.error('TestCase Failed')
        if setting.show_error_traceback:
            log.error(_exc_str)