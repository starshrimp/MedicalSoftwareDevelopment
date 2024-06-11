require 'minitest/autorun'
require 'minitest/mock'
require_relative 'exercise_1.rb' 

class TestCalculateMD5 < Minitest::Test
  def test_calculate_md5
    file_path = 'md5_test_genes.tsv'
    expected_md5 = `md5sum #{file_path}`.split.first # Use system md5sum command for expected value

    assert_equal expected_md5, calculate_MD5(file_path), "MD5 hash does not match expected value"
  end
end

class TestFindHighestKey < Minitest::Test
  def test_find_highest_key
    sample_hash = {'A' => 2, 'B' => 3, 'C' => 1}
    expected_output = "Most frequent gene type: B, Amount of Times: 3"
    assert_equal expected_output, find_highest_key(sample_hash), "Did not find the correct highest key"
  end
end

class TestProcessFile < Minitest::Test
  def setup
    @original_stdout = $stdout
    $stdout = StringIO.new
    @file_path = 'md5_test_genes.tsv' 
  end

  def teardown
    $stdout = @original_stdout
  end

  def test_process_file
    process_file(@file_path)
    expected_output = <<~OUTPUT
    MD5 Hash of the file: 05a6d4cebb961127eea12bb3f0104a40
    Question 1: 50 genes in total
    Question 2: 0 genes listed for homo sapiens
    Question 3: type_of_gene, other, protein-coding, rRNA (all different gene types)
    Question 4: Most frequent gene type: protein-coding, Amount of Times: 40
    OUTPUT
    expected_output.strip!

    assert_equal expected_output, $stdout.string.strip, "Output did not match expected"
  end
end
