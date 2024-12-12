
#include <iomanip>
#include <regex>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdint>
#include <ctime>

inline int months_since_epoch(const std::string& date_str)
{
    if (date_str.empty()) return 0;
    
    std::tm tm = {};
    std::istringstream ss(date_str);
    
    ss >> std::get_time(&tm, "%Y-%m-%d");
    
    tm.tm_hour = tm.tm_min = tm.tm_sec = 0;
    std::time_t time = std::mktime(&tm);
    return static_cast<int>(time / (24 * 60 * 60 * 30));
}

int main()
{ 
    std::ifstream csv("movie.csv");
    std::ofstream out("out.csv");

    std::string s;
    std::getline(csv, s);
    out << s << std::endl;

    std::regex pattern(R"(\d{4}-\d{2}-\d{2})");
    
    for (std::string line; std::getline(csv, line);)
        if (std::smatch match; std::regex_search(line, match, pattern))
        {
            size_t index = match.position(0);

            int64_t time = months_since_epoch(line.substr(index, std::string("yyyy-mm-dd").size()));

            std::string line_new = line.substr(0, index) + std::to_string(time) + line.substr(index + std::string("yyyy-mm-dd").size());
            out << line_new << std::endl;
        }
}
