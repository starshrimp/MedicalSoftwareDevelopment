require 'minitest/autorun'
require 'minitest/mock'
require_relative 'exercise_2.rb' 


class TestValidateFastaFile < Minitest::Test
  def setup
    @file_path = ['test_human_gene.fna','test_human_gene_2.fna']  # Path to a 2 test files (1 invalid header, 1 invalid sequence) 
  end
  def test_validate_fasta_file_raises_exception
    assert_raises(StandardError) do
      @file_path.each do |file_path|
        validate_fasta_file!(file_path)
      end
    end
  end
end

class TestProcessFile < Minitest::Test
  def setup
    @original_stdout = $stdout
    $stdout = StringIO.new
    @file_path = 'gene.fna' #testing with the mouse Gene CD28 
  end

  def teardown
    $stdout = @original_stdout
  end

  def test_process_file
    process_file(@file_path)
    expected_output = <<~OUTPUT.chomp
      Entry ID: NC_000067.7:60785547-60812521
      GC Content Percentage: 39.31%
  
      Total entries: 1
    OUTPUT
  
    assert_equal expected_output, $stdout.string.chomp, "Output did not match expected"
  end  
end
