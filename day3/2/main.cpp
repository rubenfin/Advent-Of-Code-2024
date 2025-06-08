#include <iostream>
#include <fstream>

int calculate(std::string first, std::string second)
{
    if (first == "" || second == "")
        return 0;
    int f = std::atoi(first.c_str());
    int s = std::atoi(second.c_str());
    return f * s;
}

void check_if_approved(std::string &content, size_t &pos, bool &approved)
{
    size_t p_do = content.find("do()", pos);
    size_t p_dont = content.find("don't()", pos);
    size_t p_mul = content.find("mul(", pos);

    size_t next = std::min({ p_do != std::string::npos ? p_do : content.size(),
                             p_dont != std::string::npos ? p_dont : content.size(),
                             p_mul != std::string::npos ? p_mul : content.size() });

    if (next == content.size())
    {
        pos = content.size();
        return;
    }

    if (next == p_do)
    {
        approved = true;
        pos = p_do + 4;
    }
    else if (next == p_dont)
    {
        approved = false;
        pos = p_dont + 7;
    }
}

int main()
{
    std::ifstream file("../input.txt");
    std::string content(
        (std::istreambuf_iterator<char>(file)),
        std::istreambuf_iterator<char>()
    );

    int total = 0;
    size_t pos = 0;
    bool approved = true;

    while (true)
    {
        while (true)
        {
            size_t p_mul = content.find("mul(", pos);
            size_t p_do = content.find("do()", pos);
            size_t p_dont = content.find("don't()", pos);

            size_t next = std::min({ p_do != std::string::npos ? p_do : content.size(),
                                     p_dont != std::string::npos ? p_dont : content.size(),
                                     p_mul != std::string::npos ? p_mul : content.size() });

            if (next == content.size())
            {
                pos = content.size();
                break;
            }

            if (next == p_do || next == p_dont)
                check_if_approved(content, pos, approved);
            else
                break;
        }

        size_t mul = content.find("mul(", pos);
        if (mul == std::string::npos)
            break;

        std::string first = "";
        std::string second = "";
        size_t i = mul + 4;

        while (i < content.size() && isdigit(content[i]))
            first += content[i++];

        if (i >= content.size() || content[i] != ',')
        {
            pos = mul + 1;
            continue;
        }

        i++;

        while (i < content.size() && isdigit(content[i]))
            second += content[i++];

        if (i >= content.size() || content[i] != ')')
        {
            pos = mul + 1;
            continue;
        }

        if (approved)
            total += calculate(first, second);

        pos = i + 1; 
    }

    std::cout << total << std::endl;
    return 0;
}
