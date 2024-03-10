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

  Bio::FlatFile.open(Bio::FastaFormat, file_path) do |ff|
    ff.each_entry do |entry|
      begin
        # Check for an invalid entry_id (nil or empty)
        raise InvalidEntryIDError, "Entry ID is invalid" if entry.entry_id.nil? || entry.entry_id.strip.empty?
        
        # Check for an empty sequence
        raise EmptySequenceError, "Sequence is empty" if entry.seq.empty?
        
        # If no exceptions were raised, the entry is valid
        valid_entries << entry
      rescue InvalidEntryIDError => e
        puts e.message
        invalid_entries << entry
      rescue EmptySequenceError => e
        puts e.message
        invalid_entries << entry
      end
    end
  end
  return [valid_entries, invalid_entries]
end


def output(valid_entries, invalid_entries)
  # iterates through the entries in the FASTA file & outputs the results
  valid_entries.each do |entry|
    gc = entry.seq.count("cgCG")
    portion = gc.to_f / entry.length
    puts "Entry ID: #{entry.entry_id}"
    #puts "Sequence: #{entry.seq}"
    puts "GC Content Percentage: #{format('%.10f', portion * 100)}%\n\n"
  end
  puts "Total valid entries: #{valid_entries.length} \n\n"

  invalid_entries.each do |entry|
    puts "Invalid FASTA entry found: #{entry.entry_id}"
  end
  if invalid_entries != []
    puts "Total invalid entries: #{invalid_entries.length}"
  end
end

if __FILE__ == $PROGRAM_NAME
  main()
end