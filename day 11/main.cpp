#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <unordered_map>
#include <functional>
#include <stdint.h>
using namespace std;
namespace std
{
    template <>
    struct hash<pair<uint64_t, int>>
    {
        size_t operator()(const pair<uint64_t, int> &pair) const
        {
            auto hash1 = hash<uint64_t>()(pair.first);
            auto hash2 = hash<int>()(pair.second);
            return hash1 ^ (hash2 << 1);
        }
    };
}
unordered_map<pair<uint64_t, int>, uint64_t> memo;
int num_length(uint64_t num)
{
    int len = 0;
    while (num > 0)
    {
        num /= 10;
        len++;
    }
    return len;
}

uint64_t stone_value(uint64_t num, int n)
{
    pair<uint64_t, int> num_n = {num,n};
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
            uint64_t first_half = floor(num / divisor);
            uint64_t second_half = num % divisor;
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
    vector<uint64_t> stones = {3935565, 31753, 437818, 7697, 5, 38, 0, 123};
    uint64_t total = 0;
    int blinks = 75;
    for (int i = 0; i < stones.size(); i++)
    {
        total += stone_value(stones[i], blinks);
        cout << i << endl;
    }
    cout << total << endl;
    return 0;
}