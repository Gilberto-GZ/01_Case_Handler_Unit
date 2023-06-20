from setuptools import setup

setup(
    name='Case_Handler_Unit',
    version='1.0',
    description='Transform text from the clipboard and paste the result instantly.',
    author='Gilberto Granados',
    packages=[],
    install_requires=[
        'pyperclip',
        'pytesseract',
        'SpeechRecognition'
        'pyaudio'
        'wave'
        'tempfile'
    ],
    options={
        'build_exe': {
            'icon': 'icon\icon.ico'  # Specify the path to your icon file
        }
    }
)
