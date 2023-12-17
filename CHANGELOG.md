# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.1.0] - 2023-12-17

### Added

- introduced new states -- `created` and `imported` ([#295])

### Fixed

- removed default values in `nitro_resource_map.py` ([#313], [#314], [#311])
- default monitor can now be unbound from service ([#312])
- `ip` is now not mandatory for server based resources ([#297])

## [2.0.3] - 2023-11-14

> No module specific changes in this release

- updated documentation
- updated supported_modules_matrix.md
- added GitHub workflows
- updated GitHub issue and feature template

## [2.0.2] - 2023-11-08

### Fixed

- updated secret attributes with `no_log` option ([#286])
- Prepared the collection for Ansible Automation Hub Certification

## [2.0.1] - 2023-09-30

### Fixed

- convert to lowercase while comparing string attributes ([#288])

## [2.0.0] - 2023-09-26

### Added

- Initial Release

[unreleased]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.1.0...HEAD
[2.1.0]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.3...2.1.0
[2.0.3]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/netscaler/ansible-collection-netscaleradc/releases/tag/2.0.0
[#288]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/288
[#286]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/286
[#295]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/295
[#297]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/297
[#311]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/311
[#312]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/312
[#313]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/313
[#314]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/314
