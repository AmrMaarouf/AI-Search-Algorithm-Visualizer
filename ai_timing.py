import os
import sys

# Default timeout in seconds
DEFAULT_TIMEOUT = int(os.environ.get('AI_TIMEOUT_SEC', '8'))
# On Linux increase timeout by 2x to avoid premature termination on slower systems
TIMEOUT = int(DEFAULT_TIMEOUT * 2) if sys.platform.startswith('linux') else DEFAULT_TIMEOUT
# Polling/sleep interval for loops (seconds)
POLL_SLEEP = float(os.environ.get('AI_POLL_SLEEP', '0.01'))

# Convenience: expose a small sleep helper
import time

def sleep(interval=None):
    """Sleep for POLL_SLEEP by default or the provided interval."""
    time.sleep(POLL_SLEEP if interval is None else interval)
