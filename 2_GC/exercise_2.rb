require 'bio'

# exception classes for error handling
class InvalidEntryIDError < StandardError; end
class EmptySequenceError < StandardError; end

def main
  file_path = check_filename
  begin
    valid_entries, invalid_entries = validate_fasta_file!(file_path) #raises an exeption if FASTA is invalid
    output(valid_entries, invalid_entries)
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end

def check_filename() 
  # checks whether a valid file was provided to be examined
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
  #checks whether the provided file includes valid FASTA entries 
  valid_entries = []
  invalid_entries = []
  errors = []

  Bio::FlatFile.open(Bio::FastaFormat, file_path) do |ff|
    ff.each_entry do |entry|
      if valid_entry?(entry)
        valid_entries << entry
      else 
        invalid_entries << entry
        errors << raise_errors(entry).message
      end
    end
  end
  return [valid_entries, invalid_entries]
end

def valid_entry?(entry)
  !entry.entry_id.nil? && !entry.entry_id.strip.empty? && !entry.seq.nil? && !entry.seq.empty?
rescue StandardError
  false
end

def raise_errors(entry)
  if entry.entry_id.nil? || entry.entry_id.strip.empty?
    InvalidEntryIDError.new("Entry ID is invalid")
  elsif entry.seq.empty?
    EmptySequenceError.new("Sequence is empty")
  end
end

def output(valid_entries, invalid_entries)
  process_valid_entries(valid_entries)
  process_invalid_entries(invalid_entries)
end

def process_valid_entries(valid_entries)
  valid_entries.each do |entry|
    puts "Entry ID: #{entry.entry_id}"
    puts "GC Content Percentage: #{format('%.10f', count_gc(entry) * 100)}%\n\n"
  end
  puts "Total valid entries: #{valid_entries.length} \n\n"
end

def count_gc(entry)
  gc = entry.seq.count("cgCG")
  g = entry.seq.count("G")
  c = entry.seq.count("C")
  portion = gc.to_f / entry.length
end

def process_invalid_entries(invalid_entries)
  invalid_entries.each do |entry|
    puts "Invalid FASTA entry found: #{entry.entry_id}"
  end
  puts "Total invalid entries: #{invalid_entries.length}" unless invalid_entries.empty?
end

if __FILE__ == $PROGRAM_NAME
  main()
end

