import pytest
from tests.utils import read_diff_structure, get_file_path
from gendiff.diff_structure_generator import generate_diff_structure
from gendiff.file_loader import load_file


@pytest.mark.parametrize(
    'file1_name,file2_name,diff_structure_file_name',
    [
        ('file1.json', 'file2.json', 'file1_diff_file2.json'),
        ('file1.yml', 'file2.json', 'file1_diff_file2.json'),
        ('file1.json', 'file2.yml', 'file1_diff_file2.json'),
        ('file1.yml', 'file2.yml', 'file1_diff_file2.json'),

        ('file1.yml', 'empty.json', 'file1_diff_empty.json'),
        ('file1.json', 'empty.yml', 'file1_diff_empty.json'),

        ('empty.yml', 'empty.json', 'empty_diff_empty.json'),
        ('empty.json', 'empty.yml', 'empty_diff_empty.json'),
    ]
)
def test_generate_diff_structure_with_different_file_formats(
    file1_name, file2_name, diff_structure_file_name
):
    config1 = load_file(get_file_path(file1_name))
    config2 = load_file(get_file_path(file2_name))
    structure = read_diff_structure(diff_structure_file_name)
    assert generate_diff_structure(config1, config2) == structure