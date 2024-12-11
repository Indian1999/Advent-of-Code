#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<unsigned long long int> blink(vector<unsigned long long int> stones)
{
    vector<unsigned long long int> new_stones;
    for (int i = 0; i < stones.size(); i++)
    {
        if (stones[i] == 0)
        {
            new_stones.push_back(1);
        }
        else if (to_string(stones[i]).length() % 2 == 0)
        {
            string first_half = to_string(stones[i]).substr(0, to_string(stones[i]).length() / 2);
            string second_half = to_string(stones[i]).substr(to_string(stones[i]).length() / 2);
            new_stones.push_back(stoi(first_half));
            new_stones.push_back(stoi(second_half));
        }
        else
        {
            new_stones.push_back(stones[i]*2024);
        }
    }
    return new_stones;
}

int main()
{
    vector<unsigned long long int> stones = {3935565, 31753, 437818, 7697, 5, 38, 0, 123};
    for (int i = 0; i < 75; i++)
    {
        stones = blink(stones);
        cout << i << endl;
    }
    cout << stones.size() << endl;
    return 0;
}