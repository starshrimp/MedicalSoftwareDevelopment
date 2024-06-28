require 'digest'

def main
  file_path = check_filename
  begin
    process_file(file_path)
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end

def check_filename
  if ARGV.length != 1
    puts 'Please enter it in the format like this: ruby exercise_1.rb FILENAME'
    exit
  end
  file_path = ARGV[0]
  unless File.exist?(file_path) && File.readable?(file_path)
    puts 'File does not exist or is not readable.'
    exit
  end
  file_path
end

def process_file(file_path)
  amount_of_homo_sapiens = 0
  total_rows = 0
  gene_types = Hash.new(0)
  File.foreach(file_path) do |line|
    total_rows += 1
    columns = line.split("\t")
    if columns.length < 10
      puts "Warning: Line #{total_rows} has less than 10 columns."
      next
    end
    amount_of_homo_sapiens += 1 if columns[0].to_s == '9606'
    gene_types[columns[9]] += 1 # Increment the counter for the key columns[9]
  end
  output(total_rows, amount_of_homo_sapiens, gene_types, calculate_MD5(file_path))
end

def calculate_MD5(file_path)
  Digest::MD5.file(file_path).hexdigest
end

# Modified to accept variables as parameters, including the MD5 hash
def output(total_rows, amount_of_homo_sapiens, gene_types, md5_hash)
  output = "MD5 Hash of the file: #{md5_hash}\n" # Include the MD5 hash in the output
  output += "Question 1: #{total_rows} genes in total\n"
  output += "Question 2: #{amount_of_homo_sapiens} genes listed for homo sapiens\n"
  output += "Question 3: #{gene_types.keys.join(', ')} (all different gene types)\n"
  output += "Question 4: #{find_highest_key(gene_types)}"
  print(output)
end

def find_highest_key(hash)
  "Most frequent gene type: #{hash.key(hash.values.max)}, Amount of Times: #{hash.values.max}"
end

main if __FILE__ == $PROGRAM_NAME
