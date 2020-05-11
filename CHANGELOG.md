# Changelog

<!-- markdownlint-disable MD024 -->

## [v2.2.1] - UNRELEASED

## Added

- ExifReader requirement.
- .tiff photos for testing

## Changed

- Changed so exif files also use ExifReader without the need for pyheif.

## Removed

- Exifread and pyheif requirements.
- Removed heic extra.
- Pipfile and Pipfile.lock

## [v2.2.0](https://gitlab.com/Cyb3r-Jak3/metastalk/-/releases/v2.2.0) - 2020-05-08

## Added

- Sub-directory support.
- HEIC and HEIF file support.
- Added WebP, JPEG image export options.

### Changed

- Moved all requirements files to a [requirements directory](./requirements/).
- Moved to exifread from hachoir to enable more options and heic support.
- HTML exports uses cdn for scripts.
- Removed some lines from coverage checks as they can no be processed.

## [v2.1.0](https://gitlab.com/Cyb3r-Jak3/metastalk/-/releases/v2.1.0) - 2020-05-06

### Added

- Ability to pass both directories and individual files.
- Unittests for testing.
- Footer for run time.
- Export feature.
- Added metastalk dev and image install.
- [Codacy](https://www.codacy.com/)
- Two new arguments `--no-open` and `--alphabetic`.
  - `--no-open` will make it so a new browser tab is not opened.
  - `--alphabetic` will sort all the charts alphabetically.

### Changed

- Created MetaStalk Class.
- All titles for charts are centered.

## [v2.0.0](https://gitlab.com/Cyb3r-Jak3/metastalk/-/releases/v2.0.0) - 2020-05-03

## Rename to MetaStalk

Rename to MetaStalk to create PyPi package and a lot backend development changes.

### Added

- License scanning
- [Codecov](https://codecov.io/gl/Cyb3r-Jak3/metastalk)
- Pipfile and Pipfile.lock for pipenv.
- Added .gitlab folder for service desk.
- setup.py for pypi.

### Changed

- Reverted dependency scanner to default template.
- Name from PyStalk to MetaStalk as PyStalk is taken.
- Moved all files to MetaStalk directory.
- Moved ExamplePhotos to own directory.
- License scanning now only on master branch and tags.
- Can only run on from package.

### Removed

- Dropped support for Python 3.5 as hachoir does not support it.
- Dropped using pipenv for pipeline.
- Markdownlint check in codeclimate.

## [v1.4](https://gitlab.com/Cyb3r-Jak3/metastalk/-/releases/v1.4) - 2020-02-02

### Changed

- Rewrote to use hachoir

### Removed

- Removed Flash Chart (hachoir does not support it).

## [v1.3.3] - 2020-01-10

### Changed

- Split directory searching and individual file searching to their own functions.
- Dependency scanning only takes place for master branch and scheduled runs.

### Removed

- fixme plugin for codeclimate

## [v1.3.2] - 2019-12-21

Changes made to testing and PyStalk. No new functionality added.

### Added

- Added time reporting for how long it took.

### Changed

- Added multiple coverage run.
- Readme now used LF line endings.
- Modified tests run on code climate.
- Split up the main function in PyStalk to setup and run.
- Changed linting so that it happens before for all python versions.

## [v1.3.1] - 2019-12-16

### Changed

- Changed so code coverage only run on python 3.7
- Removed random from code climate
- Updated Datetime to remove duplicate code.
- Changed DateTime date_time

## [v1.3] - 2019-12-15

### Added

- [Code Climate](https://codeclimate.com/github/Cyb3r-Jak3/PyStalk).
- [PieChart.py](modules/PieChart.py).
- Dependency and Static scanning.

### Changed

- Models, Software, Flash, Focal charts now use the same module, [PieChart.py](modules/PieChart.py).

### Removed

- Focal, Models, Flash, Focal all handled by [PieChart.py](modules/PieChart.py).

## [v1.2] - 2019-12-04

### Added

- Added 5 more example photos.
- Artifact in build stage to view logs, bandit and coverage reports.
- Added flash analyzer to show levels of flash.
- Added Software and Focal charts.
- [Deepsource](https://deepsource.io/gl/Cyb3r-Jak3/PyStalk/) tracking.

### Changed

- Made the logger wipe old log file.
- Better try/expect for GPSCheck and DateTime.
- Fixed Text Align.
- Renamed Pylint rc file to correct name for building.
- Title location for Model chart.
- Fixed module descriptions.
- Updated app title.
- Updated app header.

### Removed

- Removed Static Testing.

## [v1.1] - 2019-11-17

### Added

- Try/except in app.py for dash for clean exit.
- Logging feature which gets created with logger in utils.
- Custom log levels arguments.
- Favicon in assets folder.
- Modules folders contains all graphing features.
  - Easier for future development.
- Table that reports the gps timestamp.

### Changed

- Made plots a dictionary to improve graph name.
- Moved Geo title to initial figure.
- Changed web browser open to localhost to deal with HTTP Everywhere.
- Added all extra python code to utils directory.
- Added option to disable invalid name in pylint rcfile.
- Moved, GPS_Chart, Model_Chart and Stats to modules.
- Added development branch coverage.
- Moved Photo stats to the top.
- Renamed app.py to web.py.
- Changed GPS check to seeing if there is latitude.

## [v1.0] - 2019-11-12

### Added

- Geo Chart and Model Chart.
- dash page for displaying charts.

---
This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
