
#ifndef TYPES_H
#define TYPES_H

#include <cstdint>
#include <string>
#include <ctime>
#include <chrono>
#include <regex>
#include <cmath>

std::string date_time(int days_since_epoch)
{
    std::chrono::sys_days epoch = std::chrono::year{1970}/std::chrono::January/std::chrono::day{1};

    std::chrono::sys_days target_date = epoch + std::chrono::days{days_since_epoch};

    std::chrono::year_month_day ymd = std::chrono::year_month_day{target_date};

    std::ostringstream oss;
    oss << int(ymd.year()) << "-"
        << std::setw(2) << std::setfill('0') << unsigned(ymd.month()) << "-"
        << std::setw(2) << std::setfill('0') << unsigned(ymd.day());
    
    return oss.str();
}

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
                  int         vote_count_);
    
    int64_t id;
    std::string title;
    std::string overview;
    int release_date;
    double popularity;
    double vote_average;
    int vote_count;
};

using FV = FeatureVector;

inline FeatureVector::FeatureVector(int64_t     id_,
                                    std::string title_,
                                    std::string overview_,
                                    std::string release_date_,
                                    double      popularity_,
                                    double      vote_average_,
                                    int         vote_count_)
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
    Centroid() = default;

    void randomize()
    {
        std::random_device rd;
        std::mt19937 gen(rd());

        std::uniform_int_distribution<> year_dist(-15000, 15000);
        std::uniform_real_distribution<> popularity_dist(1.0, 3000.0);
        std::uniform_real_distribution<> vote_avg_dist(5.6, 8.7);
        std::uniform_int_distribution<> vote_count_dist(300, 36000);

        release_date = year_dist(gen);
        popularity = popularity_dist(gen);
        vote_average = vote_avg_dist(gen);
        vote_count = vote_count_dist(gen);
    }

    double dist(FeatureVector *fv)
    {
        double d = std::pow(popularity - fv->popularity, 2);
        d += std::pow(release_date - fv->release_date, 2);
        d += std::pow(vote_average - fv->vote_average, 2);
        d += std::pow(vote_count - fv->vote_count, 2);

        return std::sqrt(d);
    }

    bool reposition()
    {
        if (feature_vectors.empty()) return false;
        
        int64_t release_date_avg = 0;
        double popularity_avg = 0;
        double vote_average_avg = 0;
        int64_t vote_count_avg = 0;

        for (FeatureVector *fv : feature_vectors)
        {
            release_date_avg += fv->release_date;
            popularity_avg += fv->popularity;
            vote_average_avg += fv->vote_average;
            vote_count_avg += fv->vote_count;
        }

        release_date_avg /= feature_vectors.size();
        popularity_avg /= feature_vectors.size();
        vote_average_avg /= feature_vectors.size();
        vote_count_avg /= feature_vectors.size();

        if (int(release_date_avg) == release_date && int(vote_count_avg) == vote_count)
            return false;

        release_date = release_date_avg;
        popularity = popularity_avg;
        vote_average = vote_average_avg;
        vote_count = vote_count_avg;

        return true;
    }
    
    int release_date;
    double popularity;
    double vote_average;
    int vote_count;

    std::vector<FeatureVector*> feature_vectors;
};

#endif
