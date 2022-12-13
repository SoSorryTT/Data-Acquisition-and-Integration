-- 1 question
{
    basin(basinId:14) {
        name
        area
    }
}

-- 2 question
{
    basin(basinId:6) {
        annualRainfall(year:2003)
    }
}

-- 3 question
{
    basins {
        name
        rainfall_1994:annualRainfall(year:1994)
        rainfall_2004:annualRainfall(year:2004)
        rainfall_2011:annualRainfall(year:2011)
    }
}

-- 4 question
{
    station(stationId:48453) {
        basin{
            stations{
                name
                lat
                lon
                basinId
            }
        }
    }
}