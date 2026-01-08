
- Adding notes 
- Manufacturer OUI Lookup: 
- Automatically resolve the first three bytes of the MAC address to identify the brand (e.g., "Apple, Inc." or "Samsung"). This helps you scan the room for specific hardware.
- Signal "Heartbeat" Logging: Track how long a device has been present. If a device disappears for 2 minutes and returns, it’s likely a person who left the room and came back.
- Triangulation via Walking (Dead Reckoning): Since you only have one sensor (your laptop), you can click a button that says "Mark My Location." You move 5 meters, click it again. The software uses the difference in RSSI from Point A and Point B to pinpoint the device's exact $(x, y)$ coordinate.


- keyboard escape auto saving
```
Traceback (most recent call last):
  File "/usr/local/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/usr/local/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/base_events.py", line 725, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/Users/angelinatsuboi/Desktop/bluesnoop/versions/6_bluesnoop_1_8_17_08/bluesnoop.py", line 130, in main_loop
    await run_scanner(duration=t)
  File "/Users/angelinatsuboi/Desktop/bluesnoop/versions/6_bluesnoop_1_8_17_08/bluesnoop.py", line 75, in run_scanner
    devices = await BleakScanner.discover(timeout=2.0)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/angelinatsuboi/Desktop/bluesnoop/.venv/lib/python3.13/site-packages/bleak/__init__.py", line 284, in discover
    await asyncio.sleep(timeout)
  File "/usr/local/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/tasks.py", line 718, in sleep
    return await future
           ^^^^^^^^^^^^
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/angelinatsuboi/Desktop/bluesnoop/versions/6_bluesnoop_1_8_17_08/bluesnoop.py", line 142, in <module>
    asyncio.run(main_loop())
    ~~~~~~~~~~~^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/usr/local/Cellar/python@3.13/3.13.2/Frameworks/Python.framework/Versions/3.13/lib/python3.13/asyncio/runners.py", line 123, in run
    raise KeyboardInterrupt()
KeyboardInterrupt
```