# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Sambit\\Desktop\\Diary App'],
             binaries=[],
             datas=[],
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
	  Tree('C:\Users\Sambit\Desktop\Diary App\423-4233331_sparkle-clipart-emoji-transparent-background-sparkle-emoji-png-removebg-preview'),
          Tree('C:\Users\Sambit\Desktop\Diary App\logo.png'),
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='TrackToday',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='logo.ico')
