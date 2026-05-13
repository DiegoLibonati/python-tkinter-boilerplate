# -*- mode: python ; coding: utf-8 -*-
#
# PRODUCTION NOTE: This spec bundles `.env.prod` (not the repo-level `.env`).
# Before building a release, create `.env.prod` with your production values:
#   cp .env.example.prod .env.prod
#   # fill in real values, then:
#   pyinstaller app.spec
#
# NEVER commit `.env.prod` to version control — add it to .gitignore.
# The repo-level `.env` is for local development only and must NOT contain
# production secrets.

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('src/assets', 'src/assets'), ('.env.prod', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)