
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

#include "types.h"

int main()
{ 
    std::ifstream csv("movie.csv");

    if (!csv.is_open()) return std::cerr << "File open failed\n", 1;

    std::string line;
    std::getline(csv, line);
    
    for (std::string feature : { "index", "id", "title", "overview", "release_date", "popularity", "vote_average", "vote_count" })
        printf("%-20s", feature.c_str());
    std::cout << std::endl;

    int min_release_date = INT32_MAX, max_release_date = INT32_MIN;
    int64_t max_vote_count = INT64_MIN, min_vote_count = INT64_MAX;
    double max_popularity = DBL_MIN, min_popularity = DBL_MAX, max_vote_avg = DBL_MIN, min_vote_avg = DBL_MAX;
    
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

        title = title.substr(0, 19);
        
        is >> overview;

        if (overview.find('\"') != std::string::npos && overview.find('\"') == overview.rfind('\"'))
        {
            std::string token;
            std::getline(is, token, '\"');
            overview += token + "\"";
        }

        overview = overview.substr(0, 19);

        is >> release_date >> popularity >> vote_avg >> vote_count;

        int epoch_days = days_since_epoch(release_date);

        max_release_date = std::max(epoch_days, max_release_date);
        min_release_date = std::min(epoch_days, min_release_date);
        
        max_vote_count = std::max(vote_count, max_vote_count);
        min_vote_count = std::min(vote_count, min_vote_count);
        
        max_vote_avg = std::max(vote_avg, max_vote_avg);
        min_vote_avg = std::min(vote_avg, min_vote_avg);
        
        max_popularity = std::max(popularity, max_popularity);
        min_popularity = std::min(popularity, min_popularity);
        
        printf("%-20lld%-20lld%-20s%-20s%-20s%-20lf%-20lf%-20lld\n",
               index, id, title.c_str(), overview.c_str(), release_date.c_str(), popularity, vote_avg, vote_count);
    }

    printf("Popularity min/max: %lf, %lf\n", min_popularity, max_popularity);
    printf("Vote avg min/max: %lf, %lf\n", min_vote_avg, max_vote_avg);
    printf("Vote count min/max: %lld, %lld\n", min_vote_count, max_vote_count);

    printf("Release date min/max: %s, %s\n", date_time(min_release_date).c_str(), date_time(max_release_date).c_str());
    
    return 0;
}
