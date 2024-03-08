require 'minitest/autorun'
require 'minitest/mock'
require_relative 'exercise_1.rb' 

class TestCalculateMD5 < Minitest::Test
  def test_calculate_md5
    # Assuming 'temp_test_file.txt' is a file you've created for testing
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

require 'minitest/autorun'
require 'stringio'
require_relative 'exercise_1'  # Make sure this points to your script file

class TestProcessFile < Minitest::Test
  def setup
    @original_stdout = $stdout
    $stdout = StringIO.new
    @file_path = 'md5_test_genes.tsv'  # make sure this file exists with correct data
  end

  def teardown
    $stdout = @original_stdout
  end

  def test_process_file
    # Call the method with the file path
    process_file(@file_path)
    
    # Here you need to define what the expected output should be.
    # The expected_output must match the format of the actual output from process_file.
    # This includes whitespace, newlines, and the actual MD5 hash which must be pre-calculated for the test file.
    expected_output = <<~OUTPUT
    MD5 Hash of the file: 2e384e0c421199c1eb32d5a32ad7e569
    Question 1: 1000 genes in total
    Question 2: 0 genes listed for homo sapiens
    Question 3: type_of_gene, other, protein-coding, rRNA, pseudo, tRNA, ncRNA (all different gene types)
    Question 4: Most frequent gene type: protein-coding, Amount of Times: 948
    OUTPUT

    # The strip method is used to remove any leading/trailing whitespace or new lines that could cause the test to fail.
    expected_output.strip!

    assert_equal expected_output, $stdout.string.strip, "Output did not match expected"
  end
end
