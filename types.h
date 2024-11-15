
#ifndef TYPES_H
#define TYPES_H

#include <cstdint>
#include <string>
#include <ctime>
#include <chrono>
#include <regex>

std::string date_time(int days_since_epoch)
{
    std::chrono::sys_days epoch = std::chrono::year{1970}/std::chrono::January/std::chrono::day{1};

    // Add the number of days since epoch
    std::chrono::sys_days target_date = epoch + std::chrono::days{days_since_epoch};

    // Convert to year_month_day for easy access to year, month, and day
    std::chrono::year_month_day ymd = std::chrono::year_month_day{target_date};

    // Format the result as a string in yyyy-mm-dd format
    std::ostringstream oss;
    oss << int(ymd.year()) << "-"
        << std::setw(2) << std::setfill('0') << unsigned(ymd.month()) << "-"
        << std::setw(2) << std::setfill('0') << unsigned(ymd.day());
    
    return oss.str();
}

inline int days_since_epoch(const std::string& date_str)
{
    if (date_str.empty()) return 0;
    
    //if (!std::regex_match(date_str, std::regex("^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"))) return 0;
    
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
    
    const int seconds_per_day = 86400; // 24 * 60 * 60
    return static_cast<int>(time / seconds_per_day);
}

struct FeatureVector
{
    FeatureVector(int64_t     id_,
                  std::string title_,
                  std::string overview_,
                  std::string release_date_,
                  double      popularity_,
                  double      vote_average_,
                  double      vote_count_);
    
    int64_t id;
    std::string title;
    std::string overview;
    int release_date;
    double popularity;
    double vote_average;
    double vote_count;
};

using FV = FeatureVector;

inline FeatureVector::FeatureVector(int64_t     id_,
                                    std::string title_,
                                    std::string overview_,
                                    std::string release_date_,
                                    double      popularity_,
                                    double      vote_average_,
                                    double      vote_count_)
:   id          (id_),
    title       (title_),
    overview    (overview_),
    release_date(days_since_epoch(release_date_)),
    popularity  (popularity_),
    vote_average(vote_average_),
    vote_count  (vote_count_)
{}

struct Centroid
{
    Centroid();

    int release_date;
    double popularity;
    double vote_average;
    double vote_count;
};

Centroid::Centroid()
{
    
}

#endif
