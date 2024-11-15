#include <float.h>
#include <limits.h>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <initializer_list>
#include <algorithm>
#include <cstdint>
#include <ctime>
#include <vector>
#include <random>

inline int days_since_epoch(const std::string& date_str)
{
    if (date_str.empty()) return 0;
    
    std::tm tm = {};
    std::istringstream ss(date_str);
    
    ss >> std::get_time(&tm, "%Y-%m-%d");
    if (ss.fail())
    {
        std::cout << "Got " << date_str << std::endl;
        throw std::invalid_argument("Invalid date format. Expected yyyy-mm-dd.");
    }
    
    tm.tm_hour = 0;
    tm.tm_min = 0;
    tm.tm_sec = 0;
    
    std::time_t time = std::mktime(&tm);
    
    if (time == -1)
        throw std::runtime_error("Failed to convert date to time_t.");
    
    const int seconds_per_day = 86400 * 30; // 24 * 60 * 60 * 30
    return static_cast<int>(time / seconds_per_day);
}

int main()
{ 
    std::ifstream csv("movie.csv");
    std::ofstream out("out.csv");

    if (!csv.is_open()) return std::cerr << "File open failed\n", 1;

    std::string line;
    std::getline(csv, line);

    for (std::string line; std::getline(csv, line);)
    {
        while (line.find("\"\"") != std::string::npos)
            line.erase(line.find("\"\""), 2);

        if (line.find(",,") != std::string::npos) continue;
        
        std::replace(line.begin(), line.end(), ' ', '_');
        std::replace(line.begin(), line.end(), ',', ' ');
        std::istringstream is(line);

        int64_t index, id, vote_count;
        double popularity, vote_avg;
        std::string title, overview, release_date;

        is >> index >> id >> title;

        if (title.find('\"') != std::string::npos && title.find('\"') == title.rfind('\"'))
        {
            std::string token;
            std::getline(is, token, '\"');
            title += token + "\"";
        }
        
        is >> overview;

        if (overview.find('\"') != std::string::npos && overview.find('\"') == overview.rfind('\"'))
        {
            std::string token;
            std::getline(is, token, '\"');
            overview += token + "\"";
        }

        is >> release_date >> popularity >> vote_avg >> vote_count;

        out << id << "," << title << "," << overview << "," << days_since_epoch(release_date) << "," << popularity << "," << vote_avg << "," << vote_count << std::endl;
        
    }

    return 0;
}
