# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

files = [('db/user_store.json', 'db'),
('db/const_db.json', 'db'),
('settings.json', '.'),
('assets/audio/effects/*', 'assets/audio/effects'),
('assets/audio/bg/*', 'assets/audio/bg'),
('assets/fonts/*', 'assets/fonts'),
('assets/images/bg/*', 'assets/images/bg'),
('assets/images/sprites/*', 'assets/images/sprites'),
('assets/images/textures/*', 'assets/images/textures'),
('assets/images/*', 'assets/images')
]

a = Analysis(['run_game.py'],
             pathex=['C:\\Users\\Ayush\\Documents\\GitHub\\pyweek31'],
             binaries=[],
             datas=files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='run_game',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
