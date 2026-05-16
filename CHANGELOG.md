# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Entries below this header are appended automatically by the CI release workflow
on every push to `main`. See the [Releases page](../../releases) for downloadable
binaries.
## [v0.1.0] - 2026-05-16

### Features

- feat(ci): automate releases with auto-versioning, changelog and Windows exe (38aec98)
- feat: .python-version file added (fbbeca6)
- feat: added new test step in CI (d6f08fe)
- feat: added ci lint - ruff - audit - build (b5101d6)
- feat: initial commit (089056a)

### Bug fixes

- fix: redirect egg-info to project root to prevent it from being generated inside src/ (fee8e3f)
- fix: add build-system table to prevent egg-info from being created inside src/ (2ddfeff)
- fix: app.spec in datas files (1bdac8b)
- fix: ci (3f0d94d)

### Refactors

- refactor: replace pip install -r with pip install -e for build deps (3cd8e3a)
- refactor(models): migrate UserModel to Pydantic v2 best practices (db1a249)

### Documentation

- docs: simplify production env setup to use .env directly (238b4ce)

### Build & CI

- ci: run lint-and-audit, test, and build sequentially (14003f8)

