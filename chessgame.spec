# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/entry_point.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/bishop.png', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/boo.mp3', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/clack.mp3', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/correct.wav', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/gameDefinitions.json', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/Hide.png', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/LoginButtonImage.png', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/queen.png', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/rook.png', 'assets'), ('/home/shane/dev/github/rowan/Team4-ChessPuzzleGame/frontend/chess/assets/Show.png', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='chessgame',
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
)
