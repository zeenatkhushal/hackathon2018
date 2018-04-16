######################################
#### Opioid Shiny app test script ####
######################################

library(dplyr)
library(googleVis)


opioid_states <- read.table("C:\\Users\\Maham\\Desktop\\Opioid-Overdose-Shiny-App-master\\VSRR_Provisional_Drug_Overdose_Death_Counts.txt", header = T, na.strings = c("Unreliable", "Suppressed"))

# remove pct symbols & convert to numeric
opioid_states$PercentComplete <- as.numeric(gsub("%", "", opioid_states$PercentComplete))

opioid_states <- tbl_df(opioid_states)

opioid_states$Indicator <- as.character(opioid_states$Indicator)

opioid_2015 <- filter(opioid_states, Year == 2015)

opioid_2015_Heroin (T40.1) <- filter(opioid_states, Year == 2015, Indicator == "Heroin (T40.1)")


## group by state and year, calculate total death rates

states_grouped <- group_by(opioid_states, State, Year)

totals <- summarise(states_grouped, DataValue = sum(DataValue, na.rm = T), PercentComplete = sum(PercentComplete, na.rm = T), PercentPendingInvestigation = sum(PercentPendingInvestigation, na.rm = T))

totals$Indicator <- rep("Opioids (T40.0-T40.4,T40.6)", length(totals$State))

# Merge data frames to produce final output

opioid_merge <- select(opioid_states, State, Year, DataValue, PercentComplete, PercentPendingInvestigation, Indicator)

# Create final data frame
overdoses <- rbind(as.data.frame(opioid_merge), as.data.frame(totals))

# Arrange data by state and year

overdoses <- arrange(overdoses, desc(State), Year)

# write the dataframe to file

write.csv(overdoses, "C:\\Users\\Maham\\Desktop\\Opioid-Overdose-Shiny-App-master\\VSRR_Provisional_Drug_Overdose_Death_Counts.csv", row.names = F)



#subset to all opioids

overdose_all <- filter(overdoses, Indicator == "Opioids (T40.0-T40.4,T40.6)")
#cloropleth map - heroin overdoses

overdoseStates_DR  <- gvisGeoChart(opioid_2015_Heroin (T40.1), "State", "PercentComplete", options = list(region="US",
                                                                                             displayMode = "regions",
                                                                                             resolution = "provinces",
                                                                                             width = 600, height = 400))

overdoseStates_DR  <- gvisGeoChart(opioid_2015_Heroin (T40.1), "State", "PercentComplete", options = list(region="US",
                                                                                             displayMode = "regions",
                                                                                             resolution = "provinces",
                                                                                             width = 600, height = 400))


plot(overdoseStates_DR)


overdoseStates_All  <- gvisGeoChart(overdose_Opioids (T40.0-T40.4,T40.6), "State", "PercentComplete", options = list(region="US",
                                                                                             displayMode = "regions",
                                                                                             resolution = "provinces",
                                                                                             width = 600, height = 400))

plot(overdoseStates_All)

overdoseStates_PCT <- gvisGeoChart(opioid_2015_Heroin (T40.1), "State", "Indicator", options = list(region="US",
                                                                                                      displayMode = "regions",
                                                                                                      resolution = "provinces",
                                                                                                      width = 600, height = 400))
plot(overdoseStates_PCT)