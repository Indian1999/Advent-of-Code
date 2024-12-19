import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main
{
    // part 1: 7307 CORRECT
    // part 2: 4713 CORRECT
    List<List<Page>> updates = new ArrayList<>();
    public static void main(String[] args)
    {
        Main obj = new Main();
        obj.readInput("day 5/input.txt");
        obj.part1();
        obj.part2();
    }
    void part1()
    {
        int total = 0;
        for (List<Page> update : updates) 
        {
            if (isOrdered(update))
            {
                total += getMiddlePageNum(update);
            }
        }
        System.out.println("part 1: " + total);
    }
    void part2()
    {
        int total = 0;
        for (List<Page> update : updates) 
        {
            if (!isOrdered(update))
            {
                orderUpdate(update);
                total += getMiddlePageNum(update);
            }
        }
        System.out.println("part 2: " + total);
    }

    void orderUpdate(List<Page> update)
    {
        for (int i = 0; i < update.size()-1; i++) 
        {
            for (int j = i+1; j < update.size(); j++) 
            {
                if (update.get(j).isSmaller(update.get(i)))
                {
                    Page temp = update.get(i);
                    update.set(i, update.get(j));
                    update.set(j, temp);
                }
            }
        }
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