# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.5.2] - 2024-04-15

### Fixed

- Fixed `systemuser`'s `unset` not working ([#400])

## [2.5.1] - 2024-03-11

### Fixed

- Fixed gslbservice idempotency issues ([#377])

## [2.5.0] - 2024-02-22

### Added

- Added more examples
- fixed issue related to lbvserver_servicegroup_binding ([#352])
- fixed issue related to systemglobal_authenticationtacacspolicy_binding ([#353])
- fixed cipher group idempotency issue ([#350])

### Fixed

- Fixed hasync and hafailover issue ([#360])
- security check (bandit) for all pull requests ([#367])
- sanity tests for 2.14 and 2.16 ([#365])
- redesigned inbuilt bindings handling ([#362])
- support added for linking sslcertkey ([#318])

### Breaking Changes

## [2.4.0] - 2024-01-16

### Added

- New state `unset` added for `unset` action ([#346])

### Fixed

### Breaking Changes

- Playbook tasks with `absent` state for `unset` action will now fail. A new state `unset` has been introduced for `unset` action. ([#346])

## [2.3.0] - 2024-01-14

### Added

- New states added - `switched`, `flushed` ([#339], [#310])
- `module_defaults` action groups added ([#307])
- Integration tests added

### Fixed

- Fixed `ntpserver`'s dual primary_key issue ([#322])
- Fixed `sslprofile_sslcipher_binding`'s idempotency issue ([#292])
- Fixed `lbmonitor`'s idempotency issue ([#324])
- Removed calling of GET method for `save_config` ([#326])

## [2.2.0] - 2023-12-21

### Added

- introduced new module `save_config` ([#326])
- updated documentation

### Fixed

- fixed ansible pep8 sanity test errors

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

[unreleased]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.5.2...HEAD
[2.5.2]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.5.1...2.5.2
[2.5.1]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.5.0...2.5.1
[2.5.0]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.4.0...2.5.0
[2.4.0]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.3.0...2.4.0
[2.3.0]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.2.0...2.3.0
[2.2.0]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.1.0...2.2.0
[2.1.0]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.3...2.1.0
[2.0.3]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/netscaler/ansible-collection-netscaleradc/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/netscaler/ansible-collection-netscaleradc/releases/tag/2.0.0
[#286]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/286
[#288]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/288
[#292]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/292
[#295]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/295
[#297]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/297
[#307]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/307
[#310]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/310
[#311]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/311
[#312]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/312
[#313]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/313
[#314]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/314
[#318]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/318
[#322]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/322
[#324]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/324
[#326]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/326
[#339]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/339
[#346]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/346
[#350]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/350
[#352]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/352
[#353]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/353
[#360]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/360
[#362]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/362
[#365]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/365
[#367]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/367
[#377]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/377
[#400]: https://github.com/netscaler/ansible-collection-netscaleradc/issues/400
