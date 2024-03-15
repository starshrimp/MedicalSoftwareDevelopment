require 'minitest/autorun'
require 'minitest/mock'
require 'bio'
require_relative 'exercise_2.rb' 


class TestCalculateMD5 < Minitest::Test
  
  class Exercise1Test < Minitest::Test
    def test_check_filename_with_no_arguments
      ARGV.clear
      assert_output("Please enter it in the format like this: ruby exercise_1.rb FILENAME\n") { exit_assertion { check_filename } }
    end
  
    def test_check_filename_with_multiple_arguments
      ARGV.replace(['file1.fna', 'file2.fna'])
      assert_output("Please enter it in the format like this: ruby exercise_1.rb FILENAME\n") { exit_assertion { check_filename } }
    end
  
    def test_check_filename_with_nonexistent_file
      ARGV.replace(['nonexistent.fna'])
      assert_output("File does not exist or is not readable.\n") { exit_assertion { check_filename } }
    end
  
    def test_check_filename_with_valid_file
      file_path = 'valid_file.fna'
      File.write(file_path, ">Sample\nATCG")
      ARGV.replace([file_path])
      assert_equal file_path, check_filename
    ensure
      File.delete(file_path) if File.exist?(file_path)
    end
  
    private
  
    def exit_assertion
      yield
    rescue SystemExit => e
      assert true  # If we get here, it means exit was called, which is expected in some tests
    else
      assert false, "Expected script to exit but it didn't"
    end
  end
  
end

class Exercise1Test < Minitest::Test
  # Helper method to create a temporary FASTA file
  def create_temp_fasta(content)
    file_path = "temp.fasta"
    File.open(file_path, "w") do |file|
      file.write(content)
    end
    file_path
  end

  def test_validate_fasta_file_with_valid_entries
    content = ">Valid_1\nATCG\n>Valid_2\nGCTA"
    file_path = create_temp_fasta(content)
    valid_entries, invalid_entries = validate_fasta_file!(file_path)
    assert_equal 2, valid_entries.size
    assert_equal 0, invalid_entries.size
  ensure
    File.delete(file_path) if File.exist?(file_path)
  end

  def test_validate_fasta_file_with_invalid_entry_ids
    content = ">\nATCG\n>Valid_2\nGCTA"
    file_path = create_temp_fasta(content)
    valid_entries, invalid_entries = validate_fasta_file!(file_path)
    assert_equal 1, valid_entries.size
    assert_equal 1, invalid_entries.size
  ensure
    File.delete(file_path) if File.exist?(file_path)
  end

  def test_validate_fasta_file_with_empty_sequences
    content = ">Valid_1\n\n>Valid_2\nGCTA"
    file_path = create_temp_fasta(content)
    valid_entries, invalid_entries = validate_fasta_file!(file_path)
    assert_equal 1, valid_entries.size
    assert_equal 1, invalid_entries.size
  ensure
    File.delete(file_path) if File.exist?(file_path)
  end

  def test_validate_fasta_file_with_mixed_validity_entries
    content = ">\n\n>Valid_2\nGCTA\n>Valid_3\nATCG\n>Invalid_3\n"
    file_path = create_temp_fasta(content)
    valid_entries, invalid_entries = validate_fasta_file!(file_path)
    assert_equal 2, valid_entries.size
    assert_equal 2, invalid_entries.size
  ensure
    File.delete(file_path) if File.exist?(file_path)
  end
end
