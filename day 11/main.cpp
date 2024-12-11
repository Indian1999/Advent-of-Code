#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <unordered_map>
#include <functional>
using namespace std;
namespace std
{
    template <>
    struct hash<pair<unsigned long long int, int>>
    {
        size_t operator()(const pair<unsigned long long int, int> &pair) const
        {
            auto hash1 = hash<unsigned long long int>()(pair.first);
            auto hash2 = hash<int>()(pair.second);
            return hash1 ^ (hash2 << 1);
        }
    };
}
unordered_map<pair<unsigned long long int, int>, int> memo;
int num_length(unsigned long long int num)
{
    int len = 0;
    while (num > 0)
    {
        num /= 10;
        len++;
    }
    return len;
}

int stone_value(unsigned long long int num, int n)
{
    pair<unsigned long long int, int> num_n = {num,n};
    if (memo.find(num_n) != memo.end())
    {
        return memo[num_n];
    }
    if (n == 0)
    {
        return 1;
    }
    else
    {
        if (num == 0)
        {
            return memo[num_n] = stone_value(1, n - 1);
        }
        else if (num_length(num) % 2 == 0)
        {
            int divisor = 1;
            for (int i = 0; i < num_length(num) / 2; i++)
            {
                divisor *= 10;
            }
            unsigned long long int first_half = floor(num / divisor);
            unsigned long long int second_half = num % divisor;
            // cout << num << " / " << divisor << " " << first_half << " " << second_half << endl;
            return memo[num_n] = stone_value(first_half, n - 1) + stone_value(second_half, n - 1);
        }
        else
        {
            return memo[num_n] = stone_value(num * 2024, n - 1);
        }
    }
}
int main()
{
    vector<unsigned long long int> stones = {3935565, 31753, 437818, 7697, 5, 38, 0, 123};
    int total = 0;
    int blinks = 75;
    for (int i = 0; i < stones.size(); i++)
    {
        total += stone_value(stones[i], blinks);
        cout << i << endl;
    }
    cout << total << endl;
    return 0;
}