import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

public class TestCSVFileReading {

    @Test
    public void testReadCSVFileSuccess() throws IOException {
        // Mock CSV content
        String csvContent = "name,age\nAlice,30\nBob,25\n";

        // Mock BufferedReader to simulate file reading
        BufferedReader mockReader = Mockito.mock(BufferedReader.class);
        when(mockReader.readLine())
            .thenReturn("name,age")  // First line
            .thenReturn("Alice,30")  // Second line
            .thenReturn("Bob,25")    // Third line
            .thenReturn(null);       // End of file

        // Mock the CSVReader class to return the mocked BufferedReader
        CSVReader csvReader = Mockito.spy(new CSVReader("dummy.csv"));
        doReturn(mockReader).when(csvReader).createBufferedReader(anyString());

        // Call the method under test
        List<String[]> result = csvReader.readCSVFile();

        // Verify the content is read correctly
        List<String[]> expected = Arrays.asList(
            new String[]{"name", "age"},
            new String[]{"Alice", "30"},
            new String[]{"Bob", "25"}
        );
        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.toString(expected.get(i)), Arrays.toString(result.get(i)));
        }

        // Verify that the mocked BufferedReader was used
        verify(mockReader, times(4)).readLine(); // 3 lines + null for EOF
    }
}
