require 'bio'

def main
  file_path = check_filename
  begin
    validate_fasta_file!(file_path) #raises an exeption if FASTA is invalid
    process_file(file_path)
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end

def check_filename()
  if ARGV.length != 1
    puts "Please enter it in the format like this: ruby exercise_1.rb FILENAME"
    exit
  end
  file_path = ARGV[0]
  unless File.exist?(file_path) && File.readable?(file_path)
    puts "File does not exist or is not readable."
    exit
  end
  return file_path
end

def validate_fasta_file!(file_path)
  Bio::FlatFile.open(Bio::FastaFormat, file_path) do |ff|
    ff.each_entry do |entry|
      unless entry.entry_id && !entry.seq.empty?
        raise StandardError, "Invalid FASTA entry found: #{entry}"
      end
    end
  end
end

def process_file(file_path)
  fasta_file = Bio::FlatFile.open(Bio::FastaFormat, file_path)
  output(fasta_file)
end

def output(fasta_file)
  total_entries = 0
  fasta_file.each_entry do |entry|
    total_entries += 1
    gc = entry.seq.count("CG")
    percentage = gc.to_f / entry.length
    puts "Entry ID: #{entry.entry_id}"
    #puts "Sequence: #{entry.seq}"
    puts "GC Content Percentage: #{percentage * 100}%"
  end
  puts "Total entries: #{total_entries}"
end

if __FILE__ == $PROGRAM_NAME
  main()
end