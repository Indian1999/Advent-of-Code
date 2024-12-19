import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main
{
    // part1: 7307 CORRECT
    List<List<Page>> updates = new ArrayList<>();
    public static void main(String[] args)
    {
        Main obj = new Main();
        obj.readInput("day 5/input.txt");
        int total = 0;
        for (List<Page> update : obj.updates) 
        {
            if (obj.isOrdered(update))
            {
                total += obj.getMiddlePageNum(update);
            }
        }
        System.out.println(total);
    }

    int getMiddlePageNum(List<Page> list)
    {
        int index = (int)Math.floor( list.size() / 2 );
        return list.get(index).getPageNum();
    }

    boolean isOrdered(List<Page> list)
    {
        for (int i = 0; i < list.size()-1; i++) 
        {
            if (!list.get(i).isSmaller(list.get(i+1)))
            {
                return false;
            }
        }
        return true;
    }

    void readInput(String fileName)
    {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) 
        {
            String line;
            while (!(line = reader.readLine()).equals("updates:")) 
            {
                String[] line_split = line.split("\\|");
                int a = Integer.valueOf(line_split[0]);
                int b = Integer.valueOf(line_split[1]);
                Page.addRule(new Pair(a,b));
            }
            while ((line = reader.readLine()) != null)
            {
                String[] update_str = line.split(",");
                List<Page> update = new ArrayList<>();
                for (int i = 0; i < update_str.length; i++) 
                {
                    update.add(new Page(Integer.valueOf(update_str[i])));
                }
                updates.add(update);
            }
        } 
        catch (IOException e)
        {
            System.out.println(e.getMessage());
        }
    }
}