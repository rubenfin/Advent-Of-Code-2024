#include <iostream>
#include <fstream>

int calculate(std::string first, std::string second)
{
    if (first == "" || second == "")
        return 0;
    try
    {
        int f = std::atoi(first.c_str());
        int s = std::atoi(second.c_str());
        
        return f*s;
    }
    catch(const std::exception& e)
    {
        return 0;
    }
}

int main(int ac, char**av)
{
    std::ifstream file("../input.txt");
    std::string content(
    (std::istreambuf_iterator<char>(file)),
    std::istreambuf_iterator<char>()
    );
    int total = 0;

    while (true)
    {
        std::string first = "";
        std::string second = "";

        std::size_t mul = content.find("mul(");
        if (mul == std::string::npos)
            break;
        for (int i = mul + 4; i < content.size(); i++)
        {
            if (!isdigit(content[i]))
                break;
            while (isdigit(content[i]))
            {
                first += content[i];
                i++;
            }
            if (content[i] != ',')
                break;
            i++;
            while (isdigit(content[i]))
            {
                second += content[i];
                i++;
            }
            if (content[i] == ')')
            {
                total += calculate(first, second);
                break ;
            }
            i++;
            break;
        }
        content = content.substr(mul + 1);
    }
    std::cout << total << std::endl;
    return 0;
}