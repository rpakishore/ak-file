from pathlib import Path
import os
from ak_file.main import *

def test_file_properties():
    # create a new file for testing
    test_file = "test_file.txt"
    with open(test_file, "w") as f:
        f.write("test")

    # test file properties
    f = File(test_file)
    assert f.name == test_file
    assert f.parent == Path(os.getcwd())
    assert f.abspath == Path(os.getcwd()) / test_file
    assert f.exists() == True
    assert f.is_file() == True
    assert f.is_dir() == False
    assert isinstance(f.properties(), dict)

    # remove test file
    os.remove(test_file)

def test_update_filename():
    # create a new file for testing
    test_file = "test_file.txt"
    with open(test_file, "w") as f:
        f.write("test")

    # test update_filename function
    f = File(test_file)
    new_filename = "new_test_file.txt"
    assert f.update_filename(new_filename, rename_file=True) == new_filename
    assert f.name == new_filename
    assert f.exists() == True

    # remove test file
    os.remove(new_filename)

def test_file_not_exists():
    # test with a non-existent file
    f = File("non-existent-file.txt")
    assert f.exists() == False

def test_file_properties_not_exists():
    # test properties() method with a non-existent file
    f = File("non-existent-file.txt")
    assert isinstance(f.properties(), dict)

def test_file_creation():
    # test file creation and deletion
    test_file = "test_file.txt"
    f = File(test_file)
    assert f.exists() == False
    f.properties() # should not raise an error
    f.update_filename(test_file)
    assert f.exists() == False
    f.properties() # should not raise an error
    with open(test_file, "w") as file:
        file.write("test")
    test_file = "new_test_file.txt"
    f.update_filename(test_file, rename_file=True)
    assert f.exists() == True
    f.properties() # should not raise an error
    os.remove(test_file)
    assert f.exists() == False

def test_file_directory():
    # test file directory
    f = File("test_file.txt")
    assert f.parent == Path(os.getcwd())

    test_dir = "test_dir"
    os.mkdir(test_dir)
    f = File(test_dir)
    assert f.parent == Path(os.getcwd())
    os.rmdir(test_dir)
