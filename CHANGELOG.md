<!-- markdownlint-disable MD024 -->
# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [v1.1] - 2019-11-17

### Added

- Try/except in app.py for dash for clean exit
- Logging feature which gets created with logger in utils
- Custom log levels arguments
- Favicon in assets folder
- Modules folders contains all graphing features.
  - Easier for future development
- Table that reports the gps timestamp

### Changed

- Made plots a dictionary to improve graph name
- Moved Geo title to initial figure
- Changed web browser open to localhost to deal with HTTP Everywhere.
- Added all extra python code to utils directory
- Added option to disable invalid name in pylint rcfile
- Moved, GPS_Chart, Model_Chart and Stats to modules
- Added development branch coverage
- Moved Photo stats to the top
- Renamed app.py to web.py
- Changed GPS check to seeing if there is latitude

## [v1.0] - 2019-11-12

### Added

- Geo Chart and Model Chart
- dash page for displaying charts
