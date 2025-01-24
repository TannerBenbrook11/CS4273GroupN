import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class CSVReader {
    private String filePath;

    // Constructor
    public CSVReader(String filePath) {
        this.filePath = filePath;
    }

    // Method to create BufferedReader, allowing mock in the test
    public BufferedReader createBufferedReader(String fileName) throws IOException {
        return new BufferedReader(new FileReader(fileName));
    }

    // Method to read the CSV file
    public List<String[]> readCSVFile() throws IOException {
        List<String[]> rows = new ArrayList<>();
        try (BufferedReader br = createBufferedReader(filePath)) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] row = line.split(",");
                rows.add(row);
            }
        }
        return rows;
    }
}
