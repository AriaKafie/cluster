
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

#include "types.h"

int main()
{ 
    std::ifstream csv("movie.csv");
    std::vector<FeatureVector*> data;

    if (!csv.is_open()) return std::cerr << "File open failed\n", 1;

    std::string line;
    std::getline(csv, line);
    
    /*for (std::string feature : { "index", "id", "title", "overview", "release_date", "popularity", "vote_average", "vote_count" })
        printf("%-20s", feature.c_str());
    std::cout << std::endl;*/

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

        data.push_back(new FeatureVector(id, title, overview, release_date, popularity, vote_avg, vote_count));
    }

    for (int k = 2; k <= 2; k++)
    {
        std::cout << "K-means with K=" << k << std::endl;

        std::vector<Centroid> centroids(k);
        
        for (Centroid& c : centroids)
            c.randomize();

        for (FeatureVector *fv : data)
        {
            if (centroids[0].dist(fv) <= centroids[1].dist(fv))
                centroids[0].feature_vectors.push_back(fv);
            else
                centroids[1].feature_vectors.push_back(fv);
        }

        std::cout << centroids[0].feature_vectors.size() << std::endl;
        std::cout << centroids[1].feature_vectors.size() << std::endl;

        /*bool changed;

        do
        {
            changed = false;

            
        }
        while (changed);*/
    }
    
    /*for (FeatureVector *fv : data)
        printf("%-20lld%-20s%-20s%-20s%-20lf%-20lf%-20d\n",
        fv->id, fv->title.substr(0,19).c_str(), fv->overview.substr(0,19).c_str(), date_time(fv->release_date).c_str(), fv->popularity, fv->vote_average, fv->vote_count);*/
    
    return 0;
}
