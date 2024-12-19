import java.util.ArrayList;
import java.util.List;

public class Page 
{
    private static List<Pair> rules = new ArrayList<>(); 
    private int pageNum;

    public Page(int pageNum)
    {
        this.pageNum = pageNum;
    }

    public boolean isSmaller(Page other)
    {
        for (int i = 0; i < rules.size(); i++) 
        {
            if (rules.get(i).getFirst() == pageNum && rules.get(i).getSecond() == other.getPageNum())
            {
                return true;
            }
        }
        return false;
    }

    public int getPageNum()
    {
        return pageNum;
    }

    public static void addRule(Pair rule)
    {
        rules.add(rule);
    }

    public void clearRules()
    {
        rules.clear();
    }

    @Override
    public String toString() 
    {
        return "" + pageNum;
    }
}

