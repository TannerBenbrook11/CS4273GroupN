require 'csv'

class CSVReader
  def initialize(file_path)
    @file_path = file_path
  end

  def read_csv_file
    """
    Reads a CSV file and returns its contents as an array of rows.
    Raises an error if the file does not exist or has an invalid format.
    """
    begin
      rows = []
      headers = nil
      # This reads the csv file, and also checks to see if it's in the correct format for a csv.
      CSV.foreach(@file_path) do |row|
        if headers.nil?
          headers = row.size # Store the number of columns in the header row
        elsif row.size != headers
          raise "Invalid CSV format: row has #{row.size} columns, expected #{headers}"
        end
        rows << row
      end

      rows
    rescue Errno::ENOENT
      raise "The file #{@file_path} does not exist."
    rescue => e
      raise "An error occurred while reading the file: #{e.message}"
    end
  end
end


require 'minitest/autorun'
require 'csv'
require 'tempfile'

class TestCSVFileReading < Minitest::Test
  def test_read_csv_file_success
    """
    Test that a CSV file is opened and read successfully.
    """
    # Mock CSV content
    csv_content = "name,age\nAlice,30\nBob,25\n"

    # Create a temporary CSV file
    temp_file = Tempfile.new('dummy.csv')
    temp_file.write(csv_content)
    temp_file.close

    # Read the file using CSVReader
    csv_reader = CSVReader.new(temp_file.path)
    result = csv_reader.read_csv_file

    # Verify the content is read correctly
    expected = [["name", "age"], ["Alice", "30"], ["Bob", "25"]]
    assert_equal expected, result

    # Clean up the temporary file
    temp_file.unlink
  end

  def test_read_csv_file_not_found
    """
    Test that an error is raised when the file does not exist.
    """
    assert_raises(RuntimeError) do
      csv_reader = CSVReader.new("nonexistent.csv")
      csv_reader.read_csv_file
    end
  end

  def test_read_csv_file_invalid_format
    """
    Test that an error is raised when the file is not a valid CSV.
    """
    # Mock invalid CSV content
    invalid_content = "name,age\nAlice,30\nBob"

    # Create a temporary CSV file with invalid content
    temp_file = Tempfile.new('invalid.csv')
    temp_file.write(invalid_content)
    temp_file.close

    # Attempt to read the file
    assert_raises(RuntimeError) do
      csv_reader = CSVReader.new(temp_file.path)
      csv_reader.read_csv_file
    end

    # Clean up the temporary file
    temp_file.unlink
  end
end